from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class AccountType(models.TextChoices):
        CHECKING = "CHECKING", "Checking"
        SAVINGS = "SAVINGS", "Savings"
        OTHER = "OTHER", "Other"

    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices,
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CashFlowMonth(models.Model):
    """
    Represents a month in the cash flow calendar.
    """

    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )

    class Meta:
        ordering = ("year", "month")
        constraints = (
            models.UniqueConstraint(fields=["year", "month"], name="unique_year_month"),
        )

    def __str__(self):
        return f"{self.year}-{self.month:02d}"


class Category(models.Model):
    """
    Represents a category for cash flow events.
    """

    name = models.CharField(max_length=100, unique=True)

    class FlowType(models.TextChoices):
        INFLOW = "INFLOW", "Inflow"
        OUTFLOW = "OUTFLOW", "Outflow"
        TRANSFER_IN = "TRANSFER_IN", "Transfer In"
        TRANSFER_OUT = "TRANSFER_OUT", "Transfer Out"

    flow_type = models.CharField(
        max_length=20,
        choices=FlowType.choices,
    )

    def __str__(self):
        return self.name


class CashFlowEvent(models.Model):
    """
    Represents a ledger entry.
    """

    class Status(models.TextChoices):
        PLANNED = "PLANNED", "Planned"
        PAID = "PAID", "Paid"
        CLEARED = "CLEARED", "Cleared"
        CANCELED = "CANCELED", "Canceled"

    cash_flow_month = models.ForeignKey(
        "CashFlowMonth",
        on_delete=models.CASCADE,
        related_name="cash_flow_events",
    )

    recurring_cash_flow = models.ForeignKey(
        "RecurringCashFlow",
        on_delete=models.SET_NULL,
        related_name="cash_flow_events",
        null=True,
        blank=True,
    )

    account = models.ForeignKey(
        "Account",
        on_delete=models.PROTECT,
        related_name="cash_flow_events",
    )

    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="cash_flow_events",
    )

    description = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)
    planned_date = models.DateField()
    planned_amount = models.DecimalField(max_digits=12, decimal_places=2)
    actual_date = models.DateField(null=True, blank=True)

    actual_amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLANNED,
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("planned_date", "created_at")

    def __str__(self):
        return self.description


class RecurringCashFlow(models.Model):
    """
    Represents a recurring cash flow event expected to occur regularly.
    """

    name = models.CharField(max_length=100, unique=True)

    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="recurring_cash_flows",
    )

    account = models.ForeignKey(
        "Account",
        on_delete=models.PROTECT,
        related_name="recurring_cash_flows",
    )

    default_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Frequency(models.TextChoices):
        WEEKLY = "WEEKLY", "Weekly"
        BIWEEKLY = "BIWEEKLY", "Every two weeks"
        MONTHLY = "MONTHLY", "Monthly"

    frequency = models.CharField(
        max_length=20,
        choices=Frequency.choices,
    )

    anchor_date = models.DateField(null=True, blank=True)

    preferred_due_day = models.PositiveSmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(31)]
    )

    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

from django.core.exceptions import ValidationError
from django.test import TestCase

from ledger.models import Account, CashFlowMonth, Category


class LedgerModelTests(TestCase):
    def test_cash_flow_month_string(self):
        month = CashFlowMonth(year=2026, month=8)

        self.assertEqual(str(month), "2026-08")

    def test_cash_flow_month_rejects_invalid_month(self):
        month = CashFlowMonth(year=2026, month=13)

        with self.assertRaises(ValidationError):
            month.full_clean()

    def test_account_string(self):
        account = Account(
            name="Combined Checking",
            account_type=Account.AccountType.CHECKING,
        )

        self.assertEqual(str(account), "Combined Checking")

    def test_category_string(self):
        category = Category(
            name="Utilities",
            flow_type=Category.FlowType.OUTFLOW,
        )

        self.assertEqual(str(category), "Utilities")

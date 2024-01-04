from python_accounting.models import Transaction
from python_accounting.mixins import BuyingMixin
from typing import Any


class CashPurchase(BuyingMixin, Transaction):
    """Class for the Cash Purchase Transaction"""

    __tablename__ = None
    __mapper_args__ = {
        "polymorphic_identity": Transaction.TransactionType.CASH_PURCHASE,
    }

    def __init__(self, **kw: Any) -> None:
        from python_accounting.models import Account

        self.main_account_types: list = [
            Account.AccountType.BANK,
        ]
        self.credited = True
        self.transaction_type = Transaction.TransactionType.CASH_PURCHASE
        super().__init__(**kw)
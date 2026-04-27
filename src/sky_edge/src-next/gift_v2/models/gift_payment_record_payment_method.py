from enum import Enum


class GiftPaymentRecordPaymentMethod(str, Enum):
    CASH = "Cash"
    CHECK = "Check"
    CREDITCARD = "CreditCard"
    DIRECTDEBIT = "DirectDebit"
    NONE = "None"
    OTHER = "Other"
    PAYPAL = "PayPal"
    STANDINGORDER = "StandingOrder"
    VENMO = "Venmo"
    VOUCHER = "Voucher"

    def __str__(self) -> str:
        return str(self.value)

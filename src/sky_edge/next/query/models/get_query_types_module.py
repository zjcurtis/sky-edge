from enum import Enum


class GetQueryTypesModule(str, Enum):
    ACCOUNTSPAYABLE = "AccountsPayable"
    ACCOUNTSRECEIVABLE = "AccountsReceivable"
    CASHRECEIPTS = "CashReceipts"
    FIXEDASSETS = "FixedAssets"
    GENERALLEDGER = "GeneralLedger"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)

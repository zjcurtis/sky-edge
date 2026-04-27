from enum import Enum


class GiftReceiptReceiptStatus(str, Enum):
    DONOTRECEIPT = "DoNotReceipt"
    NONE = "None"
    NOTRECEIPTED = "NotReceipted"
    RECEIPTED = "Receipted"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ConstituentAddReceiptType(str, Enum):
    CONSOLIDATED_RECEIPTS = "Consolidated receipts"
    ONE_RECEIPT_PER_GIFT = "One receipt per gift"

    def __str__(self) -> str:
        return str(self.value)

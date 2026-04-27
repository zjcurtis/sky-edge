from enum import Enum


class GiftPaymentRecordProcessingStatus(str, Enum):
    APPROVED = "Approved"
    DECLINED = "Declined"
    PENDING = "Pending"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class AmendGiftResultRecurringGiftAmendmentStatus(str, Enum):
    COMPLETE = "Complete"
    PENDING = "Pending"
    REJECTED = "Rejected"

    def __str__(self) -> str:
        return str(self.value)

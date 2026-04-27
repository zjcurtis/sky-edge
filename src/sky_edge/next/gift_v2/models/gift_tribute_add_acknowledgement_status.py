from enum import Enum


class GiftTributeAddAcknowledgementStatus(str, Enum):
    ACKNOWLEDGED = "Acknowledged"
    DONOTACKNOWLEDGE = "DoNotAcknowledge"
    NONE = "None"
    NOTACKNOWLEDGED = "NotAcknowledged"

    def __str__(self) -> str:
        return str(self.value)

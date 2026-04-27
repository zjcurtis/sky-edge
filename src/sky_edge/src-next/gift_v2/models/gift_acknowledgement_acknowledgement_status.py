from enum import Enum


class GiftAcknowledgementAcknowledgementStatus(str, Enum):
    ACKNOWLEDGED = "Acknowledged"
    DONOTACKNOWLEDGE = "DoNotAcknowledge"
    NONE = "None"
    NOTACKNOWLEDGED = "NotAcknowledged"

    def __str__(self) -> str:
        return str(self.value)

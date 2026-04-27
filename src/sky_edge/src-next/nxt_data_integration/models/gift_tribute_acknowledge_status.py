from enum import Enum


class GiftTributeAcknowledgeStatus(str, Enum):
    ACKNOWLEDGED = "Acknowledged"
    DONOTACKNOWLEDGE = "DoNotAcknowledge"
    NOTACKNOWLEDGED = "NotAcknowledged"

    def __str__(self) -> str:
        return str(self.value)

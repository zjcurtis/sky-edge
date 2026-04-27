from enum import Enum


class GiftTributeEditAcknowledgeStatus(str, Enum):
    ACKNOWLEDGED = "Acknowledged"
    DONOTACKNOWLEDGE = "DoNotAcknowledge"
    NOTACKNOWLEDGED = "NotAcknowledged"

    def __str__(self) -> str:
        return str(self.value)

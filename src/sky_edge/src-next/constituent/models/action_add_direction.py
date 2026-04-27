from enum import Enum


class ActionAddDirection(str, Enum):
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"

    def __str__(self) -> str:
        return str(self.value)

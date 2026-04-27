from enum import Enum


class ActionEditDirection(str, Enum):
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ActionReadComputedStatus(str, Enum):
    COMPLETED = "Completed"
    OPEN = "Open"
    PASTDUE = "PastDue"

    def __str__(self) -> str:
        return str(self.value)

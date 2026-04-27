from enum import Enum


class ListActionsAllConstituentsComputedStatusItem(str, Enum):
    COMPLETED = "Completed"
    OPEN = "Open"
    PASTDUE = "PastDue"

    def __str__(self) -> str:
        return str(self.value)

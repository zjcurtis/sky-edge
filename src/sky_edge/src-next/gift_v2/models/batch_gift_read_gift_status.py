from enum import Enum


class BatchGiftReadGiftStatus(str, Enum):
    ACTIVE = "Active"
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    HELD = "Held"
    NONE = "None"
    TERMINATED = "Terminated"

    def __str__(self) -> str:
        return str(self.value)

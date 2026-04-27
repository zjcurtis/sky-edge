from enum import Enum


class ActionAddOutcome(str, Enum):
    SUCCESSFUL = "Successful"
    UNSUCCESSFUL = "Unsuccessful"

    def __str__(self) -> str:
        return str(self.value)

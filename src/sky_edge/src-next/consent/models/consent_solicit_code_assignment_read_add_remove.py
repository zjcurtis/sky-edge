from enum import Enum


class ConsentSolicitCodeAssignmentReadAddRemove(str, Enum):
    ADD = "Add"
    REMOVE = "Remove"

    def __str__(self) -> str:
        return str(self.value)

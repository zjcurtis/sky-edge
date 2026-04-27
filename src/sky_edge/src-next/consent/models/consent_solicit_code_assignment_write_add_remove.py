from enum import Enum


class ConsentSolicitCodeAssignmentWriteAddRemove(str, Enum):
    ADD = "Add"
    REMOVE = "Remove"

    def __str__(self) -> str:
        return str(self.value)

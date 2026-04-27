from enum import Enum


class DeleteQueryProduct(str, Enum):
    FE = "FE"
    RE = "RE"

    def __str__(self) -> str:
        return str(self.value)

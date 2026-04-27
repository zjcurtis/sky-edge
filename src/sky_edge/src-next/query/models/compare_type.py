from enum import Enum


class CompareType(str, Enum):
    AND = "And"
    NONE = "None"
    OR = "Or"

    def __str__(self) -> str:
        return str(self.value)

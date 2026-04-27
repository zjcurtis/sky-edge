from enum import Enum


class MergeOperator(str, Enum):
    AND = "And"
    OR = "Or"
    SUB = "Sub"
    XOR = "Xor"

    def __str__(self) -> str:
        return str(self.value)

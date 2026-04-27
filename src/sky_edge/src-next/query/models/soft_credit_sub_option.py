from enum import Enum


class SoftCreditSubOption(str, Enum):
    FULLAMOUNTTOALL = "FullAmountToAll"
    SPLITEVENLY = "SplitEvenly"
    USEAMOUNTINGRID = "UseAmountInGrid"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class OutputLimitType(str, Enum):
    RANDOMSAMPLING = "RandomSampling"
    TOPNUMBERROWS = "TopNumberRows"
    TOPPERCENTROWS = "TopPercentRows"

    def __str__(self) -> str:
        return str(self.value)

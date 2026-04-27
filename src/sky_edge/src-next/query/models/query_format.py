from enum import Enum


class QueryFormat(str, Enum):
    DYNAMIC = "Dynamic"
    STATIC = "Static"

    def __str__(self) -> str:
        return str(self.value)

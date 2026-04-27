from enum import Enum


class RatingsDataType(str, Enum):
    BOOLEAN = "Boolean"
    CURRENCY = "Currency"
    DATE = "Date"
    NUMBER = "Number"
    TABLE = "Table"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)

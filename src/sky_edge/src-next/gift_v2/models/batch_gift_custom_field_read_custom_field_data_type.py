from enum import Enum


class BatchGiftCustomFieldReadCustomFieldDataType(str, Enum):
    BOOLEAN = "Boolean"
    CONSTITUENT = "Constituent"
    CURRENCY = "Currency"
    DATE = "Date"
    FUZZYDATE = "FuzzyDate"
    NUMBER = "Number"
    TABLE = "Table"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)

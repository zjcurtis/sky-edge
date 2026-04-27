from enum import Enum


class CustomFieldDataType(str, Enum):
    BOOLEAN = "Boolean"
    CONSTITUENT = "Constituent"
    CURRENCY = "Currency"
    DATETIME = "DateTime"
    FUZZYDATE = "FuzzyDate"
    NUMERIC = "Numeric"
    TABLEENTRY = "TableEntry"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class AttributeValueType(str, Enum):
    BOOLEAN = "Boolean"
    CONSTITUENT = "Constituent"
    CURRENCY = "Currency"
    DATE = "Date"
    FUZZYDATE = "FuzzyDate"
    NUMBER = "Number"
    TABLEENTRY = "TableEntry"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)

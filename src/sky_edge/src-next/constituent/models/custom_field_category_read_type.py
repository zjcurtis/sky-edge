from enum import Enum


class CustomFieldCategoryReadType(str, Enum):
    BOOLEAN = "Boolean"
    CODETABLEENTRY = "CodeTableEntry"
    CONSTITUENTID = "ConstituentId"
    CURRENCY = "Currency"
    DATE = "Date"
    FUZZYDATE = "FuzzyDate"
    NUMBER = "Number"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)

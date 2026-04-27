from enum import Enum


class QueryValueType(str, Enum):
    BOOLEAN = "Boolean"
    DATE = "Date"
    FESUMMARYDATE = "FESummaryDate"
    FUZZYDATE = "FuzzyDate"
    LOOKUP = "Lookup"
    SEARCH = "Search"
    STATICENTRY = "StaticEntry"
    SUMMARY = "Summary"
    TABLEENTRY = "TableEntry"
    TEXT = "Text"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class RatingCategoryReadType(str, Enum):
    BOOLEAN = "Boolean"
    CODETABLE = "CodeTable"
    CURRENCY = "Currency"
    DATETIME = "DateTime"
    NUMBER = "Number"
    TEXT = "Text"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)

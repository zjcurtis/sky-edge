from enum import Enum


class QueryFieldContext(str, Enum):
    FILTER = "Filter"
    NONE = "None"
    SELECT = "Select"
    SORT = "Sort"

    def __str__(self) -> str:
        return str(self.value)

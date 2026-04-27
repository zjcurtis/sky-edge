from enum import Enum


class FilterGroupingFilterGroupingOperator(str, Enum):
    ALLOF = "AllOf"
    NONE = "None"
    ONEOF = "OneOf"

    def __str__(self) -> str:
        return str(self.value)

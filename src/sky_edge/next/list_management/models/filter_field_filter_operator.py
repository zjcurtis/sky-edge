from enum import Enum


class FilterFieldFilterOperator(str, Enum):
    ALLOF = "AllOf"
    BETWEEN = "Between"
    BLANK = "Blank"
    CONTAINS = "Contains"
    DOESNOTCONTAIN = "DoesNotContain"
    DOESNOTSTARTWITH = "DoesNotStartWith"
    EQUAL = "Equal"
    GREATERTHAN = "GreaterThan"
    GREATERTHANOREQUAL = "GreaterThanOrEqual"
    LESSTHAN = "LessThan"
    LESSTHANOREQUAL = "LessThanOrEqual"
    NONE = "None"
    NOTBLANK = "NotBlank"
    NOTEQUAL = "NotEqual"
    NOTONEOF = "NotOneOf"
    ONEOF = "OneOf"
    STARTSWITH = "StartsWith"

    def __str__(self) -> str:
        return str(self.value)

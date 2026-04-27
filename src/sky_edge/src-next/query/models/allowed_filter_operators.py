from enum import Enum


class AllowedFilterOperators(str, Enum):
    ASK = "Ask"
    BLANK = "Blank"
    DOESNOTEQUAL = "DoesNotEqual"
    EQUALS = "Equals"
    ONEOF = "OneOf"
    ONEOFEACH = "OneOfEach"
    RELATIVECOMPARISONS = "RelativeComparisons"
    SOUNDSLIKE = "SoundsLike"
    STRINGCOMPARISONS = "StringComparisons"

    def __str__(self) -> str:
        return str(self.value)

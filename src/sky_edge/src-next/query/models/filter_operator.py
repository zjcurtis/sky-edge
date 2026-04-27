from enum import Enum


class FilterOperator(str, Enum):
    ANY = "Any"
    ASK = "Ask"
    BEGINSWITH = "BeginsWith"
    BETWEEN = "Between"
    BLANK = "Blank"
    CONTAINS = "Contains"
    DOESNOTBEGINWITH = "DoesNotBeginWith"
    DOESNOTCONTAIN = "DoesNotContain"
    DOESNOTEQUAL = "DoesNotEqual"
    EQUALS = "Equals"
    GREATERTHAN = "GreaterThan"
    GREATERTHANOREQUALTO = "GreaterThanOrEqualTo"
    LESSTHAN = "LessThan"
    LESSTHANOREQUALTO = "LessThanOrEqualTo"
    LIKE = "Like"
    NOTBETWEEN = "NotBetween"
    NOTBLANK = "NotBlank"
    NOTLIKE = "NotLike"
    NOTONEOF = "NotOneOf"
    ONEOF = "OneOf"
    ONEOFEACH = "OneOfEach"
    SOUNDSLIKE = "SoundsLike"

    def __str__(self) -> str:
        return str(self.value)

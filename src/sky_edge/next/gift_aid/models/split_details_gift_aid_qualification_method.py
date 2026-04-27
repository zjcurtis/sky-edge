from enum import Enum


class SplitDetailsGiftAidQualificationMethod(str, Enum):
    APPLYRULESWHENSAVING = "ApplyRulesWhenSaving"
    NONE = "None"
    SETASNOTQUALIFIED = "SetAsNotQualified"
    SETASQUALIFIED = "SetAsQualified"

    def __str__(self) -> str:
        return str(self.value)

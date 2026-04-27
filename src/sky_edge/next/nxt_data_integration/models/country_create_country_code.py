from enum import Enum


class CountryCreateCountryCode(str, Enum):
    AUSTRALIA = "Australia"
    CANADA = "Canada"
    NEWZEALAND = "NewZealand"
    UNITEDKINGDOM = "UnitedKingdom"
    UNITEDSTATES = "UnitedStates"

    def __str__(self) -> str:
        return str(self.value)

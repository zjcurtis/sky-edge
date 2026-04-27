from enum import Enum


class MatchingGiftCreditOption(str, Enum):
    BOTH = "Both"
    DONOR = "Donor"
    MATCHINGGIFTCOMPANY = "MatchingGiftCompany"

    def __str__(self) -> str:
        return str(self.value)

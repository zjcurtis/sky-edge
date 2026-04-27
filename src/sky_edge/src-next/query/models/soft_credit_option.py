from enum import Enum


class SoftCreditOption(str, Enum):
    BOTH = "Both"
    DONOR = "Donor"
    RECIPIENTS = "Recipients"

    def __str__(self) -> str:
        return str(self.value)

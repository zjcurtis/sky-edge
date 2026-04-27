from enum import Enum


class PremiumFrequency(str, Enum):
    ANNUALLY = "Annually"
    BIMONTHLY = "BiMonthly"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SEMIANNUALLY = "SemiAnnually"

    def __str__(self) -> str:
        return str(self.value)

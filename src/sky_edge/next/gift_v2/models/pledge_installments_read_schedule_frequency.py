from enum import Enum


class PledgeInstallmentsReadScheduleFrequency(str, Enum):
    ANNUALLY = "Annually"
    EVERY_FOUR_WEEKS = "EVERY_FOUR_WEEKS"
    EVERY_SIX_MONTHS = "EVERY_SIX_MONTHS"
    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    IRREGULAR = "Irregular"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SINGLE = "Single"
    WEEKLY = "Weekly"

    def __str__(self) -> str:
        return str(self.value)

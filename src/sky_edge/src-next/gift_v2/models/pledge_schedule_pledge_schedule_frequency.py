from enum import Enum


class PledgeSchedulePledgeScheduleFrequency(str, Enum):
    ANNUALLY = "Annually"
    EVERY_TWO_WEEKS = "EVERY_TWO_WEEKS"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SINGLE = "Single"

    def __str__(self) -> str:
        return str(self.value)

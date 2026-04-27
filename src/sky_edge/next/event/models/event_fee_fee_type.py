from enum import Enum


class EventFeeFeeType(str, Enum):
    OTHER = "Other"
    REGISTRATION = "Registration"

    def __str__(self) -> str:
        return str(self.value)

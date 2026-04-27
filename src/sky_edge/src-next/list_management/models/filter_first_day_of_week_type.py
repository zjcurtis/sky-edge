from enum import Enum


class FilterFirstDayOfWeekType(str, Enum):
    MONDAY = "Monday"
    SUNDAY = "Sunday"

    def __str__(self) -> str:
        return str(self.value)

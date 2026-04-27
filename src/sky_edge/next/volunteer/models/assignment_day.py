from enum import Enum


class AssignmentDay(str, Enum):
    ALLDAYS = "AllDays"
    BLANK = "Blank"
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    WEEKDAYS = "Weekdays"
    WEEKENDS = "Weekends"

    def __str__(self) -> str:
        return str(self.value)

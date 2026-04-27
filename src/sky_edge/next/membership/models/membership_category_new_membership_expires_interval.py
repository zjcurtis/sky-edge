from enum import Enum


class MembershipCategoryNewMembershipExpiresInterval(str, Enum):
    DAYS = "Days"
    MONTHS = "Months"
    WEEKS = "Weeks"
    YEARS = "Years"

    def __str__(self) -> str:
        return str(self.value)

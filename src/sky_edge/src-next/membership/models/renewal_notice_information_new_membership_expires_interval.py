from enum import Enum


class RenewalNoticeInformationNewMembershipExpiresInterval(str, Enum):
    DAYS = "Days"
    MONTHS = "Months"
    WEEKS = "Weeks"
    YEARS = "Years"

    def __str__(self) -> str:
        return str(self.value)

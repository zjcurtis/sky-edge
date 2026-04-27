from enum import Enum


class GoalAddType(str, Enum):
    APPEAL = "Appeal"
    CAMPAIGN = "Campaign"
    FUND = "Fund"
    UNSPECIFIEDCATEGORY = "UnspecifiedCategory"

    def __str__(self) -> str:
        return str(self.value)

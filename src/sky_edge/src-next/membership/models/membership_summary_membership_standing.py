from enum import Enum


class MembershipSummaryMembershipStanding(str, Enum):
    ACTIVE = "Active"
    DROPPED = "Dropped"
    LAPSED = "Lapsed"
    NEW = "New"

    def __str__(self) -> str:
        return str(self.value)

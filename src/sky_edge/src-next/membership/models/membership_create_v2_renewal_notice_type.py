from enum import Enum


class MembershipCreateV2RenewalNoticeType(str, Enum):
    BOTH = "Both"
    DONOR = "Donor"
    PRIMARYMEMBER = "PrimaryMember"

    def __str__(self) -> str:
        return str(self.value)

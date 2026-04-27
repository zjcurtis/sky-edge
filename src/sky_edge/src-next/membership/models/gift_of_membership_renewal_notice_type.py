from enum import Enum


class GiftOfMembershipRenewalNoticeType(str, Enum):
    BOTH = "Both"
    DONOR = "Donor"
    PRIMARYMEMBER = "PrimaryMember"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class MembershipCategoryMembershipBenefitsSendTo(str, Enum):
    DONOR = "Donor"
    PRIMARYMEMBER = "PrimaryMember"

    def __str__(self) -> str:
        return str(self.value)

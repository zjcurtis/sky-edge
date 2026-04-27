from enum import Enum


class MembershipCardCreateMembershipCardsAddressToPrint(str, Enum):
    CONSTITUENT = "Constituent"
    NONE = "None"
    PRIMARYMEMBER = "PrimaryMember"

    def __str__(self) -> str:
        return str(self.value)

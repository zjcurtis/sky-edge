from enum import Enum


class RenewalNoticeInformationRenewalNoticeType(str, Enum):
    BOTH = "Both"
    DONOR = "Donor"
    PRIMARYMEMBER = "PrimaryMember"

    def __str__(self) -> str:
        return str(self.value)

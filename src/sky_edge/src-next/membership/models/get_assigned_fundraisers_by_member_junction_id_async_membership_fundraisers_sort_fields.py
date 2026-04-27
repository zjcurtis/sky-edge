from enum import Enum


class GetAssignedFundraisersByMemberJunctionIdAsyncMembershipFundraisersSortFields(str, Enum):
    FULLNAME = "FullName"

    def __str__(self) -> str:
        return str(self.value)

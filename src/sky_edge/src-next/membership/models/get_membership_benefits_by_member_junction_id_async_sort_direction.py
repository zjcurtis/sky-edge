from enum import Enum


class GetMembershipBenefitsByMemberJunctionIdAsyncSortDirection(str, Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def __str__(self) -> str:
        return str(self.value)

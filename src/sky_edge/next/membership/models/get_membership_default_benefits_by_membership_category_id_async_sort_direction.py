from enum import Enum


class GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncSortDirection(str, Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def __str__(self) -> str:
        return str(self.value)

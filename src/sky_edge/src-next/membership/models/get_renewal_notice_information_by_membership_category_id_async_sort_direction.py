from enum import Enum


class GetRenewalNoticeInformationByMembershipCategoryIdAsyncSortDirection(str, Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def __str__(self) -> str:
        return str(self.value)

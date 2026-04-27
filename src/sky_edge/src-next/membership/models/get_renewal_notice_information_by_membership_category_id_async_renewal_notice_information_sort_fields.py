from enum import Enum


class GetRenewalNoticeInformationByMembershipCategoryIdAsyncRenewalNoticeInformationSortFields(str, Enum):
    FREQUENCY = "Frequency"

    def __str__(self) -> str:
        return str(self.value)

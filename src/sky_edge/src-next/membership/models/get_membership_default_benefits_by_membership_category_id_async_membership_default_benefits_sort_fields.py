from enum import Enum


class GetMembershipDefaultBenefitsByMembershipCategoryIdAsyncMembershipDefaultBenefitsSortFields(str, Enum):
    SEQUENCE = "Sequence"

    def __str__(self) -> str:
        return str(self.value)

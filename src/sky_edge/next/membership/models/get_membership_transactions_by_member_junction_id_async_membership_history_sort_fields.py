from enum import Enum


class GetMembershipTransactionsByMemberJunctionIdAsyncMembershipHistorySortFields(
    str, Enum
):
    ACTIVITYDATE = "ActivityDate"

    def __str__(self) -> str:
        return str(self.value)

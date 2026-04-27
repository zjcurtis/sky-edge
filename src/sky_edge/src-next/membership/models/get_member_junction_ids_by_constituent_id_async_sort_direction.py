from enum import Enum


class GetMemberJunctionIdsByConstituentIdAsyncSortDirection(str, Enum):
    ASCENDING = "Ascending"
    DESCENDING = "Descending"

    def __str__(self) -> str:
        return str(self.value)

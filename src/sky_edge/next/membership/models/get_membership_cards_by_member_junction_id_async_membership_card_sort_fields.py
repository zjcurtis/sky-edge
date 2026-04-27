from enum import Enum


class GetMembershipCardsByMemberJunctionIdAsyncMembershipCardSortFields(str, Enum):
    EXPIRYDATE = "ExpiryDate"
    MEMBERNAME = "MemberName"
    RELATION = "Relation"
    SEQUENCE = "Sequence"

    def __str__(self) -> str:
        return str(self.value)

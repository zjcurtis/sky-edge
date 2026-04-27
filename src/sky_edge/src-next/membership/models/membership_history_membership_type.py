from enum import Enum


class MembershipHistoryMembershipType(str, Enum):
    DOWNGRADE = "Downgrade"
    DROPPED = "Dropped"
    JOINED = "Joined"
    REJOINED = "Rejoined"
    RENEWAL = "Renewal"
    UPGRADE = "Upgrade"

    def __str__(self) -> str:
        return str(self.value)

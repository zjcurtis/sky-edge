from enum import Enum


class MembershipRejoinRejoinType(str, Enum):
    DOWNGRADE = "Downgrade"
    SAME = "Same"
    UPGRADE = "Upgrade"

    def __str__(self) -> str:
        return str(self.value)

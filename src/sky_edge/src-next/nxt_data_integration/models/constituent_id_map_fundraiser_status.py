from enum import Enum


class ConstituentIdMapFundraiserStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)

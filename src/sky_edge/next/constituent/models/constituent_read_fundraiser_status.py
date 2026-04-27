from enum import Enum


class ConstituentReadFundraiserStatus(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)

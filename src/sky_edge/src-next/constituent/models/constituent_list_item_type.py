from enum import Enum


class ConstituentListItemType(str, Enum):
    INDIVIDUAL = "Individual"
    ORGANIZATION = "Organization"

    def __str__(self) -> str:
        return str(self.value)

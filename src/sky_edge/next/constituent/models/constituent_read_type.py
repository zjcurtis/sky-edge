from enum import Enum


class ConstituentReadType(str, Enum):
    INDIVIDUAL = "Individual"
    ORGANIZATION = "Organization"

    def __str__(self) -> str:
        return str(self.value)

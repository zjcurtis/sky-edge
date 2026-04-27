from enum import Enum


class PrimaryNameFormatAddPrimaryType(str, Enum):
    ADDRESSEE = "Addressee"
    SALUTATION = "Salutation"

    def __str__(self) -> str:
        return str(self.value)

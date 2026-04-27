from enum import Enum


class GiftAidTaxDeclarationCreateGiftAidPaysTax(str, Enum):
    NO = "No"
    UNKNOWN = "Unknown"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class GiftTaxGiftAidQualificationStatus(str, Enum):
    NONE = "None"
    NOTQUALIFIED = "NotQualified"
    PARTLYQUALIFIED = "PartlyQualified"
    QUALIFIED = "Qualified"

    def __str__(self) -> str:
        return str(self.value)

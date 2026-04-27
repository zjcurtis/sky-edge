from enum import Enum


class CreateListFromIdsRequestListType(str, Enum):
    ACTION = "Action"
    CONSTITUENT = "Constituent"
    GIFT = "Gift"
    OPPORTUNITY = "Opportunity"

    def __str__(self) -> str:
        return str(self.value)

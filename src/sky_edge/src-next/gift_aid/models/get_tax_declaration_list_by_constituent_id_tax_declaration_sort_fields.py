from enum import Enum


class GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields(str, Enum):
    MADEDATE = "MadeDate"
    STARTDATE = "StartDate"

    def __str__(self) -> str:
        return str(self.value)

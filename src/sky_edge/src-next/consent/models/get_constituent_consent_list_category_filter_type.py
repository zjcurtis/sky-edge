from enum import Enum


class GetConstituentConsentListCategoryFilterType(str, Enum):
    ANYCATEGORY = "AnyCategory"
    NOCATEGORY = "NoCategory"
    NOFILTER = "NoFilter"
    SPECIFICCATEGORY = "SpecificCategory"

    def __str__(self) -> str:
        return str(self.value)

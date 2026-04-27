from enum import Enum


class GetMembershipCategoriesAsyncMembershipCategorySortFields(str, Enum):
    CATEGORYNAME = "CategoryName"
    PROGRAMNAME = "ProgramName"

    def __str__(self) -> str:
        return str(self.value)

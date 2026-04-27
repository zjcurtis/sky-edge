from enum import Enum


class CreateListFromIdsRequestListPermissions(str, Enum):
    ONLYOWNERCANACCESS = "OnlyOwnerCanAccess"
    OTHERSCANVIEW = "OthersCanView"
    OTHERSCANVIEWANDEDIT = "OthersCanViewAndEdit"

    def __str__(self) -> str:
        return str(self.value)

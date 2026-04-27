from enum import Enum


class EditListRequestListPermission(str, Enum):
    ONLYOWNERCANACCESS = "OnlyOwnerCanAccess"
    OTHERSCANVIEW = "OthersCanView"
    OTHERSCANVIEWANDEDIT = "OthersCanViewAndEdit"

    def __str__(self) -> str:
        return str(self.value)

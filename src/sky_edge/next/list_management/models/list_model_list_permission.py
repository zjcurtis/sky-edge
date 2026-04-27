from enum import Enum


class ListModelListPermission(str, Enum):
    ONLYOWNERCANACCESS = "OnlyOwnerCanAccess"
    OTHERSCANVIEW = "OthersCanView"
    OTHERSCANVIEWANDEDIT = "OthersCanViewAndEdit"

    def __str__(self) -> str:
        return str(self.value)

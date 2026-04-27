from enum import Enum


class QueryListSortableColumn(str, Enum):
    ADDEDBY = "AddedBy"
    DATEADDED = "DateAdded"
    DATECHANGED = "DateChanged"
    DATELASTRUN = "DateLastRun"
    ELAPSEDMS = "ElapsedMs"
    LASTCHANGEDBY = "LastChangedBy"
    NAME = "Name"
    RECORDS = "Records"

    def __str__(self) -> str:
        return str(self.value)

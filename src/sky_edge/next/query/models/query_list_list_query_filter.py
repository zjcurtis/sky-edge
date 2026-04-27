from enum import Enum


class QueryListListQueryFilter(str, Enum):
    NOLISTQUERIES = "NoListQueries"
    UNSET = "Unset"

    def __str__(self) -> str:
        return str(self.value)

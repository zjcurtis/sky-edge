from enum import Enum


class AvailableFieldsSearchResultType(str, Enum):
    FIELD = "Field"
    NODE = "Node"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ConsentSolicitCodeAssignmentReadResponse(str, Enum):
    OPTIN = "OptIn"
    OPTOUT = "OptOut"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ConsentSolicitCodeAssignmentWriteResponse(str, Enum):
    NORESPONSE = "NoResponse"
    OPTIN = "OptIn"
    OPTOUT = "OptOut"

    def __str__(self) -> str:
        return str(self.value)

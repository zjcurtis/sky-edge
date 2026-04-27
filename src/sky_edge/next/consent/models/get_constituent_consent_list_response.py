from enum import Enum


class GetConstituentConsentListResponse(str, Enum):
    NORESPONSE = "NoResponse"
    OPTIN = "OptIn"
    OPTOUT = "OptOut"

    def __str__(self) -> str:
        return str(self.value)

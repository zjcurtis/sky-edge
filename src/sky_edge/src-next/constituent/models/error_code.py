from enum import Enum


class ErrorCode(str, Enum):
    ADDRESSTYPENOTFOUND = "AddressTypeNotFound"
    EMAILADDRESSTYPENOTFOUND = "EmailAddressTypeNotFound"
    PHONETYPENOTFOUND = "PhoneTypeNotFound"
    UNKNOWN = "Unknown"
    WEBADDRESSTYPENOTFOUND = "WebAddressTypeNotFound"

    def __str__(self) -> str:
        return str(self.value)

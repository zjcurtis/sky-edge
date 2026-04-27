from enum import Enum


class PhoneTypePhoneNumberType(str, Enum):
    EMAILADDRESS = "EmailAddress"
    FAXNUMBER = "FaxNumber"
    OTHER = "Other"
    TELEPHONENUMBER = "TelephoneNumber"
    WEBADDRESSURL = "WebAddressUrl"

    def __str__(self) -> str:
        return str(self.value)

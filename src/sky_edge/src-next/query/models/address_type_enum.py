from enum import Enum


class AddressTypeEnum(str, Enum):
    FIRSTINLIST = "FirstInList"
    NONE = "None"
    PREFERRED = "Preferred"
    PRIMARYBUSINESS = "PrimaryBusiness"
    SPECIFICADDRESSTYPE = "SpecificAddressType"
    SPOUSEPREFERRED = "SpousePreferred"
    SPOUSEPRIMARYBUSINESS = "SpousePrimaryBusiness"

    def __str__(self) -> str:
        return str(self.value)

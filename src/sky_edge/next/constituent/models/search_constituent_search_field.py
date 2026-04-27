from enum import Enum


class SearchConstituentSearchField(str, Enum):
    EMAIL_ADDRESS = "email_address"
    LOOKUP_ID = "lookup_id"

    def __str__(self) -> str:
        return str(self.value)

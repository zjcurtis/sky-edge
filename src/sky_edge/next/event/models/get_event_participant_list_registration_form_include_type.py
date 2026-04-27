from enum import Enum


class GetEventParticipantListRegistrationFormIncludeType(str, Enum):
    ANY = "Any"
    NONE = "None"
    SPECIFIC = "Specific"

    def __str__(self) -> str:
        return str(self.value)

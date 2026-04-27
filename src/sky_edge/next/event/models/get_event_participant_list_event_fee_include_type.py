from enum import Enum


class GetEventParticipantListEventFeeIncludeType(str, Enum):
    ANY = "Any"
    NONE = "None"
    SPECIFIC = "Specific"

    def __str__(self) -> str:
        return str(self.value)

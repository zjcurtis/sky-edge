from enum import Enum


class ConstituentEventParticipationRsvpStatus(str, Enum):
    ATTENDING = "Attending"
    CANCELED = "Canceled"
    DECLINED = "Declined"
    INTERESTED = "Interested"
    NORESPONSE = "NoResponse"
    NOTAPPLICABLE = "NotApplicable"
    WAITLISTED = "Waitlisted"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class GetConstituentEventParticipationRsvpStatusItem(str, Enum):
    ATTENDING = "Attending"
    CANCELED = "Canceled"
    DECLINED = "Declined"
    INTERESTED = "Interested"
    NORESPONSE = "NoResponse"
    NOTAPPLICABLE = "NotApplicable"
    WAITLISTED = "Waitlisted"

    def __str__(self) -> str:
        return str(self.value)

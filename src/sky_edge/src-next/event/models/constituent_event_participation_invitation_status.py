from enum import Enum


class ConstituentEventParticipationInvitationStatus(str, Enum):
    INVITED = "Invited"
    NOTAPPLICABLE = "NotApplicable"
    NOTINVITED = "NotInvited"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class ParticipantPledgeType(str, Enum):
    OTHERDONATION = "OtherDonation"
    REGISTRATIONFEE = "RegistrationFee"

    def __str__(self) -> str:
        return str(self.value)

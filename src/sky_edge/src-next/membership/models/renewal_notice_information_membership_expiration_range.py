from enum import Enum


class RenewalNoticeInformationMembershipExpirationRange(str, Enum):
    EXPIRESAFTER = "ExpiresAfter"
    EXPIRESBEFORE = "ExpiresBefore"

    def __str__(self) -> str:
        return str(self.value)

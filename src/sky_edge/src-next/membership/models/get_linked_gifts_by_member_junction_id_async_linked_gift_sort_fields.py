from enum import Enum


class GetLinkedGiftsByMemberJunctionIdAsyncLinkedGiftSortFields(str, Enum):
    APPLIEDAMOUNT = "AppliedAmount"
    GIFTDATE = "GiftDate"
    GIFTTYPE = "GiftType"

    def __str__(self) -> str:
        return str(self.value)

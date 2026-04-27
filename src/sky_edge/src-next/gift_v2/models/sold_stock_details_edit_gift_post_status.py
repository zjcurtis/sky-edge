from enum import Enum


class SoldStockDetailsEditGiftPostStatus(str, Enum):
    DONOTPOST = "DoNotPost"
    NOTPOSTED = "NotPosted"
    POSTED = "Posted"

    def __str__(self) -> str:
        return str(self.value)

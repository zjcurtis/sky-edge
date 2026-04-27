from enum import Enum


class BatchGiftAddWithTributeLookupGiftType(str, Enum):
    ADJUSTMENT = "Adjustment"
    AMENDMENT = "Amendment"
    GENERALLEDGERREVERSAL = "GeneralLedgerReversal"
    GIFTINKIND = "GiftInKind"
    MATCHINGGIFTPAYMENT = "MatchingGiftPayment"
    MATCHINGGIFTPLEDGE = "MatchingGiftPledge"
    MATCHINGGIFTWRITEOFF = "MatchingGiftWriteOff"
    NONE = "None"
    ONETIME = "OneTime"
    OTHER = "Other"
    PLANNEDGIFT = "PlannedGift"
    PLEDGE = "Pledge"
    PLEDGEPAYMENT = "PledgePayment"
    PLEDGEWRITEOFF = "PledgeWriteOff"
    RECURRINGGIFT = "RecurringGift"
    RECURRINGGIFTPAYMENT = "RecurringGiftPayment"
    SOLDSTOCK = "SoldStock"
    STOCK = "Stock"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class LinkedGiftGiftType(str, Enum):
    ADJUSTMENT = "Adjustment"
    AMENDMENT = "Amendment"
    CASH = "Cash"
    COVENANT = "Covenant"
    COVENANTPAYMENT = "CovenantPayment"
    COVENANTWRITEOFF = "CovenantWriteOff"
    GENERALLEDGERREVERSAL = "GeneralLedgerReversal"
    GIFTINKIND = "GiftInKind"
    MATCHINGGIFTPAYMENT = "MatchingGiftPayment"
    MATCHINGGIFTPLEDGE = "MatchingGiftPledge"
    MATCHINGGIFTWRITEOFF = "MatchingGiftWriteOff"
    NONE = "None"
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

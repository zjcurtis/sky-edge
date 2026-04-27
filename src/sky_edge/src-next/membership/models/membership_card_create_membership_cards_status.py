from enum import Enum


class MembershipCardCreateMembershipCardsStatus(str, Enum):
    DONOTPRINT = "DoNotPrint"
    LOST = "Lost"
    NOTPRINTED = "NotPrinted"
    PRINTED = "Printed"

    def __str__(self) -> str:
        return str(self.value)

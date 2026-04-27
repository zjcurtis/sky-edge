from enum import Enum


class MembershipCardEditMembershipCardExpires(str, Enum):
    LIFETIME = "Lifetime"
    ONEDAYAFTER = "OneDayAfter"
    ONEMONTHAFTER = "OneMonthAfter"
    ONEWEEKAFTER = "OneWeekAfter"
    SAMEDATES = "SameDates"
    SPECIFICDATES = "SpecificDates"
    THREEDAYSAFTER = "ThreeDaysAfter"
    THREEMONTHSAFTER = "ThreeMonthsAfter"
    TWODAYSAFTER = "TwoDaysAfter"
    TWOMONTHSAFTER = "TwoMonthsAfter"
    TWOWEEKSAFTER = "TwoWeeksAfter"

    def __str__(self) -> str:
        return str(self.value)

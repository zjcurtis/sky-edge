from enum import Enum


class AddressProcessingDateRange(str, Enum):
    ALLDATES = "AllDates"
    LASTDAYOFLASTCALENDARYEAR = "LastDayOfLastCalendarYear"
    LASTDAYOFLASTFISCALYEAR = "LastDayOfLastFiscalYear"
    LASTDAYOFLASTMONTH = "LastDayOfLastMonth"
    LASTDAYOFLASTQUARTER = "LastDayOfLastQuarter"
    LASTDAYOFLASTWEEK = "LastDayOfLastWeek"
    LASTDAYOFNEXTCALENDARYEAR = "LastDayOfNextCalendarYear"
    LASTDAYOFNEXTFISCALYEAR = "LastDayOfNextFiscalYear"
    LASTDAYOFNEXTMONTH = "LastDayOfNextMonth"
    LASTDAYOFNEXTQUARTER = "LastDayOfNextQuarter"
    LASTDAYOFNEXTWEEK = "LastDayOfNextWeek"
    LASTDAYOFTHISCALENDARYEAR = "LastDayOfThisCalendarYear"
    LASTDAYOFTHISFISCALYEAR = "LastDayOfThisFiscalYear"
    LASTDAYOFTHISMONTH = "LastDayOfThisMonth"
    LASTDAYOFTHISQUARTER = "LastDayOfThisQuarter"
    LASTDAYOFTHISWEEK = "LastDayOfThisWeek"
    SPECIFICDATE = "SpecificDate"
    TODAY = "Today"
    TOMORROW = "Tomorrow"
    YESTERDAY = "Yesterday"

    def __str__(self) -> str:
        return str(self.value)

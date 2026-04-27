from enum import Enum


class CountryCountryCurrencyPlacement(str, Enum):
    AFTER = "After"
    AFTERWITHSPACE = "AfterWithSpace"
    BEFORE = "Before"
    BEFOREWITHSPACE = "BeforeWithSpace"

    def __str__(self) -> str:
        return str(self.value)

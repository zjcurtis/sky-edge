from enum import Enum


class BatchGiftSoftCreditRecognitionCreditType(str, Enum):
    FUNDRAISER = "Fundraiser"
    NONE = "None"
    SOFTCREDIT = "SoftCredit"

    def __str__(self) -> str:
        return str(self.value)

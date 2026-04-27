from enum import Enum


class PhoneFormat(str, Enum):
    MASK1 = "Mask1"
    MASK10 = "Mask10"
    MASK11 = "Mask11"
    MASK2 = "Mask2"
    MASK3 = "Mask3"
    MASK4 = "Mask4"
    MASK5 = "Mask5"
    MASK6 = "Mask6"
    MASK7 = "Mask7"
    MASK8 = "Mask8"
    MASK9 = "Mask9"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)

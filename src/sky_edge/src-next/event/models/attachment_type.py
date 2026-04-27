from enum import Enum


class AttachmentType(str, Enum):
    LINK = "Link"
    PHYSICAL = "Physical"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class AttachmentAddType(str, Enum):
    LINK = "Link"
    PHYSICAL = "Physical"

    def __str__(self) -> str:
        return str(self.value)

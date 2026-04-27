from enum import Enum


class BlobContentDisposition(str, Enum):
    ATTACHMENT = "Attachment"
    INLINE = "Inline"

    def __str__(self) -> str:
        return str(self.value)

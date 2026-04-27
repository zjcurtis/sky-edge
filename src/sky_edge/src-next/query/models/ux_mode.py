from enum import Enum


class UXMode(str, Enum):
    ASYNCHRONOUS = "Asynchronous"
    SYNCHRONOUS = "Synchronous"

    def __str__(self) -> str:
        return str(self.value)

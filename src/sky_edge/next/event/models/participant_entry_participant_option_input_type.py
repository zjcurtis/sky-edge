from enum import Enum


class ParticipantEntryParticipantOptionInputType(str, Enum):
    BOOLEAN = "Boolean"
    LIST = "List"
    STRING = "String"

    def __str__(self) -> str:
        return str(self.value)

from enum import Enum


class NodeType(str, Enum):
    ONETOMANY = "OneToMany"
    ONETOONE = "OneToOne"
    SUMMARY = "Summary"

    def __str__(self) -> str:
        return str(self.value)

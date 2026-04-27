from enum import Enum


class ExecutionModes(str, Enum):
    ADHOC = "AdHoc"
    BOTH = "Both"
    BYID = "ById"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)

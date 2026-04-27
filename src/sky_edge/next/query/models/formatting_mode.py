from enum import Enum


class FormattingMode(str, Enum):
    EXPORT = "Export"
    NONE = "None"
    UI = "UI"

    def __str__(self) -> str:
        return str(self.value)

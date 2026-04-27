from enum import Enum


class IncludeReadUrl(str, Enum):
    NEVER = "Never"
    ONCECOMPLETED = "OnceCompleted"
    ONCERUNNING = "OnceRunning"

    def __str__(self) -> str:
        return str(self.value)

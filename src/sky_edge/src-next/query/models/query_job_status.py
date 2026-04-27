from enum import Enum


class QueryJobStatus(str, Enum):
    CANCELLED = "Cancelled"
    CANCELLING = "Cancelling"
    COMPLETED = "Completed"
    FAILED = "Failed"
    PENDING = "Pending"
    RUNNING = "Running"
    THROTTLED = "Throttled"

    def __str__(self) -> str:
        return str(self.value)

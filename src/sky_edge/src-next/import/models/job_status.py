from enum import Enum


class JobStatus(str, Enum):
    COMPLETED = "Completed"
    COMPLETEDWITHEXCEPTIONS = "CompletedWithExceptions"
    ENQUEUED = "Enqueued"
    FAILED = "Failed"
    PENDING = "Pending"
    RUNNING = "Running"
    STARTING = "Starting"

    def __str__(self) -> str:
        return str(self.value)

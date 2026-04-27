from enum import Enum


class SqlGenerationMode(str, Enum):
    EXPORT = "Export"
    QUERY = "Query"
    REPORT = "Report"

    def __str__(self) -> str:
        return str(self.value)

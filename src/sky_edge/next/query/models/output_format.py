from enum import Enum


class OutputFormat(str, Enum):
    CSV = "Csv"
    JSON = "Json"
    JSONL = "Jsonl"
    XLSX = "Xlsx"

    def __str__(self) -> str:
        return str(self.value)

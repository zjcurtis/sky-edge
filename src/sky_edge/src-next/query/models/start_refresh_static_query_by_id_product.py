from enum import Enum


class StartRefreshStaticQueryByIDProduct(str, Enum):
    FE = "FE"
    RE = "RE"

    def __str__(self) -> str:
        return str(self.value)

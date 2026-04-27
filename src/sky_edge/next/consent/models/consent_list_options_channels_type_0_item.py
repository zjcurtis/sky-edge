from enum import Enum


class ConsentListOptionsChannelsType0Item(str, Enum):
    AUTOPHONE = "AutoPhone"
    DATAPROCESSING = "DataProcessing"
    EMAIL = "Email"
    MAIL = "Mail"
    OTHER = "Other"
    PHONE = "Phone"
    SMS = "SMS"
    SOCIAL = "Social"

    def __str__(self) -> str:
        return str(self.value)

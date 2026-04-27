from enum import Enum


class CodeTableCategory(str, Enum):
    ACTION = "Action"
    ALL = "All"
    BIOGRAPHICAL = "Biographical"
    CFA = "CFA"
    EDUCATION = "Education"
    EVENTS = "Events"
    GIFT = "Gift"
    MEMBERSHIP = "Membership"
    PROSPECT = "Prospect"
    SOLICITOR = "Solicitor"
    VOLUNTEER = "Volunteer"
    WORKPLACEGIVING = "WorkplaceGiving"

    def __str__(self) -> str:
        return str(self.value)

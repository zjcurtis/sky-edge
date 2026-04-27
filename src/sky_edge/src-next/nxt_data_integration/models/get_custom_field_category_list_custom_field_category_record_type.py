from enum import Enum


class GetCustomFieldCategoryListCustomFieldCategoryRecordType(str, Enum):
    ACCOUNT = "Account"
    ACTION = "Action"
    ADDRESS = "Address"
    APPEAL = "Appeal"
    CAMPAIGN = "Campaign"
    CONSTITUENT = "Constituent"
    EDUCATION = "Education"
    EVENT = "Event"
    FUND = "Fund"
    GIFT = "Gift"
    INDIVIDUALRELATIONSHIP = "IndividualRelationship"
    JOB = "Job"
    MEMBERSHIP = "Membership"
    ORGANIZATIONRELATIONSHIP = "OrganizationRelationship"
    PACKAGE = "Package"
    PARTICIPANT = "Participant"
    PROPOSAL = "Proposal"

    def __str__(self) -> str:
        return str(self.value)

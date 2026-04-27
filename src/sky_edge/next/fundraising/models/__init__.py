"""Contains all the data models used in inputs/outputs"""

from .api_collection import ApiCollection
from .api_collection_appeal_read import ApiCollectionAppealRead
from .api_collection_attachment_read import ApiCollectionAttachmentRead
from .api_collection_campaign_read import ApiCollectionCampaignRead
from .api_collection_custom_field_category_read import (
    ApiCollectionCustomFieldCategoryRead,
)
from .api_collection_custom_field_read import ApiCollectionCustomFieldRead
from .api_collection_fund_read import ApiCollectionFundRead
from .api_collection_fundraiser_assignment_read import (
    ApiCollectionFundraiserAssignmentRead,
)
from .api_collection_goal_read import ApiCollectionGoalRead
from .api_collection_package_read import ApiCollectionPackageRead
from .api_collection_string import ApiCollectionString
from .api_collection_value_item import ApiCollectionValueItem
from .appeal_read import AppealRead
from .attachment_add import AttachmentAdd
from .attachment_add_type import AttachmentAddType
from .attachment_edit import AttachmentEdit
from .attachment_read import AttachmentRead
from .attachment_read_type import AttachmentReadType
from .campaign_read import CampaignRead
from .currency import Currency
from .custom_field_add import CustomFieldAdd
from .custom_field_add_value import CustomFieldAddValue
from .custom_field_category_read import CustomFieldCategoryRead
from .custom_field_category_read_type import CustomFieldCategoryReadType
from .custom_field_edit import CustomFieldEdit
from .custom_field_edit_value import CustomFieldEditValue
from .custom_field_read import CustomFieldRead
from .custom_field_read_type import CustomFieldReadType
from .custom_field_read_value import CustomFieldReadValue
from .file_definition import FileDefinition
from .fund_read import FundRead
from .fundraiser_assignment_add import FundraiserAssignmentAdd
from .fundraiser_assignment_edit import FundraiserAssignmentEdit
from .fundraiser_assignment_read import FundraiserAssignmentRead
from .goal_add import GoalAdd
from .goal_add_type import GoalAddType
from .goal_edit import GoalEdit
from .goal_edit_type import GoalEditType
from .goal_read import GoalRead
from .goal_read_type import GoalReadType
from .header import Header
from .new_document_info import NewDocumentInfo
from .package_read import PackageRead
from .post_response import PostResponse
from .request_meta_data import RequestMetaData

__all__ = (
    "ApiCollection",
    "ApiCollectionAppealRead",
    "ApiCollectionAttachmentRead",
    "ApiCollectionCampaignRead",
    "ApiCollectionCustomFieldCategoryRead",
    "ApiCollectionCustomFieldRead",
    "ApiCollectionFundraiserAssignmentRead",
    "ApiCollectionFundRead",
    "ApiCollectionGoalRead",
    "ApiCollectionPackageRead",
    "ApiCollectionString",
    "ApiCollectionValueItem",
    "AppealRead",
    "AttachmentAdd",
    "AttachmentAddType",
    "AttachmentEdit",
    "AttachmentRead",
    "AttachmentReadType",
    "CampaignRead",
    "Currency",
    "CustomFieldAdd",
    "CustomFieldAddValue",
    "CustomFieldCategoryRead",
    "CustomFieldCategoryReadType",
    "CustomFieldEdit",
    "CustomFieldEditValue",
    "CustomFieldRead",
    "CustomFieldReadType",
    "CustomFieldReadValue",
    "FileDefinition",
    "FundraiserAssignmentAdd",
    "FundraiserAssignmentEdit",
    "FundraiserAssignmentRead",
    "FundRead",
    "GoalAdd",
    "GoalAddType",
    "GoalEdit",
    "GoalEditType",
    "GoalRead",
    "GoalReadType",
    "Header",
    "NewDocumentInfo",
    "PackageRead",
    "PostResponse",
    "RequestMetaData",
)

"""Contains all the data models used in inputs/outputs"""

from .api_collection import ApiCollection
from .api_collection_attachment_read import ApiCollectionAttachmentRead
from .api_collection_custom_field_category_read import (
    ApiCollectionCustomFieldCategoryRead,
)
from .api_collection_custom_field_read import ApiCollectionCustomFieldRead
from .api_collection_opportunity_read import ApiCollectionOpportunityRead
from .api_collection_opportunity_status_history import (
    ApiCollectionOpportunityStatusHistory,
)
from .api_collection_string import ApiCollectionString
from .api_collection_value_item import ApiCollectionValueItem
from .attachment_add import AttachmentAdd
from .attachment_add_type import AttachmentAddType
from .attachment_edit import AttachmentEdit
from .attachment_read import AttachmentRead
from .attachment_read_type import AttachmentReadType
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
from .fundraiser import Fundraiser
from .header import Header
from .new_document_info import NewDocumentInfo
from .opportunity_add import OpportunityAdd
from .opportunity_edit import OpportunityEdit
from .opportunity_read import OpportunityRead
from .opportunity_status_history import OpportunityStatusHistory
from .post_response import PostResponse
from .request_meta_data import RequestMetaData

__all__ = (
    "ApiCollection",
    "ApiCollectionAttachmentRead",
    "ApiCollectionCustomFieldCategoryRead",
    "ApiCollectionCustomFieldRead",
    "ApiCollectionOpportunityRead",
    "ApiCollectionOpportunityStatusHistory",
    "ApiCollectionString",
    "ApiCollectionValueItem",
    "AttachmentAdd",
    "AttachmentAddType",
    "AttachmentEdit",
    "AttachmentRead",
    "AttachmentReadType",
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
    "Fundraiser",
    "Header",
    "NewDocumentInfo",
    "OpportunityAdd",
    "OpportunityEdit",
    "OpportunityRead",
    "OpportunityStatusHistory",
    "PostResponse",
    "RequestMetaData",
)

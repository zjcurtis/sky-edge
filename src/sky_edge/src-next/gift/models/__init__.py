"""Contains all the data models used in inputs/outputs"""

from .acknowledgement_add import AcknowledgementAdd
from .acknowledgement_edit import AcknowledgementEdit
from .acknowledgement_read import AcknowledgementRead
from .api_collection import ApiCollection
from .api_collection_attachment_read import ApiCollectionAttachmentRead
from .api_collection_custom_field_category_read import ApiCollectionCustomFieldCategoryRead
from .api_collection_custom_field_read import ApiCollectionCustomFieldRead
from .api_collection_gift_read import ApiCollectionGiftRead
from .api_collection_string import ApiCollectionString
from .api_collection_value_item import ApiCollectionValueItem
from .attachment_add import AttachmentAdd
from .attachment_add_type import AttachmentAddType
from .attachment_edit import AttachmentEdit
from .attachment_read import AttachmentRead
from .attachment_read_type import AttachmentReadType
from .batch_gift_add_results import BatchGiftAddResults
from .batch_gift_read import BatchGiftRead
from .currency import Currency
from .custom_field_add import CustomFieldAdd
from .custom_field_add_value import CustomFieldAddValue
from .custom_field_category_add import CustomFieldCategoryAdd
from .custom_field_category_add_type import CustomFieldCategoryAddType
from .custom_field_category_read import CustomFieldCategoryRead
from .custom_field_category_read_type import CustomFieldCategoryReadType
from .custom_field_edit import CustomFieldEdit
from .custom_field_edit_value import CustomFieldEditValue
from .custom_field_read import CustomFieldRead
from .custom_field_read_type import CustomFieldReadType
from .custom_field_read_value import CustomFieldReadValue
from .file_definition import FileDefinition
from .fuzzy_date import FuzzyDate
from .gift_add import GiftAdd
from .gift_batch_gift_add import GiftBatchGiftAdd
from .gift_batch_gift_error import GiftBatchGiftError
from .gift_edit import GiftEdit
from .gift_fundraiser_add import GiftFundraiserAdd
from .gift_fundraiser_read import GiftFundraiserRead
from .gift_list_options import GiftListOptions
from .gift_marketing_detail_edit import GiftMarketingDetailEdit
from .gift_read import GiftRead
from .gift_split_add import GiftSplitAdd
from .gift_split_read import GiftSplitRead
from .giftacknowledgements_acknowledgement_id_patch_200_application_json_response import (
    GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse,
)
from .giftreceipts_receipt_id_patch_200_application_json_response import (
    GiftreceiptsReceiptIdPatch200ApplicationJsonResponse,
)
from .gifts_add import GiftsAdd
from .gifts_gift_id_patch_200_application_json_response import GiftsGiftIdPatch200ApplicationJsonResponse
from .header import Header
from .new_document_info import NewDocumentInfo
from .payment_add import PaymentAdd
from .payment_read import PaymentRead
from .post_response import PostResponse
from .receipt_add import ReceiptAdd
from .receipt_edit import ReceiptEdit
from .receipt_read import ReceiptRead
from .recurring_gift_conversion_check import RecurringGiftConversionCheck
from .recurring_gift_conversion_error import RecurringGiftConversionError
from .recurring_gift_conversion_options import RecurringGiftConversionOptions
from .recurring_gift_schedule_add import RecurringGiftScheduleAdd
from .recurring_gift_schedule_read import RecurringGiftScheduleRead
from .recurring_gift_status_edit import RecurringGiftStatusEdit
from .request_meta_data import RequestMetaData
from .soft_credit_add import SoftCreditAdd
from .soft_credit_read import SoftCreditRead
from .tribute_acknowledgee_add import TributeAcknowledgeeAdd
from .tribute_acknowledgee_read import TributeAcknowledgeeRead
from .tribute_add import TributeAdd
from .tribute_read import TributeRead

__all__ = (
    "AcknowledgementAdd",
    "AcknowledgementEdit",
    "AcknowledgementRead",
    "ApiCollection",
    "ApiCollectionAttachmentRead",
    "ApiCollectionCustomFieldCategoryRead",
    "ApiCollectionCustomFieldRead",
    "ApiCollectionGiftRead",
    "ApiCollectionString",
    "ApiCollectionValueItem",
    "AttachmentAdd",
    "AttachmentAddType",
    "AttachmentEdit",
    "AttachmentRead",
    "AttachmentReadType",
    "BatchGiftAddResults",
    "BatchGiftRead",
    "Currency",
    "CustomFieldAdd",
    "CustomFieldAddValue",
    "CustomFieldCategoryAdd",
    "CustomFieldCategoryAddType",
    "CustomFieldCategoryRead",
    "CustomFieldCategoryReadType",
    "CustomFieldEdit",
    "CustomFieldEditValue",
    "CustomFieldRead",
    "CustomFieldReadType",
    "CustomFieldReadValue",
    "FileDefinition",
    "FuzzyDate",
    "GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse",
    "GiftAdd",
    "GiftBatchGiftAdd",
    "GiftBatchGiftError",
    "GiftEdit",
    "GiftFundraiserAdd",
    "GiftFundraiserRead",
    "GiftListOptions",
    "GiftMarketingDetailEdit",
    "GiftRead",
    "GiftreceiptsReceiptIdPatch200ApplicationJsonResponse",
    "GiftsAdd",
    "GiftsGiftIdPatch200ApplicationJsonResponse",
    "GiftSplitAdd",
    "GiftSplitRead",
    "Header",
    "NewDocumentInfo",
    "PaymentAdd",
    "PaymentRead",
    "PostResponse",
    "ReceiptAdd",
    "ReceiptEdit",
    "ReceiptRead",
    "RecurringGiftConversionCheck",
    "RecurringGiftConversionError",
    "RecurringGiftConversionOptions",
    "RecurringGiftScheduleAdd",
    "RecurringGiftScheduleRead",
    "RecurringGiftStatusEdit",
    "RequestMetaData",
    "SoftCreditAdd",
    "SoftCreditRead",
    "TributeAcknowledgeeAdd",
    "TributeAcknowledgeeRead",
    "TributeAdd",
    "TributeRead",
)

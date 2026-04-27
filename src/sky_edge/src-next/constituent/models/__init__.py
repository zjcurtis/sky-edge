"""Contains all the data models used in inputs/outputs"""

from .action_add import ActionAdd
from .action_add_direction import ActionAddDirection
from .action_add_outcome import ActionAddOutcome
from .action_add_priority import ActionAddPriority
from .action_edit import ActionEdit
from .action_edit_direction import ActionEditDirection
from .action_edit_outcome import ActionEditOutcome
from .action_edit_priority import ActionEditPriority
from .action_read import ActionRead
from .action_read_computed_status import ActionReadComputedStatus
from .action_read_direction import ActionReadDirection
from .action_read_outcome import ActionReadOutcome
from .action_read_priority import ActionReadPriority
from .address_add import AddressAdd
from .address_edit import AddressEdit
from .address_read import AddressRead
from .address_read_extended import AddressReadExtended
from .alias_add import AliasAdd
from .alias_add_collection import AliasAddCollection
from .alias_add_collection_alias import AliasAddCollectionAlias
from .alias_edit import AliasEdit
from .alias_read import AliasRead
from .api_collection import ApiCollection
from .api_collection_of_action_read import ApiCollectionOfActionRead
from .api_collection_of_address_read import ApiCollectionOfAddressRead
from .api_collection_of_address_read_extended import ApiCollectionOfAddressReadExtended
from .api_collection_of_alias_read import ApiCollectionOfAliasRead
from .api_collection_of_attachment_read import ApiCollectionOfAttachmentRead
from .api_collection_of_communication_preference_read import ApiCollectionOfCommunicationPreferenceRead
from .api_collection_of_constituent_appeal_read import ApiCollectionOfConstituentAppealRead
from .api_collection_of_constituent_code_read import ApiCollectionOfConstituentCodeRead
from .api_collection_of_constituent_fundraiser_read import ApiCollectionOfConstituentFundraiserRead
from .api_collection_of_constituent_list_item import ApiCollectionOfConstituentListItem
from .api_collection_of_country_read import ApiCollectionOfCountryRead
from .api_collection_of_custom_field_category_read import ApiCollectionOfCustomFieldCategoryRead
from .api_collection_of_custom_field_read import ApiCollectionOfCustomFieldRead
from .api_collection_of_duplicate_search_result_read import ApiCollectionOfDuplicateSearchResultRead
from .api_collection_of_education_read import ApiCollectionOfEducationRead
from .api_collection_of_email_address_read import ApiCollectionOfEmailAddressRead
from .api_collection_of_fundraiser_assignment_read import ApiCollectionOfFundraiserAssignmentRead
from .api_collection_of_membership_read import ApiCollectionOfMembershipRead
from .api_collection_of_name_format_configuration_read import ApiCollectionOfNameFormatConfigurationRead
from .api_collection_of_note_read import ApiCollectionOfNoteRead
from .api_collection_of_online_presence_read import ApiCollectionOfOnlinePresenceRead
from .api_collection_of_parented_note_read import ApiCollectionOfParentedNoteRead
from .api_collection_of_phone_read import ApiCollectionOfPhoneRead
from .api_collection_of_prospect_status_history import ApiCollectionOfProspectStatusHistory
from .api_collection_of_rating_category_read import ApiCollectionOfRatingCategoryRead
from .api_collection_of_rating_read import ApiCollectionOfRatingRead
from .api_collection_of_rating_source_read import ApiCollectionOfRatingSourceRead
from .api_collection_of_relationship_read import ApiCollectionOfRelationshipRead
from .api_collection_of_search_result_read import ApiCollectionOfSearchResultRead
from .api_collection_of_string import ApiCollectionOfString
from .api_collection_value_item import ApiCollectionValueItem
from .appeal_category_read import AppealCategoryRead
from .appeal_read import AppealRead
from .attachment_add import AttachmentAdd
from .attachment_add_type import AttachmentAddType
from .attachment_edit import AttachmentEdit
from .attachment_read import AttachmentRead
from .attachment_read_type import AttachmentReadType
from .campaign_read import CampaignRead
from .communication_preference_add import CommunicationPreferenceAdd
from .communication_preference_edit import CommunicationPreferenceEdit
from .communication_preference_read import CommunicationPreferenceRead
from .constituent_add import ConstituentAdd
from .constituent_add_receipt_type import ConstituentAddReceiptType
from .constituent_add_type import ConstituentAddType
from .constituent_address_add import ConstituentAddressAdd
from .constituent_appeal_read import ConstituentAppealRead
from .constituent_assigned_fundraiser import ConstituentAssignedFundraiser
from .constituent_code_add import ConstituentCodeAdd
from .constituent_code_edit import ConstituentCodeEdit
from .constituent_code_link import ConstituentCodeLink
from .constituent_code_read import ConstituentCodeRead
from .constituent_edit import ConstituentEdit
from .constituent_edit_receipt_type import ConstituentEditReceiptType
from .constituent_email_address_add import ConstituentEmailAddressAdd
from .constituent_fundraiser_read import ConstituentFundraiserRead
from .constituent_list_item import ConstituentListItem
from .constituent_list_item_fundraiser_status import ConstituentListItemFundraiserStatus
from .constituent_list_item_type import ConstituentListItemType
from .constituent_online_presence_add import ConstituentOnlinePresenceAdd
from .constituent_phone_add import ConstituentPhoneAdd
from .constituent_read import ConstituentRead
from .constituent_read_fundraiser_status import ConstituentReadFundraiserStatus
from .constituent_read_receipt_type import ConstituentReadReceiptType
from .constituent_read_type import ConstituentReadType
from .country_read import CountryRead
from .currency import Currency
from .currency_configuration_read import CurrencyConfigurationRead
from .custom_field_add import CustomFieldAdd
from .custom_field_add_value import CustomFieldAddValue
from .custom_field_category_read import CustomFieldCategoryRead
from .custom_field_category_read_type import CustomFieldCategoryReadType
from .custom_field_edit import CustomFieldEdit
from .custom_field_edit_value import CustomFieldEditValue
from .custom_field_read import CustomFieldRead
from .custom_field_read_type import CustomFieldReadType
from .custom_field_read_value import CustomFieldReadValue
from .duplicate_search_result_read import DuplicateSearchResultRead
from .education_add import EducationAdd
from .education_edit import EducationEdit
from .education_read import EducationRead
from .email_address_add import EmailAddressAdd
from .email_address_edit import EmailAddressEdit
from .email_address_read import EmailAddressRead
from .error_code import ErrorCode
from .file_definition import FileDefinition
from .fund_read import FundRead
from .fundraiser_assignment_read import FundraiserAssignmentRead
from .fuzzy_date import FuzzyDate
from .giving_summary_read import GivingSummaryRead
from .header import Header
from .lifetime_giving_read import LifetimeGivingRead
from .list_actions_all_constituents_computed_status_item import ListActionsAllConstituentsComputedStatusItem
from .membership_member_read import MembershipMemberRead
from .membership_read import MembershipRead
from .membership_read_standing import MembershipReadStanding
from .name_format_add import NameFormatAdd
from .name_format_configuration_read import NameFormatConfigurationRead
from .name_format_edit import NameFormatEdit
from .name_format_read import NameFormatRead
from .name_format_summary_read import NameFormatSummaryRead
from .new_document_info import NewDocumentInfo
from .non_constituent_add import NonConstituentAdd
from .non_constituent_add_type import NonConstituentAddType
from .non_constituent_conversion import NonConstituentConversion
from .note_add import NoteAdd
from .note_edit import NoteEdit
from .note_read import NoteRead
from .online_presence_add import OnlinePresenceAdd
from .online_presence_edit import OnlinePresenceEdit
from .online_presence_read import OnlinePresenceRead
from .package_read import PackageRead
from .parented_note_add import ParentedNoteAdd
from .parented_note_edit import ParentedNoteEdit
from .parented_note_read import ParentedNoteRead
from .phone_add import PhoneAdd
from .phone_add_collection import PhoneAddCollection
from .phone_add_collection_phone import PhoneAddCollectionPhone
from .phone_edit import PhoneEdit
from .phone_read import PhoneRead
from .post_response import PostResponse
from .primary_name_format_add import PrimaryNameFormatAdd
from .primary_name_format_add_primary_type import PrimaryNameFormatAddPrimaryType
from .primary_name_format_edit import PrimaryNameFormatEdit
from .primary_name_format_read import PrimaryNameFormatRead
from .primary_name_format_read_primary_type import PrimaryNameFormatReadPrimaryType
from .profile_picture_edit import ProfilePictureEdit
from .profile_picture_read import ProfilePictureRead
from .prospect_status_history import ProspectStatusHistory
from .prospect_status_read import ProspectStatusRead
from .rating_add import RatingAdd
from .rating_add_value import RatingAddValue
from .rating_category_read import RatingCategoryRead
from .rating_category_read_type import RatingCategoryReadType
from .rating_edit import RatingEdit
from .rating_edit_value import RatingEditValue
from .rating_read import RatingRead
from .rating_read_type import RatingReadType
from .rating_read_value import RatingReadValue
from .rating_source_read import RatingSourceRead
from .relationship_add import RelationshipAdd
from .relationship_edit import RelationshipEdit
from .relationship_read import RelationshipRead
from .request_meta_data import RequestMetaData
from .search_constituent_search_field import SearchConstituentSearchField
from .search_result_read import SearchResultRead
from .spouse_read import SpouseRead

__all__ = (
    "ActionAdd",
    "ActionAddDirection",
    "ActionAddOutcome",
    "ActionAddPriority",
    "ActionEdit",
    "ActionEditDirection",
    "ActionEditOutcome",
    "ActionEditPriority",
    "ActionRead",
    "ActionReadComputedStatus",
    "ActionReadDirection",
    "ActionReadOutcome",
    "ActionReadPriority",
    "AddressAdd",
    "AddressEdit",
    "AddressRead",
    "AddressReadExtended",
    "AliasAdd",
    "AliasAddCollection",
    "AliasAddCollectionAlias",
    "AliasEdit",
    "AliasRead",
    "ApiCollection",
    "ApiCollectionOfActionRead",
    "ApiCollectionOfAddressRead",
    "ApiCollectionOfAddressReadExtended",
    "ApiCollectionOfAliasRead",
    "ApiCollectionOfAttachmentRead",
    "ApiCollectionOfCommunicationPreferenceRead",
    "ApiCollectionOfConstituentAppealRead",
    "ApiCollectionOfConstituentCodeRead",
    "ApiCollectionOfConstituentFundraiserRead",
    "ApiCollectionOfConstituentListItem",
    "ApiCollectionOfCountryRead",
    "ApiCollectionOfCustomFieldCategoryRead",
    "ApiCollectionOfCustomFieldRead",
    "ApiCollectionOfDuplicateSearchResultRead",
    "ApiCollectionOfEducationRead",
    "ApiCollectionOfEmailAddressRead",
    "ApiCollectionOfFundraiserAssignmentRead",
    "ApiCollectionOfMembershipRead",
    "ApiCollectionOfNameFormatConfigurationRead",
    "ApiCollectionOfNoteRead",
    "ApiCollectionOfOnlinePresenceRead",
    "ApiCollectionOfParentedNoteRead",
    "ApiCollectionOfPhoneRead",
    "ApiCollectionOfProspectStatusHistory",
    "ApiCollectionOfRatingCategoryRead",
    "ApiCollectionOfRatingRead",
    "ApiCollectionOfRatingSourceRead",
    "ApiCollectionOfRelationshipRead",
    "ApiCollectionOfSearchResultRead",
    "ApiCollectionOfString",
    "ApiCollectionValueItem",
    "AppealCategoryRead",
    "AppealRead",
    "AttachmentAdd",
    "AttachmentAddType",
    "AttachmentEdit",
    "AttachmentRead",
    "AttachmentReadType",
    "CampaignRead",
    "CommunicationPreferenceAdd",
    "CommunicationPreferenceEdit",
    "CommunicationPreferenceRead",
    "ConstituentAdd",
    "ConstituentAddReceiptType",
    "ConstituentAddressAdd",
    "ConstituentAddType",
    "ConstituentAppealRead",
    "ConstituentAssignedFundraiser",
    "ConstituentCodeAdd",
    "ConstituentCodeEdit",
    "ConstituentCodeLink",
    "ConstituentCodeRead",
    "ConstituentEdit",
    "ConstituentEditReceiptType",
    "ConstituentEmailAddressAdd",
    "ConstituentFundraiserRead",
    "ConstituentListItem",
    "ConstituentListItemFundraiserStatus",
    "ConstituentListItemType",
    "ConstituentOnlinePresenceAdd",
    "ConstituentPhoneAdd",
    "ConstituentRead",
    "ConstituentReadFundraiserStatus",
    "ConstituentReadReceiptType",
    "ConstituentReadType",
    "CountryRead",
    "Currency",
    "CurrencyConfigurationRead",
    "CustomFieldAdd",
    "CustomFieldAddValue",
    "CustomFieldCategoryRead",
    "CustomFieldCategoryReadType",
    "CustomFieldEdit",
    "CustomFieldEditValue",
    "CustomFieldRead",
    "CustomFieldReadType",
    "CustomFieldReadValue",
    "DuplicateSearchResultRead",
    "EducationAdd",
    "EducationEdit",
    "EducationRead",
    "EmailAddressAdd",
    "EmailAddressEdit",
    "EmailAddressRead",
    "ErrorCode",
    "FileDefinition",
    "FundraiserAssignmentRead",
    "FundRead",
    "FuzzyDate",
    "GivingSummaryRead",
    "Header",
    "LifetimeGivingRead",
    "ListActionsAllConstituentsComputedStatusItem",
    "MembershipMemberRead",
    "MembershipRead",
    "MembershipReadStanding",
    "NameFormatAdd",
    "NameFormatConfigurationRead",
    "NameFormatEdit",
    "NameFormatRead",
    "NameFormatSummaryRead",
    "NewDocumentInfo",
    "NonConstituentAdd",
    "NonConstituentAddType",
    "NonConstituentConversion",
    "NoteAdd",
    "NoteEdit",
    "NoteRead",
    "OnlinePresenceAdd",
    "OnlinePresenceEdit",
    "OnlinePresenceRead",
    "PackageRead",
    "ParentedNoteAdd",
    "ParentedNoteEdit",
    "ParentedNoteRead",
    "PhoneAdd",
    "PhoneAddCollection",
    "PhoneAddCollectionPhone",
    "PhoneEdit",
    "PhoneRead",
    "PostResponse",
    "PrimaryNameFormatAdd",
    "PrimaryNameFormatAddPrimaryType",
    "PrimaryNameFormatEdit",
    "PrimaryNameFormatRead",
    "PrimaryNameFormatReadPrimaryType",
    "ProfilePictureEdit",
    "ProfilePictureRead",
    "ProspectStatusHistory",
    "ProspectStatusRead",
    "RatingAdd",
    "RatingAddValue",
    "RatingCategoryRead",
    "RatingCategoryReadType",
    "RatingEdit",
    "RatingEditValue",
    "RatingRead",
    "RatingReadType",
    "RatingReadValue",
    "RatingSourceRead",
    "RelationshipAdd",
    "RelationshipEdit",
    "RelationshipRead",
    "RequestMetaData",
    "SearchConstituentSearchField",
    "SearchResultRead",
    "SpouseRead",
)

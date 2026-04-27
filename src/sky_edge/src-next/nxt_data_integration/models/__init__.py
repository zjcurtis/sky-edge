"""Contains all the data models used in inputs/outputs"""

from .appeal import Appeal
from .appeal_collection import AppealCollection
from .appeal_create import AppealCreate
from .appeal_edit import AppealEdit
from .campaign import Campaign
from .campaign_collection import CampaignCollection
from .campaign_create import CampaignCreate
from .campaign_edit import CampaignEdit
from .code_table import CodeTable
from .code_table_collection import CodeTableCollection
from .code_table_create import CodeTableCreate
from .code_table_edit import CodeTableEdit
from .constituent import Constituent
from .constituent_appeal_create import ConstituentAppealCreate
from .constituent_appeal_edit import ConstituentAppealEdit
from .constituent_by_fund_collection import ConstituentByFundCollection
from .constituent_collection import ConstituentCollection
from .constituent_id_map import ConstituentIdMap
from .constituent_id_map_fundraiser_status import ConstituentIdMapFundraiserStatus
from .constituent_search_result import ConstituentSearchResult
from .country import Country
from .country_collection import CountryCollection
from .country_country_code import CountryCountryCode
from .country_country_currency_placement import CountryCountryCurrencyPlacement
from .country_create import CountryCreate
from .country_create_country_code import CountryCreateCountryCode
from .country_create_country_currency_placement import CountryCreateCountryCurrencyPlacement
from .country_create_re7_country_codes import CountryCreateRE7CountryCodes
from .country_edit import CountryEdit
from .country_edit_country_code import CountryEditCountryCode
from .country_edit_country_currency_placement import CountryEditCountryCurrencyPlacement
from .country_edit_re7_country_codes import CountryEditRE7CountryCodes
from .country_re7_country_codes import CountryRE7CountryCodes
from .custom_field_category import CustomFieldCategory
from .custom_field_category_collection import CustomFieldCategoryCollection
from .custom_field_category_create import CustomFieldCategoryCreate
from .custom_field_category_create_custom_field_category_data_type import (
    CustomFieldCategoryCreateCustomFieldCategoryDataType,
)
from .custom_field_category_create_custom_field_category_record_type import (
    CustomFieldCategoryCreateCustomFieldCategoryRecordType,
)
from .custom_field_category_custom_field_category_data_type import CustomFieldCategoryCustomFieldCategoryDataType
from .custom_field_category_custom_field_category_record_type import CustomFieldCategoryCustomFieldCategoryRecordType
from .custom_field_category_edit import CustomFieldCategoryEdit
from .custom_field_category_edit_custom_field_category_data_type import (
    CustomFieldCategoryEditCustomFieldCategoryDataType,
)
from .custom_field_category_edit_custom_field_category_record_type import (
    CustomFieldCategoryEditCustomFieldCategoryRecordType,
)
from .fund import Fund
from .fund_collection import FundCollection
from .fund_create import FundCreate
from .fund_edit import FundEdit
from .fuzzy_date import FuzzyDate
from .get_custom_field_category_list_custom_field_category_record_type import (
    GetCustomFieldCategoryListCustomFieldCategoryRecordType,
)
from .get_phone_types_list_phone_format import GetPhoneTypesListPhoneFormat
from .get_phone_types_list_phone_number_type import GetPhoneTypesListPhoneNumberType
from .gift_aid_tax_declaration import GiftAidTaxDeclaration
from .gift_aid_tax_declaration_collection import GiftAidTaxDeclarationCollection
from .gift_aid_tax_declaration_create import GiftAidTaxDeclarationCreate
from .gift_aid_tax_declaration_create_gift_aid_pays_tax import GiftAidTaxDeclarationCreateGiftAidPaysTax
from .gift_aid_tax_declaration_edit import GiftAidTaxDeclarationEdit
from .gift_aid_tax_declaration_edit_gift_aid_pays_tax import GiftAidTaxDeclarationEditGiftAidPaysTax
from .gift_aid_tax_declaration_gift_aid_pays_tax import GiftAidTaxDeclarationGiftAidPaysTax
from .gift_id_map import GiftIdMap
from .gift_note import GiftNote
from .gift_note_collection import GiftNoteCollection
from .gift_note_create import GiftNoteCreate
from .gift_note_edit import GiftNoteEdit
from .gift_tribute import GiftTribute
from .gift_tribute_acknowledge_status import GiftTributeAcknowledgeStatus
from .gift_tribute_acknowledgee import GiftTributeAcknowledgee
from .gift_tribute_acknowledgee_collection import GiftTributeAcknowledgeeCollection
from .gift_tribute_acknowledgee_edit import GiftTributeAcknowledgeeEdit
from .gift_tribute_collection import GiftTributeCollection
from .gift_tribute_create import GiftTributeCreate
from .gift_tribute_edit import GiftTributeEdit
from .gift_tribute_edit_acknowledge_status import GiftTributeEditAcknowledgeStatus
from .import_id_map import ImportIdMap
from .name_format_configuration import NameFormatConfiguration
from .name_format_configuration_collection import NameFormatConfigurationCollection
from .name_format_configuration_create import NameFormatConfigurationCreate
from .name_format_configuration_edit import NameFormatConfigurationEdit
from .name_format_configuration_field import NameFormatConfigurationField
from .name_format_configuration_field_collection import NameFormatConfigurationFieldCollection
from .name_format_configuration_field_create import NameFormatConfigurationFieldCreate
from .name_format_configuration_field_detail import NameFormatConfigurationFieldDetail
from .name_format_configuration_field_edit import NameFormatConfigurationFieldEdit
from .name_format_configuration_for_list import NameFormatConfigurationForList
from .phone_type import PhoneType
from .phone_type_collection import PhoneTypeCollection
from .phone_type_create import PhoneTypeCreate
from .phone_type_create_phone_format import PhoneTypeCreatePhoneFormat
from .phone_type_create_phone_number_type import PhoneTypeCreatePhoneNumberType
from .phone_type_edit import PhoneTypeEdit
from .phone_type_edit_phone_format import PhoneTypeEditPhoneFormat
from .phone_type_edit_phone_number_type import PhoneTypeEditPhoneNumberType
from .phone_type_phone_format import PhoneTypePhoneFormat
from .phone_type_phone_number_type import PhoneTypePhoneNumberType
from .post_response import PostResponse
from .relationship import Relationship
from .relationship_collection import RelationshipCollection
from .table_entry import TableEntry
from .table_entry_collection import TableEntryCollection
from .table_entry_create import TableEntryCreate
from .table_entry_edit import TableEntryEdit
from .tribute import Tribute
from .tribute_acknowledgee import TributeAcknowledgee
from .tribute_acknowledgee_collection import TributeAcknowledgeeCollection
from .tribute_acknowledgee_create import TributeAcknowledgeeCreate
from .tribute_collection import TributeCollection
from .tribute_create import TributeCreate
from .user import User

__all__ = (
    "Appeal",
    "AppealCollection",
    "AppealCreate",
    "AppealEdit",
    "Campaign",
    "CampaignCollection",
    "CampaignCreate",
    "CampaignEdit",
    "CodeTable",
    "CodeTableCollection",
    "CodeTableCreate",
    "CodeTableEdit",
    "Constituent",
    "ConstituentAppealCreate",
    "ConstituentAppealEdit",
    "ConstituentByFundCollection",
    "ConstituentCollection",
    "ConstituentIdMap",
    "ConstituentIdMapFundraiserStatus",
    "ConstituentSearchResult",
    "Country",
    "CountryCollection",
    "CountryCountryCode",
    "CountryCountryCurrencyPlacement",
    "CountryCreate",
    "CountryCreateCountryCode",
    "CountryCreateCountryCurrencyPlacement",
    "CountryCreateRE7CountryCodes",
    "CountryEdit",
    "CountryEditCountryCode",
    "CountryEditCountryCurrencyPlacement",
    "CountryEditRE7CountryCodes",
    "CountryRE7CountryCodes",
    "CustomFieldCategory",
    "CustomFieldCategoryCollection",
    "CustomFieldCategoryCreate",
    "CustomFieldCategoryCreateCustomFieldCategoryDataType",
    "CustomFieldCategoryCreateCustomFieldCategoryRecordType",
    "CustomFieldCategoryCustomFieldCategoryDataType",
    "CustomFieldCategoryCustomFieldCategoryRecordType",
    "CustomFieldCategoryEdit",
    "CustomFieldCategoryEditCustomFieldCategoryDataType",
    "CustomFieldCategoryEditCustomFieldCategoryRecordType",
    "Fund",
    "FundCollection",
    "FundCreate",
    "FundEdit",
    "FuzzyDate",
    "GetCustomFieldCategoryListCustomFieldCategoryRecordType",
    "GetPhoneTypesListPhoneFormat",
    "GetPhoneTypesListPhoneNumberType",
    "GiftAidTaxDeclaration",
    "GiftAidTaxDeclarationCollection",
    "GiftAidTaxDeclarationCreate",
    "GiftAidTaxDeclarationCreateGiftAidPaysTax",
    "GiftAidTaxDeclarationEdit",
    "GiftAidTaxDeclarationEditGiftAidPaysTax",
    "GiftAidTaxDeclarationGiftAidPaysTax",
    "GiftIdMap",
    "GiftNote",
    "GiftNoteCollection",
    "GiftNoteCreate",
    "GiftNoteEdit",
    "GiftTribute",
    "GiftTributeAcknowledgee",
    "GiftTributeAcknowledgeeCollection",
    "GiftTributeAcknowledgeeEdit",
    "GiftTributeAcknowledgeStatus",
    "GiftTributeCollection",
    "GiftTributeCreate",
    "GiftTributeEdit",
    "GiftTributeEditAcknowledgeStatus",
    "ImportIdMap",
    "NameFormatConfiguration",
    "NameFormatConfigurationCollection",
    "NameFormatConfigurationCreate",
    "NameFormatConfigurationEdit",
    "NameFormatConfigurationField",
    "NameFormatConfigurationFieldCollection",
    "NameFormatConfigurationFieldCreate",
    "NameFormatConfigurationFieldDetail",
    "NameFormatConfigurationFieldEdit",
    "NameFormatConfigurationForList",
    "PhoneType",
    "PhoneTypeCollection",
    "PhoneTypeCreate",
    "PhoneTypeCreatePhoneFormat",
    "PhoneTypeCreatePhoneNumberType",
    "PhoneTypeEdit",
    "PhoneTypeEditPhoneFormat",
    "PhoneTypeEditPhoneNumberType",
    "PhoneTypePhoneFormat",
    "PhoneTypePhoneNumberType",
    "PostResponse",
    "Relationship",
    "RelationshipCollection",
    "TableEntry",
    "TableEntryCollection",
    "TableEntryCreate",
    "TableEntryEdit",
    "Tribute",
    "TributeAcknowledgee",
    "TributeAcknowledgeeCollection",
    "TributeAcknowledgeeCreate",
    "TributeCollection",
    "TributeCreate",
    "User",
)

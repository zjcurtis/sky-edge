"""Contains all the data models used in inputs/outputs"""

from .bad_request_400_response_types import BadRequest400ResponseTypes
from .code_table_entry import CodeTableEntry
from .edit_gift_splits_tax import EditGiftSplitsTax
from .edit_gift_tax import EditGiftTax
from .edit_gift_tax_gift_aid_qualification_method import (
    EditGiftTaxGiftAidQualificationMethod,
)
from .get_tax_declaration_list_by_constituent_id_sort_direction import (
    GetTaxDeclarationListByConstituentIdSortDirection,
)
from .get_tax_declaration_list_by_constituent_id_tax_declaration_sort_fields import (
    GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields,
)
from .gift_tax import GiftTax
from .gift_tax_gift_aid_qualification_method import GiftTaxGiftAidQualificationMethod
from .gift_tax_gift_aid_qualification_status import GiftTaxGiftAidQualificationStatus
from .post_response import PostResponse
from .problem_details import ProblemDetails
from .split_details import SplitDetails
from .split_details_gift_aid_qualification_method import (
    SplitDetailsGiftAidQualificationMethod,
)
from .splits import Splits
from .splits_gift_aid_qualification_method import SplitsGiftAidQualificationMethod
from .tax_declaration import TaxDeclaration
from .tax_declaration_add import TaxDeclarationAdd
from .tax_declaration_add_constituent_pay_tax import TaxDeclarationAddConstituentPayTax
from .tax_declaration_collection import TaxDeclarationCollection
from .tax_declaration_constituent_pay_tax import TaxDeclarationConstituentPayTax
from .tax_declaration_update import TaxDeclarationUpdate
from .tax_declaration_update_constituent_pay_tax import (
    TaxDeclarationUpdateConstituentPayTax,
)

__all__ = (
    "BadRequest400ResponseTypes",
    "CodeTableEntry",
    "EditGiftSplitsTax",
    "EditGiftTax",
    "EditGiftTaxGiftAidQualificationMethod",
    "GetTaxDeclarationListByConstituentIdSortDirection",
    "GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields",
    "GiftTax",
    "GiftTaxGiftAidQualificationMethod",
    "GiftTaxGiftAidQualificationStatus",
    "PostResponse",
    "ProblemDetails",
    "SplitDetails",
    "SplitDetailsGiftAidQualificationMethod",
    "Splits",
    "SplitsGiftAidQualificationMethod",
    "TaxDeclaration",
    "TaxDeclarationAdd",
    "TaxDeclarationAddConstituentPayTax",
    "TaxDeclarationCollection",
    "TaxDeclarationConstituentPayTax",
    "TaxDeclarationUpdate",
    "TaxDeclarationUpdateConstituentPayTax",
)

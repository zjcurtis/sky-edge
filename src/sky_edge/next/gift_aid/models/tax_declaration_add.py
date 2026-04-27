from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.tax_declaration_add_constituent_pay_tax import (
    TaxDeclarationAddConstituentPayTax,
)

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry


T = TypeVar("T", bound="TaxDeclarationAdd")


@_attrs_define
class TaxDeclarationAdd:
    """Tax declaration create model

    Attributes:
        declaration_made_date (datetime.date): The specific date by which declaration was made.
        declaration_start_date (datetime.date): The specific date by which a declaration is start.
        constituent_pays_tax (TaxDeclarationAddConstituentPayTax | Unset): Indicates status of the Constituent pays tax.
        confirmation_sent_date (datetime.date | None | Unset): The specific date by which a confirmation is sent.
        confirmation_returned_date (datetime.date | None | Unset): The specific date by which a confirmation is
            returned.
        tax_notes (None | str | Unset): Refers to Comments on tax declaration.
        declaration_end_date (datetime.date | None | Unset): The specific date by which a declaration is end.
        declaration_indicator (CodeTableEntry | Unset): Code table entry
        scanned_docs_exist (bool | Unset): Indicates whether scanned documents exist or not.
        tax_payer_status (CodeTableEntry | Unset): Code table entry
        declaration_source (CodeTableEntry | Unset): Code table entry
    """

    declaration_made_date: datetime.date
    declaration_start_date: datetime.date
    constituent_pays_tax: TaxDeclarationAddConstituentPayTax | Unset = UNSET
    confirmation_sent_date: datetime.date | None | Unset = UNSET
    confirmation_returned_date: datetime.date | None | Unset = UNSET
    tax_notes: None | str | Unset = UNSET
    declaration_end_date: datetime.date | None | Unset = UNSET
    declaration_indicator: CodeTableEntry | Unset = UNSET
    scanned_docs_exist: bool | Unset = UNSET
    tax_payer_status: CodeTableEntry | Unset = UNSET
    declaration_source: CodeTableEntry | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        declaration_made_date = self.declaration_made_date.isoformat()

        declaration_start_date = self.declaration_start_date.isoformat()

        constituent_pays_tax: str | Unset = UNSET
        if not isinstance(self.constituent_pays_tax, Unset):
            constituent_pays_tax = self.constituent_pays_tax.value

        confirmation_sent_date: None | str | Unset
        if isinstance(self.confirmation_sent_date, Unset):
            confirmation_sent_date = UNSET
        elif isinstance(self.confirmation_sent_date, datetime.date):
            confirmation_sent_date = self.confirmation_sent_date.isoformat()
        else:
            confirmation_sent_date = self.confirmation_sent_date

        confirmation_returned_date: None | str | Unset
        if isinstance(self.confirmation_returned_date, Unset):
            confirmation_returned_date = UNSET
        elif isinstance(self.confirmation_returned_date, datetime.date):
            confirmation_returned_date = self.confirmation_returned_date.isoformat()
        else:
            confirmation_returned_date = self.confirmation_returned_date

        tax_notes: None | str | Unset
        if isinstance(self.tax_notes, Unset):
            tax_notes = UNSET
        else:
            tax_notes = self.tax_notes

        declaration_end_date: None | str | Unset
        if isinstance(self.declaration_end_date, Unset):
            declaration_end_date = UNSET
        elif isinstance(self.declaration_end_date, datetime.date):
            declaration_end_date = self.declaration_end_date.isoformat()
        else:
            declaration_end_date = self.declaration_end_date

        declaration_indicator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.declaration_indicator, Unset):
            declaration_indicator = self.declaration_indicator.to_dict()

        scanned_docs_exist = self.scanned_docs_exist

        tax_payer_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tax_payer_status, Unset):
            tax_payer_status = self.tax_payer_status.to_dict()

        declaration_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.declaration_source, Unset):
            declaration_source = self.declaration_source.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "declaration_made_date": declaration_made_date,
                "declaration_start_date": declaration_start_date,
            }
        )
        if constituent_pays_tax is not UNSET:
            field_dict["constituent_pays_tax"] = constituent_pays_tax
        if confirmation_sent_date is not UNSET:
            field_dict["confirmation_sent_date"] = confirmation_sent_date
        if confirmation_returned_date is not UNSET:
            field_dict["confirmation_returned_date"] = confirmation_returned_date
        if tax_notes is not UNSET:
            field_dict["tax_notes"] = tax_notes
        if declaration_end_date is not UNSET:
            field_dict["declaration_end_date"] = declaration_end_date
        if declaration_indicator is not UNSET:
            field_dict["declaration_indicator"] = declaration_indicator
        if scanned_docs_exist is not UNSET:
            field_dict["scanned_docs_exist"] = scanned_docs_exist
        if tax_payer_status is not UNSET:
            field_dict["tax_payer_status"] = tax_payer_status
        if declaration_source is not UNSET:
            field_dict["declaration_source"] = declaration_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry

        d = dict(src_dict)
        declaration_made_date = isoparse(d.pop("declaration_made_date")).date()

        declaration_start_date = isoparse(d.pop("declaration_start_date")).date()

        _constituent_pays_tax = d.pop("constituent_pays_tax", UNSET)
        constituent_pays_tax: TaxDeclarationAddConstituentPayTax | Unset
        if isinstance(_constituent_pays_tax, Unset):
            constituent_pays_tax = UNSET
        else:
            constituent_pays_tax = TaxDeclarationAddConstituentPayTax(
                _constituent_pays_tax
            )

        def _parse_confirmation_sent_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmation_sent_date_type_0 = isoparse(data).date()

                return confirmation_sent_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        confirmation_sent_date = _parse_confirmation_sent_date(
            d.pop("confirmation_sent_date", UNSET)
        )

        def _parse_confirmation_returned_date(
            data: object,
        ) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmation_returned_date_type_0 = isoparse(data).date()

                return confirmation_returned_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        confirmation_returned_date = _parse_confirmation_returned_date(
            d.pop("confirmation_returned_date", UNSET)
        )

        def _parse_tax_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_notes = _parse_tax_notes(d.pop("tax_notes", UNSET))

        def _parse_declaration_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                declaration_end_date_type_0 = isoparse(data).date()

                return declaration_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        declaration_end_date = _parse_declaration_end_date(
            d.pop("declaration_end_date", UNSET)
        )

        _declaration_indicator = d.pop("declaration_indicator", UNSET)
        declaration_indicator: CodeTableEntry | Unset
        if isinstance(_declaration_indicator, Unset):
            declaration_indicator = UNSET
        else:
            declaration_indicator = CodeTableEntry.from_dict(_declaration_indicator)

        scanned_docs_exist = d.pop("scanned_docs_exist", UNSET)

        _tax_payer_status = d.pop("tax_payer_status", UNSET)
        tax_payer_status: CodeTableEntry | Unset
        if isinstance(_tax_payer_status, Unset):
            tax_payer_status = UNSET
        else:
            tax_payer_status = CodeTableEntry.from_dict(_tax_payer_status)

        _declaration_source = d.pop("declaration_source", UNSET)
        declaration_source: CodeTableEntry | Unset
        if isinstance(_declaration_source, Unset):
            declaration_source = UNSET
        else:
            declaration_source = CodeTableEntry.from_dict(_declaration_source)

        tax_declaration_add = cls(
            declaration_made_date=declaration_made_date,
            declaration_start_date=declaration_start_date,
            constituent_pays_tax=constituent_pays_tax,
            confirmation_sent_date=confirmation_sent_date,
            confirmation_returned_date=confirmation_returned_date,
            tax_notes=tax_notes,
            declaration_end_date=declaration_end_date,
            declaration_indicator=declaration_indicator,
            scanned_docs_exist=scanned_docs_exist,
            tax_payer_status=tax_payer_status,
            declaration_source=declaration_source,
        )

        return tax_declaration_add

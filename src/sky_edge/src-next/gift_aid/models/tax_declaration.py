from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.tax_declaration_constituent_pay_tax import TaxDeclarationConstituentPayTax
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxDeclaration")


@_attrs_define
class TaxDeclaration:
    """Tax declaration list model

    Attributes:
        declaration_id (None | str | Unset): The immutable system record ID of the tax declaration.
        sequence (int | None | Unset): The sequence number of the tax declaration.
        constituent_id (None | str | Unset): The constituent ID of the individual.
        constituent_pays_tax (TaxDeclarationConstituentPayTax | Unset): Indicates status of the Constituent pays tax.
        declaration_made_date (datetime.date | None | Unset): The specific date by which declaration was made.
        confirmation_sent_date (datetime.date | None | Unset): The specific date by which a confirmation is sent.
        confirmation_returned_date (datetime.date | None | Unset): The specific date by which a confirmation is
            returned.
        tax_notes (None | str | Unset): Refers to any Comments on tax declaration.
        declaration_end_date (datetime.date | None | Unset): The specific date by which a declaration is end.
        declaration_start_date (datetime.date | None | Unset): The specific date by which a declaration is start.
        tax_payer_status (int | None | Unset): Indicates the status of the tax payer.
        declaration_indicator (int | None | Unset): Indicates the tax declaration.
        scanned_docs_exist (bool | Unset): Indicates whether scanned documents exist or not.
        declaration_source (int | None | Unset): Source from which the declaration was received.
        declaration_source_text (None | str | Unset): Text that refers source from which the declaration was received.
        declaration_indicator_text (None | str | Unset): Text that shows whether a declaration has been made or is
            required.
        tax_payer_status_text (None | str | Unset): Text that indicates the status of the tax payer.
    """

    declaration_id: None | str | Unset = UNSET
    sequence: int | None | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    constituent_pays_tax: TaxDeclarationConstituentPayTax | Unset = UNSET
    declaration_made_date: datetime.date | None | Unset = UNSET
    confirmation_sent_date: datetime.date | None | Unset = UNSET
    confirmation_returned_date: datetime.date | None | Unset = UNSET
    tax_notes: None | str | Unset = UNSET
    declaration_end_date: datetime.date | None | Unset = UNSET
    declaration_start_date: datetime.date | None | Unset = UNSET
    tax_payer_status: int | None | Unset = UNSET
    declaration_indicator: int | None | Unset = UNSET
    scanned_docs_exist: bool | Unset = UNSET
    declaration_source: int | None | Unset = UNSET
    declaration_source_text: None | str | Unset = UNSET
    declaration_indicator_text: None | str | Unset = UNSET
    tax_payer_status_text: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        declaration_id: None | str | Unset
        if isinstance(self.declaration_id, Unset):
            declaration_id = UNSET
        else:
            declaration_id = self.declaration_id

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        constituent_pays_tax: str | Unset = UNSET
        if not isinstance(self.constituent_pays_tax, Unset):
            constituent_pays_tax = self.constituent_pays_tax.value

        declaration_made_date: None | str | Unset
        if isinstance(self.declaration_made_date, Unset):
            declaration_made_date = UNSET
        elif isinstance(self.declaration_made_date, datetime.date):
            declaration_made_date = self.declaration_made_date.isoformat()
        else:
            declaration_made_date = self.declaration_made_date

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

        declaration_start_date: None | str | Unset
        if isinstance(self.declaration_start_date, Unset):
            declaration_start_date = UNSET
        elif isinstance(self.declaration_start_date, datetime.date):
            declaration_start_date = self.declaration_start_date.isoformat()
        else:
            declaration_start_date = self.declaration_start_date

        tax_payer_status: int | None | Unset
        if isinstance(self.tax_payer_status, Unset):
            tax_payer_status = UNSET
        else:
            tax_payer_status = self.tax_payer_status

        declaration_indicator: int | None | Unset
        if isinstance(self.declaration_indicator, Unset):
            declaration_indicator = UNSET
        else:
            declaration_indicator = self.declaration_indicator

        scanned_docs_exist = self.scanned_docs_exist

        declaration_source: int | None | Unset
        if isinstance(self.declaration_source, Unset):
            declaration_source = UNSET
        else:
            declaration_source = self.declaration_source

        declaration_source_text: None | str | Unset
        if isinstance(self.declaration_source_text, Unset):
            declaration_source_text = UNSET
        else:
            declaration_source_text = self.declaration_source_text

        declaration_indicator_text: None | str | Unset
        if isinstance(self.declaration_indicator_text, Unset):
            declaration_indicator_text = UNSET
        else:
            declaration_indicator_text = self.declaration_indicator_text

        tax_payer_status_text: None | str | Unset
        if isinstance(self.tax_payer_status_text, Unset):
            tax_payer_status_text = UNSET
        else:
            tax_payer_status_text = self.tax_payer_status_text

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if declaration_id is not UNSET:
            field_dict["declaration_id"] = declaration_id
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if constituent_pays_tax is not UNSET:
            field_dict["constituent_pays_tax"] = constituent_pays_tax
        if declaration_made_date is not UNSET:
            field_dict["declaration_made_date"] = declaration_made_date
        if confirmation_sent_date is not UNSET:
            field_dict["confirmation_sent_date"] = confirmation_sent_date
        if confirmation_returned_date is not UNSET:
            field_dict["confirmation_returned_date"] = confirmation_returned_date
        if tax_notes is not UNSET:
            field_dict["tax_notes"] = tax_notes
        if declaration_end_date is not UNSET:
            field_dict["declaration_end_date"] = declaration_end_date
        if declaration_start_date is not UNSET:
            field_dict["declaration_start_date"] = declaration_start_date
        if tax_payer_status is not UNSET:
            field_dict["tax_payer_status"] = tax_payer_status
        if declaration_indicator is not UNSET:
            field_dict["declaration_indicator"] = declaration_indicator
        if scanned_docs_exist is not UNSET:
            field_dict["scanned_docs_exist"] = scanned_docs_exist
        if declaration_source is not UNSET:
            field_dict["declaration_source"] = declaration_source
        if declaration_source_text is not UNSET:
            field_dict["declaration_source_text"] = declaration_source_text
        if declaration_indicator_text is not UNSET:
            field_dict["declaration_indicator_text"] = declaration_indicator_text
        if tax_payer_status_text is not UNSET:
            field_dict["tax_payer_status_text"] = tax_payer_status_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_declaration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        declaration_id = _parse_declaration_id(d.pop("declaration_id", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        _constituent_pays_tax = d.pop("constituent_pays_tax", UNSET)
        constituent_pays_tax: TaxDeclarationConstituentPayTax | Unset
        if isinstance(_constituent_pays_tax, Unset):
            constituent_pays_tax = UNSET
        else:
            constituent_pays_tax = TaxDeclarationConstituentPayTax(_constituent_pays_tax)

        def _parse_declaration_made_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                declaration_made_date_type_0 = isoparse(data).date()

                return declaration_made_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        declaration_made_date = _parse_declaration_made_date(d.pop("declaration_made_date", UNSET))

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

        confirmation_sent_date = _parse_confirmation_sent_date(d.pop("confirmation_sent_date", UNSET))

        def _parse_confirmation_returned_date(data: object) -> datetime.date | None | Unset:
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

        confirmation_returned_date = _parse_confirmation_returned_date(d.pop("confirmation_returned_date", UNSET))

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

        declaration_end_date = _parse_declaration_end_date(d.pop("declaration_end_date", UNSET))

        def _parse_declaration_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                declaration_start_date_type_0 = isoparse(data).date()

                return declaration_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        declaration_start_date = _parse_declaration_start_date(d.pop("declaration_start_date", UNSET))

        def _parse_tax_payer_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tax_payer_status = _parse_tax_payer_status(d.pop("tax_payer_status", UNSET))

        def _parse_declaration_indicator(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        declaration_indicator = _parse_declaration_indicator(d.pop("declaration_indicator", UNSET))

        scanned_docs_exist = d.pop("scanned_docs_exist", UNSET)

        def _parse_declaration_source(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        declaration_source = _parse_declaration_source(d.pop("declaration_source", UNSET))

        def _parse_declaration_source_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        declaration_source_text = _parse_declaration_source_text(d.pop("declaration_source_text", UNSET))

        def _parse_declaration_indicator_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        declaration_indicator_text = _parse_declaration_indicator_text(d.pop("declaration_indicator_text", UNSET))

        def _parse_tax_payer_status_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_payer_status_text = _parse_tax_payer_status_text(d.pop("tax_payer_status_text", UNSET))

        tax_declaration = cls(
            declaration_id=declaration_id,
            sequence=sequence,
            constituent_id=constituent_id,
            constituent_pays_tax=constituent_pays_tax,
            declaration_made_date=declaration_made_date,
            confirmation_sent_date=confirmation_sent_date,
            confirmation_returned_date=confirmation_returned_date,
            tax_notes=tax_notes,
            declaration_end_date=declaration_end_date,
            declaration_start_date=declaration_start_date,
            tax_payer_status=tax_payer_status,
            declaration_indicator=declaration_indicator,
            scanned_docs_exist=scanned_docs_exist,
            declaration_source=declaration_source,
            declaration_source_text=declaration_source_text,
            declaration_indicator_text=declaration_indicator_text,
            tax_payer_status_text=tax_payer_status_text,
        )

        return tax_declaration

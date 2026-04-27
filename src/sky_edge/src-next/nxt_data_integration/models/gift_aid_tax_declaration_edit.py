from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.gift_aid_tax_declaration_edit_gift_aid_pays_tax import GiftAidTaxDeclarationEditGiftAidPaysTax
from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftAidTaxDeclarationEdit")


@_attrs_define
class GiftAidTaxDeclarationEdit:
    """A record from the dbo.ConstituentTaxDeclaration table in Raiser's Edge.

    Attributes:
        declaration_starts (datetime.datetime): Date the declaration starts.
        import_id (None | str | Unset): The import id.
        constituent_pays_tax (GiftAidTaxDeclarationEditGiftAidPaysTax | Unset): Constituent pays tax status (Yes, No,
            Unknown).
        declaration_made (datetime.datetime | None | Unset): Date the declaration was made.
        confirmation_sent (datetime.datetime | None | Unset): Date the confirmation was sent.
        confirmation_returned (datetime.datetime | None | Unset): Date the confirmation was returned.
        declaration_ends (datetime.datetime | None | Unset): Date the declaration ends.
        tax_notes (None | str | Unset): Comments on the declaration.
        tax_payer_status (None | str | Unset): Tax payer status.
        declaration_indicator (None | str | Unset): Declaration indicator.
        declaration_source (None | str | Unset): Declaration source.
        sequence (int | None | Unset): The numeric sequence associated with the tax declaration.
    """

    declaration_starts: datetime.datetime
    import_id: None | str | Unset = UNSET
    constituent_pays_tax: GiftAidTaxDeclarationEditGiftAidPaysTax | Unset = UNSET
    declaration_made: datetime.datetime | None | Unset = UNSET
    confirmation_sent: datetime.datetime | None | Unset = UNSET
    confirmation_returned: datetime.datetime | None | Unset = UNSET
    declaration_ends: datetime.datetime | None | Unset = UNSET
    tax_notes: None | str | Unset = UNSET
    tax_payer_status: None | str | Unset = UNSET
    declaration_indicator: None | str | Unset = UNSET
    declaration_source: None | str | Unset = UNSET
    sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        declaration_starts = self.declaration_starts.isoformat()

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        constituent_pays_tax: str | Unset = UNSET
        if not isinstance(self.constituent_pays_tax, Unset):
            constituent_pays_tax = self.constituent_pays_tax.value

        declaration_made: None | str | Unset
        if isinstance(self.declaration_made, Unset):
            declaration_made = UNSET
        elif isinstance(self.declaration_made, datetime.datetime):
            declaration_made = self.declaration_made.isoformat()
        else:
            declaration_made = self.declaration_made

        confirmation_sent: None | str | Unset
        if isinstance(self.confirmation_sent, Unset):
            confirmation_sent = UNSET
        elif isinstance(self.confirmation_sent, datetime.datetime):
            confirmation_sent = self.confirmation_sent.isoformat()
        else:
            confirmation_sent = self.confirmation_sent

        confirmation_returned: None | str | Unset
        if isinstance(self.confirmation_returned, Unset):
            confirmation_returned = UNSET
        elif isinstance(self.confirmation_returned, datetime.datetime):
            confirmation_returned = self.confirmation_returned.isoformat()
        else:
            confirmation_returned = self.confirmation_returned

        declaration_ends: None | str | Unset
        if isinstance(self.declaration_ends, Unset):
            declaration_ends = UNSET
        elif isinstance(self.declaration_ends, datetime.datetime):
            declaration_ends = self.declaration_ends.isoformat()
        else:
            declaration_ends = self.declaration_ends

        tax_notes: None | str | Unset
        if isinstance(self.tax_notes, Unset):
            tax_notes = UNSET
        else:
            tax_notes = self.tax_notes

        tax_payer_status: None | str | Unset
        if isinstance(self.tax_payer_status, Unset):
            tax_payer_status = UNSET
        else:
            tax_payer_status = self.tax_payer_status

        declaration_indicator: None | str | Unset
        if isinstance(self.declaration_indicator, Unset):
            declaration_indicator = UNSET
        else:
            declaration_indicator = self.declaration_indicator

        declaration_source: None | str | Unset
        if isinstance(self.declaration_source, Unset):
            declaration_source = UNSET
        else:
            declaration_source = self.declaration_source

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "declaration_starts": declaration_starts,
            }
        )
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if constituent_pays_tax is not UNSET:
            field_dict["constituent_pays_tax"] = constituent_pays_tax
        if declaration_made is not UNSET:
            field_dict["declaration_made"] = declaration_made
        if confirmation_sent is not UNSET:
            field_dict["confirmation_sent"] = confirmation_sent
        if confirmation_returned is not UNSET:
            field_dict["confirmation_returned"] = confirmation_returned
        if declaration_ends is not UNSET:
            field_dict["declaration_ends"] = declaration_ends
        if tax_notes is not UNSET:
            field_dict["tax_notes"] = tax_notes
        if tax_payer_status is not UNSET:
            field_dict["tax_payer_status"] = tax_payer_status
        if declaration_indicator is not UNSET:
            field_dict["declaration_indicator"] = declaration_indicator
        if declaration_source is not UNSET:
            field_dict["declaration_source"] = declaration_source
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        declaration_starts = isoparse(d.pop("declaration_starts"))

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        _constituent_pays_tax = d.pop("constituent_pays_tax", UNSET)
        constituent_pays_tax: GiftAidTaxDeclarationEditGiftAidPaysTax | Unset
        if isinstance(_constituent_pays_tax, Unset):
            constituent_pays_tax = UNSET
        else:
            constituent_pays_tax = GiftAidTaxDeclarationEditGiftAidPaysTax(_constituent_pays_tax)

        def _parse_declaration_made(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                declaration_made_type_0 = isoparse(data)

                return declaration_made_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        declaration_made = _parse_declaration_made(d.pop("declaration_made", UNSET))

        def _parse_confirmation_sent(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmation_sent_type_0 = isoparse(data)

                return confirmation_sent_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        confirmation_sent = _parse_confirmation_sent(d.pop("confirmation_sent", UNSET))

        def _parse_confirmation_returned(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmation_returned_type_0 = isoparse(data)

                return confirmation_returned_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        confirmation_returned = _parse_confirmation_returned(d.pop("confirmation_returned", UNSET))

        def _parse_declaration_ends(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                declaration_ends_type_0 = isoparse(data)

                return declaration_ends_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        declaration_ends = _parse_declaration_ends(d.pop("declaration_ends", UNSET))

        def _parse_tax_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_notes = _parse_tax_notes(d.pop("tax_notes", UNSET))

        def _parse_tax_payer_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_payer_status = _parse_tax_payer_status(d.pop("tax_payer_status", UNSET))

        def _parse_declaration_indicator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        declaration_indicator = _parse_declaration_indicator(d.pop("declaration_indicator", UNSET))

        def _parse_declaration_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        declaration_source = _parse_declaration_source(d.pop("declaration_source", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        gift_aid_tax_declaration_edit = cls(
            declaration_starts=declaration_starts,
            import_id=import_id,
            constituent_pays_tax=constituent_pays_tax,
            declaration_made=declaration_made,
            confirmation_sent=confirmation_sent,
            confirmation_returned=confirmation_returned,
            declaration_ends=declaration_ends,
            tax_notes=tax_notes,
            tax_payer_status=tax_payer_status,
            declaration_indicator=declaration_indicator,
            declaration_source=declaration_source,
            sequence=sequence,
        )

        return gift_aid_tax_declaration_edit

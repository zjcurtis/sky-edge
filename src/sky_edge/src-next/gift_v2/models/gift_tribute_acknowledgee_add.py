from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry


T = TypeVar("T", bound="GiftTributeAcknowledgeeAdd")


@_attrs_define
class GiftTributeAcknowledgeeAdd:
    """A validatable gift tribute acknowledgee.

    Attributes:
        id (None | str | Unset): The gift tribute acknowledgee ID. Example: 12345.
        gift_legacy_id (None | str | Unset): The gift's record ID. Example: 12345.
        gift_lookup_id (None | str | Unset): The gift's lookup ID. Example: Lookup-12345.
        tribute_id (None | str | Unset): Tribute record ID. Example: 12345.
        relationships_id (None | str | Unset): Relationship record ID. Example: 12345.
        letter (CodeTableEntry | Unset): A predefined entry in a code table.
        tribute_acknowledgee_id (None | str | Unset): The tribute acknowledgee ID. Example: 12345.
        letter_date (datetime.datetime | None | Unset): The letter's date for table value.
    """

    id: None | str | Unset = UNSET
    gift_legacy_id: None | str | Unset = UNSET
    gift_lookup_id: None | str | Unset = UNSET
    tribute_id: None | str | Unset = UNSET
    relationships_id: None | str | Unset = UNSET
    letter: CodeTableEntry | Unset = UNSET
    tribute_acknowledgee_id: None | str | Unset = UNSET
    letter_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        gift_legacy_id: None | str | Unset
        if isinstance(self.gift_legacy_id, Unset):
            gift_legacy_id = UNSET
        else:
            gift_legacy_id = self.gift_legacy_id

        gift_lookup_id: None | str | Unset
        if isinstance(self.gift_lookup_id, Unset):
            gift_lookup_id = UNSET
        else:
            gift_lookup_id = self.gift_lookup_id

        tribute_id: None | str | Unset
        if isinstance(self.tribute_id, Unset):
            tribute_id = UNSET
        else:
            tribute_id = self.tribute_id

        relationships_id: None | str | Unset
        if isinstance(self.relationships_id, Unset):
            relationships_id = UNSET
        else:
            relationships_id = self.relationships_id

        letter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.letter, Unset):
            letter = self.letter.to_dict()

        tribute_acknowledgee_id: None | str | Unset
        if isinstance(self.tribute_acknowledgee_id, Unset):
            tribute_acknowledgee_id = UNSET
        else:
            tribute_acknowledgee_id = self.tribute_acknowledgee_id

        letter_date: None | str | Unset
        if isinstance(self.letter_date, Unset):
            letter_date = UNSET
        elif isinstance(self.letter_date, datetime.datetime):
            letter_date = self.letter_date.isoformat()
        else:
            letter_date = self.letter_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gift_legacy_id is not UNSET:
            field_dict["gift_legacy_id"] = gift_legacy_id
        if gift_lookup_id is not UNSET:
            field_dict["gift_lookup_id"] = gift_lookup_id
        if tribute_id is not UNSET:
            field_dict["tribute_id"] = tribute_id
        if relationships_id is not UNSET:
            field_dict["relationships_id"] = relationships_id
        if letter is not UNSET:
            field_dict["letter"] = letter
        if tribute_acknowledgee_id is not UNSET:
            field_dict["tribute_acknowledgee_id"] = tribute_acknowledgee_id
        if letter_date is not UNSET:
            field_dict["letter_date"] = letter_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_gift_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_legacy_id = _parse_gift_legacy_id(d.pop("gift_legacy_id", UNSET))

        def _parse_gift_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_lookup_id = _parse_gift_lookup_id(d.pop("gift_lookup_id", UNSET))

        def _parse_tribute_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_id = _parse_tribute_id(d.pop("tribute_id", UNSET))

        def _parse_relationships_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationships_id = _parse_relationships_id(d.pop("relationships_id", UNSET))

        _letter = d.pop("letter", UNSET)
        letter: CodeTableEntry | Unset
        if isinstance(_letter, Unset):
            letter = UNSET
        else:
            letter = CodeTableEntry.from_dict(_letter)

        def _parse_tribute_acknowledgee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_acknowledgee_id = _parse_tribute_acknowledgee_id(d.pop("tribute_acknowledgee_id", UNSET))

        def _parse_letter_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                letter_date_type_0 = isoparse(data)

                return letter_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        letter_date = _parse_letter_date(d.pop("letter_date", UNSET))

        gift_tribute_acknowledgee_add = cls(
            id=id,
            gift_legacy_id=gift_legacy_id,
            gift_lookup_id=gift_lookup_id,
            tribute_id=tribute_id,
            relationships_id=relationships_id,
            letter=letter,
            tribute_acknowledgee_id=tribute_acknowledgee_id,
            letter_date=letter_date,
        )

        return gift_tribute_acknowledgee_add

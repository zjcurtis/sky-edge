from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="GiftTributeAcknowledgee")


@_attrs_define
class GiftTributeAcknowledgee:
    """A gift tribute acknowledgee record in Raiser's Edge.

    Attributes:
        id (int | Unset): The system record ID of the gift tribute acknowledgee.
        gift_tribute_id (int | Unset): The system record ID of the gift tribute.
        self_acknowledge (bool | Unset): Indicates whether this is a self-acknowledge.
        relationships_id (int | None | Unset): The system record ID of the relationship for the acknowledgee.
        letter (int | None | Unset): The letter sent to the acknowledgee.
        letter_date (datetime.datetime | None | Unset): The date on which the letter was sent.
        import_id (None | str | Unset): The import ID of the gift tribute acknowledgee.
    """

    id: int | Unset = UNSET
    gift_tribute_id: int | Unset = UNSET
    self_acknowledge: bool | Unset = UNSET
    relationships_id: int | None | Unset = UNSET
    letter: int | None | Unset = UNSET
    letter_date: datetime.datetime | None | Unset = UNSET
    import_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        gift_tribute_id = self.gift_tribute_id

        self_acknowledge = self.self_acknowledge

        relationships_id: int | None | Unset
        if isinstance(self.relationships_id, Unset):
            relationships_id = UNSET
        else:
            relationships_id = self.relationships_id

        letter: int | None | Unset
        if isinstance(self.letter, Unset):
            letter = UNSET
        else:
            letter = self.letter

        letter_date: None | str | Unset
        if isinstance(self.letter_date, Unset):
            letter_date = UNSET
        elif isinstance(self.letter_date, datetime.datetime):
            letter_date = self.letter_date.isoformat()
        else:
            letter_date = self.letter_date

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gift_tribute_id is not UNSET:
            field_dict["gift_tribute_id"] = gift_tribute_id
        if self_acknowledge is not UNSET:
            field_dict["self_acknowledge"] = self_acknowledge
        if relationships_id is not UNSET:
            field_dict["relationships_id"] = relationships_id
        if letter is not UNSET:
            field_dict["letter"] = letter
        if letter_date is not UNSET:
            field_dict["letter_date"] = letter_date
        if import_id is not UNSET:
            field_dict["import_id"] = import_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        gift_tribute_id = d.pop("gift_tribute_id", UNSET)

        self_acknowledge = d.pop("self_acknowledge", UNSET)

        def _parse_relationships_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        relationships_id = _parse_relationships_id(d.pop("relationships_id", UNSET))

        def _parse_letter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        letter = _parse_letter(d.pop("letter", UNSET))

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

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        gift_tribute_acknowledgee = cls(
            id=id,
            gift_tribute_id=gift_tribute_id,
            self_acknowledge=self_acknowledge,
            relationships_id=relationships_id,
            letter=letter,
            letter_date=letter_date,
            import_id=import_id,
        )

        return gift_tribute_acknowledgee

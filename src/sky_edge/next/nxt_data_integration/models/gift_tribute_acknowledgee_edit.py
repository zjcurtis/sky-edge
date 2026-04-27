from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="GiftTributeAcknowledgeeEdit")


@_attrs_define
class GiftTributeAcknowledgeeEdit:
    """Represents the editable properties of a Gift Tribute Acknowledgee record in Raiser's Edge.

    Attributes:
        letter (int | None | Unset): The letter.
        letter_date (datetime.datetime | None | Unset): The letter date.
    """

    letter: int | None | Unset = UNSET
    letter_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if letter is not UNSET:
            field_dict["letter"] = letter
        if letter_date is not UNSET:
            field_dict["letter_date"] = letter_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        gift_tribute_acknowledgee_edit = cls(
            letter=letter,
            letter_date=letter_date,
        )

        return gift_tribute_acknowledgee_edit

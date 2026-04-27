from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="GiftNote")


@_attrs_define
class GiftNote:
    """Represents the fields for a gift note record in dbo.GiftNotepad.

    Attributes:
        gift_id (int | Unset): The record ID of the gift to which the note belongs; corresponds to ParentId in
            dbo.GiftNotepad.
        date (FuzzyDate | Unset):
        summary (None | str | Unset): The note summary; corresponds to Description in dbo.GiftNotepad.
        text (None | str | Unset): The text content of the note.
        type_ (None | str | Unset): The note type.
        author (None | str | Unset): The author of the note.
    """

    gift_id: int | Unset = UNSET
    date: FuzzyDate | Unset = UNSET
    summary: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    author: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_id = self.gift_id

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        text: None | str | Unset
        if isinstance(self.text, Unset):
            text = UNSET
        else:
            text = self.text

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if date is not UNSET:
            field_dict["date"] = date
        if summary is not UNSET:
            field_dict["summary"] = summary
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        gift_id = d.pop("gift_id", UNSET)

        _date = d.pop("date", UNSET)
        date: FuzzyDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FuzzyDate.from_dict(_date)

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text = _parse_text(d.pop("text", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        gift_note = cls(
            gift_id=gift_id,
            date=date,
            summary=summary,
            text=text,
            type_=type_,
            author=author,
        )

        return gift_note

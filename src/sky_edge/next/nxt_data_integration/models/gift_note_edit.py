from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="GiftNoteEdit")


@_attrs_define
class GiftNoteEdit:
    """Contains the editable fields for a gift note.

    Attributes:
        date (FuzzyDate):
        note_type_id (int): The ID for the note type.
        summary (None | str | Unset): The note summary; corresponds to Description in dbo.GiftNotepad.
        text (None | str | Unset): The text content of the note.
        author (None | str | Unset): The author of the note.
    """

    date: FuzzyDate
    note_type_id: int
    summary: None | str | Unset = UNSET
    text: None | str | Unset = UNSET
    author: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        date = self.date.to_dict()

        note_type_id = self.note_type_id

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

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "note_type_id": note_type_id,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if text is not UNSET:
            field_dict["text"] = text
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        date = FuzzyDate.from_dict(d.pop("date"))

        note_type_id = d.pop("note_type_id")

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

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        gift_note_edit = cls(
            date=date,
            note_type_id=note_type_id,
            summary=summary,
            text=text,
            author=author,
        )

        return gift_note_edit

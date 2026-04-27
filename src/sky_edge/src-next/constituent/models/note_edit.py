from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="NoteEdit")


@_attrs_define
class NoteEdit:
    """Notes track helpful or important details about constituents, gifts, or actions, such as specific interests and
    special instructions for donations. Notes connect you with donors at a more personal level as you cultivate
    relationships and track lessons learned for more effective fundraising.

        Attributes:
            date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            summary (str | Unset): The note summary. Character limit: 255.
            text (str | Unset): The note's contents.
            type_ (str | Unset): The note type. Available values are the entries in the <a href="https://developer.sky.black
                baud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListNoteTypes"><b>Notepad Types</b></a> table. This
                property cannot be set to null.
    """

    date: FuzzyDate | Unset = UNSET
    summary: str | Unset = UNSET
    text: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        summary = self.summary

        text = self.text

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if summary is not UNSET:
            field_dict["summary"] = summary
        if text is not UNSET:
            field_dict["text"] = text
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: FuzzyDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FuzzyDate.from_dict(_date)

        summary = d.pop("summary", UNSET)

        text = d.pop("text", UNSET)

        type_ = d.pop("type", UNSET)

        note_edit = cls(
            date=date,
            summary=summary,
            text=text,
            type_=type_,
        )

        note_edit.additional_properties = d
        return note_edit

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

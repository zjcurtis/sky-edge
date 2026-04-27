from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="ParentedNoteAdd")


@_attrs_define
class ParentedNoteAdd:
    """Notes track helpful or important details about constituents, gifts, or actions, such as specific interests and
    special instructions for donations. Notes connect you with donors at a more personal level as you cultivate
    relationships and track lessons learned for more effective fundraising.

        Attributes:
            parent_id (str): The immutable system record ID of the record associated with the note.
            date (FuzzyDate): Fuzzy dates provide a versatile date type to create partial dates such as February 9 (with no
                year indicated).
            type_ (str): The note type. Available values are the entries in the <a href="https://developer.sky.blackbaud.com
                /docs/services/56b76470069a0509c8f1c5b3/operations/codetables_gettableentriesbyid">Code table API using the
                <b>Notepad Types</b> table ID</a>.
            summary (str | Unset): The note summary. Character limit: 255.
            text (str | Unset): The note's contents.
            author (str | Unset): The note author. If not supplied, will have a default set based on the user's account.
                Character limit: 50.
    """

    parent_id: str
    date: FuzzyDate
    type_: str
    summary: str | Unset = UNSET
    text: str | Unset = UNSET
    author: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        date = self.date.to_dict()

        type_ = self.type_

        summary = self.summary

        text = self.text

        author = self.author

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "date": date,
                "type": type_,
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
        parent_id = d.pop("parent_id")

        date = FuzzyDate.from_dict(d.pop("date"))

        type_ = d.pop("type")

        summary = d.pop("summary", UNSET)

        text = d.pop("text", UNSET)

        author = d.pop("author", UNSET)

        parented_note_add = cls(
            parent_id=parent_id,
            date=date,
            type_=type_,
            summary=summary,
            text=text,
            author=author,
        )

        parented_note_add.additional_properties = d
        return parented_note_add

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

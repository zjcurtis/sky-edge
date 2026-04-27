from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="NoteRead")


@_attrs_define
class NoteRead:
    """Notes track helpful or important details about constituents, gifts, or actions, such as specific interests and
    special instructions for donations. Notes connect you with donors at a more personal level as you cultivate
    relationships and track lessons learned for more effective fundraising.

        Attributes:
            id (str | Unset): The immutable system record ID of the note.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the note.
            date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            date_added (datetime.datetime | Unset): The date when the note was created. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the note was last modified. Includes an offset from UTC
                in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            summary (str | Unset): The note summary. Maximum length is 255 characters.
            text (str | Unset): The note's contents.
            type_ (str | Unset): The note type. Available values are the entries in the <a href="https://developer.sky.black
                baud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListNoteTypes"><b>Notepad Types</b></a> table.
    """

    id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date: FuzzyDate | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    summary: str | Unset = UNSET
    text: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        summary = self.summary

        text = self.text

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date is not UNSET:
            field_dict["date"] = date
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
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
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _date = d.pop("date", UNSET)
        date: FuzzyDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FuzzyDate.from_dict(_date)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        summary = d.pop("summary", UNSET)

        text = d.pop("text", UNSET)

        type_ = d.pop("type", UNSET)

        note_read = cls(
            id=id,
            constituent_id=constituent_id,
            date=date,
            date_added=date_added,
            date_modified=date_modified,
            summary=summary,
            text=text,
            type_=type_,
        )

        note_read.additional_properties = d
        return note_read

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

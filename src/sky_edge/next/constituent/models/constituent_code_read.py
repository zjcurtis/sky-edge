from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="ConstituentCodeRead")


@_attrs_define
class ConstituentCodeRead:
    """Constituent codes define the high-level affiliations between constituents and your organization — such as Board
    member, Vendor, and Volunteer — to provide context for why constituents are in the database.

        Attributes:
            id (str | Unset): The immutable system record ID of the constituent code.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the constituent
                code.
            date_added (datetime.datetime | Unset): The date when the constituent code was created. The date includes an
                offset from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:
                </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the constituent code was last modified. The date
                includes an offset from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:
                </a><i>1969-11-21T10:29:43-04:00</i>.
            description (str | Unset): The description of the constituent code. Available values are the entries in the <a h
                ref="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListConstituentCodeTy
                pes"><b>Constituent Codes</b></a> table.
            end (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            inactive (bool | Unset): This computed field indicates that the constituent code is active if the current date
                is after any <code>start</code> date and before any <code>end</code> date.
            start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            sequence (int | Unset): The numeric sequence associated with the constituent code.
    """

    id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    end: FuzzyDate | Unset = UNSET
    inactive: bool | Unset = UNSET
    start: FuzzyDate | Unset = UNSET
    sequence: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        inactive = self.inactive

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        sequence = self.sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if end is not UNSET:
            field_dict["end"] = end
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if start is not UNSET:
            field_dict["start"] = start
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

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

        description = d.pop("description", UNSET)

        _end = d.pop("end", UNSET)
        end: FuzzyDate | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = FuzzyDate.from_dict(_end)

        inactive = d.pop("inactive", UNSET)

        _start = d.pop("start", UNSET)
        start: FuzzyDate | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = FuzzyDate.from_dict(_start)

        sequence = d.pop("sequence", UNSET)

        constituent_code_read = cls(
            id=id,
            constituent_id=constituent_id,
            date_added=date_added,
            date_modified=date_modified,
            description=description,
            end=end,
            inactive=inactive,
            start=start,
            sequence=sequence,
        )

        constituent_code_read.additional_properties = d
        return constituent_code_read

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

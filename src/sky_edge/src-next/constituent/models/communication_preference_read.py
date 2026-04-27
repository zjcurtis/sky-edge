from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommunicationPreferenceRead")


@_attrs_define
class CommunicationPreferenceRead:
    """Communication preferences provide guidance on how to contact constituents. These rules describe instructions and
    restrictions about when to reach out to constituents and how to tailor communications to honor their requests.

        Attributes:
            id (str | Unset): The immutable system record ID of the communication preference.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the
                communication preference.
            end (datetime.datetime | Unset): The end date of the communication preference. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            solicit_code (str | Unset): Communication instructions and/or restrictions for a constituent. Available values
                are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/opera
                tions/ListCommunicationPreferences"><b>Solicit Code</b></a> table.
            start (datetime.datetime | Unset): The start date of the communication preference. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
    """

    id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    solicit_code: str | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        solicit_code = self.solicit_code

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if end is not UNSET:
            field_dict["end"] = end
        if solicit_code is not UNSET:
            field_dict["solicit_code"] = solicit_code
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        solicit_code = d.pop("solicit_code", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        communication_preference_read = cls(
            id=id,
            constituent_id=constituent_id,
            end=end,
            solicit_code=solicit_code,
            start=start,
        )

        communication_preference_read.additional_properties = d
        return communication_preference_read

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

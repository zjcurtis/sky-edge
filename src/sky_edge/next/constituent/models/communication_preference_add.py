from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CommunicationPreferenceAdd")


@_attrs_define
class CommunicationPreferenceAdd:
    """Communication preferences provide guidance on how to contact constituents. These rules describe instructions and
    restrictions about when to reach out to constituents and how to tailor communications to honor their requests.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the communication
                preference.
            solicit_code (str): Communication instructions and/or restrictions for a constituent. Available values are the
                entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/Li
                stCommunicationPreferences"><b>Solicit Code</b></a> table.
            end (datetime.datetime | Unset): The end date of the communication preference. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            start (datetime.datetime | Unset): The start date of the communication preference. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
    """

    constituent_id: str
    solicit_code: str
    end: datetime.datetime | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        solicit_code = self.solicit_code

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
                "solicit_code": solicit_code,
            }
        )
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        solicit_code = d.pop("solicit_code")

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        communication_preference_add = cls(
            constituent_id=constituent_id,
            solicit_code=solicit_code,
            end=end,
            start=start,
        )

        communication_preference_add.additional_properties = d
        return communication_preference_add

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

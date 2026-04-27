from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProspectStatusRead")


@_attrs_define
class ProspectStatusRead:
    """Prospect statuses indicate milestones in a constituent’s relationship with your organization as fundraisers develop
    donor interest. This process identifies and acquires prospects, cultivates personal relationships, and generates
    major gift opportunities.

        Attributes:
            comments (str | Unset): The comments on the prospect status.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the prospect
                status.
            days_elapsed (int | Unset): This computed field calculates the total number of days in the current prospect
                status based on the <code>start</code> property.
            start (datetime.datetime | Unset): The start date of the prospect status. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            status (str | Unset): The constituent's current prospect status.
    """

    comments: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    days_elapsed: int | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        constituent_id = self.constituent_id

        days_elapsed = self.days_elapsed

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if days_elapsed is not UNSET:
            field_dict["days_elapsed"] = days_elapsed
        if start is not UNSET:
            field_dict["start"] = start
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        days_elapsed = d.pop("days_elapsed", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        status = d.pop("status", UNSET)

        prospect_status_read = cls(
            comments=comments,
            constituent_id=constituent_id,
            days_elapsed=days_elapsed,
            start=start,
            status=status,
        )

        prospect_status_read.additional_properties = d
        return prospect_status_read

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProspectStatusHistory")


@_attrs_define
class ProspectStatusHistory:
    """A specific part of a prospect's status history

    Attributes:
        author_id (str | Unset): The author id of the status history record.
        author_name (str | Unset): The author name of the status history record.
        comments (str | Unset): The comments for the prospect status history
        constituent_id (str | Unset): The constituent identifier for the prospect status history
        days_elapsed (int | Unset): The number of days elapsed in this particular prospect status
        id (str | Unset): The primary identifier for the prospect status history
        is_past_due (bool | Unset): Is the status past due.
        start_date (datetime.datetime | Unset): The status start date for the prospect status history
        status_id (str | Unset): The status identifier for the prospect status history
        status_description (str | Unset): The status description for the prospect status history
    """

    author_id: str | Unset = UNSET
    author_name: str | Unset = UNSET
    comments: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    days_elapsed: int | Unset = UNSET
    id: str | Unset = UNSET
    is_past_due: bool | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    status_id: str | Unset = UNSET
    status_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_id = self.author_id

        author_name = self.author_name

        comments = self.comments

        constituent_id = self.constituent_id

        days_elapsed = self.days_elapsed

        id = self.id

        is_past_due = self.is_past_due

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        status_id = self.status_id

        status_description = self.status_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if author_name is not UNSET:
            field_dict["author_name"] = author_name
        if comments is not UNSET:
            field_dict["comments"] = comments
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if days_elapsed is not UNSET:
            field_dict["days_elapsed"] = days_elapsed
        if id is not UNSET:
            field_dict["id"] = id
        if is_past_due is not UNSET:
            field_dict["is_past_due"] = is_past_due
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if status_id is not UNSET:
            field_dict["status_id"] = status_id
        if status_description is not UNSET:
            field_dict["status_description"] = status_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_id = d.pop("author_id", UNSET)

        author_name = d.pop("author_name", UNSET)

        comments = d.pop("comments", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        days_elapsed = d.pop("days_elapsed", UNSET)

        id = d.pop("id", UNSET)

        is_past_due = d.pop("is_past_due", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        status_id = d.pop("status_id", UNSET)

        status_description = d.pop("status_description", UNSET)

        prospect_status_history = cls(
            author_id=author_id,
            author_name=author_name,
            comments=comments,
            constituent_id=constituent_id,
            days_elapsed=days_elapsed,
            id=id,
            is_past_due=is_past_due,
            start_date=start_date,
            status_id=status_id,
            status_description=status_description,
        )

        prospect_status_history.additional_properties = d
        return prospect_status_history

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

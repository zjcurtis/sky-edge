from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpportunityStatusHistory")


@_attrs_define
class OpportunityStatusHistory:
    """A specific part of an opportunity's status history.

    Attributes:
        id (str | Unset): The primary identifier for the opportunity status history
        opportunity_id (str | Unset): The opportunity identifier for the opportunity status history
        status_id (str | Unset): The status identifier for the opportunity status history
        status_description (str | Unset): The status description for the opportunity status history
        start_date (datetime.datetime | Unset): The status start date for the opportunity status history
        days_elapsed (int | Unset): The number of days elapsed in this particular opportunity status
        comments (str | Unset): The comments for the opportunity status history
        author_name (str | Unset): The author name of the status history record.
        author_id (str | Unset): The author id of the status history record.
        is_blackbaud_processed (bool | Unset): Whether or not the status history record was created by Blackbaud
        is_past_due (bool | Unset): Is the status past due.
        is_closed (bool | Unset): Is the status closed.
    """

    id: str | Unset = UNSET
    opportunity_id: str | Unset = UNSET
    status_id: str | Unset = UNSET
    status_description: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    days_elapsed: int | Unset = UNSET
    comments: str | Unset = UNSET
    author_name: str | Unset = UNSET
    author_id: str | Unset = UNSET
    is_blackbaud_processed: bool | Unset = UNSET
    is_past_due: bool | Unset = UNSET
    is_closed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        opportunity_id = self.opportunity_id

        status_id = self.status_id

        status_description = self.status_description

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        days_elapsed = self.days_elapsed

        comments = self.comments

        author_name = self.author_name

        author_id = self.author_id

        is_blackbaud_processed = self.is_blackbaud_processed

        is_past_due = self.is_past_due

        is_closed = self.is_closed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if opportunity_id is not UNSET:
            field_dict["opportunity_id"] = opportunity_id
        if status_id is not UNSET:
            field_dict["status_id"] = status_id
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if days_elapsed is not UNSET:
            field_dict["days_elapsed"] = days_elapsed
        if comments is not UNSET:
            field_dict["comments"] = comments
        if author_name is not UNSET:
            field_dict["author_name"] = author_name
        if author_id is not UNSET:
            field_dict["author_id"] = author_id
        if is_blackbaud_processed is not UNSET:
            field_dict["is_blackbaud_processed"] = is_blackbaud_processed
        if is_past_due is not UNSET:
            field_dict["is_past_due"] = is_past_due
        if is_closed is not UNSET:
            field_dict["is_closed"] = is_closed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        opportunity_id = d.pop("opportunity_id", UNSET)

        status_id = d.pop("status_id", UNSET)

        status_description = d.pop("status_description", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        days_elapsed = d.pop("days_elapsed", UNSET)

        comments = d.pop("comments", UNSET)

        author_name = d.pop("author_name", UNSET)

        author_id = d.pop("author_id", UNSET)

        is_blackbaud_processed = d.pop("is_blackbaud_processed", UNSET)

        is_past_due = d.pop("is_past_due", UNSET)

        is_closed = d.pop("is_closed", UNSET)

        opportunity_status_history = cls(
            id=id,
            opportunity_id=opportunity_id,
            status_id=status_id,
            status_description=status_description,
            start_date=start_date,
            days_elapsed=days_elapsed,
            comments=comments,
            author_name=author_name,
            author_id=author_id,
            is_blackbaud_processed=is_blackbaud_processed,
            is_past_due=is_past_due,
            is_closed=is_closed,
        )

        opportunity_status_history.additional_properties = d
        return opportunity_status_history

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

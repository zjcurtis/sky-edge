from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="PackageRead")


@_attrs_define
class PackageRead:
    """Packages contain content and other items for the appeals that organizations use to solicit gifts.

    Attributes:
        id (str | Unset): The immutable system record ID of the package.
        appeal_id (str | Unset): The immutable system record ID of the appeal associated with this package.
        category (str | Unset): The category of the package.
        date_added (datetime.datetime | Unset): The date when the package was created. Includes an offset from UTC in <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
        date_modified (datetime.datetime | Unset): The date when the package was last modified. Includes an offset from
            UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
        default_gift_amount (Currency | Unset): For consistency, currency is configured at the organization level. This
            ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
        description (str | Unset): The display name of the package.
        end (datetime.datetime | Unset): The end date of the package. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-12-25T10:29:43</i>.
        goal (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
            all monetary amounts are consistent, regardless of where they are entered or viewed.
        inactive (bool | Unset): This computed field indicates that the package is active if the current date is after
            any <code>start</code> and before any <code>end</code>.
        lookup_id (str | Unset): The user-defined identifier for the package.
        notes (str | Unset): The notes on the package.
        recipient_count (int | Unset): The number of recipients of the package.
        start (datetime.datetime | Unset): The start date of the package. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
    """

    id: str | Unset = UNSET
    appeal_id: str | Unset = UNSET
    category: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    default_gift_amount: Currency | Unset = UNSET
    description: str | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    goal: Currency | Unset = UNSET
    inactive: bool | Unset = UNSET
    lookup_id: str | Unset = UNSET
    notes: str | Unset = UNSET
    recipient_count: int | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        appeal_id = self.appeal_id

        category = self.category

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        default_gift_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_gift_amount, Unset):
            default_gift_amount = self.default_gift_amount.to_dict()

        description = self.description

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        goal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.goal, Unset):
            goal = self.goal.to_dict()

        inactive = self.inactive

        lookup_id = self.lookup_id

        notes = self.notes

        recipient_count = self.recipient_count

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if category is not UNSET:
            field_dict["category"] = category
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if default_gift_amount is not UNSET:
            field_dict["default_gift_amount"] = default_gift_amount
        if description is not UNSET:
            field_dict["description"] = description
        if end is not UNSET:
            field_dict["end"] = end
        if goal is not UNSET:
            field_dict["goal"] = goal
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if recipient_count is not UNSET:
            field_dict["recipient_count"] = recipient_count
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        appeal_id = d.pop("appeal_id", UNSET)

        category = d.pop("category", UNSET)

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

        _default_gift_amount = d.pop("default_gift_amount", UNSET)
        default_gift_amount: Currency | Unset
        if isinstance(_default_gift_amount, Unset):
            default_gift_amount = UNSET
        else:
            default_gift_amount = Currency.from_dict(_default_gift_amount)

        description = d.pop("description", UNSET)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        _goal = d.pop("goal", UNSET)
        goal: Currency | Unset
        if isinstance(_goal, Unset):
            goal = UNSET
        else:
            goal = Currency.from_dict(_goal)

        inactive = d.pop("inactive", UNSET)

        lookup_id = d.pop("lookup_id", UNSET)

        notes = d.pop("notes", UNSET)

        recipient_count = d.pop("recipient_count", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        package_read = cls(
            id=id,
            appeal_id=appeal_id,
            category=category,
            date_added=date_added,
            date_modified=date_modified,
            default_gift_amount=default_gift_amount,
            description=description,
            end=end,
            goal=goal,
            inactive=inactive,
            lookup_id=lookup_id,
            notes=notes,
            recipient_count=recipient_count,
            start=start,
        )

        package_read.additional_properties = d
        return package_read

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

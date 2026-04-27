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


T = TypeVar("T", bound="FundRead")


@_attrs_define
class FundRead:
    """Funds represent how donors expect you to use their gifts. Funds can designate gifts for specific causes or earmark
    them for specific financial purposes.

        Attributes:
            id (str | Unset): The immutable system record ID of the fund.
            category (str | Unset): The category of the fund. Available values are the entries in the <b>Fund Categories</b>
                table.
            date_added (datetime.datetime | Unset): The date when the fund was created. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the fund was last modified. Includes an offset from UTC
                in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            description (str | Unset): The display name of the fund.
            end_date (datetime.datetime | Unset): The end date of the fund. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-12-25T10:29:43</i>.
            goal (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            inactive (bool | Unset): This computed field indicates that the fund is active if the current date is after any
                <code>start_date</code> and before any <code>end_date</code>.
            lookup_id (str | Unset): The user-defined identifier for the fund.
            start_date (datetime.datetime | Unset): The start date of the fund. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            type_ (str | Unset): The type of the fund. Available values are the entries in the <b>Fund Types</b> table.
    """

    id: str | Unset = UNSET
    category: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    end_date: datetime.datetime | Unset = UNSET
    goal: Currency | Unset = UNSET
    inactive: bool | Unset = UNSET
    lookup_id: str | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        goal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.goal, Unset):
            goal = self.goal.to_dict()

        inactive = self.inactive

        lookup_id = self.lookup_id

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if goal is not UNSET:
            field_dict["goal"] = goal
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

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

        description = d.pop("description", UNSET)

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _goal = d.pop("goal", UNSET)
        goal: Currency | Unset
        if isinstance(_goal, Unset):
            goal = UNSET
        else:
            goal = Currency.from_dict(_goal)

        inactive = d.pop("inactive", UNSET)

        lookup_id = d.pop("lookup_id", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        type_ = d.pop("type", UNSET)

        fund_read = cls(
            id=id,
            category=category,
            date_added=date_added,
            date_modified=date_modified,
            description=description,
            end_date=end_date,
            goal=goal,
            inactive=inactive,
            lookup_id=lookup_id,
            start_date=start_date,
            type_=type_,
        )

        fund_read.additional_properties = d
        return fund_read

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

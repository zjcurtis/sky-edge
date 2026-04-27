from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="RecurringGiftScheduleAdd")


@_attrs_define
class RecurringGiftScheduleAdd:
    """Defines a recurring gift schedule to add

    Attributes:
        frequency (str): Installment frequency of the recurring gift to add. Available values are WEEKLY,
            EVERY_TWO_WEEKS, EVERY_FOUR_WEEKS, MONTHLY, QUARTERLY, ANNUALLY.
        start_date (datetime.datetime): Date the recurring gift should start. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
        end_date (datetime.datetime | Unset): Date the recurring gift should end. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
    """

    frequency: str
    start_date: datetime.datetime
    end_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        frequency = self.frequency

        start_date = self.start_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequency": frequency,
                "start_date": start_date,
            }
        )
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        frequency = d.pop("frequency")

        start_date = isoparse(d.pop("start_date"))

        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        recurring_gift_schedule_add = cls(
            frequency=frequency,
            start_date=start_date,
            end_date=end_date,
        )

        recurring_gift_schedule_add.additional_properties = d
        return recurring_gift_schedule_add

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldUpdate")


@_attrs_define
class CustomFieldUpdate:
    """While records provide many fields to track information, organizations often require additional details. To track
    this specialized information, use custom fields.

        Attributes:
            value (str): The value of the custom field. The type property determines the format. Character limit depends on
                data type.
            date (datetime.datetime | None | Unset): The custom field date.
            comment (None | str | Unset): The comment on the custom field. Character limit: 50.
    """

    value: str
    date: datetime.datetime | None | Unset = UNSET
    comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "value": value,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        custom_field_update = cls(
            value=value,
            date=date,
            comment=comment,
        )

        return custom_field_update

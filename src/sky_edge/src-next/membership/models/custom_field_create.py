from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldCreate")


@_attrs_define
class CustomFieldCreate:
    """Represents the custom fields data to be added

    Attributes:
        category (str): The custom field category. Available values are the entries in the custom field categories table
            of the parent object.
        parent_id (str): The parent object's immutable system record ID.
        value (str): The value of the custom field. The type property determines the format. Character limit depends on
            data type. Number types only support values greater than 0.
        comment (None | str | Unset): The comment on the custom field. Character limit: 50.
        date (datetime.datetime | None | Unset): The date on the custom field. Uses ISO-8601 format:
            1969-11-21T10:29:43.
    """

    category: str
    parent_id: str
    value: str
    comment: None | str | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        parent_id = self.parent_id

        value = self.value

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "category": category,
                "parent_id": parent_id,
                "value": value,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        parent_id = d.pop("parent_id")

        value = d.pop("value")

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

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

        custom_field_create = cls(
            category=category,
            parent_id=parent_id,
            value=value,
            comment=comment,
            date=date,
        )

        return custom_field_create

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CreateCustomFieldRequest")


@_attrs_define
class CreateCustomFieldRequest:
    """Creates a new custom field request for the event.

    Attributes:
        category (None | str | Unset): The event custom field category.
        parent_id (None | str | Unset): The parent record ID.
        comment (None | str | Unset): The comment for the custom field.
        date (datetime.date | None | Unset): The date for the custom field.
        value (None | str | Unset): The custom field value.
    """

    category: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        create_custom_field_request = cls(
            category=category,
            parent_id=parent_id,
            comment=comment,
            date=date,
            value=value,
        )

        return create_custom_field_request

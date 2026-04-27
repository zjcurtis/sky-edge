from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.custom_field_type import CustomFieldType

T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """Represents the custom field for the event.

    Attributes:
        id (None | str | Unset): The ID of the custom field.
        parent_id (None | str | Unset): The ID of the parent record.
        category (None | str | Unset): The category of the custom field.
        type_ (CustomFieldType | Unset): The type of the custom field.<p>Available values:</p><ul><li><i>Text</i> -
            Defines the custom field as a string value.</li><li><i>Number</i> - Defines the custom field as a integer
            value.</li><li><i>Date</i> - Defines the custom field as a date value.</li><li><i>Currency</i> - Defines the
            custom field as a decimal value.</li><li><i>Boolean</i> - Defines the custom field as a boolean
            value.</li><li><i>CodeTableEntry</i> - Defines the custom field as a code table entry
            identifier.</li><li><i>ConstituentId</i> - Defines the custom field as a constituent
            identifier.</li><li><i>FuzzyDate</i> - Defines the custom field as a fuzzy date value.</li></ul>
        comment (None | str | Unset): The comment for the custom field.
        date (datetime.date | None | Unset): The date for the custom field.
        value (None | str | Unset): The custom field value.
    """

    id: None | str | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    type_: CustomFieldType | Unset = UNSET
    comment: None | str | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if category is not UNSET:
            field_dict["category"] = category
        if type_ is not UNSET:
            field_dict["type"] = type_
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

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: CustomFieldType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CustomFieldType(_type_)

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

        custom_field = cls(
            id=id,
            parent_id=parent_id,
            category=category,
            type_=type_,
            comment=comment,
            date=date,
            value=value,
        )

        return custom_field

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.custom_field_custom_field_type import CustomFieldCustomFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomField")


@_attrs_define
class CustomField:
    """custom fields for membership

    Attributes:
        id (None | str | Unset): The immutable system record ID of the custom field.
        category (None | str | Unset): The custom field category. Available values are the entries in the <b>Custom
            Field Categories</b> table of the parent object.
        comment (None | str | Unset): The comment on the custom field.
        date (datetime.datetime | None | Unset): The date on the custom field. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43</i>.
        date_added (datetime.datetime | None | Unset): The date when the custom field was created. The date includes an
            offset from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
            format:</a><i>1969-11-21T10:29:43-04:00</i>.
        date_modified (datetime.datetime | None | Unset): The date when the custom field was last modified. The date
            includes an offset from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
            format:</a><i>1969-11-21T10:29:43-04:00</i>.
        parent_id (None | str | Unset): The parent object's immutable system record ID.
        type_ (CustomFieldCustomFieldType | Unset): The type of data that the custom field represents. Available values
            are listed below.
        value (Any | Unset): The value of the custom field. The ```type``` property determines the format.
    """

    id: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    type_: CustomFieldCustomFieldType | Unset = UNSET
    value: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

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

        date_added: None | str | Unset
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if type_ is not UNSET:
            field_dict["type"] = type_
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

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

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

        def _parse_date_added(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = isoparse(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: CustomFieldCustomFieldType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CustomFieldCustomFieldType(_type_)

        value = d.pop("value", UNSET)

        custom_field = cls(
            id=id,
            category=category,
            comment=comment,
            date=date,
            date_added=date_added,
            date_modified=date_modified,
            parent_id=parent_id,
            type_=type_,
            value=value,
        )

        return custom_field

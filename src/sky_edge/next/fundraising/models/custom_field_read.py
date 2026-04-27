from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.custom_field_read_type import CustomFieldReadType

if TYPE_CHECKING:
    from ..models.custom_field_read_value import CustomFieldReadValue


T = TypeVar("T", bound="CustomFieldRead")


@_attrs_define
class CustomFieldRead:
    """While records provide many fields to track information, organizations often require additional details. To track
    this specialized information, use custom fields.

        Attributes:
            id (str | Unset): The immutable system record ID of the custom field.
            category (str | Unset): The custom field category. Available values are the entries in the <b>Custom Field
                Categories</b> table of the parent object.
            comment (str | Unset): The comment on the custom field.
            date (datetime.datetime | Unset): The date on the custom field. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43</i>.
            date_added (datetime.datetime | Unset): The date when the custom field was created. The date includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the custom field was last modified. The date includes
                an offset from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
                format:</a><i>1969-11-21T10:29:43-04:00</i>.
            parent_id (str | Unset): The parent object's immutable system record ID.
            type_ (CustomFieldReadType | Unset): The type of data that the custom field represents. Available values are
                listed below.
            value (CustomFieldReadValue | Unset): The value of the custom field. The <code>type</code> property determines
                the format.
    """

    id: str | Unset = UNSET
    category: str | Unset = UNSET
    comment: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    parent_id: str | Unset = UNSET
    type_: CustomFieldReadType | Unset = UNSET
    value: CustomFieldReadValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        comment = self.comment

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        parent_id = self.parent_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.custom_field_read_value import CustomFieldReadValue

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        category = d.pop("category", UNSET)

        comment = d.pop("comment", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

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

        parent_id = d.pop("parent_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CustomFieldReadType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CustomFieldReadType(_type_)

        _value = d.pop("value", UNSET)
        value: CustomFieldReadValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CustomFieldReadValue.from_dict(_value)

        custom_field_read = cls(
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

        custom_field_read.additional_properties = d
        return custom_field_read

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

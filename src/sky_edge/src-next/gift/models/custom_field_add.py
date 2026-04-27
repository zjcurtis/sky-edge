from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_add_value import CustomFieldAddValue


T = TypeVar("T", bound="CustomFieldAdd")


@_attrs_define
class CustomFieldAdd:
    """While records provide many fields to track information, organizations often require additional details. To track
    this specialized information, use custom fields.

        Attributes:
            category (str): The custom field category. Available values are the entries in the <b>Custom Field
                Categories</b> table of the parent object.
            comment (str | Unset): The comment on the custom field. Character limit: 50.
            date (datetime.datetime | Unset): The date on the custom field. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43</i>.
            parent_id (str | Unset): The parent object's immutable system record ID.
            value (CustomFieldAddValue | Unset): The value of the custom field. The <code>type</code> property determines
                the format. Character limit depends on data type. Number types only support values greater than 0.
    """

    category: str
    comment: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    parent_id: str | Unset = UNSET
    value: CustomFieldAddValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        comment = self.comment

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        parent_id = self.parent_id

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_add_value import CustomFieldAddValue

        d = dict(src_dict)
        category = d.pop("category")

        comment = d.pop("comment", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        parent_id = d.pop("parent_id", UNSET)

        _value = d.pop("value", UNSET)
        value: CustomFieldAddValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CustomFieldAddValue.from_dict(_value)

        custom_field_add = cls(
            category=category,
            comment=comment,
            date=date,
            parent_id=parent_id,
            value=value,
        )

        custom_field_add.additional_properties = d
        return custom_field_add

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

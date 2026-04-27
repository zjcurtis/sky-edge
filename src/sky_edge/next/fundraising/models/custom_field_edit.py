from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_edit_value import CustomFieldEditValue


T = TypeVar("T", bound="CustomFieldEdit")


@_attrs_define
class CustomFieldEdit:
    """While records provide many fields to track information, organizations often require additional details. To track
    this specialized information, use custom fields.

        Attributes:
            comment (str | Unset): The comment on the custom field. Character limit: 50.
            date (datetime.datetime | Unset): The date on the custom field. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43</i>.
            value (CustomFieldEditValue | Unset): The value of the custom field. The <code>type</code> property determines
                the format. Character limit depends on data type.
    """

    comment: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    value: CustomFieldEditValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field_edit_value import CustomFieldEditValue

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _value = d.pop("value", UNSET)
        value: CustomFieldEditValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CustomFieldEditValue.from_dict(_value)

        custom_field_edit = cls(
            comment=comment,
            date=date,
            value=value,
        )

        custom_field_edit.additional_properties = d
        return custom_field_edit

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

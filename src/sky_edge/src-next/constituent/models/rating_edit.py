from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rating_edit_value import RatingEditValue


T = TypeVar("T", bound="RatingEdit")


@_attrs_define
class RatingEdit:
    """Ratings indicate the estimated wealth of constituents and their capacity to give. Ratings information such as
    overall wealth ratings, suggested ask amounts, and total identified assets can help to determine where to focus
    efforts, whether to pursue prospects or major gifts, and how much to ask from donors.

        Attributes:
            comment (str | Unset): A comment about the rating. Character limit: 255.
            date (datetime.datetime | Unset): The date of the rating. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>. This property cannot
                be set to null.
            value (RatingEditValue | Unset): The value of the rating. The <code>type</code> property determines the format
                and the character limit.
    """

    comment: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    value: RatingEditValue | Unset = UNSET
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
        from ..models.rating_edit_value import RatingEditValue

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _value = d.pop("value", UNSET)
        value: RatingEditValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RatingEditValue.from_dict(_value)

        rating_edit = cls(
            comment=comment,
            date=date,
            value=value,
        )

        rating_edit.additional_properties = d
        return rating_edit

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

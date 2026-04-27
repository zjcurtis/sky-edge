from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rating_category_read_type import RatingCategoryReadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RatingCategoryRead")


@_attrs_define
class RatingCategoryRead:
    """Rating categories store the metadata to appropriately match ratings with an available type.

    Attributes:
        inactive (bool | Unset): Indicates whether the category is inactive.
        name (str | Unset): The name of the rating category.
        source_name (str | Unset): The source of the category.*
        type_ (RatingCategoryReadType | Unset): Gets or sets the type of the rating category.
    """

    inactive: bool | Unset = UNSET
    name: str | Unset = UNSET
    source_name: str | Unset = UNSET
    type_: RatingCategoryReadType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inactive = self.inactive

        name = self.name

        source_name = self.source_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if name is not UNSET:
            field_dict["name"] = name
        if source_name is not UNSET:
            field_dict["source_name"] = source_name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inactive = d.pop("inactive", UNSET)

        name = d.pop("name", UNSET)

        source_name = d.pop("source_name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RatingCategoryReadType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RatingCategoryReadType(_type_)

        rating_category_read = cls(
            inactive=inactive,
            name=name,
            source_name=source_name,
            type_=type_,
        )

        rating_category_read.additional_properties = d
        return rating_category_read

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

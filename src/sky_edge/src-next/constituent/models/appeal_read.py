from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appeal_category_read import AppealCategoryRead


T = TypeVar("T", bound="AppealRead")


@_attrs_define
class AppealRead:
    """Appeals are solicitations to generate gifts, such as direct mailings, online donation pages, phonathons, auctions,
    and events.

        Attributes:
            id (str | Unset): The immutable system record ID of the appeal.
            category (AppealCategoryRead | Unset): Represents an appeal category.
            description (str | Unset): The appeal description.
    """

    id: str | Unset = UNSET
    category: AppealCategoryRead | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appeal_category_read import AppealCategoryRead

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _category = d.pop("category", UNSET)
        category: AppealCategoryRead | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = AppealCategoryRead.from_dict(_category)

        description = d.pop("description", UNSET)

        appeal_read = cls(
            id=id,
            category=category,
            description=description,
        )

        appeal_read.additional_properties = d
        return appeal_read

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

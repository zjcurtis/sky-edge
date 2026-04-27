from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipSubCategory")


@_attrs_define
class MembershipSubCategory:
    """The sequence of the membership subcategory.

    Attributes:
        membership_subcategories_id (None | str | Unset): The immutable system record ID of the membership subcategory.
        membership_catgory_id (None | str | Unset): The immutable system record ID of the membership category.
        sequence (int | None | Unset): The sequence of membership sub category.
        membership_sub_category_name (None | str | Unset): The name of membership sub category.
    """

    membership_subcategories_id: None | str | Unset = UNSET
    membership_catgory_id: None | str | Unset = UNSET
    sequence: int | None | Unset = UNSET
    membership_sub_category_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        membership_subcategories_id: None | str | Unset
        if isinstance(self.membership_subcategories_id, Unset):
            membership_subcategories_id = UNSET
        else:
            membership_subcategories_id = self.membership_subcategories_id

        membership_catgory_id: None | str | Unset
        if isinstance(self.membership_catgory_id, Unset):
            membership_catgory_id = UNSET
        else:
            membership_catgory_id = self.membership_catgory_id

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        membership_sub_category_name: None | str | Unset
        if isinstance(self.membership_sub_category_name, Unset):
            membership_sub_category_name = UNSET
        else:
            membership_sub_category_name = self.membership_sub_category_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if membership_subcategories_id is not UNSET:
            field_dict["membership_subcategories_id"] = membership_subcategories_id
        if membership_catgory_id is not UNSET:
            field_dict["membership_catgory_id"] = membership_catgory_id
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if membership_sub_category_name is not UNSET:
            field_dict["membership_sub_category_name"] = membership_sub_category_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_membership_subcategories_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        membership_subcategories_id = _parse_membership_subcategories_id(d.pop("membership_subcategories_id", UNSET))

        def _parse_membership_catgory_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        membership_catgory_id = _parse_membership_catgory_id(d.pop("membership_catgory_id", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_membership_sub_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        membership_sub_category_name = _parse_membership_sub_category_name(d.pop("membership_sub_category_name", UNSET))

        membership_sub_category = cls(
            membership_subcategories_id=membership_subcategories_id,
            membership_catgory_id=membership_catgory_id,
            sequence=sequence,
            membership_sub_category_name=membership_sub_category_name,
        )

        return membership_sub_category

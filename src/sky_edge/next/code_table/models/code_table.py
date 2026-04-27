from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.code_table_category import CodeTableCategory

T = TypeVar("T", bound="CodeTable")


@_attrs_define
class CodeTable:
    """A Code Table record.

    Attributes:
        code_tables_id (None | str | Unset): The unique identifier for the code table.
        name (None | str | Unset): The name of the code table.
        user_defined (bool | Unset): Indicates whether the code table is user defined.
        has_short_description (bool | Unset): Indicates whether the code table supports short description.
        short_description_length (int | Unset): The length of the short description.
        can_manage (bool | Unset): Whether the current user can manage this table.
        category (CodeTableCategory | Unset): The code table categories available. Certain categories are product module
            dependent.
        product_flags (int | Unset): The product module ID restriction(s).
        country_mask (int | Unset): The countries this code table is valid for.
        has_entries (bool | Unset): Whether the code table has any table entries.
        is_field_lookup (bool | Unset): Whether the table is a field lookup table.
        supports_cleanup (bool | Unset): Whether the table supports code table cleanup.
    """

    code_tables_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    user_defined: bool | Unset = UNSET
    has_short_description: bool | Unset = UNSET
    short_description_length: int | Unset = UNSET
    can_manage: bool | Unset = UNSET
    category: CodeTableCategory | Unset = UNSET
    product_flags: int | Unset = UNSET
    country_mask: int | Unset = UNSET
    has_entries: bool | Unset = UNSET
    is_field_lookup: bool | Unset = UNSET
    supports_cleanup: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code_tables_id: None | str | Unset
        if isinstance(self.code_tables_id, Unset):
            code_tables_id = UNSET
        else:
            code_tables_id = self.code_tables_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        user_defined = self.user_defined

        has_short_description = self.has_short_description

        short_description_length = self.short_description_length

        can_manage = self.can_manage

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        product_flags = self.product_flags

        country_mask = self.country_mask

        has_entries = self.has_entries

        is_field_lookup = self.is_field_lookup

        supports_cleanup = self.supports_cleanup

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if code_tables_id is not UNSET:
            field_dict["code_tables_id"] = code_tables_id
        if name is not UNSET:
            field_dict["name"] = name
        if user_defined is not UNSET:
            field_dict["user_defined"] = user_defined
        if has_short_description is not UNSET:
            field_dict["has_short_description"] = has_short_description
        if short_description_length is not UNSET:
            field_dict["short_description_length"] = short_description_length
        if can_manage is not UNSET:
            field_dict["can_manage"] = can_manage
        if category is not UNSET:
            field_dict["category"] = category
        if product_flags is not UNSET:
            field_dict["product_flags"] = product_flags
        if country_mask is not UNSET:
            field_dict["country_mask"] = country_mask
        if has_entries is not UNSET:
            field_dict["has_entries"] = has_entries
        if is_field_lookup is not UNSET:
            field_dict["is_field_lookup"] = is_field_lookup
        if supports_cleanup is not UNSET:
            field_dict["supports_cleanup"] = supports_cleanup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_code_tables_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_tables_id = _parse_code_tables_id(d.pop("code_tables_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        user_defined = d.pop("user_defined", UNSET)

        has_short_description = d.pop("has_short_description", UNSET)

        short_description_length = d.pop("short_description_length", UNSET)

        can_manage = d.pop("can_manage", UNSET)

        _category = d.pop("category", UNSET)
        category: CodeTableCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = CodeTableCategory(_category)

        product_flags = d.pop("product_flags", UNSET)

        country_mask = d.pop("country_mask", UNSET)

        has_entries = d.pop("has_entries", UNSET)

        is_field_lookup = d.pop("is_field_lookup", UNSET)

        supports_cleanup = d.pop("supports_cleanup", UNSET)

        code_table = cls(
            code_tables_id=code_tables_id,
            name=name,
            user_defined=user_defined,
            has_short_description=has_short_description,
            short_description_length=short_description_length,
            can_manage=can_manage,
            category=category,
            product_flags=product_flags,
            country_mask=country_mask,
            has_entries=has_entries,
            is_field_lookup=is_field_lookup,
            supports_cleanup=supports_cleanup,
        )

        return code_table

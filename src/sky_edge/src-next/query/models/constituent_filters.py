from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConstituentFilters")


@_attrs_define
class ConstituentFilters:
    """Common convenience filters specific to RE queries

    Attributes:
        include_inactive (bool | Unset): Include/exclude inactive constituents
        include_deceased (bool | Unset): Include/exclude deceased constituents
        include_no_valid_addresses (bool | Unset): Include/exclude constituents with no valid addresses
    """

    include_inactive: bool | Unset = UNSET
    include_deceased: bool | Unset = UNSET
    include_no_valid_addresses: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        include_inactive = self.include_inactive

        include_deceased = self.include_deceased

        include_no_valid_addresses = self.include_no_valid_addresses

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if include_inactive is not UNSET:
            field_dict["include_inactive"] = include_inactive
        if include_deceased is not UNSET:
            field_dict["include_deceased"] = include_deceased
        if include_no_valid_addresses is not UNSET:
            field_dict["include_no_valid_addresses"] = include_no_valid_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_inactive = d.pop("include_inactive", UNSET)

        include_deceased = d.pop("include_deceased", UNSET)

        include_no_valid_addresses = d.pop("include_no_valid_addresses", UNSET)

        constituent_filters = cls(
            include_inactive=include_inactive,
            include_deceased=include_deceased,
            include_no_valid_addresses=include_no_valid_addresses,
        )

        return constituent_filters

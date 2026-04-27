from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    """Defines the data model used for an address' country.

    Attributes:
        id (None | str | Unset): The ID of the country record.
        display_name (None | str | Unset): The display name of the country.
        iso_alpha2_code (None | str | Unset): The ISO 3166-1 alpha-2 code for the country.
    """

    id: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    iso_alpha2_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        iso_alpha2_code: None | str | Unset
        if isinstance(self.iso_alpha2_code, Unset):
            iso_alpha2_code = UNSET
        else:
            iso_alpha2_code = self.iso_alpha2_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if iso_alpha2_code is not UNSET:
            field_dict["iso_alpha2_code"] = iso_alpha2_code

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

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_iso_alpha2_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        iso_alpha2_code = _parse_iso_alpha2_code(d.pop("iso_alpha2_code", UNSET))

        country = cls(
            id=id,
            display_name=display_name,
            iso_alpha2_code=iso_alpha2_code,
        )

        return country

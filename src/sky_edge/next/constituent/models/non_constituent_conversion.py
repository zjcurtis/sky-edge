from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constituent_code_link import ConstituentCodeLink


T = TypeVar("T", bound="NonConstituentConversion")


@_attrs_define
class NonConstituentConversion:
    """The non-constituent conversion object holds constituent codes to apply during the conversion.

    Attributes:
        constituent_codes (list[ConstituentCodeLink] | Unset): The constituent codes.
    """

    constituent_codes: list[ConstituentCodeLink] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_codes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.constituent_codes, Unset):
            constituent_codes = []
            for constituent_codes_item_data in self.constituent_codes:
                constituent_codes_item = constituent_codes_item_data.to_dict()
                constituent_codes.append(constituent_codes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constituent_codes is not UNSET:
            field_dict["constituent_codes"] = constituent_codes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constituent_code_link import ConstituentCodeLink

        d = dict(src_dict)
        _constituent_codes = d.pop("constituent_codes", UNSET)
        constituent_codes: list[ConstituentCodeLink] | Unset = UNSET
        if _constituent_codes is not UNSET:
            constituent_codes = []
            for constituent_codes_item_data in _constituent_codes:
                constituent_codes_item = ConstituentCodeLink.from_dict(
                    constituent_codes_item_data
                )

                constituent_codes.append(constituent_codes_item)

        non_constituent_conversion = cls(
            constituent_codes=constituent_codes,
        )

        non_constituent_conversion.additional_properties = d
        return non_constituent_conversion

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

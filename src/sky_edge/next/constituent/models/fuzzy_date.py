from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="FuzzyDate")


@_attrs_define
class FuzzyDate:
    """Fuzzy dates provide a versatile date type to create partial dates such as February 9 (with no year indicated).

    Attributes:
        d (int | Unset): The day in the fuzzy date.
        m (int | Unset): The month in the fuzzy date.
        y (int | Unset): The year in the fuzzy date.
    """

    d: int | Unset = UNSET
    m: int | Unset = UNSET
    y: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        d = self.d

        m = self.m

        y = self.y

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if d is not UNSET:
            field_dict["d"] = d
        if m is not UNSET:
            field_dict["m"] = m
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    
    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _data = dict(src_dict)
    
        d = _data.pop("d", UNSET)
        m = _data.pop("m", UNSET)
        y = _data.pop("y", UNSET)
    
        fuzzy_date = cls(
            d=d,
            m=m,
            y=y,
        )
    
        fuzzy_date.additional_properties = _data
        return fuzzy_date


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

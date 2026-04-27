from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="FuzzyDate")


@_attrs_define
class FuzzyDate:
    """Expresses a date as separate Year, Month, and Day components.

    Attributes:
        y (int | None | Unset): The year of the fuzzy date Example: 2024.
        m (int | None | Unset): The month of the fuzzy date Example: 12.
        d (int | None | Unset): The day of the fuzzy date Example: 15.
    """

    y: int | None | Unset = UNSET
    m: int | None | Unset = UNSET
    d: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        y: int | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        m: int | None | Unset
        if isinstance(self.m, Unset):
            m = UNSET
        else:
            m = self.m

        d: int | None | Unset
        if isinstance(self.d, Unset):
            d = UNSET
        else:
            d = self.d

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if y is not UNSET:
            field_dict["y"] = y
        if m is not UNSET:
            field_dict["m"] = m
        if d is not UNSET:
            field_dict["d"] = d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y = _parse_y(d.pop("y", UNSET))

        def _parse_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        m = _parse_m(d.pop("m", UNSET))

        def _parse_d(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        d = _parse_d(d.pop("d", UNSET))

        fuzzy_date = cls(
            y=y,
            m=m,
            d=d,
        )

        return fuzzy_date

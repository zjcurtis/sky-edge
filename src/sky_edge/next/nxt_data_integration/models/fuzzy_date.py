from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="FuzzyDate")


@_attrs_define
class FuzzyDate:
    """
    Attributes:
        d (int | None | Unset):  Default: 0.
        m (int | None | Unset):  Default: 0.
        y (int | None | Unset):  Default: 0.
    """

    d: int | None | Unset = 0
    m: int | None | Unset = 0
    y: int | None | Unset = 0

    def to_dict(self) -> dict[str, Any]:
        d: int | None | Unset
        if isinstance(self.d, Unset):
            d = UNSET
        else:
            d = self.d

        m: int | None | Unset
        if isinstance(self.m, Unset):
            m = UNSET
        else:
            m = self.m

        y: int | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        field_dict: dict[str, Any] = {}

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
        d = dict(src_dict)

        def _parse_d(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        d = _parse_d(d.pop("d", UNSET))

        def _parse_m(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        m = _parse_m(d.pop("m", UNSET))

        def _parse_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y = _parse_y(d.pop("y", UNSET))

        fuzzy_date = cls(
            d=d,
            m=m,
            y=y,
        )

        return fuzzy_date

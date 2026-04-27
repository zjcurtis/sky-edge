from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="IssuerDetails")


@_attrs_define
class IssuerDetails:
    """Represents issuer detils for a stock gift

    Attributes:
        issuer (None | str | Unset): Issuer name Example: Google.
        symbol (None | str | Unset): Issuer symbol Example: GOOG.
        units (int | None | Unset): Number of units of stock Example: 100.
        unit_price (float | None | Unset): Median unit price Example: 90.
    """

    issuer: None | str | Unset = UNSET
    symbol: None | str | Unset = UNSET
    units: int | None | Unset = UNSET
    unit_price: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        issuer: None | str | Unset
        if isinstance(self.issuer, Unset):
            issuer = UNSET
        else:
            issuer = self.issuer

        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        units: int | None | Unset
        if isinstance(self.units, Unset):
            units = UNSET
        else:
            units = self.units

        unit_price: float | None | Unset
        if isinstance(self.unit_price, Unset):
            unit_price = UNSET
        else:
            unit_price = self.unit_price

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if units is not UNSET:
            field_dict["units"] = units
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_issuer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issuer = _parse_issuer(d.pop("issuer", UNSET))

        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))

        def _parse_units(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        units = _parse_units(d.pop("units", UNSET))

        def _parse_unit_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        unit_price = _parse_unit_price(d.pop("unit_price", UNSET))

        issuer_details = cls(
            issuer=issuer,
            symbol=symbol,
            units=units,
            unit_price=unit_price,
        )

        return issuer_details

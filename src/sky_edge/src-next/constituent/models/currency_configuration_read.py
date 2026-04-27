from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrencyConfigurationRead")


@_attrs_define
class CurrencyConfigurationRead:
    """Currency configurations combine a country and currency for an organization's monetary amounts.

    Attributes:
        country_name (str | Unset): The country that issues the currency.
        currency_symbol (str | Unset): The symbol for the currency.
        iso_alpha_2_code (str | Unset): The ISO 3166-1 two-letter country code for the currency.
        currency_code (str | Unset): The ISO 4217 three-letter currency code for the currency.
    """

    country_name: str | Unset = UNSET
    currency_symbol: str | Unset = UNSET
    iso_alpha_2_code: str | Unset = UNSET
    currency_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_name = self.country_name

        currency_symbol = self.currency_symbol

        iso_alpha_2_code = self.iso_alpha_2_code

        currency_code = self.currency_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if iso_alpha_2_code is not UNSET:
            field_dict["iso_alpha_2_code"] = iso_alpha_2_code
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_name = d.pop("country_name", UNSET)

        currency_symbol = d.pop("currency_symbol", UNSET)

        iso_alpha_2_code = d.pop("iso_alpha_2_code", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        currency_configuration_read = cls(
            country_name=country_name,
            currency_symbol=currency_symbol,
            iso_alpha_2_code=iso_alpha_2_code,
            currency_code=currency_code,
        )

        currency_configuration_read.additional_properties = d
        return currency_configuration_read

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

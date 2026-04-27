from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.country_create_country_code import CountryCreateCountryCode
from ..models.country_create_country_currency_placement import CountryCreateCountryCurrencyPlacement
from ..models.country_create_re7_country_codes import CountryCreateRE7CountryCodes
from ..types import UNSET, Unset

T = TypeVar("T", bound="CountryCreate")


@_attrs_define
class CountryCreate:
    """RE7 Country record create class from the dbo.COUNTRY_CODES table in Raiser's Edge.

    Attributes:
        name (str): The name of the country; corresponds to the LONGDESCRIPTION in dbo.TABLEENTRIES.
        abbreviation (str): The user-defined abbreviation for the country; corresponds to the SHORTDESCRIPTION in
            dbo.TABLEENTRIES.
        exchange_rate (float): The country's currency exchange rate.
        decimal_separator (str): The the decimal separator character used by the country.
        currency_symbol (str): The currency symbol used by the country.
        currency_type_id (int | None | Unset): The identifier for the country's currency type; corresponds to TYPE in
            dbo.COUNTRY_CODES.
        thousand_separator (None | str | Unset): The thousand separator character used by the country. Default: ''.
        decimal_digits (int | Unset): The number of digits following a decimal.
        currency_placement_id (CountryCreateCountryCurrencyPlacement | Unset): The value used to determine where the
            country's currency symbol is placed.
        leading_zero (bool | Unset): Value used to indicate whether a leading zero should be placed when displaying
            currency.
        iso_code (CountryCreateRE7CountryCodes | Unset): The country's ISO code.
        label_format_country (CountryCreateCountryCode | Unset): Value used to indicate the label format for the
            country.
                Default to UK format as it is the most flexible
    """

    name: str
    abbreviation: str
    exchange_rate: float
    decimal_separator: str
    currency_symbol: str
    currency_type_id: int | None | Unset = UNSET
    thousand_separator: None | str | Unset = ""
    decimal_digits: int | Unset = UNSET
    currency_placement_id: CountryCreateCountryCurrencyPlacement | Unset = UNSET
    leading_zero: bool | Unset = UNSET
    iso_code: CountryCreateRE7CountryCodes | Unset = UNSET
    label_format_country: CountryCreateCountryCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        abbreviation = self.abbreviation

        exchange_rate = self.exchange_rate

        decimal_separator = self.decimal_separator

        currency_symbol = self.currency_symbol

        currency_type_id: int | None | Unset
        if isinstance(self.currency_type_id, Unset):
            currency_type_id = UNSET
        else:
            currency_type_id = self.currency_type_id

        thousand_separator: None | str | Unset
        if isinstance(self.thousand_separator, Unset):
            thousand_separator = UNSET
        else:
            thousand_separator = self.thousand_separator

        decimal_digits = self.decimal_digits

        currency_placement_id: str | Unset = UNSET
        if not isinstance(self.currency_placement_id, Unset):
            currency_placement_id = self.currency_placement_id.value

        leading_zero = self.leading_zero

        iso_code: str | Unset = UNSET
        if not isinstance(self.iso_code, Unset):
            iso_code = self.iso_code.value

        label_format_country: str | Unset = UNSET
        if not isinstance(self.label_format_country, Unset):
            label_format_country = self.label_format_country.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "abbreviation": abbreviation,
                "exchange_rate": exchange_rate,
                "decimal_separator": decimal_separator,
                "currency_symbol": currency_symbol,
            }
        )
        if currency_type_id is not UNSET:
            field_dict["currency_type_id"] = currency_type_id
        if thousand_separator is not UNSET:
            field_dict["thousand_separator"] = thousand_separator
        if decimal_digits is not UNSET:
            field_dict["decimal_digits"] = decimal_digits
        if currency_placement_id is not UNSET:
            field_dict["currency_placement_id"] = currency_placement_id
        if leading_zero is not UNSET:
            field_dict["leading_zero"] = leading_zero
        if iso_code is not UNSET:
            field_dict["iso_code"] = iso_code
        if label_format_country is not UNSET:
            field_dict["label_format_country"] = label_format_country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        abbreviation = d.pop("abbreviation")

        exchange_rate = d.pop("exchange_rate")

        decimal_separator = d.pop("decimal_separator")

        currency_symbol = d.pop("currency_symbol")

        def _parse_currency_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currency_type_id = _parse_currency_type_id(d.pop("currency_type_id", UNSET))

        def _parse_thousand_separator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thousand_separator = _parse_thousand_separator(d.pop("thousand_separator", UNSET))

        decimal_digits = d.pop("decimal_digits", UNSET)

        _currency_placement_id = d.pop("currency_placement_id", UNSET)
        currency_placement_id: CountryCreateCountryCurrencyPlacement | Unset
        if isinstance(_currency_placement_id, Unset):
            currency_placement_id = UNSET
        else:
            currency_placement_id = CountryCreateCountryCurrencyPlacement(_currency_placement_id)

        leading_zero = d.pop("leading_zero", UNSET)

        _iso_code = d.pop("iso_code", UNSET)
        iso_code: CountryCreateRE7CountryCodes | Unset
        if isinstance(_iso_code, Unset):
            iso_code = UNSET
        else:
            iso_code = CountryCreateRE7CountryCodes(_iso_code)

        _label_format_country = d.pop("label_format_country", UNSET)
        label_format_country: CountryCreateCountryCode | Unset
        if isinstance(_label_format_country, Unset):
            label_format_country = UNSET
        else:
            label_format_country = CountryCreateCountryCode(_label_format_country)

        country_create = cls(
            name=name,
            abbreviation=abbreviation,
            exchange_rate=exchange_rate,
            decimal_separator=decimal_separator,
            currency_symbol=currency_symbol,
            currency_type_id=currency_type_id,
            thousand_separator=thousand_separator,
            decimal_digits=decimal_digits,
            currency_placement_id=currency_placement_id,
            leading_zero=leading_zero,
            iso_code=iso_code,
            label_format_country=label_format_country,
        )

        return country_create

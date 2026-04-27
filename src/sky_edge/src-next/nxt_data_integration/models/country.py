from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.country_country_code import CountryCountryCode
from ..models.country_country_currency_placement import CountryCountryCurrencyPlacement
from ..models.country_re7_country_codes import CountryRE7CountryCodes
from ..types import UNSET, Unset

T = TypeVar("T", bound="Country")


@_attrs_define
class Country:
    """RE7 Country record read class from the dbo.COUNTRY_CODES table in Raiser's Edge.

    Attributes:
        id (int | Unset): The unique identifier for the country in the COUNTRY_CODES table.
        name (None | str | Unset): The name of the country; corresponds to the LONGDESCRIPTION in dbo.TABLEENTRIES.
        abbreviation (None | str | Unset): The user-defined abbreviation for the country; corresponds to the
            SHORTDESCRIPTION in dbo.TABLEENTRIES.
        currency_type_id (int | None | Unset): The identifier for the country's currency type; corresponds to TYPE in
            dbo.COUNTRY_CODES.
        currency_type (None | str | Unset): The currency type used by the country; corresponds to the LONGDESCRIPTION in
            dbo.TABLEENTRIES.
        thousand_separator (None | str | Unset): The thousand separator character used by the country.
        exchange_rate (float | None | Unset): The country's currency exchange rate.
        decimal_separator (None | str | Unset): The the decimal separator character used by the country.
        decimal_digits (int | Unset): The number of digits following a decimal.
        currency_symbol (None | str | Unset): The currency symbol used by the country.
        currency_placement_id (CountryCountryCurrencyPlacement | Unset): The value used to determine where the
            country's currency symbol is placed.
        leading_zero (bool | Unset): Value used to indicate whether a leading zero should be placed when displaying
            currency.
        iso_code (CountryRE7CountryCodes | Unset): The country's ISO code.
        label_format_country (CountryCountryCode | Unset): Value used to indicate the label format for the country.
        country_code_id (int | None | Unset):
    """

    id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    abbreviation: None | str | Unset = UNSET
    currency_type_id: int | None | Unset = UNSET
    currency_type: None | str | Unset = UNSET
    thousand_separator: None | str | Unset = UNSET
    exchange_rate: float | None | Unset = UNSET
    decimal_separator: None | str | Unset = UNSET
    decimal_digits: int | Unset = UNSET
    currency_symbol: None | str | Unset = UNSET
    currency_placement_id: CountryCountryCurrencyPlacement | Unset = UNSET
    leading_zero: bool | Unset = UNSET
    iso_code: CountryRE7CountryCodes | Unset = UNSET
    label_format_country: CountryCountryCode | Unset = UNSET
    country_code_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        abbreviation: None | str | Unset
        if isinstance(self.abbreviation, Unset):
            abbreviation = UNSET
        else:
            abbreviation = self.abbreviation

        currency_type_id: int | None | Unset
        if isinstance(self.currency_type_id, Unset):
            currency_type_id = UNSET
        else:
            currency_type_id = self.currency_type_id

        currency_type: None | str | Unset
        if isinstance(self.currency_type, Unset):
            currency_type = UNSET
        else:
            currency_type = self.currency_type

        thousand_separator: None | str | Unset
        if isinstance(self.thousand_separator, Unset):
            thousand_separator = UNSET
        else:
            thousand_separator = self.thousand_separator

        exchange_rate: float | None | Unset
        if isinstance(self.exchange_rate, Unset):
            exchange_rate = UNSET
        else:
            exchange_rate = self.exchange_rate

        decimal_separator: None | str | Unset
        if isinstance(self.decimal_separator, Unset):
            decimal_separator = UNSET
        else:
            decimal_separator = self.decimal_separator

        decimal_digits = self.decimal_digits

        currency_symbol: None | str | Unset
        if isinstance(self.currency_symbol, Unset):
            currency_symbol = UNSET
        else:
            currency_symbol = self.currency_symbol

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

        country_code_id: int | None | Unset
        if isinstance(self.country_code_id, Unset):
            country_code_id = UNSET
        else:
            country_code_id = self.country_code_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if abbreviation is not UNSET:
            field_dict["abbreviation"] = abbreviation
        if currency_type_id is not UNSET:
            field_dict["currency_type_id"] = currency_type_id
        if currency_type is not UNSET:
            field_dict["currency_type"] = currency_type
        if thousand_separator is not UNSET:
            field_dict["thousand_separator"] = thousand_separator
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if decimal_separator is not UNSET:
            field_dict["decimal_separator"] = decimal_separator
        if decimal_digits is not UNSET:
            field_dict["decimal_digits"] = decimal_digits
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if currency_placement_id is not UNSET:
            field_dict["currency_placement_id"] = currency_placement_id
        if leading_zero is not UNSET:
            field_dict["leading_zero"] = leading_zero
        if iso_code is not UNSET:
            field_dict["iso_code"] = iso_code
        if label_format_country is not UNSET:
            field_dict["label_format_country"] = label_format_country
        if country_code_id is not UNSET:
            field_dict["country_code_id"] = country_code_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_abbreviation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        abbreviation = _parse_abbreviation(d.pop("abbreviation", UNSET))

        def _parse_currency_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        currency_type_id = _parse_currency_type_id(d.pop("currency_type_id", UNSET))

        def _parse_currency_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_type = _parse_currency_type(d.pop("currency_type", UNSET))

        def _parse_thousand_separator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thousand_separator = _parse_thousand_separator(d.pop("thousand_separator", UNSET))

        def _parse_exchange_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        exchange_rate = _parse_exchange_rate(d.pop("exchange_rate", UNSET))

        def _parse_decimal_separator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decimal_separator = _parse_decimal_separator(d.pop("decimal_separator", UNSET))

        decimal_digits = d.pop("decimal_digits", UNSET)

        def _parse_currency_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_symbol = _parse_currency_symbol(d.pop("currency_symbol", UNSET))

        _currency_placement_id = d.pop("currency_placement_id", UNSET)
        currency_placement_id: CountryCountryCurrencyPlacement | Unset
        if isinstance(_currency_placement_id, Unset):
            currency_placement_id = UNSET
        else:
            currency_placement_id = CountryCountryCurrencyPlacement(_currency_placement_id)

        leading_zero = d.pop("leading_zero", UNSET)

        _iso_code = d.pop("iso_code", UNSET)
        iso_code: CountryRE7CountryCodes | Unset
        if isinstance(_iso_code, Unset):
            iso_code = UNSET
        else:
            iso_code = CountryRE7CountryCodes(_iso_code)

        _label_format_country = d.pop("label_format_country", UNSET)
        label_format_country: CountryCountryCode | Unset
        if isinstance(_label_format_country, Unset):
            label_format_country = UNSET
        else:
            label_format_country = CountryCountryCode(_label_format_country)

        def _parse_country_code_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        country_code_id = _parse_country_code_id(d.pop("country_code_id", UNSET))

        country = cls(
            id=id,
            name=name,
            abbreviation=abbreviation,
            currency_type_id=currency_type_id,
            currency_type=currency_type,
            thousand_separator=thousand_separator,
            exchange_rate=exchange_rate,
            decimal_separator=decimal_separator,
            decimal_digits=decimal_digits,
            currency_symbol=currency_symbol,
            currency_placement_id=currency_placement_id,
            leading_zero=leading_zero,
            iso_code=iso_code,
            label_format_country=label_format_country,
            country_code_id=country_code_id,
        )

        return country

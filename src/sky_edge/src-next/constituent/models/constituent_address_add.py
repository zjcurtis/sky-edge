from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="ConstituentAddressAdd")


@_attrs_define
class ConstituentAddressAdd:
    """Defines the shape of an address for adding with a constituent.

    Attributes:
        type_ (str): The address type. Available values are the entries in the <a href="https://developer.sky.blackbaud.
            com/docs/services/56b76470069a0509c8f1c5b3/operations/ListAddressTypes"><b>Address Types</b></a> table.
        address_lines (str | Unset): The address lines. Character limit: 150.
        city (str | Unset): The city of the address. Character limit: 50.
        country (str | Unset): The country of the address.
        county (str | Unset): The county of the address.
        do_not_mail (bool | Unset): Indicates whether the constituent requests not to be contacted at this address.
        end (datetime.datetime | Unset): The date when the constituent ceased to reside at this address. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
        postal_code (str | Unset): The postal code of the address. Character limit: 12.
        seasonal_end (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
            February 9 (with no year indicated).
        seasonal_start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
            February 9 (with no year indicated).
        start (datetime.datetime | Unset): The date when the constituent began residing at this address. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
        state (str | Unset): The state of the address.
        suburb (str | Unset): The suburb of the address.
    """

    type_: str
    address_lines: str | Unset = UNSET
    city: str | Unset = UNSET
    country: str | Unset = UNSET
    county: str | Unset = UNSET
    do_not_mail: bool | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    postal_code: str | Unset = UNSET
    seasonal_end: FuzzyDate | Unset = UNSET
    seasonal_start: FuzzyDate | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    state: str | Unset = UNSET
    suburb: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        address_lines = self.address_lines

        city = self.city

        country = self.country

        county = self.county

        do_not_mail = self.do_not_mail

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        postal_code = self.postal_code

        seasonal_end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seasonal_end, Unset):
            seasonal_end = self.seasonal_end.to_dict()

        seasonal_start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seasonal_start, Unset):
            seasonal_start = self.seasonal_start.to_dict()

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        state = self.state

        suburb = self.suburb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if address_lines is not UNSET:
            field_dict["address_lines"] = address_lines
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if county is not UNSET:
            field_dict["county"] = county
        if do_not_mail is not UNSET:
            field_dict["do_not_mail"] = do_not_mail
        if end is not UNSET:
            field_dict["end"] = end
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if seasonal_end is not UNSET:
            field_dict["seasonal_end"] = seasonal_end
        if seasonal_start is not UNSET:
            field_dict["seasonal_start"] = seasonal_start
        if start is not UNSET:
            field_dict["start"] = start
        if state is not UNSET:
            field_dict["state"] = state
        if suburb is not UNSET:
            field_dict["suburb"] = suburb

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        type_ = d.pop("type")

        address_lines = d.pop("address_lines", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        county = d.pop("county", UNSET)

        do_not_mail = d.pop("do_not_mail", UNSET)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        postal_code = d.pop("postal_code", UNSET)

        _seasonal_end = d.pop("seasonal_end", UNSET)
        seasonal_end: FuzzyDate | Unset
        if isinstance(_seasonal_end, Unset):
            seasonal_end = UNSET
        else:
            seasonal_end = FuzzyDate.from_dict(_seasonal_end)

        _seasonal_start = d.pop("seasonal_start", UNSET)
        seasonal_start: FuzzyDate | Unset
        if isinstance(_seasonal_start, Unset):
            seasonal_start = UNSET
        else:
            seasonal_start = FuzzyDate.from_dict(_seasonal_start)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        state = d.pop("state", UNSET)

        suburb = d.pop("suburb", UNSET)

        constituent_address_add = cls(
            type_=type_,
            address_lines=address_lines,
            city=city,
            country=country,
            county=county,
            do_not_mail=do_not_mail,
            end=end,
            postal_code=postal_code,
            seasonal_end=seasonal_end,
            seasonal_start=seasonal_start,
            start=start,
            state=state,
            suburb=suburb,
        )

        constituent_address_add.additional_properties = d
        return constituent_address_add

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

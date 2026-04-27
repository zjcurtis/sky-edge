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


T = TypeVar("T", bound="AddressReadExtended")


@_attrs_define
class AddressReadExtended:
    """Addresses store information about constituent residences and other addresses along with information about where,
    how, and whether to send mail.

        Attributes:
            id (str | Unset): The immutable system record ID of the address.
            address_lines (str | Unset): The address lines.
            city (str | Unset): The city of the address.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the address.
            country (str | Unset): The country of the address.
            county (str | Unset): The county of the address.
            date_added (datetime.datetime | Unset): The date when the address was created. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the address was last modified. Includes an offset from
                UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            do_not_mail (bool | Unset): Indicates whether the constituent requests not to be contacted at this address.
            end (datetime.datetime | Unset): The date when the constituent ceased to reside at this address. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            formatted_address (str | Unset): This computed field retrieves the formatted address in the configured format of
                the country.
            inactive (bool | Unset): This computed field indicates that the address is active if the current date is before
                any <code>end</code> date.
            postal_code (str | Unset): The postal code of the address.
            preferred (bool | Unset): Indicates whether this is the constituent's preferred address.
            seasonal_end (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            seasonal_start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            start (datetime.datetime | Unset): The date when the constituent began residing at this address. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            state (str | Unset): The state of the address.
            suburb (str | Unset): The suburb of the address.
            type_ (str | Unset): The address type. Available values are the entries in the <a href="https://developer.sky.bl
                ackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListAddressTypes"><b>Address Types</b></a> table.
            region (str | Unset): The region of the address.
            information_source (str | Unset): The information source for the address.
            lot (str | Unset): The Line of Travel (LOT) for the address.
            cart (str | Unset): The Carrier Route (CART) for the address.
            dpc (str | Unset): The Delivery Point Code (DPC) for the address.
    """

    id: str | Unset = UNSET
    address_lines: str | Unset = UNSET
    city: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    country: str | Unset = UNSET
    county: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    do_not_mail: bool | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    formatted_address: str | Unset = UNSET
    inactive: bool | Unset = UNSET
    postal_code: str | Unset = UNSET
    preferred: bool | Unset = UNSET
    seasonal_end: FuzzyDate | Unset = UNSET
    seasonal_start: FuzzyDate | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    state: str | Unset = UNSET
    suburb: str | Unset = UNSET
    type_: str | Unset = UNSET
    region: str | Unset = UNSET
    information_source: str | Unset = UNSET
    lot: str | Unset = UNSET
    cart: str | Unset = UNSET
    dpc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address_lines = self.address_lines

        city = self.city

        constituent_id = self.constituent_id

        country = self.country

        county = self.county

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        do_not_mail = self.do_not_mail

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        formatted_address = self.formatted_address

        inactive = self.inactive

        postal_code = self.postal_code

        preferred = self.preferred

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

        type_ = self.type_

        region = self.region

        information_source = self.information_source

        lot = self.lot

        cart = self.cart

        dpc = self.dpc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address_lines is not UNSET:
            field_dict["address_lines"] = address_lines
        if city is not UNSET:
            field_dict["city"] = city
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if country is not UNSET:
            field_dict["country"] = country
        if county is not UNSET:
            field_dict["county"] = county
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if do_not_mail is not UNSET:
            field_dict["do_not_mail"] = do_not_mail
        if end is not UNSET:
            field_dict["end"] = end
        if formatted_address is not UNSET:
            field_dict["formatted_address"] = formatted_address
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if region is not UNSET:
            field_dict["region"] = region
        if information_source is not UNSET:
            field_dict["information_source"] = information_source
        if lot is not UNSET:
            field_dict["lot"] = lot
        if cart is not UNSET:
            field_dict["cart"] = cart
        if dpc is not UNSET:
            field_dict["dpc"] = dpc

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        address_lines = d.pop("address_lines", UNSET)

        city = d.pop("city", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        country = d.pop("country", UNSET)

        county = d.pop("county", UNSET)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        do_not_mail = d.pop("do_not_mail", UNSET)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        formatted_address = d.pop("formatted_address", UNSET)

        inactive = d.pop("inactive", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        preferred = d.pop("preferred", UNSET)

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

        type_ = d.pop("type", UNSET)

        region = d.pop("region", UNSET)

        information_source = d.pop("information_source", UNSET)

        lot = d.pop("lot", UNSET)

        cart = d.pop("cart", UNSET)

        dpc = d.pop("dpc", UNSET)

        address_read_extended = cls(
            id=id,
            address_lines=address_lines,
            city=city,
            constituent_id=constituent_id,
            country=country,
            county=county,
            date_added=date_added,
            date_modified=date_modified,
            do_not_mail=do_not_mail,
            end=end,
            formatted_address=formatted_address,
            inactive=inactive,
            postal_code=postal_code,
            preferred=preferred,
            seasonal_end=seasonal_end,
            seasonal_start=seasonal_start,
            start=start,
            state=state,
            suburb=suburb,
            type_=type_,
            region=region,
            information_source=information_source,
            lot=lot,
            cart=cart,
            dpc=dpc,
        )

        address_read_extended.additional_properties = d
        return address_read_extended

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

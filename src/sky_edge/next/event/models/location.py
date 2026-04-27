from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.administrative_area import AdministrativeArea
    from ..models.country import Country
    from ..models.locality import Locality
    from ..models.sub_administrative_area import SubAdministrativeArea


T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """Defines the data model used for a location.

    Attributes:
        name (None | str | Unset): The name of the location.
        address_lines (None | str | Unset): The location's address lines.
        postal_code (None | str | Unset): The location's postal code.
        locality (Locality | Unset): Defines the data model used for an address' locality. E.g. city in the US.
        administrative_area (AdministrativeArea | Unset): Defines the data model used for an address' administrative
            area. E.g. state in the US.
        sub_administrative_area (SubAdministrativeArea | Unset): Defines the data model used for an address' sub
            administrative area. E.g. city in the US.
        country (Country | Unset): Defines the data model used for an address' country.
        formatted_address (None | str | Unset): The location's formatted address
        phone (None | str | Unset): The location's phone number.
        contact (None | str | Unset): The location's contact details.
        notes (None | str | Unset): The location's notes.
    """

    name: None | str | Unset = UNSET
    address_lines: None | str | Unset = UNSET
    postal_code: None | str | Unset = UNSET
    locality: Locality | Unset = UNSET
    administrative_area: AdministrativeArea | Unset = UNSET
    sub_administrative_area: SubAdministrativeArea | Unset = UNSET
    country: Country | Unset = UNSET
    formatted_address: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    contact: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        address_lines: None | str | Unset
        if isinstance(self.address_lines, Unset):
            address_lines = UNSET
        else:
            address_lines = self.address_lines

        postal_code: None | str | Unset
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        locality: dict[str, Any] | Unset = UNSET
        if not isinstance(self.locality, Unset):
            locality = self.locality.to_dict()

        administrative_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.administrative_area, Unset):
            administrative_area = self.administrative_area.to_dict()

        sub_administrative_area: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sub_administrative_area, Unset):
            sub_administrative_area = self.sub_administrative_area.to_dict()

        country: dict[str, Any] | Unset = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        formatted_address: None | str | Unset
        if isinstance(self.formatted_address, Unset):
            formatted_address = UNSET
        else:
            formatted_address = self.formatted_address

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        contact: None | str | Unset
        if isinstance(self.contact, Unset):
            contact = UNSET
        else:
            contact = self.contact

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if address_lines is not UNSET:
            field_dict["address_lines"] = address_lines
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if locality is not UNSET:
            field_dict["locality"] = locality
        if administrative_area is not UNSET:
            field_dict["administrative_area"] = administrative_area
        if sub_administrative_area is not UNSET:
            field_dict["sub_administrative_area"] = sub_administrative_area
        if country is not UNSET:
            field_dict["country"] = country
        if formatted_address is not UNSET:
            field_dict["formatted_address"] = formatted_address
        if phone is not UNSET:
            field_dict["phone"] = phone
        if contact is not UNSET:
            field_dict["contact"] = contact
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.administrative_area import AdministrativeArea
        from ..models.country import Country
        from ..models.locality import Locality
        from ..models.sub_administrative_area import SubAdministrativeArea

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_address_lines(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_lines = _parse_address_lines(d.pop("address_lines", UNSET))

        def _parse_postal_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_code = _parse_postal_code(d.pop("postal_code", UNSET))

        _locality = d.pop("locality", UNSET)
        locality: Locality | Unset
        if isinstance(_locality, Unset):
            locality = UNSET
        else:
            locality = Locality.from_dict(_locality)

        _administrative_area = d.pop("administrative_area", UNSET)
        administrative_area: AdministrativeArea | Unset
        if isinstance(_administrative_area, Unset):
            administrative_area = UNSET
        else:
            administrative_area = AdministrativeArea.from_dict(_administrative_area)

        _sub_administrative_area = d.pop("sub_administrative_area", UNSET)
        sub_administrative_area: SubAdministrativeArea | Unset
        if isinstance(_sub_administrative_area, Unset):
            sub_administrative_area = UNSET
        else:
            sub_administrative_area = SubAdministrativeArea.from_dict(
                _sub_administrative_area
            )

        _country = d.pop("country", UNSET)
        country: Country | Unset
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = Country.from_dict(_country)

        def _parse_formatted_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formatted_address = _parse_formatted_address(d.pop("formatted_address", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_contact(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact = _parse_contact(d.pop("contact", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        location = cls(
            name=name,
            address_lines=address_lines,
            postal_code=postal_code,
            locality=locality,
            administrative_area=administrative_area,
            sub_administrative_area=sub_administrative_area,
            country=country,
            formatted_address=formatted_address,
            phone=phone,
            contact=contact,
            notes=notes,
        )

        return location

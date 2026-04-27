from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="SearchResultRead")


@_attrs_define
class SearchResultRead:
    """The search result entity describes the search results from a basic constituent search based on provided search text.

    Attributes:
        id (str | Unset): The immutable system record ID of the constituent.
        address (str | Unset): The constituent's preferred address.
        deceased (bool | Unset): Indicates whether the constituent is deceased.
        email (str | Unset): The constituent's email address.
        fundraiser_status (str | Unset): The constituent's fundraiser status. If the constituent's <code>type</code> is
            <i>Individual</i>, this computed field indicates the whether the constituent is <i>Active</i>, <i>Inactive</i>,
            or <i>None</i>.  If the constituent's <code>type</code> is <i>Organization</i>, this value will always be
            <i>None</i>.
        inactive (bool | Unset): Indicates whether the constituent is inactive.
        lookup_id (str | Unset): The user-defined identifier for the constituent.
        name (str | Unset): The constituent name. If the constituent's <code>type</code> is <i>Individual</i>, this
            computed field indicates the full name of the constituent based on the target organization’s display name
            settings.
        number_of_subsidiaries (int | Unset): Organization's number of subsidiaries
    """

    id: str | Unset = UNSET
    address: str | Unset = UNSET
    deceased: bool | Unset = UNSET
    email: str | Unset = UNSET
    fundraiser_status: str | Unset = UNSET
    inactive: bool | Unset = UNSET
    lookup_id: str | Unset = UNSET
    name: str | Unset = UNSET
    number_of_subsidiaries: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address = self.address

        deceased = self.deceased

        email = self.email

        fundraiser_status = self.fundraiser_status

        inactive = self.inactive

        lookup_id = self.lookup_id

        name = self.name

        number_of_subsidiaries = self.number_of_subsidiaries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address is not UNSET:
            field_dict["address"] = address
        if deceased is not UNSET:
            field_dict["deceased"] = deceased
        if email is not UNSET:
            field_dict["email"] = email
        if fundraiser_status is not UNSET:
            field_dict["fundraiser_status"] = fundraiser_status
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if name is not UNSET:
            field_dict["name"] = name
        if number_of_subsidiaries is not UNSET:
            field_dict["number_of_subsidiaries"] = number_of_subsidiaries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        address = d.pop("address", UNSET)

        deceased = d.pop("deceased", UNSET)

        email = d.pop("email", UNSET)

        fundraiser_status = d.pop("fundraiser_status", UNSET)

        inactive = d.pop("inactive", UNSET)

        lookup_id = d.pop("lookup_id", UNSET)

        name = d.pop("name", UNSET)

        number_of_subsidiaries = d.pop("number_of_subsidiaries", UNSET)

        search_result_read = cls(
            id=id,
            address=address,
            deceased=deceased,
            email=email,
            fundraiser_status=fundraiser_status,
            inactive=inactive,
            lookup_id=lookup_id,
            name=name,
            number_of_subsidiaries=number_of_subsidiaries,
        )

        search_result_read.additional_properties = d
        return search_result_read

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="DuplicateSearchResultRead")


@_attrs_define
class DuplicateSearchResultRead:
    """Represents a constituent record that matches the provided duplicate search options.

    Attributes:
        id (str | Unset): The primary identifier for the constituent.
        constituent_id (str | Unset): The import identifier for the constituent.
        name (str | Unset): The constituent's name formatted according to the user-defined configuration settings in
            database view. This is how the constituent's name appears at the top of a record.
        formatted_address (str | Unset): The formatted primary address for the constituent.
        deceased (bool | Unset): Indicates whether the constituent is deceased.
        is_constituent (bool | Unset): Indicates whether the record is for a constituent.
        date_added (datetime.datetime | Unset): The date the constituent was added.
        rank (str | Unset): The search rank indicating what the constituent was matched on.
        display_name (str | Unset): The constituent's display name (first name, middle initial, and last name for
            individuals) as it appears on lists and in search results.
    """

    id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    name: str | Unset = UNSET
    formatted_address: str | Unset = UNSET
    deceased: bool | Unset = UNSET
    is_constituent: bool | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    rank: str | Unset = UNSET
    display_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        name = self.name

        formatted_address = self.formatted_address

        deceased = self.deceased

        is_constituent = self.is_constituent

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        rank = self.rank

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if name is not UNSET:
            field_dict["name"] = name
        if formatted_address is not UNSET:
            field_dict["formatted_address"] = formatted_address
        if deceased is not UNSET:
            field_dict["deceased"] = deceased
        if is_constituent is not UNSET:
            field_dict["is_constituent"] = is_constituent
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if rank is not UNSET:
            field_dict["rank"] = rank
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        name = d.pop("name", UNSET)

        formatted_address = d.pop("formatted_address", UNSET)

        deceased = d.pop("deceased", UNSET)

        is_constituent = d.pop("is_constituent", UNSET)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        rank = d.pop("rank", UNSET)

        display_name = d.pop("display_name", UNSET)

        duplicate_search_result_read = cls(
            id=id,
            constituent_id=constituent_id,
            name=name,
            formatted_address=formatted_address,
            deceased=deceased,
            is_constituent=is_constituent,
            date_added=date_added,
            rank=rank,
            display_name=display_name,
        )

        duplicate_search_result_read.additional_properties = d
        return duplicate_search_result_read

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

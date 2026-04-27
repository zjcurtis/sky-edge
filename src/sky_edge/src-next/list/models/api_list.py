from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiList")


@_attrs_define
class ApiList:
    """Represents the List entity

    Attributes:
        id (str | Unset): The immutable system record ID for the list
        name (str | Unset): The name of the list
        description (str | Unset): The description of the list
        record_count (int | Unset): The total number of records defined by this list based on the last time this list
            was saved
        date_modified (datetime.datetime | Unset): The date this list was last modified. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>
        last_modified_by_user_name (str | Unset): The name of the user that last modified the list
        last_modified_by_user_id (str | Unset): The ID of the user that last modified the list
        is_public (bool | Unset): Indicates whether this is a public or private list.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    record_count: int | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    last_modified_by_user_name: str | Unset = UNSET
    last_modified_by_user_id: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        record_count = self.record_count

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        last_modified_by_user_name = self.last_modified_by_user_name

        last_modified_by_user_id = self.last_modified_by_user_id

        is_public = self.is_public

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if record_count is not UNSET:
            field_dict["record_count"] = record_count
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if last_modified_by_user_name is not UNSET:
            field_dict["last_modified_by_user_name"] = last_modified_by_user_name
        if last_modified_by_user_id is not UNSET:
            field_dict["last_modified_by_user_id"] = last_modified_by_user_id
        if is_public is not UNSET:
            field_dict["is_public"] = is_public

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        record_count = d.pop("record_count", UNSET)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        last_modified_by_user_name = d.pop("last_modified_by_user_name", UNSET)

        last_modified_by_user_id = d.pop("last_modified_by_user_id", UNSET)

        is_public = d.pop("is_public", UNSET)

        api_list = cls(
            id=id,
            name=name,
            description=description,
            record_count=record_count,
            date_modified=date_modified,
            last_modified_by_user_name=last_modified_by_user_name,
            last_modified_by_user_id=last_modified_by_user_id,
            is_public=is_public,
        )

        api_list.additional_properties = d
        return api_list

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

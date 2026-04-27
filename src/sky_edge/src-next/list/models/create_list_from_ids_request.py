from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_list_from_ids_request_list_permissions import CreateListFromIdsRequestListPermissions
from ..models.create_list_from_ids_request_list_type import CreateListFromIdsRequestListType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateListFromIdsRequest")


@_attrs_define
class CreateListFromIdsRequest:
    """Represents a request to create a list filtered to a set of unique record identifiers

    Attributes:
        name (str): The name of the list
        list_type (CreateListFromIdsRequestListType): Determines the type of list to create. Currently supports
            'Constituent', 'Gift', 'Action', 'Opportunity'.
        list_permissions (CreateListFromIdsRequestListPermissions): Determines whether other users can access the list.
            Currently supports 'OnlyOwnerCanAccess', 'OthersCanView', 'OthersCanViewAndEdit'.
        ids (list[str]): The unique identifiers for the records contained in the list. Limited to a maximumum 100,000
            identifiers.
        description (str | Unset): The description of the list
    """

    name: str
    list_type: CreateListFromIdsRequestListType
    list_permissions: CreateListFromIdsRequestListPermissions
    ids: list[str]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        list_type = self.list_type.value

        list_permissions = self.list_permissions.value

        ids = self.ids

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "list_type": list_type,
                "list_permissions": list_permissions,
                "ids": ids,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        list_type = CreateListFromIdsRequestListType(d.pop("list_type"))

        list_permissions = CreateListFromIdsRequestListPermissions(d.pop("list_permissions"))

        ids = cast(list[str], d.pop("ids"))

        description = d.pop("description", UNSET)

        create_list_from_ids_request = cls(
            name=name,
            list_type=list_type,
            list_permissions=list_permissions,
            ids=ids,
            description=description,
        )

        create_list_from_ids_request.additional_properties = d
        return create_list_from_ids_request

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

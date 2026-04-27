from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.save_list_request_list_permission import SaveListRequestListPermission

if TYPE_CHECKING:
    from ..models.list_definition import ListDefinition


T = TypeVar("T", bound="SaveListRequest")


@_attrs_define
class SaveListRequest:
    """
    Attributes:
        list_type (str):
        name (str):
        definition (ListDefinition): Represents a list definition
        list_id (None | str | Unset):
        permissions (SaveListRequestListPermission | Unset):
        record_count (int | None | Unset):
        description (None | str | Unset):
    """

    list_type: str
    name: str
    definition: ListDefinition
    list_id: None | str | Unset = UNSET
    permissions: SaveListRequestListPermission | Unset = UNSET
    record_count: int | None | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        list_type = self.list_type

        name = self.name

        definition = self.definition.to_dict()

        list_id: None | str | Unset
        if isinstance(self.list_id, Unset):
            list_id = UNSET
        else:
            list_id = self.list_id

        permissions: str | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.value

        record_count: int | None | Unset
        if isinstance(self.record_count, Unset):
            record_count = UNSET
        else:
            record_count = self.record_count

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "list_type": list_type,
                "name": name,
                "definition": definition,
            }
        )
        if list_id is not UNSET:
            field_dict["list_id"] = list_id
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if record_count is not UNSET:
            field_dict["record_count"] = record_count
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_definition import ListDefinition

        d = dict(src_dict)
        list_type = d.pop("list_type")

        name = d.pop("name")

        definition = ListDefinition.from_dict(d.pop("definition"))

        def _parse_list_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_id = _parse_list_id(d.pop("list_id", UNSET))

        _permissions = d.pop("permissions", UNSET)
        permissions: SaveListRequestListPermission | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = SaveListRequestListPermission(_permissions)

        def _parse_record_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record_count = _parse_record_count(d.pop("record_count", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        save_list_request = cls(
            list_type=list_type,
            name=name,
            definition=definition,
            list_id=list_id,
            permissions=permissions,
            record_count=record_count,
            description=description,
        )

        return save_list_request

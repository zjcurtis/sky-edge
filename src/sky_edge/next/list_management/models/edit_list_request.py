from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.edit_list_request_list_permission import EditListRequestListPermission

if TYPE_CHECKING:
    from ..models.list_definition import ListDefinition


T = TypeVar("T", bound="EditListRequest")


@_attrs_define
class EditListRequest:
    """
    Attributes:
        name (None | str | Unset):
        definition (ListDefinition | Unset): Represents a list definition
        permissions (EditListRequestListPermission | Unset):
        record_count (int | None | Unset):
        description (None | str | Unset):
        if_match_last_changed_date (datetime.datetime | None | Unset):
    """

    name: None | str | Unset = UNSET
    definition: ListDefinition | Unset = UNSET
    permissions: EditListRequestListPermission | Unset = UNSET
    record_count: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    if_match_last_changed_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

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

        if_match_last_changed_date: None | str | Unset
        if isinstance(self.if_match_last_changed_date, Unset):
            if_match_last_changed_date = UNSET
        elif isinstance(self.if_match_last_changed_date, datetime.datetime):
            if_match_last_changed_date = self.if_match_last_changed_date.isoformat()
        else:
            if_match_last_changed_date = self.if_match_last_changed_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if definition is not UNSET:
            field_dict["definition"] = definition
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if record_count is not UNSET:
            field_dict["record_count"] = record_count
        if description is not UNSET:
            field_dict["description"] = description
        if if_match_last_changed_date is not UNSET:
            field_dict["if_match_last_changed_date"] = if_match_last_changed_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_definition import ListDefinition

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _definition = d.pop("definition", UNSET)
        definition: ListDefinition | Unset
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = ListDefinition.from_dict(_definition)

        _permissions = d.pop("permissions", UNSET)
        permissions: EditListRequestListPermission | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = EditListRequestListPermission(_permissions)

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

        def _parse_if_match_last_changed_date(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                if_match_last_changed_date_type_0 = isoparse(data)

                return if_match_last_changed_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        if_match_last_changed_date = _parse_if_match_last_changed_date(
            d.pop("if_match_last_changed_date", UNSET)
        )

        edit_list_request = cls(
            name=name,
            definition=definition,
            permissions=permissions,
            record_count=record_count,
            description=description,
            if_match_last_changed_date=if_match_last_changed_date,
        )

        return edit_list_request

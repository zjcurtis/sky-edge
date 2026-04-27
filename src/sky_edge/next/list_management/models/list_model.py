from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.list_model_list_permission import ListModelListPermission

if TYPE_CHECKING:
    from ..models.list_definition import ListDefinition


T = TypeVar("T", bound="ListModel")


@_attrs_define
class ListModel:
    """
    Attributes:
        id (None | str | Unset):
        list_type (None | str | Unset):
        name (None | str | Unset):
        public_name (None | str | Unset):
        definition (ListDefinition | Unset): Represents a list definition
        permissions (ListModelListPermission | Unset):
        created_by_user_id (None | str | Unset):
        created_by_user_name (None | str | Unset):
        created_date (datetime.datetime | None | Unset):
        last_changed_by_user_id (None | str | Unset):
        last_changed_by_user_name (None | str | Unset):
        last_changed_date (datetime.datetime | None | Unset):
        record_count (int | None | Unset):
        record_count_as_of_date (datetime.datetime | None | Unset):
        description (None | str | Unset):
        is_owner (bool | Unset):
    """

    id: None | str | Unset = UNSET
    list_type: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    public_name: None | str | Unset = UNSET
    definition: ListDefinition | Unset = UNSET
    permissions: ListModelListPermission | Unset = UNSET
    created_by_user_id: None | str | Unset = UNSET
    created_by_user_name: None | str | Unset = UNSET
    created_date: datetime.datetime | None | Unset = UNSET
    last_changed_by_user_id: None | str | Unset = UNSET
    last_changed_by_user_name: None | str | Unset = UNSET
    last_changed_date: datetime.datetime | None | Unset = UNSET
    record_count: int | None | Unset = UNSET
    record_count_as_of_date: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    is_owner: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        list_type: None | str | Unset
        if isinstance(self.list_type, Unset):
            list_type = UNSET
        else:
            list_type = self.list_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        public_name: None | str | Unset
        if isinstance(self.public_name, Unset):
            public_name = UNSET
        else:
            public_name = self.public_name

        definition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        permissions: str | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.value

        created_by_user_id: None | str | Unset
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        created_by_user_name: None | str | Unset
        if isinstance(self.created_by_user_name, Unset):
            created_by_user_name = UNSET
        else:
            created_by_user_name = self.created_by_user_name

        created_date: None | str | Unset
        if isinstance(self.created_date, Unset):
            created_date = UNSET
        elif isinstance(self.created_date, datetime.datetime):
            created_date = self.created_date.isoformat()
        else:
            created_date = self.created_date

        last_changed_by_user_id: None | str | Unset
        if isinstance(self.last_changed_by_user_id, Unset):
            last_changed_by_user_id = UNSET
        else:
            last_changed_by_user_id = self.last_changed_by_user_id

        last_changed_by_user_name: None | str | Unset
        if isinstance(self.last_changed_by_user_name, Unset):
            last_changed_by_user_name = UNSET
        else:
            last_changed_by_user_name = self.last_changed_by_user_name

        last_changed_date: None | str | Unset
        if isinstance(self.last_changed_date, Unset):
            last_changed_date = UNSET
        elif isinstance(self.last_changed_date, datetime.datetime):
            last_changed_date = self.last_changed_date.isoformat()
        else:
            last_changed_date = self.last_changed_date

        record_count: int | None | Unset
        if isinstance(self.record_count, Unset):
            record_count = UNSET
        else:
            record_count = self.record_count

        record_count_as_of_date: None | str | Unset
        if isinstance(self.record_count_as_of_date, Unset):
            record_count_as_of_date = UNSET
        elif isinstance(self.record_count_as_of_date, datetime.datetime):
            record_count_as_of_date = self.record_count_as_of_date.isoformat()
        else:
            record_count_as_of_date = self.record_count_as_of_date

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        is_owner = self.is_owner

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if list_type is not UNSET:
            field_dict["list_type"] = list_type
        if name is not UNSET:
            field_dict["name"] = name
        if public_name is not UNSET:
            field_dict["public_name"] = public_name
        if definition is not UNSET:
            field_dict["definition"] = definition
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if created_by_user_name is not UNSET:
            field_dict["created_by_user_name"] = created_by_user_name
        if created_date is not UNSET:
            field_dict["created_date"] = created_date
        if last_changed_by_user_id is not UNSET:
            field_dict["last_changed_by_user_id"] = last_changed_by_user_id
        if last_changed_by_user_name is not UNSET:
            field_dict["last_changed_by_user_name"] = last_changed_by_user_name
        if last_changed_date is not UNSET:
            field_dict["last_changed_date"] = last_changed_date
        if record_count is not UNSET:
            field_dict["record_count"] = record_count
        if record_count_as_of_date is not UNSET:
            field_dict["record_count_as_of_date"] = record_count_as_of_date
        if description is not UNSET:
            field_dict["description"] = description
        if is_owner is not UNSET:
            field_dict["is_owner"] = is_owner

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_definition import ListDefinition

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_list_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_type = _parse_list_type(d.pop("list_type", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_public_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_name = _parse_public_name(d.pop("public_name", UNSET))

        _definition = d.pop("definition", UNSET)
        definition: ListDefinition | Unset
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = ListDefinition.from_dict(_definition)

        _permissions = d.pop("permissions", UNSET)
        permissions: ListModelListPermission | Unset
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = ListModelListPermission(_permissions)

        def _parse_created_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_user_id = _parse_created_by_user_id(
            d.pop("created_by_user_id", UNSET)
        )

        def _parse_created_by_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by_user_name = _parse_created_by_user_name(
            d.pop("created_by_user_name", UNSET)
        )

        def _parse_created_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_date_type_0 = isoparse(data)

                return created_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_date = _parse_created_date(d.pop("created_date", UNSET))

        def _parse_last_changed_by_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_changed_by_user_id = _parse_last_changed_by_user_id(
            d.pop("last_changed_by_user_id", UNSET)
        )

        def _parse_last_changed_by_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_changed_by_user_name = _parse_last_changed_by_user_name(
            d.pop("last_changed_by_user_name", UNSET)
        )

        def _parse_last_changed_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_changed_date_type_0 = isoparse(data)

                return last_changed_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_changed_date = _parse_last_changed_date(d.pop("last_changed_date", UNSET))

        def _parse_record_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record_count = _parse_record_count(d.pop("record_count", UNSET))

        def _parse_record_count_as_of_date(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_count_as_of_date_type_0 = isoparse(data)

                return record_count_as_of_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        record_count_as_of_date = _parse_record_count_as_of_date(
            d.pop("record_count_as_of_date", UNSET)
        )

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        is_owner = d.pop("is_owner", UNSET)

        list_model = cls(
            id=id,
            list_type=list_type,
            name=name,
            public_name=public_name,
            definition=definition,
            permissions=permissions,
            created_by_user_id=created_by_user_id,
            created_by_user_name=created_by_user_name,
            created_date=created_date,
            last_changed_by_user_id=last_changed_by_user_id,
            last_changed_by_user_name=last_changed_by_user_name,
            last_changed_date=last_changed_date,
            record_count=record_count,
            record_count_as_of_date=record_count_as_of_date,
            description=description,
            is_owner=is_owner,
        )

        return list_model

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Represents the fields for a user record in dbo.USERS.

    Attributes:
        user_id (int | Unset): The user ID.
        name (None | str | Unset): The Raiser's Edge user name.
        constituent_id (int | None | Unset): The constituent ID associated with a user.
        is_fundraiser (bool | Unset): Indicates whether the user is a fundraiser.
    """

    user_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    constituent_id: int | None | Unset = UNSET
    is_fundraiser: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        constituent_id: int | None | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        is_fundraiser = self.is_fundraiser

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if is_fundraiser is not UNSET:
            field_dict["is_fundraiser"] = is_fundraiser

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_constituent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        is_fundraiser = d.pop("is_fundraiser", UNSET)

        user = cls(
            user_id=user_id,
            name=name,
            constituent_id=constituent_id,
            is_fundraiser=is_fundraiser,
        )

        return user

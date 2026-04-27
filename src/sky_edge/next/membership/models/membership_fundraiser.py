from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="MembershipFundraiser")


@_attrs_define
class MembershipFundraiser:
    """Membership Fundraiser

    Attributes:
        id (None | str | Unset): The immutable system record ID of the fundraiser.
        solicitor_id (int | Unset): Fundraisers ID.
        full_name (None | str | Unset): Nullable field Fundraisers full name.
    """

    id: None | str | Unset = UNSET
    solicitor_id: int | Unset = UNSET
    full_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        solicitor_id = self.solicitor_id

        full_name: None | str | Unset
        if isinstance(self.full_name, Unset):
            full_name = UNSET
        else:
            full_name = self.full_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if solicitor_id is not UNSET:
            field_dict["solicitor_id"] = solicitor_id
        if full_name is not UNSET:
            field_dict["full_name"] = full_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        solicitor_id = d.pop("solicitor_id", UNSET)

        def _parse_full_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        full_name = _parse_full_name(d.pop("full_name", UNSET))

        membership_fundraiser = cls(
            id=id,
            solicitor_id=solicitor_id,
            full_name=full_name,
        )

        return membership_fundraiser

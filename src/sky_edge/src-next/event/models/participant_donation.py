from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantDonation")


@_attrs_define
class ParticipantDonation:
    """Defines a data model for a participant donation

    Attributes:
        id (None | str | Unset): The ID of the participant donation.
        gift_id (None | str | Unset): The ID of the gift that the participant donation is linked to.
    """

    id: None | str | Unset = UNSET
    gift_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        gift_id: None | str | Unset
        if isinstance(self.gift_id, Unset):
            gift_id = UNSET
        else:
            gift_id = self.gift_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id

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

        def _parse_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_id = _parse_gift_id(d.pop("gift_id", UNSET))

        participant_donation = cls(
            id=id,
            gift_id=gift_id,
        )

        return participant_donation

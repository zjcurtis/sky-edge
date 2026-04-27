from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateParticipantDonation")


@_attrs_define
class CreateParticipantDonation:
    """Participant donations are donations made toward the event.

    Attributes:
        gift_id (str): The ID of the gift or pledge that the donation is linked to.
    """

    gift_id: str

    def to_dict(self) -> dict[str, Any]:
        gift_id = self.gift_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_id": gift_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_id = d.pop("gift_id")

        create_participant_donation = cls(
            gift_id=gift_id,
        )

        return create_participant_donation

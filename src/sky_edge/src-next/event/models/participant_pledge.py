from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.participant_pledge_type import ParticipantPledgeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantPledge")


@_attrs_define
class ParticipantPledge:
    """Defines a data model for a participant pledge

    Attributes:
        id (None | str | Unset): The ID of the participant pledge.
        gift_id (None | str | Unset): The ID of the gift that the participant pledge is linked to.
        type_ (ParticipantPledgeType | Unset): The participant gift link type<p>Available
            values:</p><ul><li><i>RegistrationFee</i> - "Registration Fee" Participant Gift Link
            Type</li><li><i>OtherDonation</i> - "Other Donation" Participant Gift Link Type</li></ul>
        applied_amount (float | Unset): The portion of the gift amount being applied to this participant's pledge.
    """

    id: None | str | Unset = UNSET
    gift_id: None | str | Unset = UNSET
    type_: ParticipantPledgeType | Unset = UNSET
    applied_amount: float | Unset = UNSET

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

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        applied_amount = self.applied_amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if applied_amount is not UNSET:
            field_dict["applied_amount"] = applied_amount

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

        _type_ = d.pop("type", UNSET)
        type_: ParticipantPledgeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ParticipantPledgeType(_type_)

        applied_amount = d.pop("applied_amount", UNSET)

        participant_pledge = cls(
            id=id,
            gift_id=gift_id,
            type_=type_,
            applied_amount=applied_amount,
        )

        return participant_pledge

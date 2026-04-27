from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantFeePayment")


@_attrs_define
class ParticipantFeePayment:
    """Defines a data model for a participant fee payment

    Attributes:
        id (None | str | Unset): The ID of the participant fee.
        participant_id (None | str | Unset): The ID of the participant that the participant fee is linked to.
        gift_id (None | str | Unset): The ID of the gift that the participant fee is linked to.
        applied_amount (float | None | Unset): The applied amount of the participant fee payment.
    """

    id: None | str | Unset = UNSET
    participant_id: None | str | Unset = UNSET
    gift_id: None | str | Unset = UNSET
    applied_amount: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        participant_id: None | str | Unset
        if isinstance(self.participant_id, Unset):
            participant_id = UNSET
        else:
            participant_id = self.participant_id

        gift_id: None | str | Unset
        if isinstance(self.gift_id, Unset):
            gift_id = UNSET
        else:
            gift_id = self.gift_id

        applied_amount: float | None | Unset
        if isinstance(self.applied_amount, Unset):
            applied_amount = UNSET
        else:
            applied_amount = self.applied_amount

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if participant_id is not UNSET:
            field_dict["participant_id"] = participant_id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
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

        def _parse_participant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_id = _parse_participant_id(d.pop("participant_id", UNSET))

        def _parse_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_id = _parse_gift_id(d.pop("gift_id", UNSET))

        def _parse_applied_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        applied_amount = _parse_applied_amount(d.pop("applied_amount", UNSET))

        participant_fee_payment = cls(
            id=id,
            participant_id=participant_id,
            gift_id=gift_id,
            applied_amount=applied_amount,
        )

        return participant_fee_payment

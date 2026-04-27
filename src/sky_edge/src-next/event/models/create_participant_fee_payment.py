from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateParticipantFeePayment")


@_attrs_define
class CreateParticipantFeePayment:
    """Participant fee payments are payments toward the participant's fees.

    Attributes:
        gift_id (str): The ID of the gift or pledge that the participant fee is linked to.
        applied_amount (float): The amount of the payment that applies toward the participant fees.
    """

    gift_id: str
    applied_amount: float

    def to_dict(self) -> dict[str, Any]:
        gift_id = self.gift_id

        applied_amount = self.applied_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_id": gift_id,
                "applied_amount": applied_amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_id = d.pop("gift_id")

        applied_amount = d.pop("applied_amount")

        create_participant_fee_payment = cls(
            gift_id=gift_id,
            applied_amount=applied_amount,
        )

        return create_participant_fee_payment

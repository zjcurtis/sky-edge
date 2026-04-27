from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="CreateParticipantFee")


@_attrs_define
class CreateParticipantFee:
    """Participant fees are how much an individual or organization pays to participate in or attend the event.

    Attributes:
        quantity (int): The quantity purchased.
        fee_amount (float): The amount of money associated with the fee.
        contribution_amount (float): The amount of the fee that's a donation above the costs of the event. This is the
            amount that typically appears on receipts.
        event_fee_id (str): The event Fee ID that corresponds to the participant fee.
        date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
            (with no year indicated).
    """

    quantity: int
    fee_amount: float
    contribution_amount: float
    event_fee_id: str
    date: FuzzyDate | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        fee_amount = self.fee_amount

        contribution_amount = self.contribution_amount

        event_fee_id = self.event_fee_id

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "quantity": quantity,
                "fee_amount": fee_amount,
                "contribution_amount": contribution_amount,
                "event_fee_id": event_fee_id,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        quantity = d.pop("quantity")

        fee_amount = d.pop("fee_amount")

        contribution_amount = d.pop("contribution_amount")

        event_fee_id = d.pop("event_fee_id")

        _date = d.pop("date", UNSET)
        date: FuzzyDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FuzzyDate.from_dict(_date)

        create_participant_fee = cls(
            quantity=quantity,
            fee_amount=fee_amount,
            contribution_amount=contribution_amount,
            event_fee_id=event_fee_id,
            date=date,
        )

        return create_participant_fee

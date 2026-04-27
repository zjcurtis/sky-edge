from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ParticipantEntryFee")


@_attrs_define
class ParticipantEntryFee:
    """Summaries of event fees that are associated with participants.

    Attributes:
        event_fee_id (None | str | Unset): The ID of the event fee.
        name (None | str | Unset): The name of the event fee.
        amount (float | Unset): The total amount charged to this participant for this fee.
        quantity (int | Unset): The number this participant purchased of this fee.
    """

    event_fee_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    amount: float | Unset = UNSET
    quantity: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event_fee_id: None | str | Unset
        if isinstance(self.event_fee_id, Unset):
            event_fee_id = UNSET
        else:
            event_fee_id = self.event_fee_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        amount = self.amount

        quantity = self.quantity

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if event_fee_id is not UNSET:
            field_dict["event_fee_id"] = event_fee_id
        if name is not UNSET:
            field_dict["name"] = name
        if amount is not UNSET:
            field_dict["amount"] = amount
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_event_fee_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_fee_id = _parse_event_fee_id(d.pop("event_fee_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        amount = d.pop("amount", UNSET)

        quantity = d.pop("quantity", UNSET)

        participant_entry_fee = cls(
            event_fee_id=event_fee_id,
            name=name,
            amount=amount,
            quantity=quantity,
        )

        return participant_entry_fee

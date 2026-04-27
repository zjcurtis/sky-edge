from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_fee import EventFee
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="ParticipantFee")


@_attrs_define
class ParticipantFee:
    """Defines a data model for a participant fee

    Attributes:
        id (None | str | Unset): The ID of the participant fee.
        participant_id (None | str | Unset): The ID of the record that the participant fee is linked to.
        quantity (int | Unset): The quantity purchased.
        fee_amount (float | Unset): The amount of the participant fee.
        tax_receiptable_amount (float | Unset): The tax receiptable amount of the participant fee.
        date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
            (with no year indicated).
        event_fee (EventFee | Unset): Event fees are how much an organization charges for individuals or organizations
            to participate in or attend the event. An organization might also charge for other add-on items such as parking
            passes or event merchandise.
    """

    id: None | str | Unset = UNSET
    participant_id: None | str | Unset = UNSET
    quantity: int | Unset = UNSET
    fee_amount: float | Unset = UNSET
    tax_receiptable_amount: float | Unset = UNSET
    date: FuzzyDate | Unset = UNSET
    event_fee: EventFee | Unset = UNSET

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

        quantity = self.quantity

        fee_amount = self.fee_amount

        tax_receiptable_amount = self.tax_receiptable_amount

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        event_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_fee, Unset):
            event_fee = self.event_fee.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if participant_id is not UNSET:
            field_dict["participant_id"] = participant_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if fee_amount is not UNSET:
            field_dict["fee_amount"] = fee_amount
        if tax_receiptable_amount is not UNSET:
            field_dict["tax_receiptable_amount"] = tax_receiptable_amount
        if date is not UNSET:
            field_dict["date"] = date
        if event_fee is not UNSET:
            field_dict["event_fee"] = event_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_fee import EventFee
        from ..models.fuzzy_date import FuzzyDate

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

        quantity = d.pop("quantity", UNSET)

        fee_amount = d.pop("fee_amount", UNSET)

        tax_receiptable_amount = d.pop("tax_receiptable_amount", UNSET)

        _date = d.pop("date", UNSET)
        date: FuzzyDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FuzzyDate.from_dict(_date)

        _event_fee = d.pop("event_fee", UNSET)
        event_fee: EventFee | Unset
        if isinstance(_event_fee, Unset):
            event_fee = UNSET
        else:
            event_fee = EventFee.from_dict(_event_fee)

        participant_fee = cls(
            id=id,
            participant_id=participant_id,
            quantity=quantity,
            fee_amount=fee_amount,
            tax_receiptable_amount=tax_receiptable_amount,
            date=date,
            event_fee=event_fee,
        )

        return participant_fee

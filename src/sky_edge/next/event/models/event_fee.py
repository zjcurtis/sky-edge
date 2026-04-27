from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.event_fee_fee_type import EventFeeFeeType

T = TypeVar("T", bound="EventFee")


@_attrs_define
class EventFee:
    """Event fees are how much an organization charges for individuals or organizations to participate in or attend the
    event. An organization might also charge for other add-on items such as parking passes or event merchandise.

        Attributes:
            id (None | str | Unset): The ID of the event fee.
            name (None | str | Unset): The name of the event fee.
            event_id (None | str | Unset): The ID of the event the fee is linked to.
            cost (float | Unset): The fee's cost.
            contribution_amount (float | Unset): The tax deductible amount for this fee.
            number_sold (int | Unset): The number of fees sold.
            pending (int | Unset): The number of fees pending from online registrations.
            registrants_included (int | Unset): If the fee is for registrations, the number of registrants it includes.
            fee_type (EventFeeFeeType | Unset): Whether the fee is for registrations or other add-ons.<p>Available
                values:</p><ul><li><i>Registration</i> - Represents fees for individuals, couples, and
                more.</li><li><i>Other</i> - Represents fees for other charges, such as parking passes or event
                merchandise.</li></ul>
            limit (int | None | Unset): The limit of an event fee.
    """

    id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    event_id: None | str | Unset = UNSET
    cost: float | Unset = UNSET
    contribution_amount: float | Unset = UNSET
    number_sold: int | Unset = UNSET
    pending: int | Unset = UNSET
    registrants_included: int | Unset = UNSET
    fee_type: EventFeeFeeType | Unset = UNSET
    limit: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        event_id: None | str | Unset
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        else:
            event_id = self.event_id

        cost = self.cost

        contribution_amount = self.contribution_amount

        number_sold = self.number_sold

        pending = self.pending

        registrants_included = self.registrants_included

        fee_type: str | Unset = UNSET
        if not isinstance(self.fee_type, Unset):
            fee_type = self.fee_type.value

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if cost is not UNSET:
            field_dict["cost"] = cost
        if contribution_amount is not UNSET:
            field_dict["contribution_amount"] = contribution_amount
        if number_sold is not UNSET:
            field_dict["number_sold"] = number_sold
        if pending is not UNSET:
            field_dict["pending"] = pending
        if registrants_included is not UNSET:
            field_dict["registrants_included"] = registrants_included
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if limit is not UNSET:
            field_dict["limit"] = limit

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_event_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_id = _parse_event_id(d.pop("event_id", UNSET))

        cost = d.pop("cost", UNSET)

        contribution_amount = d.pop("contribution_amount", UNSET)

        number_sold = d.pop("number_sold", UNSET)

        pending = d.pop("pending", UNSET)

        registrants_included = d.pop("registrants_included", UNSET)

        _fee_type = d.pop("fee_type", UNSET)
        fee_type: EventFeeFeeType | Unset
        if isinstance(_fee_type, Unset):
            fee_type = UNSET
        else:
            fee_type = EventFeeFeeType(_fee_type)

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        event_fee = cls(
            id=id,
            name=name,
            event_id=event_id,
            cost=cost,
            contribution_amount=contribution_amount,
            number_sold=number_sold,
            pending=pending,
            registrants_included=registrants_included,
            fee_type=fee_type,
            limit=limit,
        )

        return event_fee

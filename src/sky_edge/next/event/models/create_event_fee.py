from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.create_event_fee_fee_type import CreateEventFeeFeeType

T = TypeVar("T", bound="CreateEventFee")


@_attrs_define
class CreateEventFee:
    """Event fees are how much an organization charges for individuals or organizations to participate in or attend the
    event. An organization might also charge for other add-on items such as t-shirts or valet parking.

        Attributes:
            name (str): The name of the fee.
            cost (float): The amount of money associated with the fee.
            contribution_amount (float): The amount of the fee that's a donation above the costs of the event.
            registrants_included (int | None | Unset): If the fee is for registrations, the number of registrants it
                includes.
            fee_type (CreateEventFeeFeeType | Unset): Whether the fee is for registrations or other add-ons.<p>Available
                values:</p><ul><li><i>Registration</i> - Represents fees for individuals, couples, and
                more.</li><li><i>Other</i> - Represents fees for other charges, such as parking passes or event
                merchandise.</li></ul>
            limit (int | None | Unset): The limit of an event fee. Value must be greater than zero.
    """

    name: str
    cost: float
    contribution_amount: float
    registrants_included: int | None | Unset = UNSET
    fee_type: CreateEventFeeFeeType | Unset = UNSET
    limit: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        cost = self.cost

        contribution_amount = self.contribution_amount

        registrants_included: int | None | Unset
        if isinstance(self.registrants_included, Unset):
            registrants_included = UNSET
        else:
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

        field_dict.update(
            {
                "name": name,
                "cost": cost,
                "contribution_amount": contribution_amount,
            }
        )
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
        name = d.pop("name")

        cost = d.pop("cost")

        contribution_amount = d.pop("contribution_amount")

        def _parse_registrants_included(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        registrants_included = _parse_registrants_included(
            d.pop("registrants_included", UNSET)
        )

        _fee_type = d.pop("fee_type", UNSET)
        fee_type: CreateEventFeeFeeType | Unset
        if isinstance(_fee_type, Unset):
            fee_type = UNSET
        else:
            fee_type = CreateEventFeeFeeType(_fee_type)

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        create_event_fee = cls(
            name=name,
            cost=cost,
            contribution_amount=contribution_amount,
            registrants_included=registrants_included,
            fee_type=fee_type,
            limit=limit,
        )

        return create_event_fee

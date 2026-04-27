from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditEventFee")


@_attrs_define
class EditEventFee:
    """Event fees are how much an organization charges for individuals or organizations to participate in or attend the
    event. An organization might also charge for other add-on items such as t-shirts or valet parking.

        Attributes:
            name (None | str | Unset): The name of the event fee.
            cost (float | Unset): The amount of money associated with the event fee.
            contribution_amount (float | Unset): The amount of the fee that's a donation above the costs of the event.
            registrants_included (int | None | Unset): If the fee is for registrations, the number of registrants it
                includes.
            limit (int | None | Unset): The limit of an event fee. Value must be greater than zero.
    """

    name: None | str | Unset = UNSET
    cost: float | Unset = UNSET
    contribution_amount: float | Unset = UNSET
    registrants_included: int | None | Unset = UNSET
    limit: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        cost = self.cost

        contribution_amount = self.contribution_amount

        registrants_included: int | None | Unset
        if isinstance(self.registrants_included, Unset):
            registrants_included = UNSET
        else:
            registrants_included = self.registrants_included

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if cost is not UNSET:
            field_dict["cost"] = cost
        if contribution_amount is not UNSET:
            field_dict["contribution_amount"] = contribution_amount
        if registrants_included is not UNSET:
            field_dict["registrants_included"] = registrants_included
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        cost = d.pop("cost", UNSET)

        contribution_amount = d.pop("contribution_amount", UNSET)

        def _parse_registrants_included(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        registrants_included = _parse_registrants_included(d.pop("registrants_included", UNSET))

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        edit_event_fee = cls(
            name=name,
            cost=cost,
            contribution_amount=contribution_amount,
            registrants_included=registrants_included,
            limit=limit,
        )

        return edit_event_fee

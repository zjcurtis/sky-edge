from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="FundraiserAssignmentRead")


@_attrs_define
class FundraiserAssignmentRead:
    """Fundraiser constituents interact with other constituents on behalf of your organization to cultivate relationships
    and request donations. Fundraiser assignments allow you to assign specific constituents to fundraisers for
    solicitation purposes.

        Attributes:
            id (str | Unset): The immutable system record ID of the given assignment.
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            appeal_id (str | Unset): The immutable system record ID of the appeal the fundraiser should use to request
                gifts.
            campaign_id (str | Unset): The immutable system record ID of the campaign to apply resulting gifts to.
            constituent_id (str | Unset): The immutable system record ID of the target constituent.
            end (datetime.datetime | Unset): The fundraiser end date. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>2017-05-17T00:00:00</i>.
            fund_id (str | Unset): The immutable system record ID of the fund any resulting gifts should be applied to. If a
                restricted fund is selected, only campaigns and appeals associated with that fund may be selected.
            fundraiser_id (str | Unset): The immutable system record ID of the fundraiser assigned to the constituent.
            start (datetime.datetime | Unset): The fundraiser start date. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>2017-01-29T00:00:00</i>.
            type_ (str | Unset): The type of fundraiser. Available values are the entries in the <a href="https://developer.
                sky.blackbaud.com/docs/services/58bdd6c8d7dcde06046081d7/operations/ListFundraiserTypes"><b>Solicitor
                Type</b></a> table.
    """

    id: str | Unset = UNSET
    amount: Currency | Unset = UNSET
    appeal_id: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    end: datetime.datetime | Unset = UNSET
    fund_id: str | Unset = UNSET
    fundraiser_id: str | Unset = UNSET
    start: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        appeal_id = self.appeal_id

        campaign_id = self.campaign_id

        constituent_id = self.constituent_id

        end: str | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.isoformat()

        fund_id = self.fund_id

        fundraiser_id = self.fundraiser_id

        start: str | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.isoformat()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if end is not UNSET:
            field_dict["end"] = end
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if fundraiser_id is not UNSET:
            field_dict["fundraiser_id"] = fundraiser_id
        if start is not UNSET:
            field_dict["start"] = start
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        appeal_id = d.pop("appeal_id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _end = d.pop("end", UNSET)
        end: datetime.datetime | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = isoparse(_end)

        fund_id = d.pop("fund_id", UNSET)

        fundraiser_id = d.pop("fundraiser_id", UNSET)

        _start = d.pop("start", UNSET)
        start: datetime.datetime | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = isoparse(_start)

        type_ = d.pop("type", UNSET)

        fundraiser_assignment_read = cls(
            id=id,
            amount=amount,
            appeal_id=appeal_id,
            campaign_id=campaign_id,
            constituent_id=constituent_id,
            end=end,
            fund_id=fund_id,
            fundraiser_id=fundraiser_id,
            start=start,
            type_=type_,
        )

        fundraiser_assignment_read.additional_properties = d
        return fundraiser_assignment_read

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

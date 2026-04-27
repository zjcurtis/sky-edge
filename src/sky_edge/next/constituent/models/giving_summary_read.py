from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appeal_read import AppealRead
    from ..models.campaign_read import CampaignRead
    from ..models.currency import Currency
    from ..models.fund_read import FundRead


T = TypeVar("T", bound="GivingSummaryRead")


@_attrs_define
class GivingSummaryRead:
    """Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot of information associated
    with them to ensure that they are properly allocated and acknowledged.

        Attributes:
            id (str | Unset): The immutable system record ID of the gift.
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            appeals (list[AppealRead] | Unset): The set of immutable appeal system record IDs associated with the gift.
            campaigns (list[CampaignRead] | Unset): The set of immutable campaign system record IDs associated with the
                gift.
            date (datetime.datetime | Unset): The gift date. Uses <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
                format: </a><i>1969-11-21T10:29:43</i>.
            funds (list[FundRead] | Unset): The set of immutable fund system record IDs associated with the gift.
            type_ (str | Unset): The gift type.
    """

    id: str | Unset = UNSET
    amount: Currency | Unset = UNSET
    appeals: list[AppealRead] | Unset = UNSET
    campaigns: list[CampaignRead] | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    funds: list[FundRead] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        appeals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.appeals, Unset):
            appeals = []
            for appeals_item_data in self.appeals:
                appeals_item = appeals_item_data.to_dict()
                appeals.append(appeals_item)

        campaigns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaigns, Unset):
            campaigns = []
            for campaigns_item_data in self.campaigns:
                campaigns_item = campaigns_item_data.to_dict()
                campaigns.append(campaigns_item)

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        funds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.funds, Unset):
            funds = []
            for funds_item_data in self.funds:
                funds_item = funds_item_data.to_dict()
                funds.append(funds_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if appeals is not UNSET:
            field_dict["appeals"] = appeals
        if campaigns is not UNSET:
            field_dict["campaigns"] = campaigns
        if date is not UNSET:
            field_dict["date"] = date
        if funds is not UNSET:
            field_dict["funds"] = funds
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appeal_read import AppealRead
        from ..models.campaign_read import CampaignRead
        from ..models.currency import Currency
        from ..models.fund_read import FundRead

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        _appeals = d.pop("appeals", UNSET)
        appeals: list[AppealRead] | Unset = UNSET
        if _appeals is not UNSET:
            appeals = []
            for appeals_item_data in _appeals:
                appeals_item = AppealRead.from_dict(appeals_item_data)

                appeals.append(appeals_item)

        _campaigns = d.pop("campaigns", UNSET)
        campaigns: list[CampaignRead] | Unset = UNSET
        if _campaigns is not UNSET:
            campaigns = []
            for campaigns_item_data in _campaigns:
                campaigns_item = CampaignRead.from_dict(campaigns_item_data)

                campaigns.append(campaigns_item)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _funds = d.pop("funds", UNSET)
        funds: list[FundRead] | Unset = UNSET
        if _funds is not UNSET:
            funds = []
            for funds_item_data in _funds:
                funds_item = FundRead.from_dict(funds_item_data)

                funds.append(funds_item)

        type_ = d.pop("type", UNSET)

        giving_summary_read = cls(
            id=id,
            amount=amount,
            appeals=appeals,
            campaigns=campaigns,
            date=date,
            funds=funds,
            type_=type_,
        )

        giving_summary_read.additional_properties = d
        return giving_summary_read

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

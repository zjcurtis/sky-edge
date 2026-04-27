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
    from ..models.fundraiser import Fundraiser


T = TypeVar("T", bound="OpportunityEdit")


@_attrs_define
class OpportunityEdit:
    """Opportunities help you plan and track efforts to build relationships with prospects and secure major gifts. They can
    manage information about fundraising activities and the effectiveness of your efforts.

        Attributes:
            ask_amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures
                that all monetary amounts are consistent, regardless of where they are entered or viewed.
            ask_date (datetime.datetime | Unset): The date when the solicitation was made. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>2015-09-18T16:25:00</i>.
            campaign_id (str | Unset): The immutable system record ID of the campaign associated with the opportunity. The
                campaign sets the overall objectives for raising money.
            deadline (datetime.datetime | Unset): The goal date for the opportunity to result in a gift. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>2015-09-18T16:25:00</i>.
            expected_amount (Currency | Unset): For consistency, currency is configured at the organization level. This
                ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            expected_date (datetime.datetime | Unset): The date when the prospect is expected to give in response to the
                opportunity. Uses <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>2015-09-18T16:25:00</i>.
            fund_id (str | Unset): The immutable system record ID of the fund associated with the opportunity. The fund
                designates the specific financial purpose of a gift and identifies the financial account for that gift.
            funded_amount (Currency | Unset): For consistency, currency is configured at the organization level. This
                ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            funded_date (datetime.datetime | Unset): The date when the prospect gave in response to the opportunity. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>2015-09-18T16:25:00</i>.
            fundraisers (list[Fundraiser] | Unset): The set of immutable constituent system record IDs for the fundraisers
                assigned to the opportunity.
            inactive (bool | Unset): Indicates whether the opportunity is inactive.
            name (str | Unset): The name that identifies the opportunity throughout the program, such as in lists or on
                constituent records. Character limit: 255. This property cannot be set to null.
            purpose (str | Unset): The intended use for any money raised as a result of the opportunity. Available values
                are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/58e3b2597c1af25c58b9c4e3/opera
                tions/ListOpportunityPurposes"><b>Purposes</b></a> table. This property cannot be set to null.
            status (str | Unset): The status that indicates where the opportunity is in the solicitation process. Available
                values are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/58e3b2597c1af25c58b9c4e
                3/operations/ListOpportunityStatuses"><b>Proposal Status</b></a> table.
            likelihood (str | Unset): Indicates your level of confidence in receiving gifts from the opportunity. Available
                values are the entries in the <a
                href="https://developer.sky.blackbaud.com/api#api=codetable&amp;operation=GetTableEntriesList">code table</a>
                with ID 5094.
            gift_type (str | Unset): Specifies the type of gifts you expect from the opportunity, such as pledges or gifts
                in kind. Available values are the entries in the <a
                href="https://developer.sky.blackbaud.com/api#api=codetable&amp;operation=GetTableEntriesList">code table</a>
                with ID 19.
    """

    ask_amount: Currency | Unset = UNSET
    ask_date: datetime.datetime | Unset = UNSET
    campaign_id: str | Unset = UNSET
    deadline: datetime.datetime | Unset = UNSET
    expected_amount: Currency | Unset = UNSET
    expected_date: datetime.datetime | Unset = UNSET
    fund_id: str | Unset = UNSET
    funded_amount: Currency | Unset = UNSET
    funded_date: datetime.datetime | Unset = UNSET
    fundraisers: list[Fundraiser] | Unset = UNSET
    inactive: bool | Unset = UNSET
    name: str | Unset = UNSET
    purpose: str | Unset = UNSET
    status: str | Unset = UNSET
    likelihood: str | Unset = UNSET
    gift_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ask_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ask_amount, Unset):
            ask_amount = self.ask_amount.to_dict()

        ask_date: str | Unset = UNSET
        if not isinstance(self.ask_date, Unset):
            ask_date = self.ask_date.isoformat()

        campaign_id = self.campaign_id

        deadline: str | Unset = UNSET
        if not isinstance(self.deadline, Unset):
            deadline = self.deadline.isoformat()

        expected_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expected_amount, Unset):
            expected_amount = self.expected_amount.to_dict()

        expected_date: str | Unset = UNSET
        if not isinstance(self.expected_date, Unset):
            expected_date = self.expected_date.isoformat()

        fund_id = self.fund_id

        funded_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funded_amount, Unset):
            funded_amount = self.funded_amount.to_dict()

        funded_date: str | Unset = UNSET
        if not isinstance(self.funded_date, Unset):
            funded_date = self.funded_date.isoformat()

        fundraisers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fundraisers, Unset):
            fundraisers = []
            for fundraisers_item_data in self.fundraisers:
                fundraisers_item = fundraisers_item_data.to_dict()
                fundraisers.append(fundraisers_item)

        inactive = self.inactive

        name = self.name

        purpose = self.purpose

        status = self.status

        likelihood = self.likelihood

        gift_type = self.gift_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ask_amount is not UNSET:
            field_dict["ask_amount"] = ask_amount
        if ask_date is not UNSET:
            field_dict["ask_date"] = ask_date
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if expected_amount is not UNSET:
            field_dict["expected_amount"] = expected_amount
        if expected_date is not UNSET:
            field_dict["expected_date"] = expected_date
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if funded_amount is not UNSET:
            field_dict["funded_amount"] = funded_amount
        if funded_date is not UNSET:
            field_dict["funded_date"] = funded_date
        if fundraisers is not UNSET:
            field_dict["fundraisers"] = fundraisers
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if name is not UNSET:
            field_dict["name"] = name
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if status is not UNSET:
            field_dict["status"] = status
        if likelihood is not UNSET:
            field_dict["likelihood"] = likelihood
        if gift_type is not UNSET:
            field_dict["gift_type"] = gift_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.fundraiser import Fundraiser

        d = dict(src_dict)
        _ask_amount = d.pop("ask_amount", UNSET)
        ask_amount: Currency | Unset
        if isinstance(_ask_amount, Unset):
            ask_amount = UNSET
        else:
            ask_amount = Currency.from_dict(_ask_amount)

        _ask_date = d.pop("ask_date", UNSET)
        ask_date: datetime.datetime | Unset
        if isinstance(_ask_date, Unset):
            ask_date = UNSET
        else:
            ask_date = isoparse(_ask_date)

        campaign_id = d.pop("campaign_id", UNSET)

        _deadline = d.pop("deadline", UNSET)
        deadline: datetime.datetime | Unset
        if isinstance(_deadline, Unset):
            deadline = UNSET
        else:
            deadline = isoparse(_deadline)

        _expected_amount = d.pop("expected_amount", UNSET)
        expected_amount: Currency | Unset
        if isinstance(_expected_amount, Unset):
            expected_amount = UNSET
        else:
            expected_amount = Currency.from_dict(_expected_amount)

        _expected_date = d.pop("expected_date", UNSET)
        expected_date: datetime.datetime | Unset
        if isinstance(_expected_date, Unset):
            expected_date = UNSET
        else:
            expected_date = isoparse(_expected_date)

        fund_id = d.pop("fund_id", UNSET)

        _funded_amount = d.pop("funded_amount", UNSET)
        funded_amount: Currency | Unset
        if isinstance(_funded_amount, Unset):
            funded_amount = UNSET
        else:
            funded_amount = Currency.from_dict(_funded_amount)

        _funded_date = d.pop("funded_date", UNSET)
        funded_date: datetime.datetime | Unset
        if isinstance(_funded_date, Unset):
            funded_date = UNSET
        else:
            funded_date = isoparse(_funded_date)

        _fundraisers = d.pop("fundraisers", UNSET)
        fundraisers: list[Fundraiser] | Unset = UNSET
        if _fundraisers is not UNSET:
            fundraisers = []
            for fundraisers_item_data in _fundraisers:
                fundraisers_item = Fundraiser.from_dict(fundraisers_item_data)

                fundraisers.append(fundraisers_item)

        inactive = d.pop("inactive", UNSET)

        name = d.pop("name", UNSET)

        purpose = d.pop("purpose", UNSET)

        status = d.pop("status", UNSET)

        likelihood = d.pop("likelihood", UNSET)

        gift_type = d.pop("gift_type", UNSET)

        opportunity_edit = cls(
            ask_amount=ask_amount,
            ask_date=ask_date,
            campaign_id=campaign_id,
            deadline=deadline,
            expected_amount=expected_amount,
            expected_date=expected_date,
            fund_id=fund_id,
            funded_amount=funded_amount,
            funded_date=funded_date,
            fundraisers=fundraisers,
            inactive=inactive,
            name=name,
            purpose=purpose,
            status=status,
            likelihood=likelihood,
            gift_type=gift_type,
        )

        opportunity_edit.additional_properties = d
        return opportunity_edit

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

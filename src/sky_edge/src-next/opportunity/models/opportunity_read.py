from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.fundraiser import Fundraiser


T = TypeVar("T", bound="OpportunityRead")


@_attrs_define
class OpportunityRead:
    """Opportunities help you plan and track efforts to build relationships with prospects and secure major gifts. They can
    manage information about fundraising activities and the effectiveness of your efforts.

        Attributes:
            id (str | Unset): The immutable system record ID of the opportunity.
            ask_amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures
                that all monetary amounts are consistent, regardless of where they are entered or viewed.
            ask_date (datetime.datetime | Unset): The date when the solicitation was made. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>2015-09-18T16:25:00</i>.
            campaign_id (str | Unset): The immutable system record ID of the campaign associated with the opportunity. The
                campaign sets the overall objectives for raising money.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the opportunity.
            date_added (datetime.datetime | Unset): The date when the opportunity was created. Includes an offset from UTC
                in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the opportunity was last modified. Includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
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
            linked_gifts (list[str] | Unset): The  immutable system record IDs of the gifts related to the opportunity.
            name (str | Unset): The name that identifies the opportunity throughout the program, such as in lists or on
                constituent records.
            purpose (str | Unset): The intended use for any money raised as a result of the opportunity. Available values
                are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/58e3b2597c1af25c58b9c4e3/opera
                tions/ListOpportunityPurposes"><b>Purposes</b></a> table.
            status (str | Unset): The status that indicates where the opportunity is in the solicitation process. This
                property can experience a data latency of about 10 minutes on the <a href="https://developer.sky.blackbaud.com/d
                ocs/services/58e3b2597c1af25c58b9c4e3/operations/58e3b27ba9db950fa048c8a9">Opportunity (Get) endpoint</a>.
                Available values are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/58e3b2597c1af
                25c58b9c4e3/operations/ListOpportunityStatuses"><b>Proposal Status</b></a> table.
            opportunity_likelihood_name (str | Unset): Indicates your level of confidence in receiving gifts from the
                opportunity.
            opportunity_likelihood_id (str | Unset): The opportunity likelihood identifier.
            gift_type (str | Unset): Specifies the type of gifts you expect from the opportunity, such as pledges or gifts
                in kind.
            gift_type_id (str | Unset): The gift type identifier.
    """

    id: str | Unset = UNSET
    ask_amount: Currency | Unset = UNSET
    ask_date: datetime.datetime | Unset = UNSET
    campaign_id: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    deadline: datetime.datetime | Unset = UNSET
    expected_amount: Currency | Unset = UNSET
    expected_date: datetime.datetime | Unset = UNSET
    fund_id: str | Unset = UNSET
    funded_amount: Currency | Unset = UNSET
    funded_date: datetime.datetime | Unset = UNSET
    fundraisers: list[Fundraiser] | Unset = UNSET
    inactive: bool | Unset = UNSET
    linked_gifts: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    purpose: str | Unset = UNSET
    status: str | Unset = UNSET
    opportunity_likelihood_name: str | Unset = UNSET
    opportunity_likelihood_id: str | Unset = UNSET
    gift_type: str | Unset = UNSET
    gift_type_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ask_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ask_amount, Unset):
            ask_amount = self.ask_amount.to_dict()

        ask_date: str | Unset = UNSET
        if not isinstance(self.ask_date, Unset):
            ask_date = self.ask_date.isoformat()

        campaign_id = self.campaign_id

        constituent_id = self.constituent_id

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

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

        linked_gifts: list[str] | Unset = UNSET
        if not isinstance(self.linked_gifts, Unset):
            linked_gifts = self.linked_gifts

        name = self.name

        purpose = self.purpose

        status = self.status

        opportunity_likelihood_name = self.opportunity_likelihood_name

        opportunity_likelihood_id = self.opportunity_likelihood_id

        gift_type = self.gift_type

        gift_type_id = self.gift_type_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ask_amount is not UNSET:
            field_dict["ask_amount"] = ask_amount
        if ask_date is not UNSET:
            field_dict["ask_date"] = ask_date
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
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
        if linked_gifts is not UNSET:
            field_dict["linked_gifts"] = linked_gifts
        if name is not UNSET:
            field_dict["name"] = name
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if status is not UNSET:
            field_dict["status"] = status
        if opportunity_likelihood_name is not UNSET:
            field_dict["opportunity_likelihood_name"] = opportunity_likelihood_name
        if opportunity_likelihood_id is not UNSET:
            field_dict["opportunity_likelihood_id"] = opportunity_likelihood_id
        if gift_type is not UNSET:
            field_dict["gift_type"] = gift_type
        if gift_type_id is not UNSET:
            field_dict["gift_type_id"] = gift_type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.fundraiser import Fundraiser

        d = dict(src_dict)
        id = d.pop("id", UNSET)

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

        constituent_id = d.pop("constituent_id", UNSET)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

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

        linked_gifts = cast(list[str], d.pop("linked_gifts", UNSET))

        name = d.pop("name", UNSET)

        purpose = d.pop("purpose", UNSET)

        status = d.pop("status", UNSET)

        opportunity_likelihood_name = d.pop("opportunity_likelihood_name", UNSET)

        opportunity_likelihood_id = d.pop("opportunity_likelihood_id", UNSET)

        gift_type = d.pop("gift_type", UNSET)

        gift_type_id = d.pop("gift_type_id", UNSET)

        opportunity_read = cls(
            id=id,
            ask_amount=ask_amount,
            ask_date=ask_date,
            campaign_id=campaign_id,
            constituent_id=constituent_id,
            date_added=date_added,
            date_modified=date_modified,
            deadline=deadline,
            expected_amount=expected_amount,
            expected_date=expected_date,
            fund_id=fund_id,
            funded_amount=funded_amount,
            funded_date=funded_date,
            fundraisers=fundraisers,
            inactive=inactive,
            linked_gifts=linked_gifts,
            name=name,
            purpose=purpose,
            status=status,
            opportunity_likelihood_name=opportunity_likelihood_name,
            opportunity_likelihood_id=opportunity_likelihood_id,
            gift_type=gift_type,
            gift_type_id=gift_type_id,
        )

        opportunity_read.additional_properties = d
        return opportunity_read

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

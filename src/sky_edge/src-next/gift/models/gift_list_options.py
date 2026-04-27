from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftListOptions")


@_attrs_define
class GiftListOptions:
    """Defines options and filter criteria when getting a list of gifts.

    Attributes:
        date_added (datetime.datetime | Unset): Represents a filter for gifts created on or after the specified date.
            The filter respects time offsets from UTC per the ISO-8601 format: 2016-05-05T17:59:31.1600745-04:00.
        last_modified (datetime.datetime | Unset): Represents a filter for gifts modified on or after the specified
            date. The filter respects time offsets from UTC per the ISO-8601 format: 2016-05-05T17:59:31.1600745-04:00.
        sort_token (str | Unset): Represents a token filter to provide the next stable-sorted list of gifts. This will
            be provided on the next_link collection response property when last_modified or sort_token filters are specified
            on the request.
        constituent_id (list[str] | Unset): Represents a list of constituent identifiers. Returns gifts if any of the
            specified constituent identifiers match any of their constituents. For example,
            "constituent_id=280&amp;constituent_id=1232" returns gifts with either "280" or "1232" constituent identifiers.
        post_status (list[str] | Unset): Represents a list of gift post statuses. Returns gifts if their post status
            matches any specified. For example, "post_status=DoNotPost&amp;post_status=Posted" returns gifts that are marked
            either DoNotPost or Posted.
        gift_type (list[str] | Unset): Represents a list of gift types. Returns gifts if their type matches any
            specified. For example, "gift_type=MatchingGiftPledge&amp;gift_type=RecurringGift" returns gifts of type
            MatchingGiftPledge or RecurringGift.
            Available values are <i>Donation</i>, <i>GiftInKind</i>, <i>MatchingGiftPledge</i>, <i>MatchingGiftPayment</i>,
            <i>PlannedGift</i>, <i>Pledge</i>, <i>PledgePayment</i>, <i>RecurringGift</i>, <i>RecurringGiftPayment</i>,
            <i>Stock</i>, <i>SoldStock</i>, and <i>Other</i>.
        receipt_status (list[str] | Unset): Represents a list of gift receipt statuses. Returns gifts if their receipt
            status matches any specified. For example, "receipt_status=DoNotReceipt&amp;receipt_status=Receipted" returns
            gifts that are marked either DoNotReceipt or Receipted.
        acknowledgement_status (list[str] | Unset): Represents a list of gift acknowledgement statuses. Returns gifts if
            their acknowledgement status matches any specified. For example,
            "acknowledgement_status=DoNotAcknowledge&amp;acknowledgement_status=Acknowledged" returns gifts that are marked
            either DoNotAcknowledge or Acknowledged.
        campaign_id (list[str] | Unset): Represents a list of campaign identifiers. Returns gifts if any of the
            specified campaign identifiers match any of their campaigns. For example, "campaign_id=280&amp;campaign_id=1232"
            returns gifts with either "280" or "1232" campaign identifiers.
        fund_id (list[str] | Unset): Represents a list of fund identifiers. Returns gifts if any of the specified fund
            identifiers match any of their funds. For example, "fund_id=280&amp;fund_id=1232" returns gifts with either
            "280" or "1232" fund identifiers.
        appeal_id (list[str] | Unset): Represents a list of appeal identifiers. Returns gifts if any of the specified
            appeal identifiers match any of their appeals. For example, "appeal_id=280&amp;appeal_id=1232" returns gifts
            with either "280" or "1232" appeal identifiers.
        start_gift_date (datetime.datetime | Unset): Represents a filter for gifts with a gift date on or after the
            specified date. If used with end_gift_date, returns gifts with gift dates between both values.
        end_gift_date (datetime.datetime | Unset): Represents a filter for gifts with a gift date on or before the
            specified date. If used with start_gift_date, returns gifts with gift dates between both values.
        start_gift_amount (float | Unset): Represents a filter for gifts with an amount greater than or equal to the
            specified amount. If used with end_gift_amount, returns gifts with amounts between both values.
        end_gift_amount (float | Unset): Represents a filter for gifts with an amount less than or equal to the
            specified amount. If used with start_gift_amount, returns gifts with amounts between both values.
        list_id (str | Unset): Defines a list identifier used to filter the set of gifts to those included in the
            specified list. If this value is set, other specified filters will be ignored.
        sort (list[str] | Unset): Represents a list of fields to sort the results by. Returns a list that sorts gifts
            based on the supplied fields. Results are in ascending order by default, and a '-' sign denotes descending
            order. For example, "sort=date_added,-date" sorts gifts by the "date_added" field in ascending order and then by
            the "gift date" field in descending order.
            If only the date_modified field or only the date_added field is provided, then this adds the sort_token
            parameter to the next_link URL to ensure that gifts are stably sorted.
        limit (int | Unset): Represents the number of records to return. The default is 500. The maximum is 5000.
        offset (int | Unset): Represents the number of records to skip. For use with pagination.
    """

    date_added: datetime.datetime | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    sort_token: str | Unset = UNSET
    constituent_id: list[str] | Unset = UNSET
    post_status: list[str] | Unset = UNSET
    gift_type: list[str] | Unset = UNSET
    receipt_status: list[str] | Unset = UNSET
    acknowledgement_status: list[str] | Unset = UNSET
    campaign_id: list[str] | Unset = UNSET
    fund_id: list[str] | Unset = UNSET
    appeal_id: list[str] | Unset = UNSET
    start_gift_date: datetime.datetime | Unset = UNSET
    end_gift_date: datetime.datetime | Unset = UNSET
    start_gift_amount: float | Unset = UNSET
    end_gift_amount: float | Unset = UNSET
    list_id: str | Unset = UNSET
    sort: list[str] | Unset = UNSET
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        sort_token = self.sort_token

        constituent_id: list[str] | Unset = UNSET
        if not isinstance(self.constituent_id, Unset):
            constituent_id = self.constituent_id

        post_status: list[str] | Unset = UNSET
        if not isinstance(self.post_status, Unset):
            post_status = self.post_status

        gift_type: list[str] | Unset = UNSET
        if not isinstance(self.gift_type, Unset):
            gift_type = self.gift_type

        receipt_status: list[str] | Unset = UNSET
        if not isinstance(self.receipt_status, Unset):
            receipt_status = self.receipt_status

        acknowledgement_status: list[str] | Unset = UNSET
        if not isinstance(self.acknowledgement_status, Unset):
            acknowledgement_status = self.acknowledgement_status

        campaign_id: list[str] | Unset = UNSET
        if not isinstance(self.campaign_id, Unset):
            campaign_id = self.campaign_id

        fund_id: list[str] | Unset = UNSET
        if not isinstance(self.fund_id, Unset):
            fund_id = self.fund_id

        appeal_id: list[str] | Unset = UNSET
        if not isinstance(self.appeal_id, Unset):
            appeal_id = self.appeal_id

        start_gift_date: str | Unset = UNSET
        if not isinstance(self.start_gift_date, Unset):
            start_gift_date = self.start_gift_date.isoformat()

        end_gift_date: str | Unset = UNSET
        if not isinstance(self.end_gift_date, Unset):
            end_gift_date = self.end_gift_date.isoformat()

        start_gift_amount = self.start_gift_amount

        end_gift_amount = self.end_gift_amount

        list_id = self.list_id

        sort: list[str] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if last_modified is not UNSET:
            field_dict["last_modified"] = last_modified
        if sort_token is not UNSET:
            field_dict["sort_token"] = sort_token
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if post_status is not UNSET:
            field_dict["post_status"] = post_status
        if gift_type is not UNSET:
            field_dict["gift_type"] = gift_type
        if receipt_status is not UNSET:
            field_dict["receipt_status"] = receipt_status
        if acknowledgement_status is not UNSET:
            field_dict["acknowledgement_status"] = acknowledgement_status
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if start_gift_date is not UNSET:
            field_dict["start_gift_date"] = start_gift_date
        if end_gift_date is not UNSET:
            field_dict["end_gift_date"] = end_gift_date
        if start_gift_amount is not UNSET:
            field_dict["start_gift_amount"] = start_gift_amount
        if end_gift_amount is not UNSET:
            field_dict["end_gift_amount"] = end_gift_amount
        if list_id is not UNSET:
            field_dict["list_id"] = list_id
        if sort is not UNSET:
            field_dict["sort"] = sort
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _last_modified = d.pop("last_modified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        sort_token = d.pop("sort_token", UNSET)

        constituent_id = cast(list[str], d.pop("constituent_id", UNSET))

        post_status = cast(list[str], d.pop("post_status", UNSET))

        gift_type = cast(list[str], d.pop("gift_type", UNSET))

        receipt_status = cast(list[str], d.pop("receipt_status", UNSET))

        acknowledgement_status = cast(list[str], d.pop("acknowledgement_status", UNSET))

        campaign_id = cast(list[str], d.pop("campaign_id", UNSET))

        fund_id = cast(list[str], d.pop("fund_id", UNSET))

        appeal_id = cast(list[str], d.pop("appeal_id", UNSET))

        _start_gift_date = d.pop("start_gift_date", UNSET)
        start_gift_date: datetime.datetime | Unset
        if isinstance(_start_gift_date, Unset):
            start_gift_date = UNSET
        else:
            start_gift_date = isoparse(_start_gift_date)

        _end_gift_date = d.pop("end_gift_date", UNSET)
        end_gift_date: datetime.datetime | Unset
        if isinstance(_end_gift_date, Unset):
            end_gift_date = UNSET
        else:
            end_gift_date = isoparse(_end_gift_date)

        start_gift_amount = d.pop("start_gift_amount", UNSET)

        end_gift_amount = d.pop("end_gift_amount", UNSET)

        list_id = d.pop("list_id", UNSET)

        sort = cast(list[str], d.pop("sort", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        gift_list_options = cls(
            date_added=date_added,
            last_modified=last_modified,
            sort_token=sort_token,
            constituent_id=constituent_id,
            post_status=post_status,
            gift_type=gift_type,
            receipt_status=receipt_status,
            acknowledgement_status=acknowledgement_status,
            campaign_id=campaign_id,
            fund_id=fund_id,
            appeal_id=appeal_id,
            start_gift_date=start_gift_date,
            end_gift_date=end_gift_date,
            start_gift_amount=start_gift_amount,
            end_gift_amount=end_gift_amount,
            list_id=list_id,
            sort=sort,
            limit=limit,
            offset=offset,
        )

        gift_list_options.additional_properties = d
        return gift_list_options

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

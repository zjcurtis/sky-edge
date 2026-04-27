from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Appeal")


@_attrs_define
class Appeal:
    """Additional information about an appeal record.

    Attributes:
        appeal_id (str): The string identifier for the appeal.
        description (str): The appeal description that appears as the full name at the top of its record.
        appeal_category (None | str | Unset): The category associated with the appeal.
        campaign (None | str | Unset): The default campaign associated with the appeal.
        id (int | Unset): The immutable system record ID of the appeal.
        campaign_id (int | None | Unset): The ID for the default campaign associated with the appeal.
        appeal_category_id (int | None | Unset): The unique identifier for an appeal category associated with the
            appeal.
        goal (float | Unset): The target amount to raise through the appeal.
        start_date (datetime.date | None | Unset): The start date for the appeal.
        end_date (datetime.date | None | Unset): The end date for the appeal.
        inactive (bool | Unset): The active status of the appeal; an appeal is active if the current date is after the
            start date and before the end date.
        default_fund_id (int | None | Unset): The ID for the default fund associated with the appeal.
        notes (None | str | Unset): The notes associated with the appeal.
        number_solicited (int | None | Unset): The number of constituents solicited in the appeal.
        default_gift_amount (float | Unset): The monetary amount of the default gift. This property defaults to 0.00 if
            no amount is specified.
    """

    appeal_id: str
    description: str
    appeal_category: None | str | Unset = UNSET
    campaign: None | str | Unset = UNSET
    id: int | Unset = UNSET
    campaign_id: int | None | Unset = UNSET
    appeal_category_id: int | None | Unset = UNSET
    goal: float | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    inactive: bool | Unset = UNSET
    default_fund_id: int | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    number_solicited: int | None | Unset = UNSET
    default_gift_amount: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        appeal_id = self.appeal_id

        description = self.description

        appeal_category: None | str | Unset
        if isinstance(self.appeal_category, Unset):
            appeal_category = UNSET
        else:
            appeal_category = self.appeal_category

        campaign: None | str | Unset
        if isinstance(self.campaign, Unset):
            campaign = UNSET
        else:
            campaign = self.campaign

        id = self.id

        campaign_id: int | None | Unset
        if isinstance(self.campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = self.campaign_id

        appeal_category_id: int | None | Unset
        if isinstance(self.appeal_category_id, Unset):
            appeal_category_id = UNSET
        else:
            appeal_category_id = self.appeal_category_id

        goal = self.goal

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        inactive = self.inactive

        default_fund_id: int | None | Unset
        if isinstance(self.default_fund_id, Unset):
            default_fund_id = UNSET
        else:
            default_fund_id = self.default_fund_id

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        number_solicited: int | None | Unset
        if isinstance(self.number_solicited, Unset):
            number_solicited = UNSET
        else:
            number_solicited = self.number_solicited

        default_gift_amount = self.default_gift_amount

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "appeal_id": appeal_id,
                "description": description,
            }
        )
        if appeal_category is not UNSET:
            field_dict["appeal_category"] = appeal_category
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if id is not UNSET:
            field_dict["id"] = id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if appeal_category_id is not UNSET:
            field_dict["appeal_category_id"] = appeal_category_id
        if goal is not UNSET:
            field_dict["goal"] = goal
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if default_fund_id is not UNSET:
            field_dict["default_fund_id"] = default_fund_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if number_solicited is not UNSET:
            field_dict["number_solicited"] = number_solicited
        if default_gift_amount is not UNSET:
            field_dict["default_gift_amount"] = default_gift_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appeal_id = d.pop("appeal_id")

        description = d.pop("description")

        def _parse_appeal_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appeal_category = _parse_appeal_category(d.pop("appeal_category", UNSET))

        def _parse_campaign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign = _parse_campaign(d.pop("campaign", UNSET))

        id = d.pop("id", UNSET)

        def _parse_campaign_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        campaign_id = _parse_campaign_id(d.pop("campaign_id", UNSET))

        def _parse_appeal_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        appeal_category_id = _parse_appeal_category_id(d.pop("appeal_category_id", UNSET))

        goal = d.pop("goal", UNSET)

        def _parse_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data).date()

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        inactive = d.pop("inactive", UNSET)

        def _parse_default_fund_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_fund_id = _parse_default_fund_id(d.pop("default_fund_id", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_number_solicited(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_solicited = _parse_number_solicited(d.pop("number_solicited", UNSET))

        default_gift_amount = d.pop("default_gift_amount", UNSET)

        appeal = cls(
            appeal_id=appeal_id,
            description=description,
            appeal_category=appeal_category,
            campaign=campaign,
            id=id,
            campaign_id=campaign_id,
            appeal_category_id=appeal_category_id,
            goal=goal,
            start_date=start_date,
            end_date=end_date,
            inactive=inactive,
            default_fund_id=default_fund_id,
            notes=notes,
            number_solicited=number_solicited,
            default_gift_amount=default_gift_amount,
        )

        return appeal

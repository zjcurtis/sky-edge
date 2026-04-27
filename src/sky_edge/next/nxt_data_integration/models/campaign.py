from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="Campaign")


@_attrs_define
class Campaign:
    """A record from the dbo.CAMPAIGN table in Raiser's Edge.

    Attributes:
        campaign_id (str): The string identifier for the campaign.
        description (str): The campaign description.
        campaign_category (None | str | Unset): The campaign category.
        id (int | Unset): The immutable system record ID of the campaign.
        campaign_category_id (int | None | Unset): The identifier for a campaign category associated with the campaign.
        start_date (datetime.date | None | Unset): The start date for the campaign.
        end_date (datetime.date | None | Unset): The end date for the campaign.
        inactive (bool | Unset): The active status of the campaign; a campaign is active if the current date is after
            the start date and before the end date.
        default_fund_id (int | None | Unset): The ID for the default fund associated with the campaign.
        goal (float | None | Unset): The target amount to raise through the campaign.
        notes (None | str | Unset): The notes associated with the campaign.
    """

    campaign_id: str
    description: str
    campaign_category: None | str | Unset = UNSET
    id: int | Unset = UNSET
    campaign_category_id: int | None | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    inactive: bool | Unset = UNSET
    default_fund_id: int | None | Unset = UNSET
    goal: float | None | Unset = UNSET
    notes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        campaign_id = self.campaign_id

        description = self.description

        campaign_category: None | str | Unset
        if isinstance(self.campaign_category, Unset):
            campaign_category = UNSET
        else:
            campaign_category = self.campaign_category

        id = self.id

        campaign_category_id: int | None | Unset
        if isinstance(self.campaign_category_id, Unset):
            campaign_category_id = UNSET
        else:
            campaign_category_id = self.campaign_category_id

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

        goal: float | None | Unset
        if isinstance(self.goal, Unset):
            goal = UNSET
        else:
            goal = self.goal

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "campaign_id": campaign_id,
                "description": description,
            }
        )
        if campaign_category is not UNSET:
            field_dict["campaign_category"] = campaign_category
        if id is not UNSET:
            field_dict["id"] = id
        if campaign_category_id is not UNSET:
            field_dict["campaign_category_id"] = campaign_category_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if default_fund_id is not UNSET:
            field_dict["default_fund_id"] = default_fund_id
        if goal is not UNSET:
            field_dict["goal"] = goal
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        campaign_id = d.pop("campaign_id")

        description = d.pop("description")

        def _parse_campaign_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign_category = _parse_campaign_category(d.pop("campaign_category", UNSET))

        id = d.pop("id", UNSET)

        def _parse_campaign_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        campaign_category_id = _parse_campaign_category_id(
            d.pop("campaign_category_id", UNSET)
        )

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

        def _parse_goal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        goal = _parse_goal(d.pop("goal", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        campaign = cls(
            campaign_id=campaign_id,
            description=description,
            campaign_category=campaign_category,
            id=id,
            campaign_category_id=campaign_category_id,
            start_date=start_date,
            end_date=end_date,
            inactive=inactive,
            default_fund_id=default_fund_id,
            goal=goal,
            notes=notes,
        )

        return campaign

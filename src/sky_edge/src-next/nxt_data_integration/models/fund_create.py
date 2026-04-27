from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FundCreate")


@_attrs_define
class FundCreate:
    """A record from the dbo.FUND table in Raiser's Edge.

    Attributes:
        fund_id (str): The string identifier for the fund.
        description (str): The fund description.
        fund_category_id (int | None | Unset): The table entry ID for the fund category associated with the fund.
        fund_type_id (int | None | Unset): The table entry ID for the fund type associated with the fund.
        campaign_id (int | None | Unset): The system identifier for the campaign associated with the fund.
        start_date (datetime.date | None | Unset): The start date for the fund.
        end_date (datetime.date | None | Unset): The end date for the fund.
        inactive (bool | Unset): The active status of the fund; a fund is active if the current date is after the start
            date and before the end date.
        default_appeal_id (int | None | Unset): The ID for the default appeal associated with the fund.
        notes (None | str | Unset): The text notes associated with the fund.
        goal (float | None | Unset): The target amount to raise for the fund.
        restricted (bool | Unset): Value used to indicate whether the fund is restricted to specific users.
    """

    fund_id: str
    description: str
    fund_category_id: int | None | Unset = UNSET
    fund_type_id: int | None | Unset = UNSET
    campaign_id: int | None | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    inactive: bool | Unset = UNSET
    default_appeal_id: int | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    goal: float | None | Unset = UNSET
    restricted: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        fund_id = self.fund_id

        description = self.description

        fund_category_id: int | None | Unset
        if isinstance(self.fund_category_id, Unset):
            fund_category_id = UNSET
        else:
            fund_category_id = self.fund_category_id

        fund_type_id: int | None | Unset
        if isinstance(self.fund_type_id, Unset):
            fund_type_id = UNSET
        else:
            fund_type_id = self.fund_type_id

        campaign_id: int | None | Unset
        if isinstance(self.campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = self.campaign_id

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

        default_appeal_id: int | None | Unset
        if isinstance(self.default_appeal_id, Unset):
            default_appeal_id = UNSET
        else:
            default_appeal_id = self.default_appeal_id

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        goal: float | None | Unset
        if isinstance(self.goal, Unset):
            goal = UNSET
        else:
            goal = self.goal

        restricted = self.restricted

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fund_id": fund_id,
                "description": description,
            }
        )
        if fund_category_id is not UNSET:
            field_dict["fund_category_id"] = fund_category_id
        if fund_type_id is not UNSET:
            field_dict["fund_type_id"] = fund_type_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if default_appeal_id is not UNSET:
            field_dict["default_appeal_id"] = default_appeal_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if goal is not UNSET:
            field_dict["goal"] = goal
        if restricted is not UNSET:
            field_dict["restricted"] = restricted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fund_id = d.pop("fund_id")

        description = d.pop("description")

        def _parse_fund_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fund_category_id = _parse_fund_category_id(d.pop("fund_category_id", UNSET))

        def _parse_fund_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fund_type_id = _parse_fund_type_id(d.pop("fund_type_id", UNSET))

        def _parse_campaign_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        campaign_id = _parse_campaign_id(d.pop("campaign_id", UNSET))

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

        def _parse_default_appeal_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_appeal_id = _parse_default_appeal_id(d.pop("default_appeal_id", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_goal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        goal = _parse_goal(d.pop("goal", UNSET))

        restricted = d.pop("restricted", UNSET)

        fund_create = cls(
            fund_id=fund_id,
            description=description,
            fund_category_id=fund_category_id,
            fund_type_id=fund_type_id,
            campaign_id=campaign_id,
            start_date=start_date,
            end_date=end_date,
            inactive=inactive,
            default_appeal_id=default_appeal_id,
            notes=notes,
            goal=goal,
            restricted=restricted,
        )

        return fund_create

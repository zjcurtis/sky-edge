from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_event_location import EditEventLocation
    from ..models.event_category_lookup import EventCategoryLookup
    from ..models.event_group_lookup import EventGroupLookup


T = TypeVar("T", bound="EditEvent")


@_attrs_define
class EditEvent:
    """Events are planned occasions that help organizations raise awareness for their missions, engage constituents, and
    encourage donations.

        Attributes:
            category (EventCategoryLookup | Unset): Event category is the custom categorization for the event.
            group (EventGroupLookup | Unset): Event group is the custom group for the event.
            location (EditEventLocation | Unset): Defines the data model used for edit location.
            lookup_id (None | str | Unset): The lookup ID of the event.
            name (None | str | Unset): The name of the event.
            description (None | str | Unset): The description of the event.
            start_date (datetime.date | None | Unset): The start date of the event. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>.
            start_time (None | str | Unset): The start time of the event. Uses HH:mm format: <i>07:30</i>.
            end_date (datetime.date | None | Unset): The end date of the event. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>.
            end_time (None | str | Unset): The end time of the event. Uses HH:mm format: <i>07:30</i>.
            inactive (bool | Unset): Whether the event is inactive. True if inactive.
            capacity (int | None | Unset): The number of people that can attend the event.
            goal (float | None | Unset): The monetary goal of the event.
            campaign_id (None | str | Unset): The ID of the campaign affiliated with the event.
            fund_id (None | str | Unset): The ID of the fund affiliated with the event.
            appeal_id (None | str | Unset): The ID of the appeal affiliated with the event.
            package_id (None | str | Unset): The ID of the package affiliated with the event.
    """

    category: EventCategoryLookup | Unset = UNSET
    group: EventGroupLookup | Unset = UNSET
    location: EditEventLocation | Unset = UNSET
    lookup_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    start_time: None | str | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    end_time: None | str | Unset = UNSET
    inactive: bool | Unset = UNSET
    capacity: int | None | Unset = UNSET
    goal: float | None | Unset = UNSET
    campaign_id: None | str | Unset = UNSET
    fund_id: None | str | Unset = UNSET
    appeal_id: None | str | Unset = UNSET
    package_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        lookup_id: None | str | Unset
        if isinstance(self.lookup_id, Unset):
            lookup_id = UNSET
        else:
            lookup_id = self.lookup_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        else:
            start_time = self.start_time

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        inactive = self.inactive

        capacity: int | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        goal: float | None | Unset
        if isinstance(self.goal, Unset):
            goal = UNSET
        else:
            goal = self.goal

        campaign_id: None | str | Unset
        if isinstance(self.campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = self.campaign_id

        fund_id: None | str | Unset
        if isinstance(self.fund_id, Unset):
            fund_id = UNSET
        else:
            fund_id = self.fund_id

        appeal_id: None | str | Unset
        if isinstance(self.appeal_id, Unset):
            appeal_id = UNSET
        else:
            appeal_id = self.appeal_id

        package_id: None | str | Unset
        if isinstance(self.package_id, Unset):
            package_id = UNSET
        else:
            package_id = self.package_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if group is not UNSET:
            field_dict["group"] = group
        if location is not UNSET:
            field_dict["location"] = location
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if goal is not UNSET:
            field_dict["goal"] = goal
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if package_id is not UNSET:
            field_dict["package_id"] = package_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_event_location import EditEventLocation
        from ..models.event_category_lookup import EventCategoryLookup
        from ..models.event_group_lookup import EventGroupLookup

        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: EventCategoryLookup | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = EventCategoryLookup.from_dict(_category)

        _group = d.pop("group", UNSET)
        group: EventGroupLookup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = EventGroupLookup.from_dict(_group)

        _location = d.pop("location", UNSET)
        location: EditEventLocation | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = EditEventLocation.from_dict(_location)

        def _parse_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lookup_id = _parse_lookup_id(d.pop("lookup_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_start_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

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

        def _parse_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        inactive = d.pop("inactive", UNSET)

        def _parse_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))

        def _parse_goal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        goal = _parse_goal(d.pop("goal", UNSET))

        def _parse_campaign_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign_id = _parse_campaign_id(d.pop("campaign_id", UNSET))

        def _parse_fund_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fund_id = _parse_fund_id(d.pop("fund_id", UNSET))

        def _parse_appeal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appeal_id = _parse_appeal_id(d.pop("appeal_id", UNSET))

        def _parse_package_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_id = _parse_package_id(d.pop("package_id", UNSET))

        edit_event = cls(
            category=category,
            group=group,
            location=location,
            lookup_id=lookup_id,
            name=name,
            description=description,
            start_date=start_date,
            start_time=start_time,
            end_date=end_date,
            end_time=end_time,
            inactive=inactive,
            capacity=capacity,
            goal=goal,
            campaign_id=campaign_id,
            fund_id=fund_id,
            appeal_id=appeal_id,
            package_id=package_id,
        )

        return edit_event

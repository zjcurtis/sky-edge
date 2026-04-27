from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_category import EventCategory
    from ..models.event_group import EventGroup


T = TypeVar("T", bound="EventListEntry")


@_attrs_define
class EventListEntry:
    """Defines an entry in a list of events.

    Attributes:
        id (None | str | Unset): The unique identifier for the event.
        lookup_id (None | str | Unset): The custom identifier for the event.
        name (None | str | Unset): The name of the event.
        start_date (datetime.date | None | Unset): The start date of the event. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>.
        start_time (None | str | Unset): The start time of the event. Uses HH:mm format: <i>07:30</i>.
        end_date (datetime.date | None | Unset): The end date of the event. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>.
        end_time (None | str | Unset): The end time of the event. Uses HH:mm format: <i>07:30</i>.
        attending_count (int | None | Unset): The number of event participants who plan to attend.
        invited_count (int | None | Unset): The number of event invitees.
        revenue (float | None | Unset): The realized revenue of the event.
        goal (float | None | Unset): The goal revenue of the event.
        percent_of_goal (int | None | Unset): The realized revenue as a percentage of the goal revenue.
        date_added (datetime.datetime | None | Unset): The date the event was created. Includes an offset from UTC in <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
        date_modified (datetime.datetime | None | Unset): The date when the event was last modified. Includes an offset
            from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
        capacity (int | None | Unset): The number of people that can attend the event.
        inactive (bool | None | Unset): If the event inactive or not.  True if inactive and false otherwise.
        attended_count (int | None | Unset): The number of event attendees.
        category (EventCategory | Unset): Event category is the custom categorization for the event.
        group (EventGroup | Unset): Event group is the custom grouping for the event.
        expenses (float | None | Unset): The expense total for this event.
        net (float | None | Unset): The net revenue of the event.
        location_name (None | str | Unset): The location name of the event.
        payments_balance (float | None | Unset): The balance of payments due from fees for this event.
    """

    id: None | str | Unset = UNSET
    lookup_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    start_date: datetime.date | None | Unset = UNSET
    start_time: None | str | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    end_time: None | str | Unset = UNSET
    attending_count: int | None | Unset = UNSET
    invited_count: int | None | Unset = UNSET
    revenue: float | None | Unset = UNSET
    goal: float | None | Unset = UNSET
    percent_of_goal: int | None | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    capacity: int | None | Unset = UNSET
    inactive: bool | None | Unset = UNSET
    attended_count: int | None | Unset = UNSET
    category: EventCategory | Unset = UNSET
    group: EventGroup | Unset = UNSET
    expenses: float | None | Unset = UNSET
    net: float | None | Unset = UNSET
    location_name: None | str | Unset = UNSET
    payments_balance: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        attending_count: int | None | Unset
        if isinstance(self.attending_count, Unset):
            attending_count = UNSET
        else:
            attending_count = self.attending_count

        invited_count: int | None | Unset
        if isinstance(self.invited_count, Unset):
            invited_count = UNSET
        else:
            invited_count = self.invited_count

        revenue: float | None | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        goal: float | None | Unset
        if isinstance(self.goal, Unset):
            goal = UNSET
        else:
            goal = self.goal

        percent_of_goal: int | None | Unset
        if isinstance(self.percent_of_goal, Unset):
            percent_of_goal = UNSET
        else:
            percent_of_goal = self.percent_of_goal

        date_added: None | str | Unset
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        capacity: int | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        inactive: bool | None | Unset
        if isinstance(self.inactive, Unset):
            inactive = UNSET
        else:
            inactive = self.inactive

        attended_count: int | None | Unset
        if isinstance(self.attended_count, Unset):
            attended_count = UNSET
        else:
            attended_count = self.attended_count

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        expenses: float | None | Unset
        if isinstance(self.expenses, Unset):
            expenses = UNSET
        else:
            expenses = self.expenses

        net: float | None | Unset
        if isinstance(self.net, Unset):
            net = UNSET
        else:
            net = self.net

        location_name: None | str | Unset
        if isinstance(self.location_name, Unset):
            location_name = UNSET
        else:
            location_name = self.location_name

        payments_balance: float | None | Unset
        if isinstance(self.payments_balance, Unset):
            payments_balance = UNSET
        else:
            payments_balance = self.payments_balance

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if attending_count is not UNSET:
            field_dict["attending_count"] = attending_count
        if invited_count is not UNSET:
            field_dict["invited_count"] = invited_count
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if goal is not UNSET:
            field_dict["goal"] = goal
        if percent_of_goal is not UNSET:
            field_dict["percent_of_goal"] = percent_of_goal
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if attended_count is not UNSET:
            field_dict["attended_count"] = attended_count
        if category is not UNSET:
            field_dict["category"] = category
        if group is not UNSET:
            field_dict["group"] = group
        if expenses is not UNSET:
            field_dict["expenses"] = expenses
        if net is not UNSET:
            field_dict["net"] = net
        if location_name is not UNSET:
            field_dict["location_name"] = location_name
        if payments_balance is not UNSET:
            field_dict["payments_balance"] = payments_balance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_category import EventCategory
        from ..models.event_group import EventGroup

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_attending_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        attending_count = _parse_attending_count(d.pop("attending_count", UNSET))

        def _parse_invited_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        invited_count = _parse_invited_count(d.pop("invited_count", UNSET))

        def _parse_revenue(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))

        def _parse_goal(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        goal = _parse_goal(d.pop("goal", UNSET))

        def _parse_percent_of_goal(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        percent_of_goal = _parse_percent_of_goal(d.pop("percent_of_goal", UNSET))

        def _parse_date_added(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = isoparse(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_capacity(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))

        def _parse_inactive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inactive = _parse_inactive(d.pop("inactive", UNSET))

        def _parse_attended_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        attended_count = _parse_attended_count(d.pop("attended_count", UNSET))

        _category = d.pop("category", UNSET)
        category: EventCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = EventCategory.from_dict(_category)

        _group = d.pop("group", UNSET)
        group: EventGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = EventGroup.from_dict(_group)

        def _parse_expenses(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expenses = _parse_expenses(d.pop("expenses", UNSET))

        def _parse_net(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        net = _parse_net(d.pop("net", UNSET))

        def _parse_location_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name = _parse_location_name(d.pop("location_name", UNSET))

        def _parse_payments_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        payments_balance = _parse_payments_balance(d.pop("payments_balance", UNSET))

        event_list_entry = cls(
            id=id,
            lookup_id=lookup_id,
            name=name,
            start_date=start_date,
            start_time=start_time,
            end_date=end_date,
            end_time=end_time,
            attending_count=attending_count,
            invited_count=invited_count,
            revenue=revenue,
            goal=goal,
            percent_of_goal=percent_of_goal,
            date_added=date_added,
            date_modified=date_modified,
            capacity=capacity,
            inactive=inactive,
            attended_count=attended_count,
            category=category,
            group=group,
            expenses=expenses,
            net=net,
            location_name=location_name,
            payments_balance=payments_balance,
        )

        return event_list_entry

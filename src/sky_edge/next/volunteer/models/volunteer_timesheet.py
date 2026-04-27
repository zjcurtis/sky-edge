from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="VolunteerTimesheet")


@_attrs_define
class VolunteerTimesheet:
    """Represents a volunteer timesheet

    Attributes:
        id (int | Unset): Gets or sets the timesheet ID
        job (None | str | Unset): Gets or sets the job name
        job_id (int | None | Unset): Gets or sets the job ID
        department (None | str | Unset): Gets or sets the department
        location (None | str | Unset): Gets or sets the location
        category (None | str | Unset): Gets or sets the category
        position (None | str | Unset): Gets or sets the position
        task (None | str | Unset): Gets or sets the task
        volunteer_type (None | str | Unset): Gets or sets the volunteer type
        hours (float | None | Unset): Gets or sets the number of hours worked
        hourly_wage (float | None | Unset): Gets or sets the hourly wage
        value (float | None | Unset): Gets or sets the calculated value (hourly wage * hours)
        notes (None | str | Unset): Gets or sets the notes
        timesheet_date (datetime.datetime | None | Unset): Gets or sets the timesheet date
    """

    id: int | Unset = UNSET
    job: None | str | Unset = UNSET
    job_id: int | None | Unset = UNSET
    department: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    position: None | str | Unset = UNSET
    task: None | str | Unset = UNSET
    volunteer_type: None | str | Unset = UNSET
    hours: float | None | Unset = UNSET
    hourly_wage: float | None | Unset = UNSET
    value: float | None | Unset = UNSET
    notes: None | str | Unset = UNSET
    timesheet_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        job: None | str | Unset
        if isinstance(self.job, Unset):
            job = UNSET
        else:
            job = self.job

        job_id: int | None | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        position: None | str | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        task: None | str | Unset
        if isinstance(self.task, Unset):
            task = UNSET
        else:
            task = self.task

        volunteer_type: None | str | Unset
        if isinstance(self.volunteer_type, Unset):
            volunteer_type = UNSET
        else:
            volunteer_type = self.volunteer_type

        hours: float | None | Unset
        if isinstance(self.hours, Unset):
            hours = UNSET
        else:
            hours = self.hours

        hourly_wage: float | None | Unset
        if isinstance(self.hourly_wage, Unset):
            hourly_wage = UNSET
        else:
            hourly_wage = self.hourly_wage

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        timesheet_date: None | str | Unset
        if isinstance(self.timesheet_date, Unset):
            timesheet_date = UNSET
        elif isinstance(self.timesheet_date, datetime.datetime):
            timesheet_date = self.timesheet_date.isoformat()
        else:
            timesheet_date = self.timesheet_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if job is not UNSET:
            field_dict["job"] = job
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if department is not UNSET:
            field_dict["department"] = department
        if location is not UNSET:
            field_dict["location"] = location
        if category is not UNSET:
            field_dict["category"] = category
        if position is not UNSET:
            field_dict["position"] = position
        if task is not UNSET:
            field_dict["task"] = task
        if volunteer_type is not UNSET:
            field_dict["volunteer_type"] = volunteer_type
        if hours is not UNSET:
            field_dict["hours"] = hours
        if hourly_wage is not UNSET:
            field_dict["hourly_wage"] = hourly_wage
        if value is not UNSET:
            field_dict["value"] = value
        if notes is not UNSET:
            field_dict["notes"] = notes
        if timesheet_date is not UNSET:
            field_dict["timesheet_date"] = timesheet_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_job(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job = _parse_job(d.pop("job", UNSET))

        def _parse_job_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("department", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_position(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_task(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task = _parse_task(d.pop("task", UNSET))

        def _parse_volunteer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volunteer_type = _parse_volunteer_type(d.pop("volunteer_type", UNSET))

        def _parse_hours(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hours = _parse_hours(d.pop("hours", UNSET))

        def _parse_hourly_wage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hourly_wage = _parse_hourly_wage(d.pop("hourly_wage", UNSET))

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_timesheet_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                timesheet_date_type_0 = isoparse(data)

                return timesheet_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        timesheet_date = _parse_timesheet_date(d.pop("timesheet_date", UNSET))

        volunteer_timesheet = cls(
            id=id,
            job=job,
            job_id=job_id,
            department=department,
            location=location,
            category=category,
            position=position,
            task=task,
            volunteer_type=volunteer_type,
            hours=hours,
            hourly_wage=hourly_wage,
            value=value,
            notes=notes,
            timesheet_date=timesheet_date,
        )

        return volunteer_timesheet

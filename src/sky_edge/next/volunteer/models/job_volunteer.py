from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.assignment_day import AssignmentDay

T = TypeVar("T", bound="JobVolunteer")


@_attrs_define
class JobVolunteer:
    """Represents a volunteer assigned to a job

    Attributes:
        id (int | Unset): Gets or sets the assignment ID (from VOL_ASSIGNMENT.ID)
        constituent_id (int | Unset): Gets or sets the constituent record ID
        job_id (int | Unset): Gets or sets the job ID
        start_date (datetime.datetime | None | Unset): Gets or sets the assignment start date. No timezone information.
        end_date (datetime.datetime | None | Unset): Gets or sets the assignment end date. No timezone information.
        start_time (datetime.datetime | None | Unset): Gets or sets the assignment start time. No timezone information.
        end_time (datetime.datetime | None | Unset): Gets or sets the assignment end time. No timezone information.
        department (None | str | Unset): Gets or sets the department
        location (None | str | Unset): Gets or sets the location
        position (None | str | Unset): Gets or sets the position
        category (None | str | Unset): Gets or sets the category
        volunteer_type (None | str | Unset): Gets or sets the volunteer type
        status (None | str | Unset): Gets or sets the status
        requested_on (datetime.datetime | None | Unset): Gets or sets the date requested on. No timezone information.
        letter_sent (bool | None | Unset): Gets or sets whether a letter was sent
        letter_sent_on (datetime.datetime | None | Unset): Gets or sets the date the letter was sent on. No timezone
            information.
        first_name (None | str | Unset): Gets or sets the first name
        middle_name (None | str | Unset): Gets or sets the middle name
        last_name (None | str | Unset): Gets or sets the last name
        task (None | str | Unset): Gets or sets the task
        supervisor (None | str | Unset): Gets or sets the supervisor
        notes (None | str | Unset): Gets or sets the notes
        day_of_week (AssignmentDay | Unset): Represents the day of the week on which an assignment falls.
    """

    id: int | Unset = UNSET
    constituent_id: int | Unset = UNSET
    job_id: int | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    start_time: datetime.datetime | None | Unset = UNSET
    end_time: datetime.datetime | None | Unset = UNSET
    department: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    position: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    volunteer_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    requested_on: datetime.datetime | None | Unset = UNSET
    letter_sent: bool | None | Unset = UNSET
    letter_sent_on: datetime.datetime | None | Unset = UNSET
    first_name: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    task: None | str | Unset = UNSET
    supervisor: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    day_of_week: AssignmentDay | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        job_id = self.job_id

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        start_time: None | str | Unset
        if isinstance(self.start_time, Unset):
            start_time = UNSET
        elif isinstance(self.start_time, datetime.datetime):
            start_time = self.start_time.isoformat()
        else:
            start_time = self.start_time

        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        elif isinstance(self.end_time, datetime.datetime):
            end_time = self.end_time.isoformat()
        else:
            end_time = self.end_time

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

        position: None | str | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        volunteer_type: None | str | Unset
        if isinstance(self.volunteer_type, Unset):
            volunteer_type = UNSET
        else:
            volunteer_type = self.volunteer_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        requested_on: None | str | Unset
        if isinstance(self.requested_on, Unset):
            requested_on = UNSET
        elif isinstance(self.requested_on, datetime.datetime):
            requested_on = self.requested_on.isoformat()
        else:
            requested_on = self.requested_on

        letter_sent: bool | None | Unset
        if isinstance(self.letter_sent, Unset):
            letter_sent = UNSET
        else:
            letter_sent = self.letter_sent

        letter_sent_on: None | str | Unset
        if isinstance(self.letter_sent_on, Unset):
            letter_sent_on = UNSET
        elif isinstance(self.letter_sent_on, datetime.datetime):
            letter_sent_on = self.letter_sent_on.isoformat()
        else:
            letter_sent_on = self.letter_sent_on

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        task: None | str | Unset
        if isinstance(self.task, Unset):
            task = UNSET
        else:
            task = self.task

        supervisor: None | str | Unset
        if isinstance(self.supervisor, Unset):
            supervisor = UNSET
        else:
            supervisor = self.supervisor

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        day_of_week: str | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if department is not UNSET:
            field_dict["department"] = department
        if location is not UNSET:
            field_dict["location"] = location
        if position is not UNSET:
            field_dict["position"] = position
        if category is not UNSET:
            field_dict["category"] = category
        if volunteer_type is not UNSET:
            field_dict["volunteer_type"] = volunteer_type
        if status is not UNSET:
            field_dict["status"] = status
        if requested_on is not UNSET:
            field_dict["requested_on"] = requested_on
        if letter_sent is not UNSET:
            field_dict["letter_sent"] = letter_sent
        if letter_sent_on is not UNSET:
            field_dict["letter_sent_on"] = letter_sent_on
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if task is not UNSET:
            field_dict["task"] = task
        if supervisor is not UNSET:
            field_dict["supervisor"] = supervisor
        if notes is not UNSET:
            field_dict["notes"] = notes
        if day_of_week is not UNSET:
            field_dict["day_of_week"] = day_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        job_id = d.pop("job_id", UNSET)

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_start_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_type_0 = isoparse(data)

                return start_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_time = _parse_start_time(d.pop("start_time", UNSET))

        def _parse_end_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_type_0 = isoparse(data)

                return end_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

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

        def _parse_position(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_volunteer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volunteer_type = _parse_volunteer_type(d.pop("volunteer_type", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_requested_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                requested_on_type_0 = isoparse(data)

                return requested_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        requested_on = _parse_requested_on(d.pop("requested_on", UNSET))

        def _parse_letter_sent(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        letter_sent = _parse_letter_sent(d.pop("letter_sent", UNSET))

        def _parse_letter_sent_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                letter_sent_on_type_0 = isoparse(data)

                return letter_sent_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        letter_sent_on = _parse_letter_sent_on(d.pop("letter_sent_on", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_task(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task = _parse_task(d.pop("task", UNSET))

        def _parse_supervisor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        supervisor = _parse_supervisor(d.pop("supervisor", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _day_of_week = d.pop("day_of_week", UNSET)
        day_of_week: AssignmentDay | Unset
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = AssignmentDay(_day_of_week)

        job_volunteer = cls(
            id=id,
            constituent_id=constituent_id,
            job_id=job_id,
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            department=department,
            location=location,
            position=position,
            category=category,
            volunteer_type=volunteer_type,
            status=status,
            requested_on=requested_on,
            letter_sent=letter_sent,
            letter_sent_on=letter_sent_on,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            task=task,
            supervisor=supervisor,
            notes=notes,
            day_of_week=day_of_week,
        )

        return job_volunteer

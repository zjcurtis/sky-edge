from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """Represents volunteer job information

    Attributes:
        id (int | Unset): Gets or sets the unique identifier for the job
        name (None | str | Unset): Gets or sets the job name
        category (None | str | Unset): Gets or sets the job category.
        position (None | str | Unset): Gets or sets the position.
        volunteer_type (None | str | Unset): Gets or sets the volunteer type.
        minimum_age (int | None | Unset): Gets or sets the minimum age.
        start_date (datetime.datetime | None | Unset): Gets or sets the start date. Date only, no time or timezone
            information.
        end_date (datetime.datetime | None | Unset): Gets or sets the end date. Date only, no time or timezone
            information.
        organization_id (int | None | Unset): Gets or sets the organization ID.
        event_id (int | None | Unset): Gets or sets the event ID.
        allow_mandate (bool | None | Unset): Gets or sets whether the job allows mandate.
        completed (bool | None | Unset): Gets or sets whether the job is completed.
        description (None | str | Unset): Gets or sets the job description.
        added_by_id (int | Unset): Gets or sets the ID of the user who added this job.
        import_id (None | str | Unset): Gets or sets the import ID.
        date_added (datetime.datetime | Unset): Gets or sets the date the job was added. No timezone information.
        date_modified (datetime.datetime | Unset): Gets or sets the date the job was last modified. No timezone
            information.
        last_modified_by_id (int | Unset): Gets or sets the ID of the user who last modified this job.
    """

    id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    position: None | str | Unset = UNSET
    volunteer_type: None | str | Unset = UNSET
    minimum_age: int | None | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    organization_id: int | None | Unset = UNSET
    event_id: int | None | Unset = UNSET
    allow_mandate: bool | None | Unset = UNSET
    completed: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    added_by_id: int | Unset = UNSET
    import_id: None | str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    last_modified_by_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        volunteer_type: None | str | Unset
        if isinstance(self.volunteer_type, Unset):
            volunteer_type = UNSET
        else:
            volunteer_type = self.volunteer_type

        minimum_age: int | None | Unset
        if isinstance(self.minimum_age, Unset):
            minimum_age = UNSET
        else:
            minimum_age = self.minimum_age

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

        organization_id: int | None | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        event_id: int | None | Unset
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        else:
            event_id = self.event_id

        allow_mandate: bool | None | Unset
        if isinstance(self.allow_mandate, Unset):
            allow_mandate = UNSET
        else:
            allow_mandate = self.allow_mandate

        completed: bool | None | Unset
        if isinstance(self.completed, Unset):
            completed = UNSET
        else:
            completed = self.completed

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        added_by_id = self.added_by_id

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        last_modified_by_id = self.last_modified_by_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if position is not UNSET:
            field_dict["position"] = position
        if volunteer_type is not UNSET:
            field_dict["volunteer_type"] = volunteer_type
        if minimum_age is not UNSET:
            field_dict["minimum_age"] = minimum_age
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if allow_mandate is not UNSET:
            field_dict["allow_mandate"] = allow_mandate
        if completed is not UNSET:
            field_dict["completed"] = completed
        if description is not UNSET:
            field_dict["description"] = description
        if added_by_id is not UNSET:
            field_dict["added_by_id"] = added_by_id
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if last_modified_by_id is not UNSET:
            field_dict["last_modified_by_id"] = last_modified_by_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_volunteer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        volunteer_type = _parse_volunteer_type(d.pop("volunteer_type", UNSET))

        def _parse_minimum_age(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minimum_age = _parse_minimum_age(d.pop("minimum_age", UNSET))

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

        def _parse_organization_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_event_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        event_id = _parse_event_id(d.pop("event_id", UNSET))

        def _parse_allow_mandate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_mandate = _parse_allow_mandate(d.pop("allow_mandate", UNSET))

        def _parse_completed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        completed = _parse_completed(d.pop("completed", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        added_by_id = d.pop("added_by_id", UNSET)

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

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

        last_modified_by_id = d.pop("last_modified_by_id", UNSET)

        job = cls(
            id=id,
            name=name,
            category=category,
            position=position,
            volunteer_type=volunteer_type,
            minimum_age=minimum_age,
            start_date=start_date,
            end_date=end_date,
            organization_id=organization_id,
            event_id=event_id,
            allow_mandate=allow_mandate,
            completed=completed,
            description=description,
            added_by_id=added_by_id,
            import_id=import_id,
            date_added=date_added,
            date_modified=date_modified,
            last_modified_by_id=last_modified_by_id,
        )

        return job

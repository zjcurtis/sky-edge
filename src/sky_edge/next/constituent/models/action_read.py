from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.action_read_computed_status import ActionReadComputedStatus
from ..models.action_read_direction import ActionReadDirection
from ..models.action_read_outcome import ActionReadOutcome
from ..models.action_read_priority import ActionReadPriority

T = TypeVar("T", bound="ActionRead")


@_attrs_define
class ActionRead:
    """Actions track the interactions and tasks that are required to secure gifts and cultivate relationships with
    constituents.

        Attributes:
            id (str | Unset): The immutable system record ID of the action.
            category (str | Unset): The channel or intent of the constituent interaction. Available values are <i>Phone
                Call</i>, <i>Meeting</i>, <i>Mailing</i>, <i>Email</i>, and <i>Task/Other</i>.
            completed (bool | Unset): Indicates whether the action is complete. If the system is configured to use custom
                action statuses, this value is based on the action status value. This property defaults to <i>false</i> if no
                value is provided.
            completed_date (datetime.datetime | Unset): The date when the action was completed. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            computed_status (ActionReadComputedStatus | Unset): The computed action status. If the system is not configured
                to use custom action statuses, this field computes the status based on the <code>completed</code> and
                <code>date</code> properties. If not, the field calculates the status based on the action's date property and
                whether action's <code>Action Status</code> property is configured as completed.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the action.
            date (datetime.datetime | Unset): The action date. Uses <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
                format: </a><i>1969-11-21T10:29:43</i>.
            date_added (datetime.datetime | Unset): The date when the action was created. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the action was last modified. Includes an offset from
                UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            description (str | Unset): The detailed explanation that elaborates on the action summary.
            direction (ActionReadDirection | Unset): The direction of the action. Available values are <i>Inbound</i> and
                <i>Outbound</i>.
            end_time (str | Unset): The end time of the action. Uses 24-hour time in the <i>HH:mm</i> format. For example,
                17:30 represents 5:30 p.m.
            fundraisers (list[str] | Unset): The set of immutable constituent system record IDs for the fundraisers
                associated with the action.
            location (str | Unset): The location of the action. Available values are the entries in the <a href="https://dev
                eloper.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListActionLocations"><b>Action
                Locations</b></a> table.
            opportunity_id (str | Unset): The immutable system record ID of the opportunity associated with the action.
            outcome (ActionReadOutcome | Unset): The outcome of the action. Available values are <i>Successful</i> and
                <i>Unsuccessful</i>.
            priority (ActionReadPriority | Unset): The priority of the action. Available values are <i>Normal</i>,
                <i>High</i>, and <i>Low</i>. The default is <i>Normal</i>.
            start_time (str | Unset): The start time of the action. Uses 24-hour time in the <i>HH:mm</i> format. For
                example, 17:30 represents 5:30 p.m.
            status (str | Unset): The action status. If the system is configured to use custom action statuses, available
                values are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b
                3/operations/ListActionStatusTypes"><b>Action Status</b></a> table. If not, this field computes the status based
                on the <code>completed</code> and <code>date</code> properties: If an action is not completed and has a current
                or future date, the status is Open; if an action is not completed and has a past date, the status is Past due;
                and if an action is completed, the status is Completed.
            status_code (str | Unset): The action status code. Available values are in the <a href="https://developer.sky.bl
                ackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListActionStatusTypes"><b>Action Status</b></a>
                table. This property is only returned when the system is configured to use custom action statuses.
            summary (str | Unset): The short description of the action that appears at the top of the record.
            type_ (str | Unset): Additional description of the action to complement the category. Available values are the
                entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/Li
                stActionTypes"><b>Actions</b></a> table.
    """

    id: str | Unset = UNSET
    category: str | Unset = UNSET
    completed: bool | Unset = UNSET
    completed_date: datetime.datetime | Unset = UNSET
    computed_status: ActionReadComputedStatus | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    direction: ActionReadDirection | Unset = UNSET
    end_time: str | Unset = UNSET
    fundraisers: list[str] | Unset = UNSET
    location: str | Unset = UNSET
    opportunity_id: str | Unset = UNSET
    outcome: ActionReadOutcome | Unset = UNSET
    priority: ActionReadPriority | Unset = UNSET
    start_time: str | Unset = UNSET
    status: str | Unset = UNSET
    status_code: str | Unset = UNSET
    summary: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        completed = self.completed

        completed_date: str | Unset = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

        computed_status: str | Unset = UNSET
        if not isinstance(self.computed_status, Unset):
            computed_status = self.computed_status.value

        constituent_id = self.constituent_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        end_time = self.end_time

        fundraisers: list[str] | Unset = UNSET
        if not isinstance(self.fundraisers, Unset):
            fundraisers = self.fundraisers

        location = self.location

        opportunity_id = self.opportunity_id

        outcome: str | Unset = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        priority: str | Unset = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        start_time = self.start_time

        status = self.status

        status_code = self.status_code

        summary = self.summary

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if completed is not UNSET:
            field_dict["completed"] = completed
        if completed_date is not UNSET:
            field_dict["completed_date"] = completed_date
        if computed_status is not UNSET:
            field_dict["computed_status"] = computed_status
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date is not UNSET:
            field_dict["date"] = date
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if direction is not UNSET:
            field_dict["direction"] = direction
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if fundraisers is not UNSET:
            field_dict["fundraisers"] = fundraisers
        if location is not UNSET:
            field_dict["location"] = location
        if opportunity_id is not UNSET:
            field_dict["opportunity_id"] = opportunity_id
        if outcome is not UNSET:
            field_dict["outcome"] = outcome
        if priority is not UNSET:
            field_dict["priority"] = priority
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if summary is not UNSET:
            field_dict["summary"] = summary
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        category = d.pop("category", UNSET)

        completed = d.pop("completed", UNSET)

        _completed_date = d.pop("completed_date", UNSET)
        completed_date: datetime.datetime | Unset
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

        _computed_status = d.pop("computed_status", UNSET)
        computed_status: ActionReadComputedStatus | Unset
        if isinstance(_computed_status, Unset):
            computed_status = UNSET
        else:
            computed_status = ActionReadComputedStatus(_computed_status)

        constituent_id = d.pop("constituent_id", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

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

        description = d.pop("description", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: ActionReadDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = ActionReadDirection(_direction)

        end_time = d.pop("end_time", UNSET)

        fundraisers = cast(list[str], d.pop("fundraisers", UNSET))

        location = d.pop("location", UNSET)

        opportunity_id = d.pop("opportunity_id", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: ActionReadOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = ActionReadOutcome(_outcome)

        _priority = d.pop("priority", UNSET)
        priority: ActionReadPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ActionReadPriority(_priority)

        start_time = d.pop("start_time", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("status_code", UNSET)

        summary = d.pop("summary", UNSET)

        type_ = d.pop("type", UNSET)

        action_read = cls(
            id=id,
            category=category,
            completed=completed,
            completed_date=completed_date,
            computed_status=computed_status,
            constituent_id=constituent_id,
            date=date,
            date_added=date_added,
            date_modified=date_modified,
            description=description,
            direction=direction,
            end_time=end_time,
            fundraisers=fundraisers,
            location=location,
            opportunity_id=opportunity_id,
            outcome=outcome,
            priority=priority,
            start_time=start_time,
            status=status,
            status_code=status_code,
            summary=summary,
            type_=type_,
        )

        action_read.additional_properties = d
        return action_read

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

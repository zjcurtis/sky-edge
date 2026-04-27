from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.action_edit_direction import ActionEditDirection
from ..models.action_edit_outcome import ActionEditOutcome
from ..models.action_edit_priority import ActionEditPriority

T = TypeVar("T", bound="ActionEdit")


@_attrs_define
class ActionEdit:
    """Actions track the interactions and tasks that are required to secure gifts and cultivate relationships with
    constituents.

        Attributes:
            category (str | Unset): The channel or intent of the constituent interaction. Available values are <i>Phone
                Call</i>, <i>Meeting</i>, <i>Mailing</i>, <i>Email</i>, and <i>Task/Other</i>. This property cannot be set to
                null.
            completed (bool | Unset): Indicates whether the action is complete. If the system is configured to use custom
                action statuses, this value is based on the action status value. This property defaults to <i>false</i> if no
                value is provided.
            completed_date (datetime.datetime | Unset): The date when the action was completed. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            date (datetime.datetime | Unset): The action date. Uses <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
                format: </a><i>1969-11-21T10:29:43</i>. This property cannot be set to null.
            description (str | Unset): The detailed explanation that elaborates on the action summary.
            direction (ActionEditDirection | Unset): The direction of the action. Available values are <i>Inbound</i> and
                <i>Outbound</i>.
            end_time (str | Unset): The end time of the action. Uses 24-hour time in the <i>HH:mm</i> format. For example,
                17:30 represents 5:30 p.m.
            fundraisers (list[str] | Unset): The set of immutable constituent system record IDs for the fundraisers
                associated with the action.
            location (str | Unset): The location of the action. Available values are the entries in the <a href="https://dev
                eloper.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListActionLocations"><b>Action
                Locations</b></a> table.
            opportunity_id (str | Unset): The immutable system record ID of the opportunity associated with the action.
            outcome (ActionEditOutcome | Unset): The outcome of the action. Available values are <i>Successful</i> and
                <i>Unsuccessful</i>.
            priority (ActionEditPriority | Unset): The priority of the action. Available values are <i>Normal</i>,
                <i>High</i>, and <i>Low</i>. The default is <i>Normal</i>.
            start_time (str | Unset): The start time of the action. Uses 24-hour time in the <i>HH:mm</i> format. For
                example, 17:30 represents 5:30 p.m.
            status (str | Unset): The action status. If the system is configured to use custom action statuses, available
                values are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b
                3/operations/ListActionStatusTypes"><b>Action Status</b></a> table. If not, this field computes the status based
                on the <code>completed</code> and <code>date</code> properties: If an action is not completed and has a current
                or future date, the status is Open; if an action is not completed and has a past date, the status is Past due;
                and if an action is completed, the status is Completed.
            summary (str | Unset): The short description of the action that appears at the top of the record. Character
                limit: 255.
            type_ (str | Unset): Additional description of the action to complement the category. Available values are the
                entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/Li
                stActionTypes"><b>Actions</b></a> table.
    """

    category: str | Unset = UNSET
    completed: bool | Unset = UNSET
    completed_date: datetime.datetime | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    direction: ActionEditDirection | Unset = UNSET
    end_time: str | Unset = UNSET
    fundraisers: list[str] | Unset = UNSET
    location: str | Unset = UNSET
    opportunity_id: str | Unset = UNSET
    outcome: ActionEditOutcome | Unset = UNSET
    priority: ActionEditPriority | Unset = UNSET
    start_time: str | Unset = UNSET
    status: str | Unset = UNSET
    summary: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        completed = self.completed

        completed_date: str | Unset = UNSET
        if not isinstance(self.completed_date, Unset):
            completed_date = self.completed_date.isoformat()

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

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

        summary = self.summary

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if completed is not UNSET:
            field_dict["completed"] = completed
        if completed_date is not UNSET:
            field_dict["completed_date"] = completed_date
        if date is not UNSET:
            field_dict["date"] = date
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
        if summary is not UNSET:
            field_dict["summary"] = summary
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        completed = d.pop("completed", UNSET)

        _completed_date = d.pop("completed_date", UNSET)
        completed_date: datetime.datetime | Unset
        if isinstance(_completed_date, Unset):
            completed_date = UNSET
        else:
            completed_date = isoparse(_completed_date)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        description = d.pop("description", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: ActionEditDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = ActionEditDirection(_direction)

        end_time = d.pop("end_time", UNSET)

        fundraisers = cast(list[str], d.pop("fundraisers", UNSET))

        location = d.pop("location", UNSET)

        opportunity_id = d.pop("opportunity_id", UNSET)

        _outcome = d.pop("outcome", UNSET)
        outcome: ActionEditOutcome | Unset
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = ActionEditOutcome(_outcome)

        _priority = d.pop("priority", UNSET)
        priority: ActionEditPriority | Unset
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = ActionEditPriority(_priority)

        start_time = d.pop("start_time", UNSET)

        status = d.pop("status", UNSET)

        summary = d.pop("summary", UNSET)

        type_ = d.pop("type", UNSET)

        action_edit = cls(
            category=category,
            completed=completed,
            completed_date=completed_date,
            date=date,
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
            summary=summary,
            type_=type_,
        )

        action_edit.additional_properties = d
        return action_edit

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

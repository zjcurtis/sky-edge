from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="VolunteerTypeUpdate")


@_attrs_define
class VolunteerTypeUpdate:
    """Represents volunteer type update information for a volunteer

    Attributes:
        type_ (None | str | Unset): Gets or sets the volunteer type description
        status (None | str | Unset): Gets or sets the status description
        date_started (FuzzyDate | Unset): Represents a fuzzy date that may contain only a year, year and month, or a
            complete date.
        date_finished (FuzzyDate | Unset): Represents a fuzzy date that may contain only a year, year and month, or a
            complete date.
        reason_finished (None | str | Unset): Gets or sets the reason the classification ceased to be valid
    """

    type_: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    date_started: FuzzyDate | Unset = UNSET
    date_finished: FuzzyDate | Unset = UNSET
    reason_finished: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        date_started: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_started, Unset):
            date_started = self.date_started.to_dict()

        date_finished: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_finished, Unset):
            date_finished = self.date_finished.to_dict()

        reason_finished: None | str | Unset
        if isinstance(self.reason_finished, Unset):
            reason_finished = UNSET
        else:
            reason_finished = self.reason_finished

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if date_started is not UNSET:
            field_dict["date_started"] = date_started
        if date_finished is not UNSET:
            field_dict["date_finished"] = date_finished
        if reason_finished is not UNSET:
            field_dict["reason_finished"] = reason_finished

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        _date_started = d.pop("date_started", UNSET)
        date_started: FuzzyDate | Unset
        if isinstance(_date_started, Unset):
            date_started = UNSET
        else:
            date_started = FuzzyDate.from_dict(_date_started)

        _date_finished = d.pop("date_finished", UNSET)
        date_finished: FuzzyDate | Unset
        if isinstance(_date_finished, Unset):
            date_finished = UNSET
        else:
            date_finished = FuzzyDate.from_dict(_date_finished)

        def _parse_reason_finished(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason_finished = _parse_reason_finished(d.pop("reason_finished", UNSET))

        volunteer_type_update = cls(
            type_=type_,
            status=status,
            date_started=date_started,
            date_finished=date_finished,
            reason_finished=reason_finished,
        )

        return volunteer_type_update

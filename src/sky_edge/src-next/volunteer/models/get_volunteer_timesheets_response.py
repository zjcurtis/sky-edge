from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volunteer_timesheet import VolunteerTimesheet


T = TypeVar("T", bound="GetVolunteerTimesheetsResponse")


@_attrs_define
class GetVolunteerTimesheetsResponse:
    """Response model for getting volunteer timesheets

    Attributes:
        total_count (int | Unset): Gets or sets the total count of timesheets
        timesheets (list[VolunteerTimesheet] | None | Unset): Gets or sets the collection of timesheets
    """

    total_count: int | Unset = UNSET
    timesheets: list[VolunteerTimesheet] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        timesheets: list[dict[str, Any]] | None | Unset
        if isinstance(self.timesheets, Unset):
            timesheets = UNSET
        elif isinstance(self.timesheets, list):
            timesheets = []
            for timesheets_type_0_item_data in self.timesheets:
                timesheets_type_0_item = timesheets_type_0_item_data.to_dict()
                timesheets.append(timesheets_type_0_item)

        else:
            timesheets = self.timesheets

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if timesheets is not UNSET:
            field_dict["timesheets"] = timesheets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volunteer_timesheet import VolunteerTimesheet

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        def _parse_timesheets(data: object) -> list[VolunteerTimesheet] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                timesheets_type_0 = []
                _timesheets_type_0 = data
                for timesheets_type_0_item_data in _timesheets_type_0:
                    timesheets_type_0_item = VolunteerTimesheet.from_dict(timesheets_type_0_item_data)

                    timesheets_type_0.append(timesheets_type_0_item)

                return timesheets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VolunteerTimesheet] | None | Unset, data)

        timesheets = _parse_timesheets(d.pop("timesheets", UNSET))

        get_volunteer_timesheets_response = cls(
            total_count=total_count,
            timesheets=timesheets,
        )

        return get_volunteer_timesheets_response

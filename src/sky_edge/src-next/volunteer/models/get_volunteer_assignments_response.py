from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volunteer_assignment import VolunteerAssignment


T = TypeVar("T", bound="GetVolunteerAssignmentsResponse")


@_attrs_define
class GetVolunteerAssignmentsResponse:
    """Response model for volunteer assignments

    Attributes:
        total_count (int | Unset): Gets or sets the total count of assignments
        assignments (list[VolunteerAssignment] | None | Unset): Gets or sets the collection of assignments
    """

    total_count: int | Unset = UNSET
    assignments: list[VolunteerAssignment] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        assignments: list[dict[str, Any]] | None | Unset
        if isinstance(self.assignments, Unset):
            assignments = UNSET
        elif isinstance(self.assignments, list):
            assignments = []
            for assignments_type_0_item_data in self.assignments:
                assignments_type_0_item = assignments_type_0_item_data.to_dict()
                assignments.append(assignments_type_0_item)

        else:
            assignments = self.assignments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if assignments is not UNSET:
            field_dict["assignments"] = assignments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volunteer_assignment import VolunteerAssignment

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        def _parse_assignments(data: object) -> list[VolunteerAssignment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignments_type_0 = []
                _assignments_type_0 = data
                for assignments_type_0_item_data in _assignments_type_0:
                    assignments_type_0_item = VolunteerAssignment.from_dict(assignments_type_0_item_data)

                    assignments_type_0.append(assignments_type_0_item)

                return assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VolunteerAssignment] | None | Unset, data)

        assignments = _parse_assignments(d.pop("assignments", UNSET))

        get_volunteer_assignments_response = cls(
            total_count=total_count,
            assignments=assignments,
        )

        return get_volunteer_assignments_response

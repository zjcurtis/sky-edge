from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_volunteer import JobVolunteer


T = TypeVar("T", bound="GetJobVolunteersResponse")


@_attrs_define
class GetJobVolunteersResponse:
    """Response model for job volunteers

    Attributes:
        total_count (int | Unset): Count of total volunteers
        volunteers (list[JobVolunteer] | None | Unset): List of volunteers assigned to the job
    """

    total_count: int | Unset = UNSET
    volunteers: list[JobVolunteer] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        volunteers: list[dict[str, Any]] | None | Unset
        if isinstance(self.volunteers, Unset):
            volunteers = UNSET
        elif isinstance(self.volunteers, list):
            volunteers = []
            for volunteers_type_0_item_data in self.volunteers:
                volunteers_type_0_item = volunteers_type_0_item_data.to_dict()
                volunteers.append(volunteers_type_0_item)

        else:
            volunteers = self.volunteers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if volunteers is not UNSET:
            field_dict["volunteers"] = volunteers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_volunteer import JobVolunteer

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        def _parse_volunteers(data: object) -> list[JobVolunteer] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                volunteers_type_0 = []
                _volunteers_type_0 = data
                for volunteers_type_0_item_data in _volunteers_type_0:
                    volunteers_type_0_item = JobVolunteer.from_dict(volunteers_type_0_item_data)

                    volunteers_type_0.append(volunteers_type_0_item)

                return volunteers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobVolunteer] | None | Unset, data)

        volunteers = _parse_volunteers(d.pop("volunteers", UNSET))

        get_job_volunteers_response = cls(
            total_count=total_count,
            volunteers=volunteers,
        )

        return get_job_volunteers_response

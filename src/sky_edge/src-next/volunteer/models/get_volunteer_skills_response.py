from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volunteer_skill import VolunteerSkill


T = TypeVar("T", bound="GetVolunteerSkillsResponse")


@_attrs_define
class GetVolunteerSkillsResponse:
    """Response model for getting volunteer skills

    Attributes:
        total_count (int | Unset): Gets or sets the total count of volunteer skills
        skills (list[VolunteerSkill] | None | Unset): Gets or sets the collection of volunteer skills
    """

    total_count: int | Unset = UNSET
    skills: list[VolunteerSkill] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        skills: list[dict[str, Any]] | None | Unset
        if isinstance(self.skills, Unset):
            skills = UNSET
        elif isinstance(self.skills, list):
            skills = []
            for skills_type_0_item_data in self.skills:
                skills_type_0_item = skills_type_0_item_data.to_dict()
                skills.append(skills_type_0_item)

        else:
            skills = self.skills

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if skills is not UNSET:
            field_dict["skills"] = skills

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volunteer_skill import VolunteerSkill

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        def _parse_skills(data: object) -> list[VolunteerSkill] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skills_type_0 = []
                _skills_type_0 = data
                for skills_type_0_item_data in _skills_type_0:
                    skills_type_0_item = VolunteerSkill.from_dict(skills_type_0_item_data)

                    skills_type_0.append(skills_type_0_item)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VolunteerSkill] | None | Unset, data)

        skills = _parse_skills(d.pop("skills", UNSET))

        get_volunteer_skills_response = cls(
            total_count=total_count,
            skills=skills,
        )

        return get_volunteer_skills_response

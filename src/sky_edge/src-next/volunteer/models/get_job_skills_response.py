from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_skill import JobSkill


T = TypeVar("T", bound="GetJobSkillsResponse")


@_attrs_define
class GetJobSkillsResponse:
    """Response model for job skills

    Attributes:
        skills (list[JobSkill] | None | Unset): List of skills and experience requirements for the job
    """

    skills: list[JobSkill] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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
        if skills is not UNSET:
            field_dict["skills"] = skills

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_skill import JobSkill

        d = dict(src_dict)

        def _parse_skills(data: object) -> list[JobSkill] | None | Unset:
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
                    skills_type_0_item = JobSkill.from_dict(skills_type_0_item_data)

                    skills_type_0.append(skills_type_0_item)

                return skills_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JobSkill] | None | Unset, data)

        skills = _parse_skills(d.pop("skills", UNSET))

        get_job_skills_response = cls(
            skills=skills,
        )

        return get_job_skills_response

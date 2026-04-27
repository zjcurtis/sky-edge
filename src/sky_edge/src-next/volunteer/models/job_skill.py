from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSkill")


@_attrs_define
class JobSkill:
    """Represents a skill or experience requirement for a volunteer job

    Attributes:
        job_id (int | Unset): Gets or sets the job ID
        description (None | str | Unset): Gets or sets the skill description
        skill_level (None | str | Unset): Gets or sets the skill level
        license_type (None | str | Unset): Gets or sets the license type
    """

    job_id: int | Unset = UNSET
    description: None | str | Unset = UNSET
    skill_level: None | str | Unset = UNSET
    license_type: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        skill_level: None | str | Unset
        if isinstance(self.skill_level, Unset):
            skill_level = UNSET
        else:
            skill_level = self.skill_level

        license_type: None | str | Unset
        if isinstance(self.license_type, Unset):
            license_type = UNSET
        else:
            license_type = self.license_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if description is not UNSET:
            field_dict["description"] = description
        if skill_level is not UNSET:
            field_dict["skill_level"] = skill_level
        if license_type is not UNSET:
            field_dict["license_type"] = license_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_skill_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        skill_level = _parse_skill_level(d.pop("skill_level", UNSET))

        def _parse_license_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_type = _parse_license_type(d.pop("license_type", UNSET))

        job_skill = cls(
            job_id=job_id,
            description=description,
            skill_level=skill_level,
            license_type=license_type,
        )

        return job_skill

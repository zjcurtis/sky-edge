from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="VolunteerSkillUpdate")


@_attrs_define
class VolunteerSkillUpdate:
    """Represents volunteer skill update information for a volunteer

    Attributes:
        skill_description (None | str | Unset): Gets or sets the skill description
        skill_level (None | str | Unset): Gets or sets the skill level
        license_type (None | str | Unset): Gets or sets the license type
        expiration_date (FuzzyDate | Unset): Represents a fuzzy date that may contain only a year, year and month, or a
            complete date.
        comments (None | str | Unset): Gets or sets user comments associated with the skill
    """

    skill_description: None | str | Unset = UNSET
    skill_level: None | str | Unset = UNSET
    license_type: None | str | Unset = UNSET
    expiration_date: FuzzyDate | Unset = UNSET
    comments: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        skill_description: None | str | Unset
        if isinstance(self.skill_description, Unset):
            skill_description = UNSET
        else:
            skill_description = self.skill_description

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

        expiration_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.to_dict()

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if skill_description is not UNSET:
            field_dict["skill_description"] = skill_description
        if skill_level is not UNSET:
            field_dict["skill_level"] = skill_level
        if license_type is not UNSET:
            field_dict["license_type"] = license_type
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)

        def _parse_skill_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        skill_description = _parse_skill_description(d.pop("skill_description", UNSET))

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

        _expiration_date = d.pop("expiration_date", UNSET)
        expiration_date: FuzzyDate | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = FuzzyDate.from_dict(_expiration_date)

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        volunteer_skill_update = cls(
            skill_description=skill_description,
            skill_level=skill_level,
            license_type=license_type,
            expiration_date=expiration_date,
            comments=comments,
        )

        return volunteer_skill_update

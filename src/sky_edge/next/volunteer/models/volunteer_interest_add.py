from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="VolunteerInterestAdd")


@_attrs_define
class VolunteerInterestAdd:
    """Represents a request to add an interest for a volunteer

    Attributes:
        constituent_id (str): The parent constituent's immutable system record ID.
        description (str): Gets or sets the description
    """

    constituent_id: str
    description: str

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "constituent_id": constituent_id,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        description = d.pop("description")

        volunteer_interest_add = cls(
            constituent_id=constituent_id,
            description=description,
        )

        return volunteer_interest_add

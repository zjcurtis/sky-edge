from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VolunteerInterest")


@_attrs_define
class VolunteerInterest:
    """Represents an interest for a volunteer

    Attributes:
        constituent_id (str): The parent constituent's immutable system record ID.
        description (str): Gets or sets the description
        id (int | Unset): Gets or sets the unique identifier for the interest
    """

    constituent_id: str
    description: str
    id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        description = self.description

        id = self.id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "constituent_id": constituent_id,
                "description": description,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        description = d.pop("description")

        id = d.pop("id", UNSET)

        volunteer_interest = cls(
            constituent_id=constituent_id,
            description=description,
            id=id,
        )

        return volunteer_interest

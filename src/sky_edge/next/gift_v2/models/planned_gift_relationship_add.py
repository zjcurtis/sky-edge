from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PlannedGiftRelationshipAdd")


@_attrs_define
class PlannedGiftRelationshipAdd:
    """Model for adding a new planned gift relationship.

    Attributes:
        type_of_relationship (str): The type of relationship. Valid values: "Individual", "Organization", "Financial",
            "Education".
        relationship_id (str): The relationship record identifier. This is the ID from the corresponding relationship
            table
            (CONSTIT_RELATIONSHIPS, CONSTITUENT_BANK, or EDUCATION) depending on the type_of_relationship.
    """

    type_of_relationship: str
    relationship_id: str

    def to_dict(self) -> dict[str, Any]:
        type_of_relationship = self.type_of_relationship

        relationship_id = self.relationship_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type_of_relationship": type_of_relationship,
                "relationship_id": relationship_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_of_relationship = d.pop("type_of_relationship")

        relationship_id = d.pop("relationship_id")

        planned_gift_relationship_add = cls(
            type_of_relationship=type_of_relationship,
            relationship_id=relationship_id,
        )

        return planned_gift_relationship_add

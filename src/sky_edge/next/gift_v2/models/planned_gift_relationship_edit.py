from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="PlannedGiftRelationshipEdit")


@_attrs_define
class PlannedGiftRelationshipEdit:
    """Model for editing an existing planned gift relationship. All fields are optional for PATCH semantics.

    Attributes:
        type_of_relationship (None | str | Unset): The type of relationship. Valid values: "Individual", "Organization",
            "Financial", "Education".
        relationship_id (None | str | Unset): The relationship record identifier.
    """

    type_of_relationship: None | str | Unset = UNSET
    relationship_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_of_relationship: None | str | Unset
        if isinstance(self.type_of_relationship, Unset):
            type_of_relationship = UNSET
        else:
            type_of_relationship = self.type_of_relationship

        relationship_id: None | str | Unset
        if isinstance(self.relationship_id, Unset):
            relationship_id = UNSET
        else:
            relationship_id = self.relationship_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_of_relationship is not UNSET:
            field_dict["type_of_relationship"] = type_of_relationship
        if relationship_id is not UNSET:
            field_dict["relationship_id"] = relationship_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_of_relationship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_relationship = _parse_type_of_relationship(
            d.pop("type_of_relationship", UNSET)
        )

        def _parse_relationship_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship_id = _parse_relationship_id(d.pop("relationship_id", UNSET))

        planned_gift_relationship_edit = cls(
            type_of_relationship=type_of_relationship,
            relationship_id=relationship_id,
        )

        return planned_gift_relationship_edit

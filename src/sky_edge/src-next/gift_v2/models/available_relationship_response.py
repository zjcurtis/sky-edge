from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableRelationshipResponse")


@_attrs_define
class AvailableRelationshipResponse:
    """Represents an available constituent relationship that could be added
    to a planned gift as a relationship or beneficiary.

        Attributes:
            relationship_source_id (None | str): The source record identifier from the respective table
                (CONSTIT_RELATIONSHIPS.ID for types 1/2, CONSTITUENT_BANK.ID for type 3, EDUCATION.ID for type 4).
            relationship_type (None | str): The relationship type: Individual, Organization, Financial, or Education.
            gift_relationship (bool): Whether this relationship is already added as a gift relationship on this planned
                gift.
            gift_beneficiary (bool): Whether this relationship is already added as a gift beneficiary on this planned gift.
            name (None | str | Unset): The display name of the related entity.
            relation_code (None | str | Unset): The relation code description (Individual/Organization types only).
    """

    relationship_source_id: None | str
    relationship_type: None | str
    gift_relationship: bool
    gift_beneficiary: bool
    name: None | str | Unset = UNSET
    relation_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        relationship_source_id: None | str
        relationship_source_id = self.relationship_source_id

        relationship_type: None | str
        relationship_type = self.relationship_type

        gift_relationship = self.gift_relationship

        gift_beneficiary = self.gift_beneficiary

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        relation_code: None | str | Unset
        if isinstance(self.relation_code, Unset):
            relation_code = UNSET
        else:
            relation_code = self.relation_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "relationship_source_id": relationship_source_id,
                "relationship_type": relationship_type,
                "gift_relationship": gift_relationship,
                "gift_beneficiary": gift_beneficiary,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if relation_code is not UNSET:
            field_dict["relation_code"] = relation_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_relationship_source_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relationship_source_id = _parse_relationship_source_id(d.pop("relationship_source_id"))

        def _parse_relationship_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relationship_type = _parse_relationship_type(d.pop("relationship_type"))

        gift_relationship = d.pop("gift_relationship")

        gift_beneficiary = d.pop("gift_beneficiary")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_relation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation_code = _parse_relation_code(d.pop("relation_code", UNSET))

        available_relationship_response = cls(
            relationship_source_id=relationship_source_id,
            relationship_type=relationship_type,
            gift_relationship=gift_relationship,
            gift_beneficiary=gift_beneficiary,
            name=name,
            relation_code=relation_code,
        )

        return available_relationship_response

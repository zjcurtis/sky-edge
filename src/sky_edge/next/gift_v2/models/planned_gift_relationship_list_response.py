from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.planned_gift_relationship_response import (
        PlannedGiftRelationshipResponse,
    )


T = TypeVar("T", bound="PlannedGiftRelationshipListResponse")


@_attrs_define
class PlannedGiftRelationshipListResponse:
    """Represents the paginated list response for planned gift relationships.

    Attributes:
        count (int): The total number of relationships.
        offset (int): The number of records that were skipped in the current request.
        limit (int): The maximum number of records that were requested.
        relationships (list[PlannedGiftRelationshipResponse]): The list of planned gift relationships.
    """

    count: int
    offset: int
    limit: int
    relationships: list[PlannedGiftRelationshipResponse]

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        offset = self.offset

        limit = self.limit

        relationships = []
        for relationships_item_data in self.relationships:
            relationships_item = relationships_item_data.to_dict()
            relationships.append(relationships_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "offset": offset,
                "limit": limit,
                "relationships": relationships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.planned_gift_relationship_response import (
            PlannedGiftRelationshipResponse,
        )

        d = dict(src_dict)
        count = d.pop("count")

        offset = d.pop("offset")

        limit = d.pop("limit")

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = PlannedGiftRelationshipResponse.from_dict(
                relationships_item_data
            )

            relationships.append(relationships_item)

        planned_gift_relationship_list_response = cls(
            count=count,
            offset=offset,
            limit=limit,
            relationships=relationships,
        )

        return planned_gift_relationship_list_response

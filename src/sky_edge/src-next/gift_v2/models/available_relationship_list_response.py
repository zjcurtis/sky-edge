from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.available_relationship_response import AvailableRelationshipResponse


T = TypeVar("T", bound="AvailableRelationshipListResponse")


@_attrs_define
class AvailableRelationshipListResponse:
    """Represents the paginated list response for available relationships.

    Attributes:
        count (int): The total number of available relationships.
        offset (int): The number of records that were skipped in the current request.
        limit (int): The maximum number of records that were requested.
        available_relationships (list[AvailableRelationshipResponse]): The list of available relationships.
    """

    count: int
    offset: int
    limit: int
    available_relationships: list[AvailableRelationshipResponse]

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        offset = self.offset

        limit = self.limit

        available_relationships = []
        for available_relationships_item_data in self.available_relationships:
            available_relationships_item = available_relationships_item_data.to_dict()
            available_relationships.append(available_relationships_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "offset": offset,
                "limit": limit,
                "available_relationships": available_relationships,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.available_relationship_response import AvailableRelationshipResponse

        d = dict(src_dict)
        count = d.pop("count")

        offset = d.pop("offset")

        limit = d.pop("limit")

        available_relationships = []
        _available_relationships = d.pop("available_relationships")
        for available_relationships_item_data in _available_relationships:
            available_relationships_item = AvailableRelationshipResponse.from_dict(available_relationships_item_data)

            available_relationships.append(available_relationships_item)

        available_relationship_list_response = cls(
            count=count,
            offset=offset,
            limit=limit,
            available_relationships=available_relationships,
        )

        return available_relationship_list_response

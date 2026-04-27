from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="QueryNodesRequest")


@_attrs_define
class QueryNodesRequest:
    """A request for a set of available fields tree nodes.

    Attributes:
        node_ids (list[int]): The set of nodes to retrieve.
    """

    node_ids: list[int]

    def to_dict(self) -> dict[str, Any]:
        node_ids = self.node_ids

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "node_ids": node_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_ids = cast(list[int], d.pop("node_ids"))

        query_nodes_request = cls(
            node_ids=node_ids,
        )

        return query_nodes_request

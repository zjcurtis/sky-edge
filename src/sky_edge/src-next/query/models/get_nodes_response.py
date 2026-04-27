from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_node_response import GetNodeResponse


T = TypeVar("T", bound="GetNodesResponse")


@_attrs_define
class GetNodesResponse:
    """Response containing the requested set of nodes.

    Attributes:
        nodes (list[GetNodeResponse] | None | Unset): The requested set of nodes.
    """

    nodes: list[GetNodeResponse] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        nodes: list[dict[str, Any]] | None | Unset
        if isinstance(self.nodes, Unset):
            nodes = UNSET
        elif isinstance(self.nodes, list):
            nodes = []
            for nodes_type_0_item_data in self.nodes:
                nodes_type_0_item = nodes_type_0_item_data.to_dict()
                nodes.append(nodes_type_0_item)

        else:
            nodes = self.nodes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if nodes is not UNSET:
            field_dict["nodes"] = nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_node_response import GetNodeResponse

        d = dict(src_dict)

        def _parse_nodes(data: object) -> list[GetNodeResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                nodes_type_0 = []
                _nodes_type_0 = data
                for nodes_type_0_item_data in _nodes_type_0:
                    nodes_type_0_item = GetNodeResponse.from_dict(nodes_type_0_item_data)

                    nodes_type_0.append(nodes_type_0_item)

                return nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GetNodeResponse] | None | Unset, data)

        nodes = _parse_nodes(d.pop("nodes", UNSET))

        get_nodes_response = cls(
            nodes=nodes,
        )

        return get_nodes_response

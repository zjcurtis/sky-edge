from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_field import QueryField
    from ..models.query_node import QueryNode


T = TypeVar("T", bound="GetNodeResponse")


@_attrs_define
class GetNodeResponse:
    """A requested node.

    Attributes:
        node_id (int | Unset): The ID of the node.
        nodes (list[QueryNode] | None | Unset): The requested QueryNodes
        fields (list[QueryField] | None | Unset): The requested QueryFields
    """

    node_id: int | Unset = UNSET
    nodes: list[QueryNode] | None | Unset = UNSET
    fields: list[QueryField] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

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

        fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, list):
            fields = []
            for fields_type_0_item_data in self.fields:
                fields_type_0_item = fields_type_0_item_data.to_dict()
                fields.append(fields_type_0_item)

        else:
            fields = self.fields

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if nodes is not UNSET:
            field_dict["nodes"] = nodes
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_field import QueryField
        from ..models.query_node import QueryNode

        d = dict(src_dict)
        node_id = d.pop("node_id", UNSET)

        def _parse_nodes(data: object) -> list[QueryNode] | None | Unset:
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
                    nodes_type_0_item = QueryNode.from_dict(nodes_type_0_item_data)

                    nodes_type_0.append(nodes_type_0_item)

                return nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[QueryNode] | None | Unset, data)

        nodes = _parse_nodes(d.pop("nodes", UNSET))

        def _parse_fields(data: object) -> list[QueryField] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_0 = []
                _fields_type_0 = data
                for fields_type_0_item_data in _fields_type_0:
                    fields_type_0_item = QueryField.from_dict(fields_type_0_item_data)

                    fields_type_0.append(fields_type_0_item)

                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[QueryField] | None | Unset, data)

        fields = _parse_fields(d.pop("fields", UNSET))

        get_node_response = cls(
            node_id=node_id,
            nodes=nodes,
            fields=fields,
        )

        return get_node_response

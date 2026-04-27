from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.merge_operator import MergeOperator

T = TypeVar("T", bound="MergedQueryDetails")


@_attrs_define
class MergedQueryDetails:
    """Details for queries that merge two other queries to create a base select

    Attributes:
        query1_id (int | Unset): The ID of the first merged query
        query2_id (int | Unset): The ID of the second merged query
        operator (MergeOperator | Unset): The method used to merge two queries<p>Members:</p><ul><li><i>And</i> -
            Contains results that are in query A and query B; equivalent to SQL Server INTERSECT</li><li><i>Or</i> -
            Contains results that are in query A or query B; equivalent to SQL Server UNION</li><li><i>Xor</i> - Contains
            results that are in query A or query B but not both</li><li><i>Sub</i> - Contains results that are in query A
            but not query B; equivalent to SQL Server EXCEPT</li></ul>
    """

    query1_id: int | Unset = UNSET
    query2_id: int | Unset = UNSET
    operator: MergeOperator | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query1_id = self.query1_id

        query2_id = self.query2_id

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if query1_id is not UNSET:
            field_dict["query1_id"] = query1_id
        if query2_id is not UNSET:
            field_dict["query2_id"] = query2_id
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query1_id = d.pop("query1_id", UNSET)

        query2_id = d.pop("query2_id", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: MergeOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = MergeOperator(_operator)

        merged_query_details = cls(
            query1_id=query1_id,
            query2_id=query2_id,
            operator=operator,
        )

        return merged_query_details

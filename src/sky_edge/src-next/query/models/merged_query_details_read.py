from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.merge_operator import MergeOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="MergedQueryDetailsRead")


@_attrs_define
class MergedQueryDetailsRead:
    """Details for queries that merge two other queries to create a base select

    Attributes:
        query1_name (None | str | Unset): The name of the first merged query
        query2_name (None | str | Unset): The name of the second merged query
        query1_id (int | Unset): The ID of the first merged query
        query2_id (int | Unset): The ID of the second merged query
        operator (MergeOperator | Unset): The method used to merge two queries<p>Members:</p><ul><li><i>And</i> -
            Contains results that are in query A and query B; equivalent to SQL Server INTERSECT</li><li><i>Or</i> -
            Contains results that are in query A or query B; equivalent to SQL Server UNION</li><li><i>Xor</i> - Contains
            results that are in query A or query B but not both</li><li><i>Sub</i> - Contains results that are in query A
            but not query B; equivalent to SQL Server EXCEPT</li></ul>
    """

    query1_name: None | str | Unset = UNSET
    query2_name: None | str | Unset = UNSET
    query1_id: int | Unset = UNSET
    query2_id: int | Unset = UNSET
    operator: MergeOperator | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query1_name: None | str | Unset
        if isinstance(self.query1_name, Unset):
            query1_name = UNSET
        else:
            query1_name = self.query1_name

        query2_name: None | str | Unset
        if isinstance(self.query2_name, Unset):
            query2_name = UNSET
        else:
            query2_name = self.query2_name

        query1_id = self.query1_id

        query2_id = self.query2_id

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if query1_name is not UNSET:
            field_dict["query1_name"] = query1_name
        if query2_name is not UNSET:
            field_dict["query2_name"] = query2_name
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

        def _parse_query1_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query1_name = _parse_query1_name(d.pop("query1_name", UNSET))

        def _parse_query2_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query2_name = _parse_query2_name(d.pop("query2_name", UNSET))

        query1_id = d.pop("query1_id", UNSET)

        query2_id = d.pop("query2_id", UNSET)

        _operator = d.pop("operator", UNSET)
        operator: MergeOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = MergeOperator(_operator)

        merged_query_details_read = cls(
            query1_name=query1_name,
            query2_name=query2_name,
            query1_id=query1_id,
            query2_id=query2_id,
            operator=operator,
        )

        return merged_query_details_read

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter
    from ..models.output import Output
    from ..models.sort import Sort


T = TypeVar("T", bound="ListDefinition")


@_attrs_define
class ListDefinition:
    """Represents a list definition

    Attributes:
        filter_ (Filter | Unset): Filter information for a query or report execution
        output (Output | Unset): Output information for a query execution
        sort (Sort | Unset): Describes how to sort a list request
            ///
    """

    filter_: Filter | Unset = UNSET
    output: Output | Unset = UNSET
    sort: Sort | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if output is not UNSET:
            field_dict["output"] = output
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_ import Filter
        from ..models.output import Output
        from ..models.sort import Sort

        d = dict(src_dict)
        _filter_ = d.pop("filter", UNSET)
        filter_: Filter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        _output = d.pop("output", UNSET)
        output: Output | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = Output.from_dict(_output)

        _sort = d.pop("sort", UNSET)
        sort: Sort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = Sort.from_dict(_sort)

        list_definition = cls(
            filter_=filter_,
            output=output,
            sort=sort,
        )

        return list_definition

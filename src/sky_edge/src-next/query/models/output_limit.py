from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.output_limit_type import OutputLimitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputLimit")


@_attrs_define
class OutputLimit:
    """A limit on the number of rows saved for a static query

    Attributes:
        type_ (OutputLimitType | Unset): The method of limiting the number of rows for a static
            query<p>Members:</p><ul><li><i>RandomSampling</i> - A random sampling of rows</li><li><i>TopNumberRows</i> - Top
            n rows</li><li><i>TopPercentRows</i> - Top n% of rows</li></ul>
        limit (int | Unset): The number or percent of rows to save (depending on the specified OutputLimitType)
    """

    type_: OutputLimitType | Unset = UNSET
    limit: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: OutputLimitType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OutputLimitType(_type_)

        limit = d.pop("limit", UNSET)

        output_limit = cls(
            type_=type_,
            limit=limit,
        )

        return output_limit

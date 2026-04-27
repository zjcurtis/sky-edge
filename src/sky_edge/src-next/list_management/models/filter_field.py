from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.filter_field_filter_operator import FilterFieldFilterOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field_value import FilterFieldValue


T = TypeVar("T", bound="FilterField")


@_attrs_define
class FilterField:
    """Represents filter information for a specific field

    Attributes:
        value (FilterFieldValue | Unset): Represents the value for a filter field
        field_id (None | str | Unset): The identifier of the field the filter applies to
        operator (FilterFieldFilterOperator | Unset): The operator for the filter
        is_aggregate (bool | None | Unset): Determines if the filter is an aggregate filter
    """

    value: FilterFieldValue | Unset = UNSET
    field_id: None | str | Unset = UNSET
    operator: FilterFieldFilterOperator | Unset = UNSET
    is_aggregate: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_id: None | str | Unset
        if isinstance(self.field_id, Unset):
            field_id = UNSET
        else:
            field_id = self.field_id

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        is_aggregate: bool | None | Unset
        if isinstance(self.is_aggregate, Unset):
            is_aggregate = UNSET
        else:
            is_aggregate = self.is_aggregate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if field_id is not UNSET:
            field_dict["field_id"] = field_id
        if operator is not UNSET:
            field_dict["operator"] = operator
        if is_aggregate is not UNSET:
            field_dict["is_aggregate"] = is_aggregate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_field_value import FilterFieldValue

        d = dict(src_dict)
        _value = d.pop("value", UNSET)
        value: FilterFieldValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = FilterFieldValue.from_dict(_value)

        def _parse_field_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_id = _parse_field_id(d.pop("field_id", UNSET))

        _operator = d.pop("operator", UNSET)
        operator: FilterFieldFilterOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FilterFieldFilterOperator(_operator)

        def _parse_is_aggregate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_aggregate = _parse_is_aggregate(d.pop("is_aggregate", UNSET))

        filter_field = cls(
            value=value,
            field_id=field_id,
            operator=operator,
            is_aggregate=is_aggregate,
        )

        return filter_field

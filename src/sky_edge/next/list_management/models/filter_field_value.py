from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="FilterFieldValue")


@_attrs_define
class FilterFieldValue:
    """Represents the value for a filter field

    Attributes:
        value (Any | Unset): The value for the filter
        label (None | str | Unset): An optional label associated with the
            Blackbaud.ListPlatform.Contracts.FilterFieldValue
    """

    value: Any | Unset = UNSET
    label: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        filter_field_value = cls(
            value=value,
            label=label,
        )

        return filter_field_value

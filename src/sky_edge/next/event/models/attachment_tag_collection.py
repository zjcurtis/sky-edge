from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="AttachmentTagCollection")


@_attrs_define
class AttachmentTagCollection:
    """Defines a collection of attachment tags.

    Attributes:
        count (int | Unset): The total number of items in the collection before limit/offset.
        value (list[str] | None | Unset): The set of items included in the response. This may be a subset of the items
            in the collection.
    """

    count: int | Unset = UNSET
    value: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        value: list[str] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_value(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = cast(list[str], data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        attachment_tag_collection = cls(
            count=count,
            value=value,
        )

        return attachment_tag_collection

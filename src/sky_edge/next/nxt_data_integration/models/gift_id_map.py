from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="GiftIdMap")


@_attrs_define
class GiftIdMap:
    """A mapping between a system record ID and a gift ID.

    Attributes:
        gift_id (None | str | Unset): The gift ID.
        system_record_id (int | Unset): The system record ID.
    """

    gift_id: None | str | Unset = UNSET
    system_record_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_id: None | str | Unset
        if isinstance(self.gift_id, Unset):
            gift_id = UNSET
        else:
            gift_id = self.gift_id

        system_record_id = self.system_record_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if system_record_id is not UNSET:
            field_dict["system_record_id"] = system_record_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_id = _parse_gift_id(d.pop("gift_id", UNSET))

        system_record_id = d.pop("system_record_id", UNSET)

        gift_id_map = cls(
            gift_id=gift_id,
            system_record_id=system_record_id,
        )

        return gift_id_map

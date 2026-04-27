from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.gift_tribute_edit_acknowledge_status import (
    GiftTributeEditAcknowledgeStatus,
)

T = TypeVar("T", bound="GiftTributeEdit")


@_attrs_define
class GiftTributeEdit:
    """Represents the editable properties of a Gift Tribute record in Raiser's Edge.

    Attributes:
        tribute_type (int | None | Unset): The tribute type.
        acknowledge (GiftTributeEditAcknowledgeStatus | Unset): The gift tribute acknowledge status.
    """

    tribute_type: int | None | Unset = UNSET
    acknowledge: GiftTributeEditAcknowledgeStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tribute_type: int | None | Unset
        if isinstance(self.tribute_type, Unset):
            tribute_type = UNSET
        else:
            tribute_type = self.tribute_type

        acknowledge: str | Unset = UNSET
        if not isinstance(self.acknowledge, Unset):
            acknowledge = self.acknowledge.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tribute_type is not UNSET:
            field_dict["tribute_type"] = tribute_type
        if acknowledge is not UNSET:
            field_dict["acknowledge"] = acknowledge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_tribute_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tribute_type = _parse_tribute_type(d.pop("tribute_type", UNSET))

        _acknowledge = d.pop("acknowledge", UNSET)
        acknowledge: GiftTributeEditAcknowledgeStatus | Unset
        if isinstance(_acknowledge, Unset):
            acknowledge = UNSET
        else:
            acknowledge = GiftTributeEditAcknowledgeStatus(_acknowledge)

        gift_tribute_edit = cls(
            tribute_type=tribute_type,
            acknowledge=acknowledge,
        )

        return gift_tribute_edit

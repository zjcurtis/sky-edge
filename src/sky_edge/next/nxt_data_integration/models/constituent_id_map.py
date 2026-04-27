from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.constituent_id_map_fundraiser_status import (
    ConstituentIdMapFundraiserStatus,
)

T = TypeVar("T", bound="ConstituentIdMap")


@_attrs_define
class ConstituentIdMap:
    """A mapping between a system record ID and a constituent ID.

    Attributes:
        constituent_id (None | str | Unset): The constituent ID.
        system_record_id (int | Unset): The system record ID.
        fundraiser_status (ConstituentIdMapFundraiserStatus | Unset): The fundraiser status.
    """

    constituent_id: None | str | Unset = UNSET
    system_record_id: int | Unset = UNSET
    fundraiser_status: ConstituentIdMapFundraiserStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        system_record_id = self.system_record_id

        fundraiser_status: str | Unset = UNSET
        if not isinstance(self.fundraiser_status, Unset):
            fundraiser_status = self.fundraiser_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if system_record_id is not UNSET:
            field_dict["system_record_id"] = system_record_id
        if fundraiser_status is not UNSET:
            field_dict["fundraiser_status"] = fundraiser_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        system_record_id = d.pop("system_record_id", UNSET)

        _fundraiser_status = d.pop("fundraiser_status", UNSET)
        fundraiser_status: ConstituentIdMapFundraiserStatus | Unset
        if isinstance(_fundraiser_status, Unset):
            fundraiser_status = UNSET
        else:
            fundraiser_status = ConstituentIdMapFundraiserStatus(_fundraiser_status)

        constituent_id_map = cls(
            constituent_id=constituent_id,
            system_record_id=system_record_id,
            fundraiser_status=fundraiser_status,
        )

        return constituent_id_map

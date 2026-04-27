from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CreatedBatch")


@_attrs_define
class CreatedBatch:
    """Defines fields returned when a batch is created

    Attributes:
        batch_id (None | str | Unset): The immutable system record ID of the created batch.
    """

    batch_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        created_batch = cls(
            batch_id=batch_id,
        )

        return created_batch

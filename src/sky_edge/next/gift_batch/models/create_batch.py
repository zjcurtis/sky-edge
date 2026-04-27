from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="CreateBatch")


@_attrs_define
class CreateBatch:
    """Defines fields for a batch to be added to the data store

    Attributes:
        batch_description (None | str | Unset): The description of the batch.
        batch_number (None | str | Unset): The unique ID specific to the batch.
        expected_batch_total (float | None | Unset): The total value of all gifts the batch is expected to contain.
        expected_number (int | None | Unset): The total number of gifts the batch is expected to contain.
    """

    batch_description: None | str | Unset = UNSET
    batch_number: None | str | Unset = UNSET
    expected_batch_total: float | None | Unset = UNSET
    expected_number: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        batch_description: None | str | Unset
        if isinstance(self.batch_description, Unset):
            batch_description = UNSET
        else:
            batch_description = self.batch_description

        batch_number: None | str | Unset
        if isinstance(self.batch_number, Unset):
            batch_number = UNSET
        else:
            batch_number = self.batch_number

        expected_batch_total: float | None | Unset
        if isinstance(self.expected_batch_total, Unset):
            expected_batch_total = UNSET
        else:
            expected_batch_total = self.expected_batch_total

        expected_number: int | None | Unset
        if isinstance(self.expected_number, Unset):
            expected_number = UNSET
        else:
            expected_number = self.expected_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if batch_description is not UNSET:
            field_dict["batch_description"] = batch_description
        if batch_number is not UNSET:
            field_dict["batch_number"] = batch_number
        if expected_batch_total is not UNSET:
            field_dict["expected_batch_total"] = expected_batch_total
        if expected_number is not UNSET:
            field_dict["expected_number"] = expected_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_batch_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_description = _parse_batch_description(d.pop("batch_description", UNSET))

        def _parse_batch_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_number = _parse_batch_number(d.pop("batch_number", UNSET))

        def _parse_expected_batch_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        expected_batch_total = _parse_expected_batch_total(
            d.pop("expected_batch_total", UNSET)
        )

        def _parse_expected_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_number = _parse_expected_number(d.pop("expected_number", UNSET))

        create_batch = cls(
            batch_description=batch_description,
            batch_number=batch_number,
            expected_batch_total=expected_batch_total,
            expected_number=expected_number,
        )

        return create_batch

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="GiftBatchGiftError")


@_attrs_define
class GiftBatchGiftError:
    """Represents a batch

    Attributes:
        affected_field (str | Unset): The field affected by the error
        batch_id (str | Unset): The immutable system record ID of the batch
        exception_error_code (int | Unset): The exception error code
        exception_error_message (str | Unset): The exception error message
        exception_error_name (str | Unset): The exception error name
        gift_id (str | Unset): The immutable system record ID of the gift
        lookup_id (str | Unset): The user-defined identifier for the gift.
    """

    affected_field: str | Unset = UNSET
    batch_id: str | Unset = UNSET
    exception_error_code: int | Unset = UNSET
    exception_error_message: str | Unset = UNSET
    exception_error_name: str | Unset = UNSET
    gift_id: str | Unset = UNSET
    lookup_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affected_field = self.affected_field

        batch_id = self.batch_id

        exception_error_code = self.exception_error_code

        exception_error_message = self.exception_error_message

        exception_error_name = self.exception_error_name

        gift_id = self.gift_id

        lookup_id = self.lookup_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if affected_field is not UNSET:
            field_dict["affected_field"] = affected_field
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if exception_error_code is not UNSET:
            field_dict["exception_error_code"] = exception_error_code
        if exception_error_message is not UNSET:
            field_dict["exception_error_message"] = exception_error_message
        if exception_error_name is not UNSET:
            field_dict["exception_error_name"] = exception_error_name
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        affected_field = d.pop("affected_field", UNSET)

        batch_id = d.pop("batch_id", UNSET)

        exception_error_code = d.pop("exception_error_code", UNSET)

        exception_error_message = d.pop("exception_error_message", UNSET)

        exception_error_name = d.pop("exception_error_name", UNSET)

        gift_id = d.pop("gift_id", UNSET)

        lookup_id = d.pop("lookup_id", UNSET)

        gift_batch_gift_error = cls(
            affected_field=affected_field,
            batch_id=batch_id,
            exception_error_code=exception_error_code,
            exception_error_message=exception_error_message,
            exception_error_name=exception_error_name,
            gift_id=gift_id,
            lookup_id=lookup_id,
        )

        gift_batch_gift_error.additional_properties = d
        return gift_batch_gift_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

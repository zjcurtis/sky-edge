from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_gift_read import BatchGiftRead
    from ..models.gift_batch_gift_error import GiftBatchGiftError


T = TypeVar("T", bound="BatchGiftAddResults")


@_attrs_define
class BatchGiftAddResults:
    """Contains a collection of batch gift error records and the batch gifts that the operation added

    Attributes:
        errors (list[GiftBatchGiftError] | Unset): The batch gift errors associated with the batch gift add operation
        gifts (list[BatchGiftRead] | Unset): The collection of batch gifts that were added by the batch gift add
            operation
    """

    errors: list[GiftBatchGiftError] | Unset = UNSET
    gifts: list[BatchGiftRead] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        gifts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gifts, Unset):
            gifts = []
            for gifts_item_data in self.gifts:
                gifts_item = gifts_item_data.to_dict()
                gifts.append(gifts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if gifts is not UNSET:
            field_dict["gifts"] = gifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_gift_read import BatchGiftRead
        from ..models.gift_batch_gift_error import GiftBatchGiftError

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[GiftBatchGiftError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = GiftBatchGiftError.from_dict(errors_item_data)

                errors.append(errors_item)

        _gifts = d.pop("gifts", UNSET)
        gifts: list[BatchGiftRead] | Unset = UNSET
        if _gifts is not UNSET:
            gifts = []
            for gifts_item_data in _gifts:
                gifts_item = BatchGiftRead.from_dict(gifts_item_data)

                gifts.append(gifts_item)

        batch_gift_add_results = cls(
            errors=errors,
            gifts=gifts,
        )

        batch_gift_add_results.additional_properties = d
        return batch_gift_add_results

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

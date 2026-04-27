from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_gift_add import BatchGiftAdd
    from ..models.gift_validation_error import GiftValidationError


T = TypeVar("T", bound="AddGiftsToBatchResult")


@_attrs_define
class AddGiftsToBatchResult:
    """The result of add gifts to batch operation.

    Attributes:
        added_batch_gifts (list[BatchGiftAdd] | None | Unset): List of added batch gifts
        gift_validation_errors (list[GiftValidationError] | None | Unset): List of gift validation errors
    """

    added_batch_gifts: list[BatchGiftAdd] | None | Unset = UNSET
    gift_validation_errors: list[GiftValidationError] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        added_batch_gifts: list[dict[str, Any]] | None | Unset
        if isinstance(self.added_batch_gifts, Unset):
            added_batch_gifts = UNSET
        elif isinstance(self.added_batch_gifts, list):
            added_batch_gifts = []
            for added_batch_gifts_type_0_item_data in self.added_batch_gifts:
                added_batch_gifts_type_0_item = (
                    added_batch_gifts_type_0_item_data.to_dict()
                )
                added_batch_gifts.append(added_batch_gifts_type_0_item)

        else:
            added_batch_gifts = self.added_batch_gifts

        gift_validation_errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.gift_validation_errors, Unset):
            gift_validation_errors = UNSET
        elif isinstance(self.gift_validation_errors, list):
            gift_validation_errors = []
            for gift_validation_errors_type_0_item_data in self.gift_validation_errors:
                gift_validation_errors_type_0_item = (
                    gift_validation_errors_type_0_item_data.to_dict()
                )
                gift_validation_errors.append(gift_validation_errors_type_0_item)

        else:
            gift_validation_errors = self.gift_validation_errors

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if added_batch_gifts is not UNSET:
            field_dict["added_batch_gifts"] = added_batch_gifts
        if gift_validation_errors is not UNSET:
            field_dict["gift_validation_errors"] = gift_validation_errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_gift_add import BatchGiftAdd
        from ..models.gift_validation_error import GiftValidationError

        d = dict(src_dict)

        def _parse_added_batch_gifts(data: object) -> list[BatchGiftAdd] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                added_batch_gifts_type_0 = []
                _added_batch_gifts_type_0 = data
                for added_batch_gifts_type_0_item_data in _added_batch_gifts_type_0:
                    added_batch_gifts_type_0_item = BatchGiftAdd.from_dict(
                        added_batch_gifts_type_0_item_data
                    )

                    added_batch_gifts_type_0.append(added_batch_gifts_type_0_item)

                return added_batch_gifts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftAdd] | None | Unset, data)

        added_batch_gifts = _parse_added_batch_gifts(d.pop("added_batch_gifts", UNSET))

        def _parse_gift_validation_errors(
            data: object,
        ) -> list[GiftValidationError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gift_validation_errors_type_0 = []
                _gift_validation_errors_type_0 = data
                for (
                    gift_validation_errors_type_0_item_data
                ) in _gift_validation_errors_type_0:
                    gift_validation_errors_type_0_item = GiftValidationError.from_dict(
                        gift_validation_errors_type_0_item_data
                    )

                    gift_validation_errors_type_0.append(
                        gift_validation_errors_type_0_item
                    )

                return gift_validation_errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftValidationError] | None | Unset, data)

        gift_validation_errors = _parse_gift_validation_errors(
            d.pop("gift_validation_errors", UNSET)
        )

        add_gifts_to_batch_result = cls(
            added_batch_gifts=added_batch_gifts,
            gift_validation_errors=gift_validation_errors,
        )

        return add_gifts_to_batch_result

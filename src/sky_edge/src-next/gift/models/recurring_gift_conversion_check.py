from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recurring_gift_conversion_error import RecurringGiftConversionError


T = TypeVar("T", bound="RecurringGiftConversionCheck")


@_attrs_define
class RecurringGiftConversionCheck:
    """The result of a recurring gift conversion check.  This indicates if a recurring gift can be converted to an
    automated recurring gift.

        Attributes:
            can_be_converted (bool | Unset): Indicates if the gift can be converted to an automated recurring gift.
            token_will_be_required (bool | Unset): Indicates if a token will be required to an automated recurring gift.
            gift_id (str | Unset): The immutable system record ID of the gift.
            errors (list[RecurringGiftConversionError] | Unset): The collection of errors explaining why the gift cannot be
                converted to automated, if it cannot be.
    """

    can_be_converted: bool | Unset = UNSET
    token_will_be_required: bool | Unset = UNSET
    gift_id: str | Unset = UNSET
    errors: list[RecurringGiftConversionError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_be_converted = self.can_be_converted

        token_will_be_required = self.token_will_be_required

        gift_id = self.gift_id

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_be_converted is not UNSET:
            field_dict["can_be_converted"] = can_be_converted
        if token_will_be_required is not UNSET:
            field_dict["token_will_be_required"] = token_will_be_required
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recurring_gift_conversion_error import RecurringGiftConversionError

        d = dict(src_dict)
        can_be_converted = d.pop("can_be_converted", UNSET)

        token_will_be_required = d.pop("token_will_be_required", UNSET)

        gift_id = d.pop("gift_id", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[RecurringGiftConversionError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = RecurringGiftConversionError.from_dict(errors_item_data)

                errors.append(errors_item)

        recurring_gift_conversion_check = cls(
            can_be_converted=can_be_converted,
            token_will_be_required=token_will_be_required,
            gift_id=gift_id,
            errors=errors,
        )

        recurring_gift_conversion_check.additional_properties = d
        return recurring_gift_conversion_check

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

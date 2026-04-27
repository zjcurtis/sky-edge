from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.gift_validation_error_invalid_input_error_code import GiftValidationErrorInvalidInputErrorCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftValidationError")


@_attrs_define
class GiftValidationError:
    """An error with a gift.

    Attributes:
        gift_id (None | Unset | UUID): The ID of the gift.
        legacy_gift_id (None | str | Unset): The Legacy ID of the gift.
        lookup_id (None | str | Unset): The lookup ID of the gift.
        error_code (GiftValidationErrorInvalidInputErrorCode | Unset): Error codes for invalid input
        error_message (None | str | Unset): The validation error message.
        affected_field (None | str | Unset): The field of the gift which failed validation.
        exception_error_name (None | str | Unset): The name of the validation exception.
        exception (Any | Unset): The validation exception.
        hard_exception (bool | None | Unset): Indicates if this is a hard exception.
        batch_id (None | str | Unset): The ID of the batch for when this exception is for a batch gift.
    """

    gift_id: None | Unset | UUID = UNSET
    legacy_gift_id: None | str | Unset = UNSET
    lookup_id: None | str | Unset = UNSET
    error_code: GiftValidationErrorInvalidInputErrorCode | Unset = UNSET
    error_message: None | str | Unset = UNSET
    affected_field: None | str | Unset = UNSET
    exception_error_name: None | str | Unset = UNSET
    exception: Any | Unset = UNSET
    hard_exception: bool | None | Unset = UNSET
    batch_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_id: None | str | Unset
        if isinstance(self.gift_id, Unset):
            gift_id = UNSET
        elif isinstance(self.gift_id, UUID):
            gift_id = str(self.gift_id)
        else:
            gift_id = self.gift_id

        legacy_gift_id: None | str | Unset
        if isinstance(self.legacy_gift_id, Unset):
            legacy_gift_id = UNSET
        else:
            legacy_gift_id = self.legacy_gift_id

        lookup_id: None | str | Unset
        if isinstance(self.lookup_id, Unset):
            lookup_id = UNSET
        else:
            lookup_id = self.lookup_id

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        affected_field: None | str | Unset
        if isinstance(self.affected_field, Unset):
            affected_field = UNSET
        else:
            affected_field = self.affected_field

        exception_error_name: None | str | Unset
        if isinstance(self.exception_error_name, Unset):
            exception_error_name = UNSET
        else:
            exception_error_name = self.exception_error_name

        exception = self.exception

        hard_exception: bool | None | Unset
        if isinstance(self.hard_exception, Unset):
            hard_exception = UNSET
        else:
            hard_exception = self.hard_exception

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if legacy_gift_id is not UNSET:
            field_dict["legacy_gift_id"] = legacy_gift_id
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if affected_field is not UNSET:
            field_dict["affected_field"] = affected_field
        if exception_error_name is not UNSET:
            field_dict["exception_error_name"] = exception_error_name
        if exception is not UNSET:
            field_dict["exception"] = exception
        if hard_exception is not UNSET:
            field_dict["hard_exception"] = hard_exception
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_gift_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gift_id_type_0 = UUID(data)

                return gift_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        gift_id = _parse_gift_id(d.pop("gift_id", UNSET))

        def _parse_legacy_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legacy_gift_id = _parse_legacy_gift_id(d.pop("legacy_gift_id", UNSET))

        def _parse_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lookup_id = _parse_lookup_id(d.pop("lookup_id", UNSET))

        _error_code = d.pop("error_code", UNSET)
        error_code: GiftValidationErrorInvalidInputErrorCode | Unset
        if isinstance(_error_code, Unset):
            error_code = UNSET
        else:
            error_code = GiftValidationErrorInvalidInputErrorCode(_error_code)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_affected_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        affected_field = _parse_affected_field(d.pop("affected_field", UNSET))

        def _parse_exception_error_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception_error_name = _parse_exception_error_name(d.pop("exception_error_name", UNSET))

        exception = d.pop("exception", UNSET)

        def _parse_hard_exception(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        hard_exception = _parse_hard_exception(d.pop("hard_exception", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        gift_validation_error = cls(
            gift_id=gift_id,
            legacy_gift_id=legacy_gift_id,
            lookup_id=lookup_id,
            error_code=error_code,
            error_message=error_message,
            affected_field=affected_field,
            exception_error_name=exception_error_name,
            exception=exception,
            hard_exception=hard_exception,
            batch_id=batch_id,
        )

        return gift_validation_error

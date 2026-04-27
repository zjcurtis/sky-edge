from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchGiftErrorRecord")


@_attrs_define
class BatchGiftErrorRecord:
    """A validation error for a batch gift

    Attributes:
        id (None | str | Unset): ID of the error record. Read Only.
        gift_id (None | str | Unset): The identifier of the gift
        batch_id (None | str | Unset): The identifier of the batch
        lookup_id (None | str | Unset): The lookup identifier for the gift
        exception_error_name (None | str | Unset): The batch gift error name
        exception_error_code (int | None | Unset): The batch gift exception error code
        exception_error_message (None | str | Unset): The batch gift exception error message
        affected_field (None | str | Unset): The batch gift field where the error occurred
    """

    id: None | str | Unset = UNSET
    gift_id: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    lookup_id: None | str | Unset = UNSET
    exception_error_name: None | str | Unset = UNSET
    exception_error_code: int | None | Unset = UNSET
    exception_error_message: None | str | Unset = UNSET
    affected_field: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        gift_id: None | str | Unset
        if isinstance(self.gift_id, Unset):
            gift_id = UNSET
        else:
            gift_id = self.gift_id

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        lookup_id: None | str | Unset
        if isinstance(self.lookup_id, Unset):
            lookup_id = UNSET
        else:
            lookup_id = self.lookup_id

        exception_error_name: None | str | Unset
        if isinstance(self.exception_error_name, Unset):
            exception_error_name = UNSET
        else:
            exception_error_name = self.exception_error_name

        exception_error_code: int | None | Unset
        if isinstance(self.exception_error_code, Unset):
            exception_error_code = UNSET
        else:
            exception_error_code = self.exception_error_code

        exception_error_message: None | str | Unset
        if isinstance(self.exception_error_message, Unset):
            exception_error_message = UNSET
        else:
            exception_error_message = self.exception_error_message

        affected_field: None | str | Unset
        if isinstance(self.affected_field, Unset):
            affected_field = UNSET
        else:
            affected_field = self.affected_field

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if exception_error_name is not UNSET:
            field_dict["exception_error_name"] = exception_error_name
        if exception_error_code is not UNSET:
            field_dict["exception_error_code"] = exception_error_code
        if exception_error_message is not UNSET:
            field_dict["exception_error_message"] = exception_error_message
        if affected_field is not UNSET:
            field_dict["affected_field"] = affected_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_id = _parse_gift_id(d.pop("gift_id", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        def _parse_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lookup_id = _parse_lookup_id(d.pop("lookup_id", UNSET))

        def _parse_exception_error_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception_error_name = _parse_exception_error_name(d.pop("exception_error_name", UNSET))

        def _parse_exception_error_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exception_error_code = _parse_exception_error_code(d.pop("exception_error_code", UNSET))

        def _parse_exception_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exception_error_message = _parse_exception_error_message(d.pop("exception_error_message", UNSET))

        def _parse_affected_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        affected_field = _parse_affected_field(d.pop("affected_field", UNSET))

        batch_gift_error_record = cls(
            id=id,
            gift_id=gift_id,
            batch_id=batch_id,
            lookup_id=lookup_id,
            exception_error_name=exception_error_name,
            exception_error_code=exception_error_code,
            exception_error_message=exception_error_message,
            affected_field=affected_field,
        )

        return batch_gift_error_record

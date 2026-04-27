from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceError")


@_attrs_define
class ServiceError:
    """Base service error contract.

    Attributes:
        message (None | str | Unset): The message of the service error with any string arguments replaced.
        error_name (None | str | Unset): The name of the service error.
        error_code (int | Unset): Code number of the service error.
        raw_message (None | str | Unset): The raw message of the service error. This message may contain string
            replacement arguments (ie: {0}, {1}, etc) that map to the 'error_args' property and will be replaced when you
            get the full message from the 'message' property.
        error_args (list[str] | None | Unset): A list of arguments to be replaced in the raw message. Useful for when
            the message needs to be localized.
    """

    message: None | str | Unset = UNSET
    error_name: None | str | Unset = UNSET
    error_code: int | Unset = UNSET
    raw_message: None | str | Unset = UNSET
    error_args: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        error_name: None | str | Unset
        if isinstance(self.error_name, Unset):
            error_name = UNSET
        else:
            error_name = self.error_name

        error_code = self.error_code

        raw_message: None | str | Unset
        if isinstance(self.raw_message, Unset):
            raw_message = UNSET
        else:
            raw_message = self.raw_message

        error_args: list[str] | None | Unset
        if isinstance(self.error_args, Unset):
            error_args = UNSET
        elif isinstance(self.error_args, list):
            error_args = self.error_args

        else:
            error_args = self.error_args

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if error_name is not UNSET:
            field_dict["error_name"] = error_name
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if raw_message is not UNSET:
            field_dict["raw_message"] = raw_message
        if error_args is not UNSET:
            field_dict["error_args"] = error_args

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_error_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_name = _parse_error_name(d.pop("error_name", UNSET))

        error_code = d.pop("error_code", UNSET)

        def _parse_raw_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        raw_message = _parse_raw_message(d.pop("raw_message", UNSET))

        def _parse_error_args(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                error_args_type_0 = cast(list[str], data)

                return error_args_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        error_args = _parse_error_args(d.pop("error_args", UNSET))

        service_error = cls(
            message=message,
            error_name=error_name,
            error_code=error_code,
            raw_message=raw_message,
            error_args=error_args,
        )

        return service_error

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ExtensionException")


@_attrs_define
class ExtensionException:
    """A validation exception for an extension.

    Attributes:
        error_message (None | str | Unset): The error message describing the validation failure.
        affected_field (None | str | Unset): The JSON path of the field that caused the validation failure.
    """

    error_message: None | str | Unset = UNSET
    affected_field: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if affected_field is not UNSET:
            field_dict["affected_field"] = affected_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        extension_exception = cls(
            error_message=error_message,
            affected_field=affected_field,
        )

        return extension_exception

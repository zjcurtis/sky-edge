from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditParticipantOption")


@_attrs_define
class EditParticipantOption:
    """A participant option

    Attributes:
        option_value (None | str | Unset): The participant's response to the option.
    """

    option_value: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        option_value: None | str | Unset
        if isinstance(self.option_value, Unset):
            option_value = UNSET
        else:
            option_value = self.option_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if option_value is not UNSET:
            field_dict["option_value"] = option_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_option_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        option_value = _parse_option_value(d.pop("option_value", UNSET))

        edit_participant_option = cls(
            option_value=option_value,
        )

        return edit_participant_option

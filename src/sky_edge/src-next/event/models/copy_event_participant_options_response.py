from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyEventParticipantOptionsResponse")


@_attrs_define
class CopyEventParticipantOptionsResponse:
    """Response for copy event participant options.

    Attributes:
        event_participant_option_ids (list[str] | None | Unset): List of Ids from the new event participant options.
    """

    event_participant_option_ids: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        event_participant_option_ids: list[str] | None | Unset
        if isinstance(self.event_participant_option_ids, Unset):
            event_participant_option_ids = UNSET
        elif isinstance(self.event_participant_option_ids, list):
            event_participant_option_ids = self.event_participant_option_ids

        else:
            event_participant_option_ids = self.event_participant_option_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if event_participant_option_ids is not UNSET:
            field_dict["event_participant_option_ids"] = event_participant_option_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_event_participant_option_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                event_participant_option_ids_type_0 = cast(list[str], data)

                return event_participant_option_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        event_participant_option_ids = _parse_event_participant_option_ids(d.pop("event_participant_option_ids", UNSET))

        copy_event_participant_options_response = cls(
            event_participant_option_ids=event_participant_option_ids,
        )

        return copy_event_participant_options_response

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CopyEventParticipantOptionsRequest")


@_attrs_define
class CopyEventParticipantOptionsRequest:
    """Request participant options to copy from one event to another event.

    Attributes:
        source_event_id (str): The ID of the event to copy participant options from.
        target_event_id (str): The ID of the event to copy participant options to.
    """

    source_event_id: str
    target_event_id: str

    def to_dict(self) -> dict[str, Any]:
        source_event_id = self.source_event_id

        target_event_id = self.target_event_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source_event_id": source_event_id,
                "target_event_id": target_event_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_event_id = d.pop("source_event_id")

        target_event_id = d.pop("target_event_id")

        copy_event_participant_options_request = cls(
            source_event_id=source_event_id,
            target_event_id=target_event_id,
        )

        return copy_event_participant_options_request

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateParticipantOption")


@_attrs_define
class CreateParticipantOption:
    """Participant options are the responses to an event participant option.

    Attributes:
        event_participant_option_id (str): The ID of the event participant option.
        option_value (str): The participant's response to the option.
    """

    event_participant_option_id: str
    option_value: str

    def to_dict(self) -> dict[str, Any]:
        event_participant_option_id = self.event_participant_option_id

        option_value = self.option_value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "event_participant_option_id": event_participant_option_id,
                "option_value": option_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_participant_option_id = d.pop("event_participant_option_id")

        option_value = d.pop("option_value")

        create_participant_option = cls(
            event_participant_option_id=event_participant_option_id,
            option_value=option_value,
        )

        return create_participant_option

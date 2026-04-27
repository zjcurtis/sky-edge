from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditParticipantSeating")


@_attrs_define
class EditParticipantSeating:
    """A participant's seat is their seating assignment for an event.

    Attributes:
        seat (None | str | Unset): The seat assigned to the participant.
        seating_group (None | str | Unset): The grouping details of the participant's seat.
        seating_notes (None | str | Unset): Any additional notes or instructions related to the seat assigned to the
            participant.
    """

    seat: None | str | Unset = UNSET
    seating_group: None | str | Unset = UNSET
    seating_notes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        seat: None | str | Unset
        if isinstance(self.seat, Unset):
            seat = UNSET
        else:
            seat = self.seat

        seating_group: None | str | Unset
        if isinstance(self.seating_group, Unset):
            seating_group = UNSET
        else:
            seating_group = self.seating_group

        seating_notes: None | str | Unset
        if isinstance(self.seating_notes, Unset):
            seating_notes = UNSET
        else:
            seating_notes = self.seating_notes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if seat is not UNSET:
            field_dict["seat"] = seat
        if seating_group is not UNSET:
            field_dict["seating_group"] = seating_group
        if seating_notes is not UNSET:
            field_dict["seating_notes"] = seating_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_seat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seat = _parse_seat(d.pop("seat", UNSET))

        def _parse_seating_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seating_group = _parse_seating_group(d.pop("seating_group", UNSET))

        def _parse_seating_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seating_notes = _parse_seating_notes(d.pop("seating_notes", UNSET))

        edit_participant_seating = cls(
            seat=seat,
            seating_group=seating_group,
            seating_notes=seating_notes,
        )

        return edit_participant_seating

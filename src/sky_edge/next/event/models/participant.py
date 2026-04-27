from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.participant_invitation_status import ParticipantInvitationStatus
from ..models.participant_rsvp_status import ParticipantRsvpStatus

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate
    from ..models.participation_level import ParticipationLevel


T = TypeVar("T", bound="Participant")


@_attrs_define
class Participant:
    """Participants are individuals or organizations who engage with the organization through an event.
    They can include constituents who receive invitations or register for the event.

        Attributes:
            id (None | str | Unset): The ID of the participant.
            constituent_id (None | str | Unset): The constituent ID or contact ID of the participant, including non-
                constituent IDs.
            event_id (None | str | Unset): ID of the event being attended.
            date_added (datetime.datetime | Unset): The date when the participant was created. Uses<a
                href="https://tools.ietf.org/html/rfc3339"> ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the participant was last modified. Uses<a
                href="https://tools.ietf.org/html/rfc3339"> ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
            host_id (None | str | Unset): The ID of the host's participant record.
            rsvp_status (ParticipantRsvpStatus | Unset): The status of the participant's engagement with the
                event.<p>Available values:</p><ul><li><i>NoResponse</i> - No response.</li><li><i>Attending</i> -
                Attending.</li><li><i>Declined</i> - Declined.</li><li><i>Interested</i> - Interested.</li><li><i>Canceled</i> -
                Canceled.</li><li><i>Waitlisted</i> - Waitlisted.</li><li><i>NotApplicable</i> - Not applicable.</li></ul>
            attended (bool | Unset): Whether the participant attended the event.
            invitation_status (ParticipantInvitationStatus | Unset): The status of the invitation to the
                participant.<p>Available values:</p><ul><li><i>NotApplicable</i> - Not applicable.</li><li><i>NotInvited</i> -
                Not invited.</li><li><i>Invited</i> - Invited.</li></ul>
            rsvp_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            invitation_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            participation_level (ParticipationLevel | Unset): Participation levels are the level of involvement participants
                have in an event.
            summary_note (None | str | Unset): Quick reference information pinned to the participant's record.
    """

    id: None | str | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    event_id: None | str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    host_id: None | str | Unset = UNSET
    rsvp_status: ParticipantRsvpStatus | Unset = UNSET
    attended: bool | Unset = UNSET
    invitation_status: ParticipantInvitationStatus | Unset = UNSET
    rsvp_date: FuzzyDate | Unset = UNSET
    invitation_date: FuzzyDate | Unset = UNSET
    participation_level: ParticipationLevel | Unset = UNSET
    summary_note: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        event_id: None | str | Unset
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        else:
            event_id = self.event_id

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        host_id: None | str | Unset
        if isinstance(self.host_id, Unset):
            host_id = UNSET
        else:
            host_id = self.host_id

        rsvp_status: str | Unset = UNSET
        if not isinstance(self.rsvp_status, Unset):
            rsvp_status = self.rsvp_status.value

        attended = self.attended

        invitation_status: str | Unset = UNSET
        if not isinstance(self.invitation_status, Unset):
            invitation_status = self.invitation_status.value

        rsvp_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rsvp_date, Unset):
            rsvp_date = self.rsvp_date.to_dict()

        invitation_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.invitation_date, Unset):
            invitation_date = self.invitation_date.to_dict()

        participation_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participation_level, Unset):
            participation_level = self.participation_level.to_dict()

        summary_note: None | str | Unset
        if isinstance(self.summary_note, Unset):
            summary_note = UNSET
        else:
            summary_note = self.summary_note

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if host_id is not UNSET:
            field_dict["host_id"] = host_id
        if rsvp_status is not UNSET:
            field_dict["rsvp_status"] = rsvp_status
        if attended is not UNSET:
            field_dict["attended"] = attended
        if invitation_status is not UNSET:
            field_dict["invitation_status"] = invitation_status
        if rsvp_date is not UNSET:
            field_dict["rsvp_date"] = rsvp_date
        if invitation_date is not UNSET:
            field_dict["invitation_date"] = invitation_date
        if participation_level is not UNSET:
            field_dict["participation_level"] = participation_level
        if summary_note is not UNSET:
            field_dict["summary_note"] = summary_note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate
        from ..models.participation_level import ParticipationLevel

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_event_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_id = _parse_event_id(d.pop("event_id", UNSET))

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        def _parse_host_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_id = _parse_host_id(d.pop("host_id", UNSET))

        _rsvp_status = d.pop("rsvp_status", UNSET)
        rsvp_status: ParticipantRsvpStatus | Unset
        if isinstance(_rsvp_status, Unset):
            rsvp_status = UNSET
        else:
            rsvp_status = ParticipantRsvpStatus(_rsvp_status)

        attended = d.pop("attended", UNSET)

        _invitation_status = d.pop("invitation_status", UNSET)
        invitation_status: ParticipantInvitationStatus | Unset
        if isinstance(_invitation_status, Unset):
            invitation_status = UNSET
        else:
            invitation_status = ParticipantInvitationStatus(_invitation_status)

        _rsvp_date = d.pop("rsvp_date", UNSET)
        rsvp_date: FuzzyDate | Unset
        if isinstance(_rsvp_date, Unset):
            rsvp_date = UNSET
        else:
            rsvp_date = FuzzyDate.from_dict(_rsvp_date)

        _invitation_date = d.pop("invitation_date", UNSET)
        invitation_date: FuzzyDate | Unset
        if isinstance(_invitation_date, Unset):
            invitation_date = UNSET
        else:
            invitation_date = FuzzyDate.from_dict(_invitation_date)

        _participation_level = d.pop("participation_level", UNSET)
        participation_level: ParticipationLevel | Unset
        if isinstance(_participation_level, Unset):
            participation_level = UNSET
        else:
            participation_level = ParticipationLevel.from_dict(_participation_level)

        def _parse_summary_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary_note = _parse_summary_note(d.pop("summary_note", UNSET))

        participant = cls(
            id=id,
            constituent_id=constituent_id,
            event_id=event_id,
            date_added=date_added,
            date_modified=date_modified,
            host_id=host_id,
            rsvp_status=rsvp_status,
            attended=attended,
            invitation_status=invitation_status,
            rsvp_date=rsvp_date,
            invitation_date=invitation_date,
            participation_level=participation_level,
            summary_note=summary_note,
        )

        return participant

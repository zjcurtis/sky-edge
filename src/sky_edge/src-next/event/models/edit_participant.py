from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.edit_participant_invitation_status import EditParticipantInvitationStatus
from ..models.edit_participant_rsvp_status import EditParticipantRsvpStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate
    from ..models.participation_level import ParticipationLevel


T = TypeVar("T", bound="EditParticipant")


@_attrs_define
class EditParticipant:
    """Participants are individuals or organizations who engage with the organization through an event.
    They can include constituents who receive invitations or register for the event.

        Attributes:
            constituent_id (None | str | Unset): The constituent ID or contact ID of the participant, including non-
                constituent IDs.
            host_id (None | str | Unset): The ID of the host's participant record.
            rsvp_status (EditParticipantRsvpStatus | Unset): The status of the participant's engagement with the
                event.<p>Available values:</p><ul><li><i>NoResponse</i> - No response.</li><li><i>Attending</i> -
                Attending.</li><li><i>Declined</i> - Declined.</li><li><i>Interested</i> - Interested.</li><li><i>Canceled</i> -
                Canceled.</li><li><i>Waitlisted</i> - Waitlisted.</li><li><i>NotApplicable</i> - Not applicable.</li></ul>
            attended (bool | Unset): Whether the participant attended the event.
            invitation_status (EditParticipantInvitationStatus | Unset): The status of the invitation to the
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

    constituent_id: None | str | Unset = UNSET
    host_id: None | str | Unset = UNSET
    rsvp_status: EditParticipantRsvpStatus | Unset = UNSET
    attended: bool | Unset = UNSET
    invitation_status: EditParticipantInvitationStatus | Unset = UNSET
    rsvp_date: FuzzyDate | Unset = UNSET
    invitation_date: FuzzyDate | Unset = UNSET
    participation_level: ParticipationLevel | Unset = UNSET
    summary_note: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

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
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
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

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_host_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_id = _parse_host_id(d.pop("host_id", UNSET))

        _rsvp_status = d.pop("rsvp_status", UNSET)
        rsvp_status: EditParticipantRsvpStatus | Unset
        if isinstance(_rsvp_status, Unset):
            rsvp_status = UNSET
        else:
            rsvp_status = EditParticipantRsvpStatus(_rsvp_status)

        attended = d.pop("attended", UNSET)

        _invitation_status = d.pop("invitation_status", UNSET)
        invitation_status: EditParticipantInvitationStatus | Unset
        if isinstance(_invitation_status, Unset):
            invitation_status = UNSET
        else:
            invitation_status = EditParticipantInvitationStatus(_invitation_status)

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

        edit_participant = cls(
            constituent_id=constituent_id,
            host_id=host_id,
            rsvp_status=rsvp_status,
            attended=attended,
            invitation_status=invitation_status,
            rsvp_date=rsvp_date,
            invitation_date=invitation_date,
            participation_level=participation_level,
            summary_note=summary_note,
        )

        return edit_participant

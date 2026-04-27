from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.constituent_event_participation_invitation_status import (
    ConstituentEventParticipationInvitationStatus,
)
from ..models.constituent_event_participation_rsvp_status import (
    ConstituentEventParticipationRsvpStatus,
)

if TYPE_CHECKING:
    from ..models.participation_level import ParticipationLevel


T = TypeVar("T", bound="ConstituentEventParticipation")


@_attrs_define
class ConstituentEventParticipation:
    """An event participation associated with a constituent.

    Attributes:
        participant_id (None | str | Unset): The ID of the participant.
        event_id (None | str | Unset): The ID of the event.
        event_name (None | str | Unset): The name of the event.
        event_start_date (datetime.date | None | Unset): The date the event starts. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>.
        event_end_date (datetime.date | None | Unset): The date the event ends. Uses <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>.
        invitation_status (ConstituentEventParticipationInvitationStatus | Unset): The status of the invitation to the
            participant.<p>Available values:</p><ul><li><i>NotApplicable</i> - Not applicable.</li><li><i>NotInvited</i> -
            Not invited.</li><li><i>Invited</i> - Invited.</li></ul>
        rsvp_status (ConstituentEventParticipationRsvpStatus | Unset): The status of the participant's engagement with
            the event.<p>Available values:</p><ul><li><i>NoResponse</i> - No response.</li><li><i>Attending</i> -
            Attending.</li><li><i>Declined</i> - Declined.</li><li><i>Interested</i> - Interested.</li><li><i>Canceled</i> -
            Canceled.</li><li><i>Waitlisted</i> - Waitlisted.</li><li><i>NotApplicable</i> - Not applicable.</li></ul>
        attended (bool | Unset): Whether the constituent attended the event.
        participation_level (ParticipationLevel | Unset): Participation levels are the level of involvement participants
            have in an event.
        total_registration_fees (float | Unset): The sum of the participant's fee amounts.
        total_paid (float | Unset): The sum of the participant's paid gifts with a type of Registration Fees.
    """

    participant_id: None | str | Unset = UNSET
    event_id: None | str | Unset = UNSET
    event_name: None | str | Unset = UNSET
    event_start_date: datetime.date | None | Unset = UNSET
    event_end_date: datetime.date | None | Unset = UNSET
    invitation_status: ConstituentEventParticipationInvitationStatus | Unset = UNSET
    rsvp_status: ConstituentEventParticipationRsvpStatus | Unset = UNSET
    attended: bool | Unset = UNSET
    participation_level: ParticipationLevel | Unset = UNSET
    total_registration_fees: float | Unset = UNSET
    total_paid: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        participant_id: None | str | Unset
        if isinstance(self.participant_id, Unset):
            participant_id = UNSET
        else:
            participant_id = self.participant_id

        event_id: None | str | Unset
        if isinstance(self.event_id, Unset):
            event_id = UNSET
        else:
            event_id = self.event_id

        event_name: None | str | Unset
        if isinstance(self.event_name, Unset):
            event_name = UNSET
        else:
            event_name = self.event_name

        event_start_date: None | str | Unset
        if isinstance(self.event_start_date, Unset):
            event_start_date = UNSET
        elif isinstance(self.event_start_date, datetime.date):
            event_start_date = self.event_start_date.isoformat()
        else:
            event_start_date = self.event_start_date

        event_end_date: None | str | Unset
        if isinstance(self.event_end_date, Unset):
            event_end_date = UNSET
        elif isinstance(self.event_end_date, datetime.date):
            event_end_date = self.event_end_date.isoformat()
        else:
            event_end_date = self.event_end_date

        invitation_status: str | Unset = UNSET
        if not isinstance(self.invitation_status, Unset):
            invitation_status = self.invitation_status.value

        rsvp_status: str | Unset = UNSET
        if not isinstance(self.rsvp_status, Unset):
            rsvp_status = self.rsvp_status.value

        attended = self.attended

        participation_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participation_level, Unset):
            participation_level = self.participation_level.to_dict()

        total_registration_fees = self.total_registration_fees

        total_paid = self.total_paid

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if participant_id is not UNSET:
            field_dict["participant_id"] = participant_id
        if event_id is not UNSET:
            field_dict["event_id"] = event_id
        if event_name is not UNSET:
            field_dict["event_name"] = event_name
        if event_start_date is not UNSET:
            field_dict["event_start_date"] = event_start_date
        if event_end_date is not UNSET:
            field_dict["event_end_date"] = event_end_date
        if invitation_status is not UNSET:
            field_dict["invitation_status"] = invitation_status
        if rsvp_status is not UNSET:
            field_dict["rsvp_status"] = rsvp_status
        if attended is not UNSET:
            field_dict["attended"] = attended
        if participation_level is not UNSET:
            field_dict["participation_level"] = participation_level
        if total_registration_fees is not UNSET:
            field_dict["total_registration_fees"] = total_registration_fees
        if total_paid is not UNSET:
            field_dict["total_paid"] = total_paid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.participation_level import ParticipationLevel

        d = dict(src_dict)

        def _parse_participant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_id = _parse_participant_id(d.pop("participant_id", UNSET))

        def _parse_event_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_id = _parse_event_id(d.pop("event_id", UNSET))

        def _parse_event_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name = _parse_event_name(d.pop("event_name", UNSET))

        def _parse_event_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_start_date_type_0 = isoparse(data).date()

                return event_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        event_start_date = _parse_event_start_date(d.pop("event_start_date", UNSET))

        def _parse_event_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_end_date_type_0 = isoparse(data).date()

                return event_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        event_end_date = _parse_event_end_date(d.pop("event_end_date", UNSET))

        _invitation_status = d.pop("invitation_status", UNSET)
        invitation_status: ConstituentEventParticipationInvitationStatus | Unset
        if isinstance(_invitation_status, Unset):
            invitation_status = UNSET
        else:
            invitation_status = ConstituentEventParticipationInvitationStatus(
                _invitation_status
            )

        _rsvp_status = d.pop("rsvp_status", UNSET)
        rsvp_status: ConstituentEventParticipationRsvpStatus | Unset
        if isinstance(_rsvp_status, Unset):
            rsvp_status = UNSET
        else:
            rsvp_status = ConstituentEventParticipationRsvpStatus(_rsvp_status)

        attended = d.pop("attended", UNSET)

        _participation_level = d.pop("participation_level", UNSET)
        participation_level: ParticipationLevel | Unset
        if isinstance(_participation_level, Unset):
            participation_level = UNSET
        else:
            participation_level = ParticipationLevel.from_dict(_participation_level)

        total_registration_fees = d.pop("total_registration_fees", UNSET)

        total_paid = d.pop("total_paid", UNSET)

        constituent_event_participation = cls(
            participant_id=participant_id,
            event_id=event_id,
            event_name=event_name,
            event_start_date=event_start_date,
            event_end_date=event_end_date,
            invitation_status=invitation_status,
            rsvp_status=rsvp_status,
            attended=attended,
            participation_level=participation_level,
            total_registration_fees=total_registration_fees,
            total_paid=total_paid,
        )

        return constituent_event_participation

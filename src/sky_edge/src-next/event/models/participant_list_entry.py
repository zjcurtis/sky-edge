from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.participant_list_entry_invitation_status import ParticipantListEntryInvitationStatus
from ..models.participant_list_entry_online_data_health import ParticipantListEntryOnlineDataHealth
from ..models.participant_list_entry_rsvp_status import ParticipantListEntryRsvpStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate
    from ..models.membership import Membership
    from ..models.participant_entry_fee import ParticipantEntryFee
    from ..models.participant_entry_participant_option import ParticipantEntryParticipantOption
    from ..models.participant_entry_registration_form import ParticipantEntryRegistrationForm
    from ..models.participant_list_participant_summary import ParticipantListParticipantSummary
    from ..models.participation_level import ParticipationLevel


T = TypeVar("T", bound="ParticipantListEntry")


@_attrs_define
class ParticipantListEntry:
    """Participant list entries contain the list information for participants

    Attributes:
        id (None | str | Unset): The ID of the participant.
        contact_id (None | str | Unset): The ID of the contact attending the event.
        date_added (datetime.datetime | None | Unset): The date the participant was created. Includes an offset from UTC
            in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21T10:29:43-04:00</i>.
        date_modified (datetime.datetime | None | Unset): The date when the participant was last modified. Includes an
            offset from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>:
            <i>1969-11-21T10:29:43-04:00</i>.
        is_constituent (bool | None | Unset): Indicates whether the participant is a constituent.
        lookup_id (None | str | Unset): The LookupId of the participant.
        name (None | str | Unset): The participant's full name.
        first_name (None | str | Unset): The participant's first name.
        middle_name (None | str | Unset): The participant's middle name.
        last_name (None | str | Unset): The participant's last name.
        preferred_name (None | str | Unset): The participant's preferred name.
        former_name (None | str | Unset): The participant's former name.
        title (None | str | Unset): The participant's title.
        suffix (None | str | Unset): The participant's suffix.
        class_of (None | str | Unset): The participant's graduating class.
        phone (None | str | Unset): The participant's phone number.
        do_not_call (bool | None | Unset): The participant's phone call preference.
        email (None | str | Unset): The participant's email address.
        do_not_email (bool | None | Unset): The participant's email preference.
        participation_level (ParticipationLevel | Unset): Participation levels are the level of involvement participants
            have in an event.
        attended (bool | None | Unset): Whether the participant attended the event.
        rsvp_status (ParticipantListEntryRsvpStatus | Unset): The status of the participant's engagement with the
            event.<p>Available values:</p><ul><li><i>NoResponse</i> - No response.</li><li><i>Attending</i> -
            Attending.</li><li><i>Declined</i> - Declined.</li><li><i>Interested</i> - Interested.</li><li><i>Canceled</i> -
            Canceled.</li><li><i>Waitlisted</i> - Waitlisted.</li><li><i>NotApplicable</i> - Not applicable.</li></ul>
        invitation_status (ParticipantListEntryInvitationStatus | Unset): The status of the invitation to the
            participant.<p>Available values:</p><ul><li><i>NotApplicable</i> - Not applicable.</li><li><i>NotInvited</i> -
            Not invited.</li><li><i>Invited</i> - Invited.</li></ul>
        rsvp_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
            February 9 (with no year indicated).
        total_paid (float | None | Unset): The sum of the participant's paid gifts associated with fees.
        host (ParticipantListParticipantSummary | Unset): The participant's basic summary information.
        guests (list[ParticipantListParticipantSummary] | None | Unset): The guests of the participant.
        seat (None | str | Unset): The seat assignment for the participant.
        seating_notes (None | str | Unset): Any additional notes or instructions related to the seat assigned to the
            participant.
        seating_group (None | str | Unset): The grouping details of the participant's seat.
        name_tag (None | str | Unset): The name tag for the participant
        summary_note (None | str | Unset): Quick reference information pinned to the participant's record.
        memberships (list[Membership] | None | Unset): The membership information for the participant.
        participant_options (list[ParticipantEntryParticipantOption] | None | Unset): The requested participant options
            for the participant
        registration_form (ParticipantEntryRegistrationForm | Unset): A registration form for a participant entry
        donations (float | None | Unset): The sum of the participant's paid gifts with a type of Donations.
        revenue (float | None | Unset): The sum of the participant's paid gifts across all types.
        online_data_health (ParticipantListEntryOnlineDataHealth | Unset): For a participant who registers online, shows
            their online data health status, such as if they were matched to an existing constituent or added as a possible
            duplicate.<p>Available values:</p><ul><li><i>Matched</i> - Indicates that a constituent from an online
            registration was matched to an existing constituent record.</li><li><i>PossibleDuplicate</i> - Indicates that a
            new constituent was created from online registrations because there were records that matched on name but not on
            contact information.</li><li><i>NewNamedGuest</i> - Indicates that a named guest record was created because the
            constituent was already registered as a participant, or there was not enough contact information from online
            registrations to create a constituent record.</li><li><i>NewConstituent</i> - Indicates the constituent record
            was created because the system didn't find existing records that matched constituent information from online
            registrations.</li><li><i>FormerPossibleDuplicate</i> - Indicates the possible duplicate has been resolved or
            the system determined there are no more possible duplicates.</li><li><i>ManuallyChanged</i> - Indicates the
            constituent from online registrations that was linked to the participant was manually changed by a
            user.</li></ul>
        total_fees (float | None | Unset): The sum of the participant's fee amounts.
        fees (list[ParticipantEntryFee] | None | Unset): The summary of fees associated with the participant.
    """

    id: None | str | Unset = UNSET
    contact_id: None | str | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    is_constituent: bool | None | Unset = UNSET
    lookup_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    former_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    suffix: None | str | Unset = UNSET
    class_of: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    do_not_call: bool | None | Unset = UNSET
    email: None | str | Unset = UNSET
    do_not_email: bool | None | Unset = UNSET
    participation_level: ParticipationLevel | Unset = UNSET
    attended: bool | None | Unset = UNSET
    rsvp_status: ParticipantListEntryRsvpStatus | Unset = UNSET
    invitation_status: ParticipantListEntryInvitationStatus | Unset = UNSET
    rsvp_date: FuzzyDate | Unset = UNSET
    total_paid: float | None | Unset = UNSET
    host: ParticipantListParticipantSummary | Unset = UNSET
    guests: list[ParticipantListParticipantSummary] | None | Unset = UNSET
    seat: None | str | Unset = UNSET
    seating_notes: None | str | Unset = UNSET
    seating_group: None | str | Unset = UNSET
    name_tag: None | str | Unset = UNSET
    summary_note: None | str | Unset = UNSET
    memberships: list[Membership] | None | Unset = UNSET
    participant_options: list[ParticipantEntryParticipantOption] | None | Unset = UNSET
    registration_form: ParticipantEntryRegistrationForm | Unset = UNSET
    donations: float | None | Unset = UNSET
    revenue: float | None | Unset = UNSET
    online_data_health: ParticipantListEntryOnlineDataHealth | Unset = UNSET
    total_fees: float | None | Unset = UNSET
    fees: list[ParticipantEntryFee] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = self.contact_id

        date_added: None | str | Unset
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        is_constituent: bool | None | Unset
        if isinstance(self.is_constituent, Unset):
            is_constituent = UNSET
        else:
            is_constituent = self.is_constituent

        lookup_id: None | str | Unset
        if isinstance(self.lookup_id, Unset):
            lookup_id = UNSET
        else:
            lookup_id = self.lookup_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        former_name: None | str | Unset
        if isinstance(self.former_name, Unset):
            former_name = UNSET
        else:
            former_name = self.former_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        suffix: None | str | Unset
        if isinstance(self.suffix, Unset):
            suffix = UNSET
        else:
            suffix = self.suffix

        class_of: None | str | Unset
        if isinstance(self.class_of, Unset):
            class_of = UNSET
        else:
            class_of = self.class_of

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        do_not_call: bool | None | Unset
        if isinstance(self.do_not_call, Unset):
            do_not_call = UNSET
        else:
            do_not_call = self.do_not_call

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        do_not_email: bool | None | Unset
        if isinstance(self.do_not_email, Unset):
            do_not_email = UNSET
        else:
            do_not_email = self.do_not_email

        participation_level: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participation_level, Unset):
            participation_level = self.participation_level.to_dict()

        attended: bool | None | Unset
        if isinstance(self.attended, Unset):
            attended = UNSET
        else:
            attended = self.attended

        rsvp_status: str | Unset = UNSET
        if not isinstance(self.rsvp_status, Unset):
            rsvp_status = self.rsvp_status.value

        invitation_status: str | Unset = UNSET
        if not isinstance(self.invitation_status, Unset):
            invitation_status = self.invitation_status.value

        rsvp_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rsvp_date, Unset):
            rsvp_date = self.rsvp_date.to_dict()

        total_paid: float | None | Unset
        if isinstance(self.total_paid, Unset):
            total_paid = UNSET
        else:
            total_paid = self.total_paid

        host: dict[str, Any] | Unset = UNSET
        if not isinstance(self.host, Unset):
            host = self.host.to_dict()

        guests: list[dict[str, Any]] | None | Unset
        if isinstance(self.guests, Unset):
            guests = UNSET
        elif isinstance(self.guests, list):
            guests = []
            for guests_type_0_item_data in self.guests:
                guests_type_0_item = guests_type_0_item_data.to_dict()
                guests.append(guests_type_0_item)

        else:
            guests = self.guests

        seat: None | str | Unset
        if isinstance(self.seat, Unset):
            seat = UNSET
        else:
            seat = self.seat

        seating_notes: None | str | Unset
        if isinstance(self.seating_notes, Unset):
            seating_notes = UNSET
        else:
            seating_notes = self.seating_notes

        seating_group: None | str | Unset
        if isinstance(self.seating_group, Unset):
            seating_group = UNSET
        else:
            seating_group = self.seating_group

        name_tag: None | str | Unset
        if isinstance(self.name_tag, Unset):
            name_tag = UNSET
        else:
            name_tag = self.name_tag

        summary_note: None | str | Unset
        if isinstance(self.summary_note, Unset):
            summary_note = UNSET
        else:
            summary_note = self.summary_note

        memberships: list[dict[str, Any]] | None | Unset
        if isinstance(self.memberships, Unset):
            memberships = UNSET
        elif isinstance(self.memberships, list):
            memberships = []
            for memberships_type_0_item_data in self.memberships:
                memberships_type_0_item = memberships_type_0_item_data.to_dict()
                memberships.append(memberships_type_0_item)

        else:
            memberships = self.memberships

        participant_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.participant_options, Unset):
            participant_options = UNSET
        elif isinstance(self.participant_options, list):
            participant_options = []
            for participant_options_type_0_item_data in self.participant_options:
                participant_options_type_0_item = participant_options_type_0_item_data.to_dict()
                participant_options.append(participant_options_type_0_item)

        else:
            participant_options = self.participant_options

        registration_form: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_form, Unset):
            registration_form = self.registration_form.to_dict()

        donations: float | None | Unset
        if isinstance(self.donations, Unset):
            donations = UNSET
        else:
            donations = self.donations

        revenue: float | None | Unset
        if isinstance(self.revenue, Unset):
            revenue = UNSET
        else:
            revenue = self.revenue

        online_data_health: str | Unset = UNSET
        if not isinstance(self.online_data_health, Unset):
            online_data_health = self.online_data_health.value

        total_fees: float | None | Unset
        if isinstance(self.total_fees, Unset):
            total_fees = UNSET
        else:
            total_fees = self.total_fees

        fees: list[dict[str, Any]] | None | Unset
        if isinstance(self.fees, Unset):
            fees = UNSET
        elif isinstance(self.fees, list):
            fees = []
            for fees_type_0_item_data in self.fees:
                fees_type_0_item = fees_type_0_item_data.to_dict()
                fees.append(fees_type_0_item)

        else:
            fees = self.fees

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if is_constituent is not UNSET:
            field_dict["is_constituent"] = is_constituent
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if former_name is not UNSET:
            field_dict["former_name"] = former_name
        if title is not UNSET:
            field_dict["title"] = title
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if class_of is not UNSET:
            field_dict["class_of"] = class_of
        if phone is not UNSET:
            field_dict["phone"] = phone
        if do_not_call is not UNSET:
            field_dict["do_not_call"] = do_not_call
        if email is not UNSET:
            field_dict["email"] = email
        if do_not_email is not UNSET:
            field_dict["do_not_email"] = do_not_email
        if participation_level is not UNSET:
            field_dict["participation_level"] = participation_level
        if attended is not UNSET:
            field_dict["attended"] = attended
        if rsvp_status is not UNSET:
            field_dict["rsvp_status"] = rsvp_status
        if invitation_status is not UNSET:
            field_dict["invitation_status"] = invitation_status
        if rsvp_date is not UNSET:
            field_dict["rsvp_date"] = rsvp_date
        if total_paid is not UNSET:
            field_dict["total_paid"] = total_paid
        if host is not UNSET:
            field_dict["host"] = host
        if guests is not UNSET:
            field_dict["guests"] = guests
        if seat is not UNSET:
            field_dict["seat"] = seat
        if seating_notes is not UNSET:
            field_dict["seating_notes"] = seating_notes
        if seating_group is not UNSET:
            field_dict["seating_group"] = seating_group
        if name_tag is not UNSET:
            field_dict["name_tag"] = name_tag
        if summary_note is not UNSET:
            field_dict["summary_note"] = summary_note
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if participant_options is not UNSET:
            field_dict["participant_options"] = participant_options
        if registration_form is not UNSET:
            field_dict["registration_form"] = registration_form
        if donations is not UNSET:
            field_dict["donations"] = donations
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if online_data_health is not UNSET:
            field_dict["online_data_health"] = online_data_health
        if total_fees is not UNSET:
            field_dict["total_fees"] = total_fees
        if fees is not UNSET:
            field_dict["fees"] = fees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate
        from ..models.membership import Membership
        from ..models.participant_entry_fee import ParticipantEntryFee
        from ..models.participant_entry_participant_option import ParticipantEntryParticipantOption
        from ..models.participant_entry_registration_form import ParticipantEntryRegistrationForm
        from ..models.participant_list_participant_summary import ParticipantListParticipantSummary
        from ..models.participation_level import ParticipationLevel

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_contact_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_id = _parse_contact_id(d.pop("contact_id", UNSET))

        def _parse_date_added(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = isoparse(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_is_constituent(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_constituent = _parse_is_constituent(d.pop("is_constituent", UNSET))

        def _parse_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lookup_id = _parse_lookup_id(d.pop("lookup_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        def _parse_former_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        former_name = _parse_former_name(d.pop("former_name", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suffix = _parse_suffix(d.pop("suffix", UNSET))

        def _parse_class_of(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_of = _parse_class_of(d.pop("class_of", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_do_not_call(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        do_not_call = _parse_do_not_call(d.pop("do_not_call", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_do_not_email(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        do_not_email = _parse_do_not_email(d.pop("do_not_email", UNSET))

        _participation_level = d.pop("participation_level", UNSET)
        participation_level: ParticipationLevel | Unset
        if isinstance(_participation_level, Unset):
            participation_level = UNSET
        else:
            participation_level = ParticipationLevel.from_dict(_participation_level)

        def _parse_attended(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        attended = _parse_attended(d.pop("attended", UNSET))

        _rsvp_status = d.pop("rsvp_status", UNSET)
        rsvp_status: ParticipantListEntryRsvpStatus | Unset
        if isinstance(_rsvp_status, Unset):
            rsvp_status = UNSET
        else:
            rsvp_status = ParticipantListEntryRsvpStatus(_rsvp_status)

        _invitation_status = d.pop("invitation_status", UNSET)
        invitation_status: ParticipantListEntryInvitationStatus | Unset
        if isinstance(_invitation_status, Unset):
            invitation_status = UNSET
        else:
            invitation_status = ParticipantListEntryInvitationStatus(_invitation_status)

        _rsvp_date = d.pop("rsvp_date", UNSET)
        rsvp_date: FuzzyDate | Unset
        if isinstance(_rsvp_date, Unset):
            rsvp_date = UNSET
        else:
            rsvp_date = FuzzyDate.from_dict(_rsvp_date)

        def _parse_total_paid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_paid = _parse_total_paid(d.pop("total_paid", UNSET))

        _host = d.pop("host", UNSET)
        host: ParticipantListParticipantSummary | Unset
        if isinstance(_host, Unset):
            host = UNSET
        else:
            host = ParticipantListParticipantSummary.from_dict(_host)

        def _parse_guests(data: object) -> list[ParticipantListParticipantSummary] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guests_type_0 = []
                _guests_type_0 = data
                for guests_type_0_item_data in _guests_type_0:
                    guests_type_0_item = ParticipantListParticipantSummary.from_dict(guests_type_0_item_data)

                    guests_type_0.append(guests_type_0_item)

                return guests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ParticipantListParticipantSummary] | None | Unset, data)

        guests = _parse_guests(d.pop("guests", UNSET))

        def _parse_seat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seat = _parse_seat(d.pop("seat", UNSET))

        def _parse_seating_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seating_notes = _parse_seating_notes(d.pop("seating_notes", UNSET))

        def _parse_seating_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        seating_group = _parse_seating_group(d.pop("seating_group", UNSET))

        def _parse_name_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tag = _parse_name_tag(d.pop("name_tag", UNSET))

        def _parse_summary_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary_note = _parse_summary_note(d.pop("summary_note", UNSET))

        def _parse_memberships(data: object) -> list[Membership] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                memberships_type_0 = []
                _memberships_type_0 = data
                for memberships_type_0_item_data in _memberships_type_0:
                    memberships_type_0_item = Membership.from_dict(memberships_type_0_item_data)

                    memberships_type_0.append(memberships_type_0_item)

                return memberships_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Membership] | None | Unset, data)

        memberships = _parse_memberships(d.pop("memberships", UNSET))

        def _parse_participant_options(data: object) -> list[ParticipantEntryParticipantOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                participant_options_type_0 = []
                _participant_options_type_0 = data
                for participant_options_type_0_item_data in _participant_options_type_0:
                    participant_options_type_0_item = ParticipantEntryParticipantOption.from_dict(
                        participant_options_type_0_item_data
                    )

                    participant_options_type_0.append(participant_options_type_0_item)

                return participant_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ParticipantEntryParticipantOption] | None | Unset, data)

        participant_options = _parse_participant_options(d.pop("participant_options", UNSET))

        _registration_form = d.pop("registration_form", UNSET)
        registration_form: ParticipantEntryRegistrationForm | Unset
        if isinstance(_registration_form, Unset):
            registration_form = UNSET
        else:
            registration_form = ParticipantEntryRegistrationForm.from_dict(_registration_form)

        def _parse_donations(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        donations = _parse_donations(d.pop("donations", UNSET))

        def _parse_revenue(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        revenue = _parse_revenue(d.pop("revenue", UNSET))

        _online_data_health = d.pop("online_data_health", UNSET)
        online_data_health: ParticipantListEntryOnlineDataHealth | Unset
        if isinstance(_online_data_health, Unset):
            online_data_health = UNSET
        else:
            online_data_health = ParticipantListEntryOnlineDataHealth(_online_data_health)

        def _parse_total_fees(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_fees = _parse_total_fees(d.pop("total_fees", UNSET))

        def _parse_fees(data: object) -> list[ParticipantEntryFee] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fees_type_0 = []
                _fees_type_0 = data
                for fees_type_0_item_data in _fees_type_0:
                    fees_type_0_item = ParticipantEntryFee.from_dict(fees_type_0_item_data)

                    fees_type_0.append(fees_type_0_item)

                return fees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ParticipantEntryFee] | None | Unset, data)

        fees = _parse_fees(d.pop("fees", UNSET))

        participant_list_entry = cls(
            id=id,
            contact_id=contact_id,
            date_added=date_added,
            date_modified=date_modified,
            is_constituent=is_constituent,
            lookup_id=lookup_id,
            name=name,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            preferred_name=preferred_name,
            former_name=former_name,
            title=title,
            suffix=suffix,
            class_of=class_of,
            phone=phone,
            do_not_call=do_not_call,
            email=email,
            do_not_email=do_not_email,
            participation_level=participation_level,
            attended=attended,
            rsvp_status=rsvp_status,
            invitation_status=invitation_status,
            rsvp_date=rsvp_date,
            total_paid=total_paid,
            host=host,
            guests=guests,
            seat=seat,
            seating_notes=seating_notes,
            seating_group=seating_group,
            name_tag=name_tag,
            summary_note=summary_note,
            memberships=memberships,
            participant_options=participant_options,
            registration_form=registration_form,
            donations=donations,
            revenue=revenue,
            online_data_health=online_data_health,
            total_fees=total_fees,
            fees=fees,
        )

        return participant_list_entry

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.membership_category_membership_benefits_send_to import MembershipCategoryMembershipBenefitsSendTo
from ..models.membership_category_new_membership_expires_interval import MembershipCategoryNewMembershipExpiresInterval
from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipCategory")


@_attrs_define
class MembershipCategory:
    """Membership category collection

    Attributes:
        membership_category_id (int | Unset): The immutable system record ID of the membership category.
        category_name (None | str | Unset): The name of the membership category.
        default_expires_date (datetime.date | None | Unset): The default expiration date for a new membership category.
        program_name (None | str | Unset): The membership program name. category.
        sequence (int | None | Unset): The sequence number of the membership category.
        inactive (bool | Unset): This computed field indicates that the membership category is active or not.
        lifetime_membership (bool | Unset): Indicates whether the membership category comes with a lifetime membership.
        print_renewals (bool | Unset): Indicates whether to print renewals.
        default_expires_days (int | None | Unset): The default number of days after which a new membership category
            expires.
        new_mem_expires_value (int | None | Unset): The new membership category expires value.
        new_mem_expires_interval (MembershipCategoryNewMembershipExpiresInterval | Unset): The new membership category
            expires interval.
        maximum_members (int | None | Unset): The maximum number of members allowed for this category
        benefit_notes (None | str | Unset): Benefit notes of a membership category.
        send_benefits_to (MembershipCategoryMembershipBenefitsSendTo | Unset): Send notice of renewal notice type.
        minimum_dues (float | None | Unset): The minimum amount required to qualify for this membership category.
        maximum_dues (float | None | Unset): The maximum amount expected for this membership category.
        dues_level (None | str | Unset): Membership dues is used to establish dues which are required to qualify for
            that membership category. It help control how much a constituent is expected to pay and under what conditions.
            For e.g. - Dues level is - Individual with minimum dues as $25 and maximum dues as $50
    """

    membership_category_id: int | Unset = UNSET
    category_name: None | str | Unset = UNSET
    default_expires_date: datetime.date | None | Unset = UNSET
    program_name: None | str | Unset = UNSET
    sequence: int | None | Unset = UNSET
    inactive: bool | Unset = UNSET
    lifetime_membership: bool | Unset = UNSET
    print_renewals: bool | Unset = UNSET
    default_expires_days: int | None | Unset = UNSET
    new_mem_expires_value: int | None | Unset = UNSET
    new_mem_expires_interval: MembershipCategoryNewMembershipExpiresInterval | Unset = UNSET
    maximum_members: int | None | Unset = UNSET
    benefit_notes: None | str | Unset = UNSET
    send_benefits_to: MembershipCategoryMembershipBenefitsSendTo | Unset = UNSET
    minimum_dues: float | None | Unset = UNSET
    maximum_dues: float | None | Unset = UNSET
    dues_level: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        membership_category_id = self.membership_category_id

        category_name: None | str | Unset
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        default_expires_date: None | str | Unset
        if isinstance(self.default_expires_date, Unset):
            default_expires_date = UNSET
        elif isinstance(self.default_expires_date, datetime.date):
            default_expires_date = self.default_expires_date.isoformat()
        else:
            default_expires_date = self.default_expires_date

        program_name: None | str | Unset
        if isinstance(self.program_name, Unset):
            program_name = UNSET
        else:
            program_name = self.program_name

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        inactive = self.inactive

        lifetime_membership = self.lifetime_membership

        print_renewals = self.print_renewals

        default_expires_days: int | None | Unset
        if isinstance(self.default_expires_days, Unset):
            default_expires_days = UNSET
        else:
            default_expires_days = self.default_expires_days

        new_mem_expires_value: int | None | Unset
        if isinstance(self.new_mem_expires_value, Unset):
            new_mem_expires_value = UNSET
        else:
            new_mem_expires_value = self.new_mem_expires_value

        new_mem_expires_interval: str | Unset = UNSET
        if not isinstance(self.new_mem_expires_interval, Unset):
            new_mem_expires_interval = self.new_mem_expires_interval.value

        maximum_members: int | None | Unset
        if isinstance(self.maximum_members, Unset):
            maximum_members = UNSET
        else:
            maximum_members = self.maximum_members

        benefit_notes: None | str | Unset
        if isinstance(self.benefit_notes, Unset):
            benefit_notes = UNSET
        else:
            benefit_notes = self.benefit_notes

        send_benefits_to: str | Unset = UNSET
        if not isinstance(self.send_benefits_to, Unset):
            send_benefits_to = self.send_benefits_to.value

        minimum_dues: float | None | Unset
        if isinstance(self.minimum_dues, Unset):
            minimum_dues = UNSET
        else:
            minimum_dues = self.minimum_dues

        maximum_dues: float | None | Unset
        if isinstance(self.maximum_dues, Unset):
            maximum_dues = UNSET
        else:
            maximum_dues = self.maximum_dues

        dues_level: None | str | Unset
        if isinstance(self.dues_level, Unset):
            dues_level = UNSET
        else:
            dues_level = self.dues_level

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if membership_category_id is not UNSET:
            field_dict["membership_category_id"] = membership_category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if default_expires_date is not UNSET:
            field_dict["default_expires_date"] = default_expires_date
        if program_name is not UNSET:
            field_dict["program_name"] = program_name
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if lifetime_membership is not UNSET:
            field_dict["lifetime_membership"] = lifetime_membership
        if print_renewals is not UNSET:
            field_dict["print_renewals"] = print_renewals
        if default_expires_days is not UNSET:
            field_dict["default_expires_days"] = default_expires_days
        if new_mem_expires_value is not UNSET:
            field_dict["new_mem_expires_value"] = new_mem_expires_value
        if new_mem_expires_interval is not UNSET:
            field_dict["new_mem_expires_interval"] = new_mem_expires_interval
        if maximum_members is not UNSET:
            field_dict["maximum_members"] = maximum_members
        if benefit_notes is not UNSET:
            field_dict["benefit_notes"] = benefit_notes
        if send_benefits_to is not UNSET:
            field_dict["send_benefits_to"] = send_benefits_to
        if minimum_dues is not UNSET:
            field_dict["minimum_dues"] = minimum_dues
        if maximum_dues is not UNSET:
            field_dict["maximum_dues"] = maximum_dues
        if dues_level is not UNSET:
            field_dict["dues_level"] = dues_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        membership_category_id = d.pop("membership_category_id", UNSET)

        def _parse_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_name = _parse_category_name(d.pop("category_name", UNSET))

        def _parse_default_expires_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                default_expires_date_type_0 = isoparse(data).date()

                return default_expires_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        default_expires_date = _parse_default_expires_date(d.pop("default_expires_date", UNSET))

        def _parse_program_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_name = _parse_program_name(d.pop("program_name", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        inactive = d.pop("inactive", UNSET)

        lifetime_membership = d.pop("lifetime_membership", UNSET)

        print_renewals = d.pop("print_renewals", UNSET)

        def _parse_default_expires_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_expires_days = _parse_default_expires_days(d.pop("default_expires_days", UNSET))

        def _parse_new_mem_expires_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        new_mem_expires_value = _parse_new_mem_expires_value(d.pop("new_mem_expires_value", UNSET))

        _new_mem_expires_interval = d.pop("new_mem_expires_interval", UNSET)
        new_mem_expires_interval: MembershipCategoryNewMembershipExpiresInterval | Unset
        if isinstance(_new_mem_expires_interval, Unset):
            new_mem_expires_interval = UNSET
        else:
            new_mem_expires_interval = MembershipCategoryNewMembershipExpiresInterval(_new_mem_expires_interval)

        def _parse_maximum_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maximum_members = _parse_maximum_members(d.pop("maximum_members", UNSET))

        def _parse_benefit_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        benefit_notes = _parse_benefit_notes(d.pop("benefit_notes", UNSET))

        _send_benefits_to = d.pop("send_benefits_to", UNSET)
        send_benefits_to: MembershipCategoryMembershipBenefitsSendTo | Unset
        if isinstance(_send_benefits_to, Unset):
            send_benefits_to = UNSET
        else:
            send_benefits_to = MembershipCategoryMembershipBenefitsSendTo(_send_benefits_to)

        def _parse_minimum_dues(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        minimum_dues = _parse_minimum_dues(d.pop("minimum_dues", UNSET))

        def _parse_maximum_dues(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        maximum_dues = _parse_maximum_dues(d.pop("maximum_dues", UNSET))

        def _parse_dues_level(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dues_level = _parse_dues_level(d.pop("dues_level", UNSET))

        membership_category = cls(
            membership_category_id=membership_category_id,
            category_name=category_name,
            default_expires_date=default_expires_date,
            program_name=program_name,
            sequence=sequence,
            inactive=inactive,
            lifetime_membership=lifetime_membership,
            print_renewals=print_renewals,
            default_expires_days=default_expires_days,
            new_mem_expires_value=new_mem_expires_value,
            new_mem_expires_interval=new_mem_expires_interval,
            maximum_members=maximum_members,
            benefit_notes=benefit_notes,
            send_benefits_to=send_benefits_to,
            minimum_dues=minimum_dues,
            maximum_dues=maximum_dues,
            dues_level=dues_level,
        )

        return membership_category

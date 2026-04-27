from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.membership_summary_membership_standing import (
    MembershipSummaryMembershipStanding,
)

T = TypeVar("T", bound="MembershipSummary")


@_attrs_define
class MembershipSummary:
    """This defines the current status of a membership.

    Attributes:
        custom_membership_id (None | str | Unset): The user defined ID of the membership.
        notes (None | str | Unset): The membership notes.
        standing (MembershipSummaryMembershipStanding | Unset): The membership status. Possible values include: Joined,
            Dropped, Upgraded, Downgraded, Renewal and Rejoined.
        constituent_id (None | str | Unset): The constituent ID associated with the membership.
        constituent_name (None | str | Unset): The constituent name associated with the membership.
        expires_on_date (datetime.date | None | Unset): The date when the membership expires.
        primary_member_constituent_id (None | str | Unset): Primary member constituent ID
        primary_member_constituent_name (None | str | Unset): Primary member constituent name
        primary (bool | Unset): Primary member or not
    """

    custom_membership_id: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    standing: MembershipSummaryMembershipStanding | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    constituent_name: None | str | Unset = UNSET
    expires_on_date: datetime.date | None | Unset = UNSET
    primary_member_constituent_id: None | str | Unset = UNSET
    primary_member_constituent_name: None | str | Unset = UNSET
    primary: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        custom_membership_id: None | str | Unset
        if isinstance(self.custom_membership_id, Unset):
            custom_membership_id = UNSET
        else:
            custom_membership_id = self.custom_membership_id

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        standing: str | Unset = UNSET
        if not isinstance(self.standing, Unset):
            standing = self.standing.value

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        constituent_name: None | str | Unset
        if isinstance(self.constituent_name, Unset):
            constituent_name = UNSET
        else:
            constituent_name = self.constituent_name

        expires_on_date: None | str | Unset
        if isinstance(self.expires_on_date, Unset):
            expires_on_date = UNSET
        elif isinstance(self.expires_on_date, datetime.date):
            expires_on_date = self.expires_on_date.isoformat()
        else:
            expires_on_date = self.expires_on_date

        primary_member_constituent_id: None | str | Unset
        if isinstance(self.primary_member_constituent_id, Unset):
            primary_member_constituent_id = UNSET
        else:
            primary_member_constituent_id = self.primary_member_constituent_id

        primary_member_constituent_name: None | str | Unset
        if isinstance(self.primary_member_constituent_name, Unset):
            primary_member_constituent_name = UNSET
        else:
            primary_member_constituent_name = self.primary_member_constituent_name

        primary = self.primary

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if custom_membership_id is not UNSET:
            field_dict["custom_membership_id"] = custom_membership_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if standing is not UNSET:
            field_dict["standing"] = standing
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if constituent_name is not UNSET:
            field_dict["constituent_name"] = constituent_name
        if expires_on_date is not UNSET:
            field_dict["expires_on_date"] = expires_on_date
        if primary_member_constituent_id is not UNSET:
            field_dict["primary_member_constituent_id"] = primary_member_constituent_id
        if primary_member_constituent_name is not UNSET:
            field_dict["primary_member_constituent_name"] = (
                primary_member_constituent_name
            )
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_custom_membership_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_membership_id = _parse_custom_membership_id(
            d.pop("custom_membership_id", UNSET)
        )

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _standing = d.pop("standing", UNSET)
        standing: MembershipSummaryMembershipStanding | Unset
        if isinstance(_standing, Unset):
            standing = UNSET
        else:
            standing = MembershipSummaryMembershipStanding(_standing)

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_constituent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_name = _parse_constituent_name(d.pop("constituent_name", UNSET))

        def _parse_expires_on_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_on_date_type_0 = isoparse(data).date()

                return expires_on_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        expires_on_date = _parse_expires_on_date(d.pop("expires_on_date", UNSET))

        def _parse_primary_member_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_member_constituent_id = _parse_primary_member_constituent_id(
            d.pop("primary_member_constituent_id", UNSET)
        )

        def _parse_primary_member_constituent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_member_constituent_name = _parse_primary_member_constituent_name(
            d.pop("primary_member_constituent_name", UNSET)
        )

        primary = d.pop("primary", UNSET)

        membership_summary = cls(
            custom_membership_id=custom_membership_id,
            notes=notes,
            standing=standing,
            constituent_id=constituent_id,
            constituent_name=constituent_name,
            expires_on_date=expires_on_date,
            primary_member_constituent_id=primary_member_constituent_id,
            primary_member_constituent_name=primary_member_constituent_name,
            primary=primary,
        )

        return membership_summary

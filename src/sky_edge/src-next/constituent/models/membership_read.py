from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.membership_read_standing import MembershipReadStanding
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.membership_member_read import MembershipMemberRead


T = TypeVar("T", bound="MembershipRead")


@_attrs_define
class MembershipRead:
    """Membership programs encourage donor loyalty and reward constituents for their support with exclusive, personalized
    benefits. Memberships also encourage occasional donors to become regular givers through annual renewals.

        Attributes:
            id (str | Unset): The immutable system record ID of the membership.
            category (str | Unset): The membership category.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the membership.
            date_added (datetime.datetime | Unset): The date when the membership was created. Includes an offset from UTC in
                <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the membership was last modified. Includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            dues (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            expires (datetime.datetime | Unset): The date when the membership expires. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            joined (datetime.datetime | Unset): The date when the membership becomes active. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            members (list[MembershipMemberRead] | Unset): The set of members who belong to the membership.
            program (str | Unset): The membership program.
            standing (MembershipReadStanding | Unset): The membership status. Available values are <i>New</i>,
                <i>Active</i>, <i>Lapsed</i>, and <i>Dropped</i>.
            subcategory (str | Unset): The membership subcategory.
            custom_membership_id (str | Unset): The user defined membership id.
    """

    id: str | Unset = UNSET
    category: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    dues: Currency | Unset = UNSET
    expires: datetime.datetime | Unset = UNSET
    joined: datetime.datetime | Unset = UNSET
    members: list[MembershipMemberRead] | Unset = UNSET
    program: str | Unset = UNSET
    standing: MembershipReadStanding | Unset = UNSET
    subcategory: str | Unset = UNSET
    custom_membership_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        constituent_id = self.constituent_id

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        dues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dues, Unset):
            dues = self.dues.to_dict()

        expires: str | Unset = UNSET
        if not isinstance(self.expires, Unset):
            expires = self.expires.isoformat()

        joined: str | Unset = UNSET
        if not isinstance(self.joined, Unset):
            joined = self.joined.isoformat()

        members: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        program = self.program

        standing: str | Unset = UNSET
        if not isinstance(self.standing, Unset):
            standing = self.standing.value

        subcategory = self.subcategory

        custom_membership_id = self.custom_membership_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if dues is not UNSET:
            field_dict["dues"] = dues
        if expires is not UNSET:
            field_dict["expires"] = expires
        if joined is not UNSET:
            field_dict["joined"] = joined
        if members is not UNSET:
            field_dict["members"] = members
        if program is not UNSET:
            field_dict["program"] = program
        if standing is not UNSET:
            field_dict["standing"] = standing
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if custom_membership_id is not UNSET:
            field_dict["custom_membership_id"] = custom_membership_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.membership_member_read import MembershipMemberRead

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        category = d.pop("category", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

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

        _dues = d.pop("dues", UNSET)
        dues: Currency | Unset
        if isinstance(_dues, Unset):
            dues = UNSET
        else:
            dues = Currency.from_dict(_dues)

        _expires = d.pop("expires", UNSET)
        expires: datetime.datetime | Unset
        if isinstance(_expires, Unset):
            expires = UNSET
        else:
            expires = isoparse(_expires)

        _joined = d.pop("joined", UNSET)
        joined: datetime.datetime | Unset
        if isinstance(_joined, Unset):
            joined = UNSET
        else:
            joined = isoparse(_joined)

        _members = d.pop("members", UNSET)
        members: list[MembershipMemberRead] | Unset = UNSET
        if _members is not UNSET:
            members = []
            for members_item_data in _members:
                members_item = MembershipMemberRead.from_dict(members_item_data)

                members.append(members_item)

        program = d.pop("program", UNSET)

        _standing = d.pop("standing", UNSET)
        standing: MembershipReadStanding | Unset
        if isinstance(_standing, Unset):
            standing = UNSET
        else:
            standing = MembershipReadStanding(_standing)

        subcategory = d.pop("subcategory", UNSET)

        custom_membership_id = d.pop("custom_membership_id", UNSET)

        membership_read = cls(
            id=id,
            category=category,
            constituent_id=constituent_id,
            date_added=date_added,
            date_modified=date_modified,
            dues=dues,
            expires=expires,
            joined=joined,
            members=members,
            program=program,
            standing=standing,
            subcategory=subcategory,
            custom_membership_id=custom_membership_id,
        )

        membership_read.additional_properties = d
        return membership_read

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

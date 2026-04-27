from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category
    from ..models.code_table_entry import CodeTableEntry
    from ..models.sub_category import SubCategory


T = TypeVar("T", bound="MembershipCreate")


@_attrs_define
class MembershipCreate:
    """Membership create request model

    Attributes:
        category (Category): Category drop down data
        joined_date (datetime.date): The create, renewal, rejoin, or drop date of the transaction.
        lifetime_membership (bool): Gets or sets value to lifetime membership.
        print_renewals (bool): Gets or sets value to print renewals.
        total_members (int): Gets or sets the value of total members allowed in this membership Default: 1.
        total_children (int): Gets or sets the value of total children allowed in this membership Default: 0.
        membership_id (None | str | Unset): The membership identifier associated with the membership.
        dues (float | None | Unset): The dues for the membership transaction.
        program (CodeTableEntry | Unset): A predefined entry in a code table.
        reason (CodeTableEntry | Unset): A predefined entry in a code table.
        subcategory (SubCategory | Unset): SubCategory drop down data
        expires_on_date (datetime.date | None | Unset): Gets or sets the date on which the membership expires.
        mem_comment (None | str | Unset): Gets or sets value of comment.
        member_sequence (int | None | Unset): Order in which this member appears
        membership_transaction_sequence (int | None | Unset): Order in which this membership appears.
    """

    category: Category
    joined_date: datetime.date
    lifetime_membership: bool
    print_renewals: bool
    total_members: int = 1
    total_children: int = 0
    membership_id: None | str | Unset = UNSET
    dues: float | None | Unset = UNSET
    program: CodeTableEntry | Unset = UNSET
    reason: CodeTableEntry | Unset = UNSET
    subcategory: SubCategory | Unset = UNSET
    expires_on_date: datetime.date | None | Unset = UNSET
    mem_comment: None | str | Unset = UNSET
    member_sequence: int | None | Unset = UNSET
    membership_transaction_sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category = self.category.to_dict()

        joined_date = self.joined_date.isoformat()

        lifetime_membership = self.lifetime_membership

        print_renewals = self.print_renewals

        total_members = self.total_members

        total_children = self.total_children

        membership_id: None | str | Unset
        if isinstance(self.membership_id, Unset):
            membership_id = UNSET
        else:
            membership_id = self.membership_id

        dues: float | None | Unset
        if isinstance(self.dues, Unset):
            dues = UNSET
        else:
            dues = self.dues

        program: dict[str, Any] | Unset = UNSET
        if not isinstance(self.program, Unset):
            program = self.program.to_dict()

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        subcategory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subcategory, Unset):
            subcategory = self.subcategory.to_dict()

        expires_on_date: None | str | Unset
        if isinstance(self.expires_on_date, Unset):
            expires_on_date = UNSET
        elif isinstance(self.expires_on_date, datetime.date):
            expires_on_date = self.expires_on_date.isoformat()
        else:
            expires_on_date = self.expires_on_date

        mem_comment: None | str | Unset
        if isinstance(self.mem_comment, Unset):
            mem_comment = UNSET
        else:
            mem_comment = self.mem_comment

        member_sequence: int | None | Unset
        if isinstance(self.member_sequence, Unset):
            member_sequence = UNSET
        else:
            member_sequence = self.member_sequence

        membership_transaction_sequence: int | None | Unset
        if isinstance(self.membership_transaction_sequence, Unset):
            membership_transaction_sequence = UNSET
        else:
            membership_transaction_sequence = self.membership_transaction_sequence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "category": category,
                "joined_date": joined_date,
                "lifetime_membership": lifetime_membership,
                "print_renewals": print_renewals,
                "total_members": total_members,
                "total_children": total_children,
            }
        )
        if membership_id is not UNSET:
            field_dict["membership_id"] = membership_id
        if dues is not UNSET:
            field_dict["dues"] = dues
        if program is not UNSET:
            field_dict["program"] = program
        if reason is not UNSET:
            field_dict["reason"] = reason
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if expires_on_date is not UNSET:
            field_dict["expires_on_date"] = expires_on_date
        if mem_comment is not UNSET:
            field_dict["mem_comment"] = mem_comment
        if member_sequence is not UNSET:
            field_dict["member_sequence"] = member_sequence
        if membership_transaction_sequence is not UNSET:
            field_dict["membership_transaction_sequence"] = (
                membership_transaction_sequence
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category
        from ..models.code_table_entry import CodeTableEntry
        from ..models.sub_category import SubCategory

        d = dict(src_dict)
        category = Category.from_dict(d.pop("category"))

        joined_date = isoparse(d.pop("joined_date")).date()

        lifetime_membership = d.pop("lifetime_membership")

        print_renewals = d.pop("print_renewals")

        total_members = d.pop("total_members")

        total_children = d.pop("total_children")

        def _parse_membership_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        membership_id = _parse_membership_id(d.pop("membership_id", UNSET))

        def _parse_dues(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dues = _parse_dues(d.pop("dues", UNSET))

        _program = d.pop("program", UNSET)
        program: CodeTableEntry | Unset
        if isinstance(_program, Unset):
            program = UNSET
        else:
            program = CodeTableEntry.from_dict(_program)

        _reason = d.pop("reason", UNSET)
        reason: CodeTableEntry | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = CodeTableEntry.from_dict(_reason)

        _subcategory = d.pop("subcategory", UNSET)
        subcategory: SubCategory | Unset
        if isinstance(_subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = SubCategory.from_dict(_subcategory)

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

        def _parse_mem_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mem_comment = _parse_mem_comment(d.pop("mem_comment", UNSET))

        def _parse_member_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        member_sequence = _parse_member_sequence(d.pop("member_sequence", UNSET))

        def _parse_membership_transaction_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        membership_transaction_sequence = _parse_membership_transaction_sequence(
            d.pop("membership_transaction_sequence", UNSET)
        )

        membership_create = cls(
            category=category,
            joined_date=joined_date,
            lifetime_membership=lifetime_membership,
            print_renewals=print_renewals,
            total_members=total_members,
            total_children=total_children,
            membership_id=membership_id,
            dues=dues,
            program=program,
            reason=reason,
            subcategory=subcategory,
            expires_on_date=expires_on_date,
            mem_comment=mem_comment,
            member_sequence=member_sequence,
            membership_transaction_sequence=membership_transaction_sequence,
        )

        return membership_create

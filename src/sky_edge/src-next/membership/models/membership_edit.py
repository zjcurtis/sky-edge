from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category
    from ..models.code_table_entry import CodeTableEntry
    from ..models.sub_category import SubCategory


T = TypeVar("T", bound="MembershipEdit")


@_attrs_define
class MembershipEdit:
    """Membership update request model

    Attributes:
        membership_id (None | str | Unset): The membership identifier associated with the membership.
        dues (float | None | Unset): The dues for the membership transaction.
        program (CodeTableEntry | Unset): A predefined entry in a code table.
        subcategory (SubCategory | Unset): SubCategory drop down data
        category (Category | Unset): Category drop down data
        activity_date (datetime.date | None | Unset): The create, renewal, rejoin, or drop date of the transaction.
        lifetime_membership (bool | Unset): Gets or sets value to lifetime membership.
        expires_on_date (datetime.date | None | Unset): Gets or sets the date on which the membership expires.
        print_renewals (bool | Unset): Gets or sets value to print renewals.
        total_members (int | None | Unset): Gets or sets the value of total members allowed in this membership Default:
            1.
        total_children (int | None | Unset): Gets or sets the value of total children allowed in this membership
            Default: 0.
        notes (None | str | Unset): Gets or sets the membership notes.
        reason (CodeTableEntry | Unset): A predefined entry in a code table.
        mem_comment (None | str | Unset): Gets or sets value of comment.
    """

    membership_id: None | str | Unset = UNSET
    dues: float | None | Unset = UNSET
    program: CodeTableEntry | Unset = UNSET
    subcategory: SubCategory | Unset = UNSET
    category: Category | Unset = UNSET
    activity_date: datetime.date | None | Unset = UNSET
    lifetime_membership: bool | Unset = UNSET
    expires_on_date: datetime.date | None | Unset = UNSET
    print_renewals: bool | Unset = UNSET
    total_members: int | None | Unset = 1
    total_children: int | None | Unset = 0
    notes: None | str | Unset = UNSET
    reason: CodeTableEntry | Unset = UNSET
    mem_comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        subcategory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subcategory, Unset):
            subcategory = self.subcategory.to_dict()

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        activity_date: None | str | Unset
        if isinstance(self.activity_date, Unset):
            activity_date = UNSET
        elif isinstance(self.activity_date, datetime.date):
            activity_date = self.activity_date.isoformat()
        else:
            activity_date = self.activity_date

        lifetime_membership = self.lifetime_membership

        expires_on_date: None | str | Unset
        if isinstance(self.expires_on_date, Unset):
            expires_on_date = UNSET
        elif isinstance(self.expires_on_date, datetime.date):
            expires_on_date = self.expires_on_date.isoformat()
        else:
            expires_on_date = self.expires_on_date

        print_renewals = self.print_renewals

        total_members: int | None | Unset
        if isinstance(self.total_members, Unset):
            total_members = UNSET
        else:
            total_members = self.total_members

        total_children: int | None | Unset
        if isinstance(self.total_children, Unset):
            total_children = UNSET
        else:
            total_children = self.total_children

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        mem_comment: None | str | Unset
        if isinstance(self.mem_comment, Unset):
            mem_comment = UNSET
        else:
            mem_comment = self.mem_comment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if membership_id is not UNSET:
            field_dict["membership_id"] = membership_id
        if dues is not UNSET:
            field_dict["dues"] = dues
        if program is not UNSET:
            field_dict["program"] = program
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if category is not UNSET:
            field_dict["category"] = category
        if activity_date is not UNSET:
            field_dict["activity_date"] = activity_date
        if lifetime_membership is not UNSET:
            field_dict["lifetime_membership"] = lifetime_membership
        if expires_on_date is not UNSET:
            field_dict["expires_on_date"] = expires_on_date
        if print_renewals is not UNSET:
            field_dict["print_renewals"] = print_renewals
        if total_members is not UNSET:
            field_dict["total_members"] = total_members
        if total_children is not UNSET:
            field_dict["total_children"] = total_children
        if notes is not UNSET:
            field_dict["notes"] = notes
        if reason is not UNSET:
            field_dict["reason"] = reason
        if mem_comment is not UNSET:
            field_dict["mem_comment"] = mem_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category
        from ..models.code_table_entry import CodeTableEntry
        from ..models.sub_category import SubCategory

        d = dict(src_dict)

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

        _subcategory = d.pop("subcategory", UNSET)
        subcategory: SubCategory | Unset
        if isinstance(_subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = SubCategory.from_dict(_subcategory)

        _category = d.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)

        def _parse_activity_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                activity_date_type_0 = isoparse(data).date()

                return activity_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        activity_date = _parse_activity_date(d.pop("activity_date", UNSET))

        lifetime_membership = d.pop("lifetime_membership", UNSET)

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

        print_renewals = d.pop("print_renewals", UNSET)

        def _parse_total_members(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_members = _parse_total_members(d.pop("total_members", UNSET))

        def _parse_total_children(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_children = _parse_total_children(d.pop("total_children", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _reason = d.pop("reason", UNSET)
        reason: CodeTableEntry | Unset
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = CodeTableEntry.from_dict(_reason)

        def _parse_mem_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mem_comment = _parse_mem_comment(d.pop("mem_comment", UNSET))

        membership_edit = cls(
            membership_id=membership_id,
            dues=dues,
            program=program,
            subcategory=subcategory,
            category=category,
            activity_date=activity_date,
            lifetime_membership=lifetime_membership,
            expires_on_date=expires_on_date,
            print_renewals=print_renewals,
            total_members=total_members,
            total_children=total_children,
            notes=notes,
            reason=reason,
            mem_comment=mem_comment,
        )

        return membership_edit

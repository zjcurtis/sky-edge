from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.membership_rejoin_rejoin_type import MembershipRejoinRejoinType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category
    from ..models.code_table_entry import CodeTableEntry
    from ..models.sub_category import SubCategory


T = TypeVar("T", bound="MembershipRejoin")


@_attrs_define
class MembershipRejoin:
    """Membership rejoin request model

    Attributes:
        rejoin_type (MembershipRejoinRejoinType): The rejoin type indicating whether the membership level is changing.
            Use 'Same' when the membership level is not changing, 'Upgrade' when moving to a higher level,
            or 'Downgrade' when moving to a lower level.
        dues (float): The dues for the membership rejoin transaction.
        program (CodeTableEntry | Unset): A predefined entry in a code table.
        reason (CodeTableEntry | Unset): A predefined entry in a code table.
        subcategory (SubCategory | Unset): SubCategory drop down data
        category (Category | Unset): Category drop down data
        rejoin_date (datetime.date | None | Unset): The rejoin date of the transaction. If not provided and the business
            rule
            "Default 'Rejoined on' date to previous 'Expires' date" is enabled,
            this will default to the previous transaction's expires date.
        lifetime_membership (bool | Unset): Gets or sets value to lifetime membership.
        expires_on_date (datetime.date | None | Unset): Gets or sets the date on which the membership expires.
            If not provided and the membership category has expiration defaults configured,
            this will be calculated automatically based on the category settings.
        print_renewals (bool | None | Unset): Gets or sets value to print renewals.
        mem_comment (None | str | Unset): Gets or sets value of comment.
    """

    rejoin_type: MembershipRejoinRejoinType
    dues: float
    program: CodeTableEntry | Unset = UNSET
    reason: CodeTableEntry | Unset = UNSET
    subcategory: SubCategory | Unset = UNSET
    category: Category | Unset = UNSET
    rejoin_date: datetime.date | None | Unset = UNSET
    lifetime_membership: bool | Unset = UNSET
    expires_on_date: datetime.date | None | Unset = UNSET
    print_renewals: bool | None | Unset = UNSET
    mem_comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        rejoin_type = self.rejoin_type.value

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

        category: dict[str, Any] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        rejoin_date: None | str | Unset
        if isinstance(self.rejoin_date, Unset):
            rejoin_date = UNSET
        elif isinstance(self.rejoin_date, datetime.date):
            rejoin_date = self.rejoin_date.isoformat()
        else:
            rejoin_date = self.rejoin_date

        lifetime_membership = self.lifetime_membership

        expires_on_date: None | str | Unset
        if isinstance(self.expires_on_date, Unset):
            expires_on_date = UNSET
        elif isinstance(self.expires_on_date, datetime.date):
            expires_on_date = self.expires_on_date.isoformat()
        else:
            expires_on_date = self.expires_on_date

        print_renewals: bool | None | Unset
        if isinstance(self.print_renewals, Unset):
            print_renewals = UNSET
        else:
            print_renewals = self.print_renewals

        mem_comment: None | str | Unset
        if isinstance(self.mem_comment, Unset):
            mem_comment = UNSET
        else:
            mem_comment = self.mem_comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "rejoin_type": rejoin_type,
                "dues": dues,
            }
        )
        if program is not UNSET:
            field_dict["program"] = program
        if reason is not UNSET:
            field_dict["reason"] = reason
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if category is not UNSET:
            field_dict["category"] = category
        if rejoin_date is not UNSET:
            field_dict["rejoin_date"] = rejoin_date
        if lifetime_membership is not UNSET:
            field_dict["lifetime_membership"] = lifetime_membership
        if expires_on_date is not UNSET:
            field_dict["expires_on_date"] = expires_on_date
        if print_renewals is not UNSET:
            field_dict["print_renewals"] = print_renewals
        if mem_comment is not UNSET:
            field_dict["mem_comment"] = mem_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category
        from ..models.code_table_entry import CodeTableEntry
        from ..models.sub_category import SubCategory

        d = dict(src_dict)
        rejoin_type = MembershipRejoinRejoinType(d.pop("rejoin_type"))

        dues = d.pop("dues")

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

        _category = d.pop("category", UNSET)
        category: Category | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = Category.from_dict(_category)

        def _parse_rejoin_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rejoin_date_type_0 = isoparse(data).date()

                return rejoin_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        rejoin_date = _parse_rejoin_date(d.pop("rejoin_date", UNSET))

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

        def _parse_print_renewals(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        print_renewals = _parse_print_renewals(d.pop("print_renewals", UNSET))

        def _parse_mem_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mem_comment = _parse_mem_comment(d.pop("mem_comment", UNSET))

        membership_rejoin = cls(
            rejoin_type=rejoin_type,
            dues=dues,
            program=program,
            reason=reason,
            subcategory=subcategory,
            category=category,
            rejoin_date=rejoin_date,
            lifetime_membership=lifetime_membership,
            expires_on_date=expires_on_date,
            print_renewals=print_renewals,
            mem_comment=mem_comment,
        )

        return membership_rejoin

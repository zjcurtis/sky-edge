from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.membership_history_membership_type import MembershipHistoryMembershipType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_gift import TransactionGift


T = TypeVar("T", bound="MembershipHistory")


@_attrs_define
class MembershipHistory:
    """Membership history contains all transaction related to membership.

    Attributes:
        id (None | str | Unset): The immutable system record ID of the membership history.
        category_name (None | str | Unset): The membership category name.
        program_name (None | str | Unset): The membership program name.
        sub_category_name (None | str | Unset): The membership subcategory name.
        reason (None | str | Unset): The selected reason for membership.
        membership_comment (None | str | Unset): The membership comment for membership.
        activity_date (datetime.date | Unset): The membership activity date.
        type_ (MembershipHistoryMembershipType | Unset): The membership type. Possible values include: Joined, Dropped,
            Upgraded, Downgraded, Renewal and Rejoined.
        gifts (list[TransactionGift] | None | Unset): The list of gifts associated with membership.
    """

    id: None | str | Unset = UNSET
    category_name: None | str | Unset = UNSET
    program_name: None | str | Unset = UNSET
    sub_category_name: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    membership_comment: None | str | Unset = UNSET
    activity_date: datetime.date | Unset = UNSET
    type_: MembershipHistoryMembershipType | Unset = UNSET
    gifts: list[TransactionGift] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        category_name: None | str | Unset
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        program_name: None | str | Unset
        if isinstance(self.program_name, Unset):
            program_name = UNSET
        else:
            program_name = self.program_name

        sub_category_name: None | str | Unset
        if isinstance(self.sub_category_name, Unset):
            sub_category_name = UNSET
        else:
            sub_category_name = self.sub_category_name

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        membership_comment: None | str | Unset
        if isinstance(self.membership_comment, Unset):
            membership_comment = UNSET
        else:
            membership_comment = self.membership_comment

        activity_date: str | Unset = UNSET
        if not isinstance(self.activity_date, Unset):
            activity_date = self.activity_date.isoformat()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        gifts: list[dict[str, Any]] | None | Unset
        if isinstance(self.gifts, Unset):
            gifts = UNSET
        elif isinstance(self.gifts, list):
            gifts = []
            for gifts_type_0_item_data in self.gifts:
                gifts_type_0_item = gifts_type_0_item_data.to_dict()
                gifts.append(gifts_type_0_item)

        else:
            gifts = self.gifts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if program_name is not UNSET:
            field_dict["program_name"] = program_name
        if sub_category_name is not UNSET:
            field_dict["sub_category_name"] = sub_category_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if membership_comment is not UNSET:
            field_dict["membership_comment"] = membership_comment
        if activity_date is not UNSET:
            field_dict["activity_date"] = activity_date
        if type_ is not UNSET:
            field_dict["type"] = type_
        if gifts is not UNSET:
            field_dict["gifts"] = gifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_gift import TransactionGift

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_name = _parse_category_name(d.pop("category_name", UNSET))

        def _parse_program_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_name = _parse_program_name(d.pop("program_name", UNSET))

        def _parse_sub_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_category_name = _parse_sub_category_name(d.pop("sub_category_name", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_membership_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        membership_comment = _parse_membership_comment(d.pop("membership_comment", UNSET))

        _activity_date = d.pop("activity_date", UNSET)
        activity_date: datetime.date | Unset
        if isinstance(_activity_date, Unset):
            activity_date = UNSET
        else:
            activity_date = isoparse(_activity_date).date()

        _type_ = d.pop("type", UNSET)
        type_: MembershipHistoryMembershipType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MembershipHistoryMembershipType(_type_)

        def _parse_gifts(data: object) -> list[TransactionGift] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gifts_type_0 = []
                _gifts_type_0 = data
                for gifts_type_0_item_data in _gifts_type_0:
                    gifts_type_0_item = TransactionGift.from_dict(gifts_type_0_item_data)

                    gifts_type_0.append(gifts_type_0_item)

                return gifts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TransactionGift] | None | Unset, data)

        gifts = _parse_gifts(d.pop("gifts", UNSET))

        membership_history = cls(
            id=id,
            category_name=category_name,
            program_name=program_name,
            sub_category_name=sub_category_name,
            reason=reason,
            membership_comment=membership_comment,
            activity_date=activity_date,
            type_=type_,
            gifts=gifts,
        )

        return membership_history

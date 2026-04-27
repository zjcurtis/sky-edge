from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.membership_create_v2_membership_benefits_send_to import MembershipCreateV2MembershipBenefitsSendTo
from ..models.membership_create_v2_renewal_notice_type import MembershipCreateV2RenewalNoticeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category import Category
    from ..models.code_table_entry import CodeTableEntry
    from ..models.link_gift_create import LinkGiftCreate
    from ..models.membership_add_form_card_create import MembershipAddFormCardCreate
    from ..models.membership_benefit_create import MembershipBenefitCreate
    from ..models.sub_category import SubCategory


T = TypeVar("T", bound="MembershipCreateV2")


@_attrs_define
class MembershipCreateV2:
    """Membership create request model

    Attributes:
        category (Category): Category drop down data
        joined_date (datetime.date): The create, renewal, rejoin, or drop date of the transaction.
        lifetime_membership (bool): Gets or sets value to lifetime membership.
        print_renewals (bool): Gets or sets value to print renewals.
        total_members (int): Gets or sets the value of total members allowed in this membership Default: 1.
        total_children (int): Gets or sets the value of total children allowed in this membership Default: 0.
        send_benefits_to (MembershipCreateV2MembershipBenefitsSendTo | Unset): Specifies the recipient of the benefits
            Default: MembershipCreateV2MembershipBenefitsSendTo.PRIMARYMEMBER.
        benefits_notes (None | str | Unset): Benefits notes
        membership_cards (list[MembershipAddFormCardCreate] | None | Unset): List of member and cards
        membership_benefits (list[MembershipBenefitCreate] | None | Unset): List of membership benefits
        given_by_id (None | str | Unset): The ID of the constituent giving this membership as a gift.
        special_message (None | str | Unset): Special message
        membership_fundraisers (list[int] | None | Unset): List of membership fundraisers
        membership_link_gift (LinkGiftCreate | Unset): Create memberships link to gift
        default_card (bool | Unset): Field to find out wheather the card is default or not Default: False.
        default_benefits (bool | Unset): Field to find out wheather the benefits is default or not Default: False.
        override_renewal_defaults (bool | Unset): Field to find out wheather to override renewal is defaults or not
        send_notice_to (MembershipCreateV2RenewalNoticeType | Unset): Field to find out wheather the send notice
            Default: MembershipCreateV2RenewalNoticeType.DONOR.
        waive_benefits (bool | Unset): Waive Benefits
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
    send_benefits_to: MembershipCreateV2MembershipBenefitsSendTo | Unset = (
        MembershipCreateV2MembershipBenefitsSendTo.PRIMARYMEMBER
    )
    benefits_notes: None | str | Unset = UNSET
    membership_cards: list[MembershipAddFormCardCreate] | None | Unset = UNSET
    membership_benefits: list[MembershipBenefitCreate] | None | Unset = UNSET
    given_by_id: None | str | Unset = UNSET
    special_message: None | str | Unset = UNSET
    membership_fundraisers: list[int] | None | Unset = UNSET
    membership_link_gift: LinkGiftCreate | Unset = UNSET
    default_card: bool | Unset = False
    default_benefits: bool | Unset = False
    override_renewal_defaults: bool | Unset = UNSET
    send_notice_to: MembershipCreateV2RenewalNoticeType | Unset = MembershipCreateV2RenewalNoticeType.DONOR
    waive_benefits: bool | Unset = UNSET
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

        send_benefits_to: str | Unset = UNSET
        if not isinstance(self.send_benefits_to, Unset):
            send_benefits_to = self.send_benefits_to.value

        benefits_notes: None | str | Unset
        if isinstance(self.benefits_notes, Unset):
            benefits_notes = UNSET
        else:
            benefits_notes = self.benefits_notes

        membership_cards: list[dict[str, Any]] | None | Unset
        if isinstance(self.membership_cards, Unset):
            membership_cards = UNSET
        elif isinstance(self.membership_cards, list):
            membership_cards = []
            for membership_cards_type_0_item_data in self.membership_cards:
                membership_cards_type_0_item = membership_cards_type_0_item_data.to_dict()
                membership_cards.append(membership_cards_type_0_item)

        else:
            membership_cards = self.membership_cards

        membership_benefits: list[dict[str, Any]] | None | Unset
        if isinstance(self.membership_benefits, Unset):
            membership_benefits = UNSET
        elif isinstance(self.membership_benefits, list):
            membership_benefits = []
            for membership_benefits_type_0_item_data in self.membership_benefits:
                membership_benefits_type_0_item = membership_benefits_type_0_item_data.to_dict()
                membership_benefits.append(membership_benefits_type_0_item)

        else:
            membership_benefits = self.membership_benefits

        given_by_id: None | str | Unset
        if isinstance(self.given_by_id, Unset):
            given_by_id = UNSET
        else:
            given_by_id = self.given_by_id

        special_message: None | str | Unset
        if isinstance(self.special_message, Unset):
            special_message = UNSET
        else:
            special_message = self.special_message

        membership_fundraisers: list[int] | None | Unset
        if isinstance(self.membership_fundraisers, Unset):
            membership_fundraisers = UNSET
        elif isinstance(self.membership_fundraisers, list):
            membership_fundraisers = self.membership_fundraisers

        else:
            membership_fundraisers = self.membership_fundraisers

        membership_link_gift: dict[str, Any] | Unset = UNSET
        if not isinstance(self.membership_link_gift, Unset):
            membership_link_gift = self.membership_link_gift.to_dict()

        default_card = self.default_card

        default_benefits = self.default_benefits

        override_renewal_defaults = self.override_renewal_defaults

        send_notice_to: str | Unset = UNSET
        if not isinstance(self.send_notice_to, Unset):
            send_notice_to = self.send_notice_to.value

        waive_benefits = self.waive_benefits

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
        if send_benefits_to is not UNSET:
            field_dict["send_benefits_to"] = send_benefits_to
        if benefits_notes is not UNSET:
            field_dict["benefits_notes"] = benefits_notes
        if membership_cards is not UNSET:
            field_dict["membership_cards"] = membership_cards
        if membership_benefits is not UNSET:
            field_dict["membership_benefits"] = membership_benefits
        if given_by_id is not UNSET:
            field_dict["given_by_id"] = given_by_id
        if special_message is not UNSET:
            field_dict["special_message"] = special_message
        if membership_fundraisers is not UNSET:
            field_dict["membership_fundraisers"] = membership_fundraisers
        if membership_link_gift is not UNSET:
            field_dict["membership_link_gift"] = membership_link_gift
        if default_card is not UNSET:
            field_dict["default_card"] = default_card
        if default_benefits is not UNSET:
            field_dict["default_benefits"] = default_benefits
        if override_renewal_defaults is not UNSET:
            field_dict["override_renewal_defaults"] = override_renewal_defaults
        if send_notice_to is not UNSET:
            field_dict["send_notice_to"] = send_notice_to
        if waive_benefits is not UNSET:
            field_dict["waive_benefits"] = waive_benefits
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
            field_dict["membership_transaction_sequence"] = membership_transaction_sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category import Category
        from ..models.code_table_entry import CodeTableEntry
        from ..models.link_gift_create import LinkGiftCreate
        from ..models.membership_add_form_card_create import MembershipAddFormCardCreate
        from ..models.membership_benefit_create import MembershipBenefitCreate
        from ..models.sub_category import SubCategory

        d = dict(src_dict)
        category = Category.from_dict(d.pop("category"))

        joined_date = isoparse(d.pop("joined_date")).date()

        lifetime_membership = d.pop("lifetime_membership")

        print_renewals = d.pop("print_renewals")

        total_members = d.pop("total_members")

        total_children = d.pop("total_children")

        _send_benefits_to = d.pop("send_benefits_to", UNSET)
        send_benefits_to: MembershipCreateV2MembershipBenefitsSendTo | Unset
        if isinstance(_send_benefits_to, Unset):
            send_benefits_to = UNSET
        else:
            send_benefits_to = MembershipCreateV2MembershipBenefitsSendTo(_send_benefits_to)

        def _parse_benefits_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        benefits_notes = _parse_benefits_notes(d.pop("benefits_notes", UNSET))

        def _parse_membership_cards(data: object) -> list[MembershipAddFormCardCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                membership_cards_type_0 = []
                _membership_cards_type_0 = data
                for membership_cards_type_0_item_data in _membership_cards_type_0:
                    membership_cards_type_0_item = MembershipAddFormCardCreate.from_dict(
                        membership_cards_type_0_item_data
                    )

                    membership_cards_type_0.append(membership_cards_type_0_item)

                return membership_cards_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipAddFormCardCreate] | None | Unset, data)

        membership_cards = _parse_membership_cards(d.pop("membership_cards", UNSET))

        def _parse_membership_benefits(data: object) -> list[MembershipBenefitCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                membership_benefits_type_0 = []
                _membership_benefits_type_0 = data
                for membership_benefits_type_0_item_data in _membership_benefits_type_0:
                    membership_benefits_type_0_item = MembershipBenefitCreate.from_dict(
                        membership_benefits_type_0_item_data
                    )

                    membership_benefits_type_0.append(membership_benefits_type_0_item)

                return membership_benefits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MembershipBenefitCreate] | None | Unset, data)

        membership_benefits = _parse_membership_benefits(d.pop("membership_benefits", UNSET))

        def _parse_given_by_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_by_id = _parse_given_by_id(d.pop("given_by_id", UNSET))

        def _parse_special_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        special_message = _parse_special_message(d.pop("special_message", UNSET))

        def _parse_membership_fundraisers(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                membership_fundraisers_type_0 = cast(list[int], data)

                return membership_fundraisers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        membership_fundraisers = _parse_membership_fundraisers(d.pop("membership_fundraisers", UNSET))

        _membership_link_gift = d.pop("membership_link_gift", UNSET)
        membership_link_gift: LinkGiftCreate | Unset
        if isinstance(_membership_link_gift, Unset):
            membership_link_gift = UNSET
        else:
            membership_link_gift = LinkGiftCreate.from_dict(_membership_link_gift)

        default_card = d.pop("default_card", UNSET)

        default_benefits = d.pop("default_benefits", UNSET)

        override_renewal_defaults = d.pop("override_renewal_defaults", UNSET)

        _send_notice_to = d.pop("send_notice_to", UNSET)
        send_notice_to: MembershipCreateV2RenewalNoticeType | Unset
        if isinstance(_send_notice_to, Unset):
            send_notice_to = UNSET
        else:
            send_notice_to = MembershipCreateV2RenewalNoticeType(_send_notice_to)

        waive_benefits = d.pop("waive_benefits", UNSET)

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

        membership_create_v2 = cls(
            category=category,
            joined_date=joined_date,
            lifetime_membership=lifetime_membership,
            print_renewals=print_renewals,
            total_members=total_members,
            total_children=total_children,
            send_benefits_to=send_benefits_to,
            benefits_notes=benefits_notes,
            membership_cards=membership_cards,
            membership_benefits=membership_benefits,
            given_by_id=given_by_id,
            special_message=special_message,
            membership_fundraisers=membership_fundraisers,
            membership_link_gift=membership_link_gift,
            default_card=default_card,
            default_benefits=default_benefits,
            override_renewal_defaults=override_renewal_defaults,
            send_notice_to=send_notice_to,
            waive_benefits=waive_benefits,
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

        return membership_create_v2

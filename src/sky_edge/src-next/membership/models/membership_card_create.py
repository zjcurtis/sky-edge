from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.membership_card_create_membership_card_expires import MembershipCardCreateMembershipCardExpires
from ..models.membership_card_create_membership_cards_address_to_print import (
    MembershipCardCreateMembershipCardsAddressToPrint,
)
from ..models.membership_card_create_membership_cards_status import MembershipCardCreateMembershipCardsStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry


T = TypeVar("T", bound="MembershipCardCreate")


@_attrs_define
class MembershipCardCreate:
    """Create memberships and cards

    Attributes:
        name_on_card (str): Name of member on card
        editable (bool | Unset): Membership Card's editable field
        constit_add_sal_id (int | None | Unset): Membership card's constituent salutation ID
        relation_type (CodeTableEntry | Unset): A predefined entry in a code table.
        card_expires (MembershipCardCreateMembershipCardExpires | Unset): Membership card's card expire
        address_to_print (MembershipCardCreateMembershipCardsAddressToPrint | Unset): Membership card's address to print
            Default: MembershipCardCreateMembershipCardsAddressToPrint.PRIMARYMEMBER.
        valid_from_date (datetime.date | None | Unset): Membership card's valid from date
        relationship_id (int | None | Unset): Membership card's relationship ID
        joint_member (bool | Unset): Whether the member is a joint member or not
        joint_member_id (int | None | Unset): Joint member ID
        card_member (bool | Unset): Whether a card member is checked
        no_of_cards (int | Unset): Number of cards
        valid_to_date (datetime.date | None | Unset): Membership card's valid To date
        last_printed_on_date (datetime.date | None | Unset): Last printed on date
        card_type (CodeTableEntry | Unset): A predefined entry in a code table.
        status (MembershipCardCreateMembershipCardsStatus | Unset): Status of membership card Default:
            MembershipCardCreateMembershipCardsStatus.NOTPRINTED.
    """

    name_on_card: str
    editable: bool | Unset = UNSET
    constit_add_sal_id: int | None | Unset = UNSET
    relation_type: CodeTableEntry | Unset = UNSET
    card_expires: MembershipCardCreateMembershipCardExpires | Unset = UNSET
    address_to_print: MembershipCardCreateMembershipCardsAddressToPrint | Unset = (
        MembershipCardCreateMembershipCardsAddressToPrint.PRIMARYMEMBER
    )
    valid_from_date: datetime.date | None | Unset = UNSET
    relationship_id: int | None | Unset = UNSET
    joint_member: bool | Unset = UNSET
    joint_member_id: int | None | Unset = UNSET
    card_member: bool | Unset = UNSET
    no_of_cards: int | Unset = UNSET
    valid_to_date: datetime.date | None | Unset = UNSET
    last_printed_on_date: datetime.date | None | Unset = UNSET
    card_type: CodeTableEntry | Unset = UNSET
    status: MembershipCardCreateMembershipCardsStatus | Unset = MembershipCardCreateMembershipCardsStatus.NOTPRINTED

    def to_dict(self) -> dict[str, Any]:
        name_on_card = self.name_on_card

        editable = self.editable

        constit_add_sal_id: int | None | Unset
        if isinstance(self.constit_add_sal_id, Unset):
            constit_add_sal_id = UNSET
        else:
            constit_add_sal_id = self.constit_add_sal_id

        relation_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation_type, Unset):
            relation_type = self.relation_type.to_dict()

        card_expires: str | Unset = UNSET
        if not isinstance(self.card_expires, Unset):
            card_expires = self.card_expires.value

        address_to_print: str | Unset = UNSET
        if not isinstance(self.address_to_print, Unset):
            address_to_print = self.address_to_print.value

        valid_from_date: None | str | Unset
        if isinstance(self.valid_from_date, Unset):
            valid_from_date = UNSET
        elif isinstance(self.valid_from_date, datetime.date):
            valid_from_date = self.valid_from_date.isoformat()
        else:
            valid_from_date = self.valid_from_date

        relationship_id: int | None | Unset
        if isinstance(self.relationship_id, Unset):
            relationship_id = UNSET
        else:
            relationship_id = self.relationship_id

        joint_member = self.joint_member

        joint_member_id: int | None | Unset
        if isinstance(self.joint_member_id, Unset):
            joint_member_id = UNSET
        else:
            joint_member_id = self.joint_member_id

        card_member = self.card_member

        no_of_cards = self.no_of_cards

        valid_to_date: None | str | Unset
        if isinstance(self.valid_to_date, Unset):
            valid_to_date = UNSET
        elif isinstance(self.valid_to_date, datetime.date):
            valid_to_date = self.valid_to_date.isoformat()
        else:
            valid_to_date = self.valid_to_date

        last_printed_on_date: None | str | Unset
        if isinstance(self.last_printed_on_date, Unset):
            last_printed_on_date = UNSET
        elif isinstance(self.last_printed_on_date, datetime.date):
            last_printed_on_date = self.last_printed_on_date.isoformat()
        else:
            last_printed_on_date = self.last_printed_on_date

        card_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card_type, Unset):
            card_type = self.card_type.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name_on_card": name_on_card,
            }
        )
        if editable is not UNSET:
            field_dict["editable"] = editable
        if constit_add_sal_id is not UNSET:
            field_dict["constit_add_sal_id"] = constit_add_sal_id
        if relation_type is not UNSET:
            field_dict["relation_type"] = relation_type
        if card_expires is not UNSET:
            field_dict["card_expires"] = card_expires
        if address_to_print is not UNSET:
            field_dict["address_to_print"] = address_to_print
        if valid_from_date is not UNSET:
            field_dict["valid_from_date"] = valid_from_date
        if relationship_id is not UNSET:
            field_dict["relationship_id"] = relationship_id
        if joint_member is not UNSET:
            field_dict["joint_member"] = joint_member
        if joint_member_id is not UNSET:
            field_dict["joint_member_id"] = joint_member_id
        if card_member is not UNSET:
            field_dict["card_member"] = card_member
        if no_of_cards is not UNSET:
            field_dict["no_of_cards"] = no_of_cards
        if valid_to_date is not UNSET:
            field_dict["valid_to_date"] = valid_to_date
        if last_printed_on_date is not UNSET:
            field_dict["last_printed_on_date"] = last_printed_on_date
        if card_type is not UNSET:
            field_dict["card_type"] = card_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry

        d = dict(src_dict)
        name_on_card = d.pop("name_on_card")

        editable = d.pop("editable", UNSET)

        def _parse_constit_add_sal_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        constit_add_sal_id = _parse_constit_add_sal_id(d.pop("constit_add_sal_id", UNSET))

        _relation_type = d.pop("relation_type", UNSET)
        relation_type: CodeTableEntry | Unset
        if isinstance(_relation_type, Unset):
            relation_type = UNSET
        else:
            relation_type = CodeTableEntry.from_dict(_relation_type)

        _card_expires = d.pop("card_expires", UNSET)
        card_expires: MembershipCardCreateMembershipCardExpires | Unset
        if isinstance(_card_expires, Unset):
            card_expires = UNSET
        else:
            card_expires = MembershipCardCreateMembershipCardExpires(_card_expires)

        _address_to_print = d.pop("address_to_print", UNSET)
        address_to_print: MembershipCardCreateMembershipCardsAddressToPrint | Unset
        if isinstance(_address_to_print, Unset):
            address_to_print = UNSET
        else:
            address_to_print = MembershipCardCreateMembershipCardsAddressToPrint(_address_to_print)

        def _parse_valid_from_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_date_type_0 = isoparse(data).date()

                return valid_from_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        valid_from_date = _parse_valid_from_date(d.pop("valid_from_date", UNSET))

        def _parse_relationship_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        relationship_id = _parse_relationship_id(d.pop("relationship_id", UNSET))

        joint_member = d.pop("joint_member", UNSET)

        def _parse_joint_member_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        joint_member_id = _parse_joint_member_id(d.pop("joint_member_id", UNSET))

        card_member = d.pop("card_member", UNSET)

        no_of_cards = d.pop("no_of_cards", UNSET)

        def _parse_valid_to_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_to_date_type_0 = isoparse(data).date()

                return valid_to_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        valid_to_date = _parse_valid_to_date(d.pop("valid_to_date", UNSET))

        def _parse_last_printed_on_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_printed_on_date_type_0 = isoparse(data).date()

                return last_printed_on_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_printed_on_date = _parse_last_printed_on_date(d.pop("last_printed_on_date", UNSET))

        _card_type = d.pop("card_type", UNSET)
        card_type: CodeTableEntry | Unset
        if isinstance(_card_type, Unset):
            card_type = UNSET
        else:
            card_type = CodeTableEntry.from_dict(_card_type)

        _status = d.pop("status", UNSET)
        status: MembershipCardCreateMembershipCardsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MembershipCardCreateMembershipCardsStatus(_status)

        membership_card_create = cls(
            name_on_card=name_on_card,
            editable=editable,
            constit_add_sal_id=constit_add_sal_id,
            relation_type=relation_type,
            card_expires=card_expires,
            address_to_print=address_to_print,
            valid_from_date=valid_from_date,
            relationship_id=relationship_id,
            joint_member=joint_member,
            joint_member_id=joint_member_id,
            card_member=card_member,
            no_of_cards=no_of_cards,
            valid_to_date=valid_to_date,
            last_printed_on_date=last_printed_on_date,
            card_type=card_type,
            status=status,
        )

        return membership_card_create

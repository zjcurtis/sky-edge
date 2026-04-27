from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipCard")


@_attrs_define
class MembershipCard:
    """Membership Card Response Model

    Attributes:
        membership_cards_id (int | Unset): Membership Cards ID
        membership_id (int | Unset): Membership ID
        joint_member (bool | Unset): Whether the member is a joint member or not
        joint_member_id (int | None | Unset): Joint Member ID
        member_name (None | str | Unset): Member's Display Name
        name_on_card (None | str | Unset): Name Of Member On Card
        relation (None | str | Unset): Relation with primary member
        primary (bool | Unset): Whether a Primary Member
        card_member (bool | Unset): Whether the member have a card
        number_of_cards (int | Unset): Number Of Cards
        card_type (None | str | Unset): Type Of Membership Card
        status (None | str | Unset): Status Of Membership Card. The available values are "Printed", "NotPrinted",
            "DoNotPrint", and "Lost".
        valid_to_date (datetime.datetime | None | Unset): Membership Card's Valid To Date
        last_printed_on (datetime.datetime | None | Unset): Last Printed Date
        sequence (int | Unset): Sequence of membership cards
        card_expires (None | str | Unset): Card expiration setting. The available values are "SameDates",
            "OneWeekAfter", "TwoWeeksAfter", "OneMonthAfter", "TwoMonthsAfter", "ThreeMonthsAfter", "OneDayAfter",
            "TwoDaysAfter", "ThreeDaysAfter", "SpecificDates", and "Lifetime".
        address_to_print (None | str | Unset): Address to print option. The available values are "PrimaryMember",
            "None", and "Constituent".
        valid_from_date (datetime.datetime | None | Unset): Valid from date for the membership card
        editable (bool | Unset): Whether the name on the card is editable
    """

    membership_cards_id: int | Unset = UNSET
    membership_id: int | Unset = UNSET
    joint_member: bool | Unset = UNSET
    joint_member_id: int | None | Unset = UNSET
    member_name: None | str | Unset = UNSET
    name_on_card: None | str | Unset = UNSET
    relation: None | str | Unset = UNSET
    primary: bool | Unset = UNSET
    card_member: bool | Unset = UNSET
    number_of_cards: int | Unset = UNSET
    card_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    valid_to_date: datetime.datetime | None | Unset = UNSET
    last_printed_on: datetime.datetime | None | Unset = UNSET
    sequence: int | Unset = UNSET
    card_expires: None | str | Unset = UNSET
    address_to_print: None | str | Unset = UNSET
    valid_from_date: datetime.datetime | None | Unset = UNSET
    editable: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        membership_cards_id = self.membership_cards_id

        membership_id = self.membership_id

        joint_member = self.joint_member

        joint_member_id: int | None | Unset
        if isinstance(self.joint_member_id, Unset):
            joint_member_id = UNSET
        else:
            joint_member_id = self.joint_member_id

        member_name: None | str | Unset
        if isinstance(self.member_name, Unset):
            member_name = UNSET
        else:
            member_name = self.member_name

        name_on_card: None | str | Unset
        if isinstance(self.name_on_card, Unset):
            name_on_card = UNSET
        else:
            name_on_card = self.name_on_card

        relation: None | str | Unset
        if isinstance(self.relation, Unset):
            relation = UNSET
        else:
            relation = self.relation

        primary = self.primary

        card_member = self.card_member

        number_of_cards = self.number_of_cards

        card_type: None | str | Unset
        if isinstance(self.card_type, Unset):
            card_type = UNSET
        else:
            card_type = self.card_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        valid_to_date: None | str | Unset
        if isinstance(self.valid_to_date, Unset):
            valid_to_date = UNSET
        elif isinstance(self.valid_to_date, datetime.datetime):
            valid_to_date = self.valid_to_date.isoformat()
        else:
            valid_to_date = self.valid_to_date

        last_printed_on: None | str | Unset
        if isinstance(self.last_printed_on, Unset):
            last_printed_on = UNSET
        elif isinstance(self.last_printed_on, datetime.datetime):
            last_printed_on = self.last_printed_on.isoformat()
        else:
            last_printed_on = self.last_printed_on

        sequence = self.sequence

        card_expires: None | str | Unset
        if isinstance(self.card_expires, Unset):
            card_expires = UNSET
        else:
            card_expires = self.card_expires

        address_to_print: None | str | Unset
        if isinstance(self.address_to_print, Unset):
            address_to_print = UNSET
        else:
            address_to_print = self.address_to_print

        valid_from_date: None | str | Unset
        if isinstance(self.valid_from_date, Unset):
            valid_from_date = UNSET
        elif isinstance(self.valid_from_date, datetime.datetime):
            valid_from_date = self.valid_from_date.isoformat()
        else:
            valid_from_date = self.valid_from_date

        editable = self.editable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if membership_cards_id is not UNSET:
            field_dict["membership_cards_id"] = membership_cards_id
        if membership_id is not UNSET:
            field_dict["membership_id"] = membership_id
        if joint_member is not UNSET:
            field_dict["joint_member"] = joint_member
        if joint_member_id is not UNSET:
            field_dict["joint_member_id"] = joint_member_id
        if member_name is not UNSET:
            field_dict["member_name"] = member_name
        if name_on_card is not UNSET:
            field_dict["name_on_card"] = name_on_card
        if relation is not UNSET:
            field_dict["relation"] = relation
        if primary is not UNSET:
            field_dict["primary"] = primary
        if card_member is not UNSET:
            field_dict["card_member"] = card_member
        if number_of_cards is not UNSET:
            field_dict["number_of_cards"] = number_of_cards
        if card_type is not UNSET:
            field_dict["card_type"] = card_type
        if status is not UNSET:
            field_dict["status"] = status
        if valid_to_date is not UNSET:
            field_dict["valid_to_date"] = valid_to_date
        if last_printed_on is not UNSET:
            field_dict["last_printed_on"] = last_printed_on
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if card_expires is not UNSET:
            field_dict["card_expires"] = card_expires
        if address_to_print is not UNSET:
            field_dict["address_to_print"] = address_to_print
        if valid_from_date is not UNSET:
            field_dict["valid_from_date"] = valid_from_date
        if editable is not UNSET:
            field_dict["editable"] = editable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        membership_cards_id = d.pop("membership_cards_id", UNSET)

        membership_id = d.pop("membership_id", UNSET)

        joint_member = d.pop("joint_member", UNSET)

        def _parse_joint_member_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        joint_member_id = _parse_joint_member_id(d.pop("joint_member_id", UNSET))

        def _parse_member_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        member_name = _parse_member_name(d.pop("member_name", UNSET))

        def _parse_name_on_card(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_on_card = _parse_name_on_card(d.pop("name_on_card", UNSET))

        def _parse_relation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation = _parse_relation(d.pop("relation", UNSET))

        primary = d.pop("primary", UNSET)

        card_member = d.pop("card_member", UNSET)

        number_of_cards = d.pop("number_of_cards", UNSET)

        def _parse_card_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_type = _parse_card_type(d.pop("card_type", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_valid_to_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_to_date_type_0 = isoparse(data)

                return valid_to_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_to_date = _parse_valid_to_date(d.pop("valid_to_date", UNSET))

        def _parse_last_printed_on(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_printed_on_type_0 = isoparse(data)

                return last_printed_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_printed_on = _parse_last_printed_on(d.pop("last_printed_on", UNSET))

        sequence = d.pop("sequence", UNSET)

        def _parse_card_expires(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_expires = _parse_card_expires(d.pop("card_expires", UNSET))

        def _parse_address_to_print(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_to_print = _parse_address_to_print(d.pop("address_to_print", UNSET))

        def _parse_valid_from_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                valid_from_date_type_0 = isoparse(data)

                return valid_from_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        valid_from_date = _parse_valid_from_date(d.pop("valid_from_date", UNSET))

        editable = d.pop("editable", UNSET)

        membership_card = cls(
            membership_cards_id=membership_cards_id,
            membership_id=membership_id,
            joint_member=joint_member,
            joint_member_id=joint_member_id,
            member_name=member_name,
            name_on_card=name_on_card,
            relation=relation,
            primary=primary,
            card_member=card_member,
            number_of_cards=number_of_cards,
            card_type=card_type,
            status=status,
            valid_to_date=valid_to_date,
            last_printed_on=last_printed_on,
            sequence=sequence,
            card_expires=card_expires,
            address_to_print=address_to_print,
            valid_from_date=valid_from_date,
            editable=editable,
        )

        return membership_card

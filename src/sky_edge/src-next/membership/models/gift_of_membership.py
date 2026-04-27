from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.gift_of_membership_renewal_notice_type import GiftOfMembershipRenewalNoticeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftOfMembership")


@_attrs_define
class GiftOfMembership:
    """Record for gift of membership.

    Attributes:
        id (None | str | Unset): The immutable system record ID of the gift of membership.
        special_message (None | str | Unset): Special message from membership.
        send_notice_to (GiftOfMembershipRenewalNoticeType | Unset): Send notice to of renewal notice type.
        given_by (None | str | Unset): Membership given by name.
        given_by_id (None | str | Unset): Membership given by ID.
    """

    id: None | str | Unset = UNSET
    special_message: None | str | Unset = UNSET
    send_notice_to: GiftOfMembershipRenewalNoticeType | Unset = UNSET
    given_by: None | str | Unset = UNSET
    given_by_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        special_message: None | str | Unset
        if isinstance(self.special_message, Unset):
            special_message = UNSET
        else:
            special_message = self.special_message

        send_notice_to: str | Unset = UNSET
        if not isinstance(self.send_notice_to, Unset):
            send_notice_to = self.send_notice_to.value

        given_by: None | str | Unset
        if isinstance(self.given_by, Unset):
            given_by = UNSET
        else:
            given_by = self.given_by

        given_by_id: None | str | Unset
        if isinstance(self.given_by_id, Unset):
            given_by_id = UNSET
        else:
            given_by_id = self.given_by_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if special_message is not UNSET:
            field_dict["special_message"] = special_message
        if send_notice_to is not UNSET:
            field_dict["send_notice_to"] = send_notice_to
        if given_by is not UNSET:
            field_dict["given_by"] = given_by
        if given_by_id is not UNSET:
            field_dict["given_by_id"] = given_by_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_special_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        special_message = _parse_special_message(d.pop("special_message", UNSET))

        _send_notice_to = d.pop("send_notice_to", UNSET)
        send_notice_to: GiftOfMembershipRenewalNoticeType | Unset
        if isinstance(_send_notice_to, Unset):
            send_notice_to = UNSET
        else:
            send_notice_to = GiftOfMembershipRenewalNoticeType(_send_notice_to)

        def _parse_given_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_by = _parse_given_by(d.pop("given_by", UNSET))

        def _parse_given_by_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_by_id = _parse_given_by_id(d.pop("given_by_id", UNSET))

        gift_of_membership = cls(
            id=id,
            special_message=special_message,
            send_notice_to=send_notice_to,
            given_by=given_by,
            given_by_id=given_by_id,
        )

        return gift_of_membership

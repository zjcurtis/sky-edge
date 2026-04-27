from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="UpdateGiftOfMembership")


@_attrs_define
class UpdateGiftOfMembership:
    """Update gift of membership.

    Attributes:
        special_message (None | str | Unset): Special message from membership.
        send_notice_to (None | str | Unset): Send notice to of renewal notice type.
            Valid options: Donor, PrimaryMember, Both
        given_by_id (None | str | Unset): The ID of the constituent giving this membership as a gift.
            Required if special_message, override_renewal_defaults, or send_notice_to (non-Donor) are provided.
        override_renewal_defaults (bool | Unset): Membership override renewal defaults
    """

    special_message: None | str | Unset = UNSET
    send_notice_to: None | str | Unset = UNSET
    given_by_id: None | str | Unset = UNSET
    override_renewal_defaults: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        special_message: None | str | Unset
        if isinstance(self.special_message, Unset):
            special_message = UNSET
        else:
            special_message = self.special_message

        send_notice_to: None | str | Unset
        if isinstance(self.send_notice_to, Unset):
            send_notice_to = UNSET
        else:
            send_notice_to = self.send_notice_to

        given_by_id: None | str | Unset
        if isinstance(self.given_by_id, Unset):
            given_by_id = UNSET
        else:
            given_by_id = self.given_by_id

        override_renewal_defaults = self.override_renewal_defaults

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if special_message is not UNSET:
            field_dict["special_message"] = special_message
        if send_notice_to is not UNSET:
            field_dict["send_notice_to"] = send_notice_to
        if given_by_id is not UNSET:
            field_dict["given_by_id"] = given_by_id
        if override_renewal_defaults is not UNSET:
            field_dict["override_renewal_defaults"] = override_renewal_defaults

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_special_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        special_message = _parse_special_message(d.pop("special_message", UNSET))

        def _parse_send_notice_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        send_notice_to = _parse_send_notice_to(d.pop("send_notice_to", UNSET))

        def _parse_given_by_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        given_by_id = _parse_given_by_id(d.pop("given_by_id", UNSET))

        override_renewal_defaults = d.pop("override_renewal_defaults", UNSET)

        update_gift_of_membership = cls(
            special_message=special_message,
            send_notice_to=send_notice_to,
            given_by_id=given_by_id,
            override_renewal_defaults=override_renewal_defaults,
        )

        return update_gift_of_membership

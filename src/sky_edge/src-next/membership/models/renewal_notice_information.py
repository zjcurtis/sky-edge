from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.renewal_notice_information_membership_expiration_range import (
    RenewalNoticeInformationMembershipExpirationRange,
)
from ..models.renewal_notice_information_new_membership_expires_interval import (
    RenewalNoticeInformationNewMembershipExpiresInterval,
)
from ..models.renewal_notice_information_renewal_notice_type import RenewalNoticeInformationRenewalNoticeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RenewalNoticeInformation")


@_attrs_define
class RenewalNoticeInformation:
    """Renewal notice information of a membership

    Attributes:
        category_renewals_id (int | Unset): Category renewal ID
        letters (None | str | Unset): Letters description
        comments (None | str | Unset): User text associated with the record
        send_renewals_to (RenewalNoticeInformationRenewalNoticeType | Unset): Define the send notice of renewal notice
            type
        renewal_number (int | None | Unset): Time period to send notices
        frequency (RenewalNoticeInformationNewMembershipExpiresInterval | Unset): Defines the frequency of membership
            expiry
        renewal_type (RenewalNoticeInformationMembershipExpirationRange | Unset): Define the renewal type of expiration
            range
        for_membership_gifts (bool | Unset): Whether the renewal notice is standard or has gift of membership
    """

    category_renewals_id: int | Unset = UNSET
    letters: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    send_renewals_to: RenewalNoticeInformationRenewalNoticeType | Unset = UNSET
    renewal_number: int | None | Unset = UNSET
    frequency: RenewalNoticeInformationNewMembershipExpiresInterval | Unset = UNSET
    renewal_type: RenewalNoticeInformationMembershipExpirationRange | Unset = UNSET
    for_membership_gifts: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category_renewals_id = self.category_renewals_id

        letters: None | str | Unset
        if isinstance(self.letters, Unset):
            letters = UNSET
        else:
            letters = self.letters

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        send_renewals_to: str | Unset = UNSET
        if not isinstance(self.send_renewals_to, Unset):
            send_renewals_to = self.send_renewals_to.value

        renewal_number: int | None | Unset
        if isinstance(self.renewal_number, Unset):
            renewal_number = UNSET
        else:
            renewal_number = self.renewal_number

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        renewal_type: str | Unset = UNSET
        if not isinstance(self.renewal_type, Unset):
            renewal_type = self.renewal_type.value

        for_membership_gifts = self.for_membership_gifts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category_renewals_id is not UNSET:
            field_dict["category_renewals_id"] = category_renewals_id
        if letters is not UNSET:
            field_dict["letters"] = letters
        if comments is not UNSET:
            field_dict["comments"] = comments
        if send_renewals_to is not UNSET:
            field_dict["send_renewals_to"] = send_renewals_to
        if renewal_number is not UNSET:
            field_dict["renewal_number"] = renewal_number
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if renewal_type is not UNSET:
            field_dict["renewal_type"] = renewal_type
        if for_membership_gifts is not UNSET:
            field_dict["for_membership_gifts"] = for_membership_gifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_renewals_id = d.pop("category_renewals_id", UNSET)

        def _parse_letters(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        letters = _parse_letters(d.pop("letters", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        _send_renewals_to = d.pop("send_renewals_to", UNSET)
        send_renewals_to: RenewalNoticeInformationRenewalNoticeType | Unset
        if isinstance(_send_renewals_to, Unset):
            send_renewals_to = UNSET
        else:
            send_renewals_to = RenewalNoticeInformationRenewalNoticeType(_send_renewals_to)

        def _parse_renewal_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        renewal_number = _parse_renewal_number(d.pop("renewal_number", UNSET))

        _frequency = d.pop("frequency", UNSET)
        frequency: RenewalNoticeInformationNewMembershipExpiresInterval | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = RenewalNoticeInformationNewMembershipExpiresInterval(_frequency)

        _renewal_type = d.pop("renewal_type", UNSET)
        renewal_type: RenewalNoticeInformationMembershipExpirationRange | Unset
        if isinstance(_renewal_type, Unset):
            renewal_type = UNSET
        else:
            renewal_type = RenewalNoticeInformationMembershipExpirationRange(_renewal_type)

        for_membership_gifts = d.pop("for_membership_gifts", UNSET)

        renewal_notice_information = cls(
            category_renewals_id=category_renewals_id,
            letters=letters,
            comments=comments,
            send_renewals_to=send_renewals_to,
            renewal_number=renewal_number,
            frequency=frequency,
            renewal_type=renewal_type,
            for_membership_gifts=for_membership_gifts,
        )

        return renewal_notice_information

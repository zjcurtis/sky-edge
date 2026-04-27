from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditPaymentInformation")


@_attrs_define
class EditPaymentInformation:
    """Information to edit payment information for a gift

    Attributes:
        account_token (str): Account token
        update_all_gifts_with_matching_account_token (bool | None | Unset): True if other recurring gifts with the same
            account token should also have their payment information amended.
        origin (None | str | Unset): The origin of the amendment (optional)
    """

    account_token: str
    update_all_gifts_with_matching_account_token: bool | None | Unset = UNSET
    origin: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_token = self.account_token

        update_all_gifts_with_matching_account_token: bool | None | Unset
        if isinstance(self.update_all_gifts_with_matching_account_token, Unset):
            update_all_gifts_with_matching_account_token = UNSET
        else:
            update_all_gifts_with_matching_account_token = self.update_all_gifts_with_matching_account_token

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account_token": account_token,
            }
        )
        if update_all_gifts_with_matching_account_token is not UNSET:
            field_dict["update_all_gifts_with_matching_account_token"] = update_all_gifts_with_matching_account_token
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_token = d.pop("account_token")

        def _parse_update_all_gifts_with_matching_account_token(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        update_all_gifts_with_matching_account_token = _parse_update_all_gifts_with_matching_account_token(
            d.pop("update_all_gifts_with_matching_account_token", UNSET)
        )

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        edit_payment_information = cls(
            account_token=account_token,
            update_all_gifts_with_matching_account_token=update_all_gifts_with_matching_account_token,
            origin=origin,
        )

        return edit_payment_information

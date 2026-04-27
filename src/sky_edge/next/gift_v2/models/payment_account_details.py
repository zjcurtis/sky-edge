from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="PaymentAccountDetails")


@_attrs_define
class PaymentAccountDetails:
    """Account details for credit card and direct debit accounts tokenized in BB Payment Services.

    Attributes:
        account_holder (None | str | Unset): The name of the account holder. Unified for Credit Card and Direct Debit.
            Example: Robert Hernandez.
        account_number (None | str | Unset): The account number. Unified for Credit Card and Direct Debit. Example:
            xxxxxxxxxxxx1234.
        account_type (None | str | Unset): The direct debit account type, for direct debit accounts. Example: Checking.
        card_type (None | str | Unset): The card type, for credit card accounts. Example: Visa.
        expiration_date (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        routing_number (None | str | Unset): The routing number for direct debit accounts. Example: 12345678.
    """

    account_holder: None | str | Unset = UNSET
    account_number: None | str | Unset = UNSET
    account_type: None | str | Unset = UNSET
    card_type: None | str | Unset = UNSET
    expiration_date: FuzzyDate | Unset = UNSET
    routing_number: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_holder: None | str | Unset
        if isinstance(self.account_holder, Unset):
            account_holder = UNSET
        else:
            account_holder = self.account_holder

        account_number: None | str | Unset
        if isinstance(self.account_number, Unset):
            account_number = UNSET
        else:
            account_number = self.account_number

        account_type: None | str | Unset
        if isinstance(self.account_type, Unset):
            account_type = UNSET
        else:
            account_type = self.account_type

        card_type: None | str | Unset
        if isinstance(self.card_type, Unset):
            card_type = UNSET
        else:
            card_type = self.card_type

        expiration_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.to_dict()

        routing_number: None | str | Unset
        if isinstance(self.routing_number, Unset):
            routing_number = UNSET
        else:
            routing_number = self.routing_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if account_holder is not UNSET:
            field_dict["account_holder"] = account_holder
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if account_type is not UNSET:
            field_dict["account_type"] = account_type
        if card_type is not UNSET:
            field_dict["card_type"] = card_type
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if routing_number is not UNSET:
            field_dict["routing_number"] = routing_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)

        def _parse_account_holder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_holder = _parse_account_holder(d.pop("account_holder", UNSET))

        def _parse_account_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_number = _parse_account_number(d.pop("account_number", UNSET))

        def _parse_account_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_type = _parse_account_type(d.pop("account_type", UNSET))

        def _parse_card_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        card_type = _parse_card_type(d.pop("card_type", UNSET))

        _expiration_date = d.pop("expiration_date", UNSET)
        expiration_date: FuzzyDate | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = FuzzyDate.from_dict(_expiration_date)

        def _parse_routing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        routing_number = _parse_routing_number(d.pop("routing_number", UNSET))

        payment_account_details = cls(
            account_holder=account_holder,
            account_number=account_number,
            account_type=account_type,
            card_type=card_type,
            expiration_date=expiration_date,
            routing_number=routing_number,
        )

        return payment_account_details

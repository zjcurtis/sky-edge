from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="PaymentRead")


@_attrs_define
class PaymentRead:
    """Donors can use a variety of methods — such as Cash, Personal check, Credit card, and Direct debit — to pay for
    gifts.

        Attributes:
            account_token (str | Unset): The tokenized account information (e.g. credit card) from the external payment
                provider. Only applies to payment methods of <i>CreditCard</i> and <i>DirectDebit</i>.
            bbps_configuration_id (str | Unset): The bbps configuration ID. Only applies to payment methods of
                <i>CreditCard</i> and <i>DirectDebit</i>.
            bbps_transaction_id (str | Unset): The bbps transaction ID. Only applies to payment methods of <i>CreditCard</i>
                and <i>DirectDebit</i>.
            check_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            check_number (str | Unset): The check number. Only applies to payment method of <i>PersonalCheck</i>.
            checkout_transaction_id (str | Unset): The checkout transaction ID. Only applies to payment methods of
                <i>CreditCard</i> and <i>DirectDebit</i>.
            payment_method (str | Unset): The payment method. Available values are listed below.
            reference (str | Unset): The reference. Only applies to payment method of <i>Other</i>.
            reference_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
    """

    account_token: str | Unset = UNSET
    bbps_configuration_id: str | Unset = UNSET
    bbps_transaction_id: str | Unset = UNSET
    check_date: FuzzyDate | Unset = UNSET
    check_number: str | Unset = UNSET
    checkout_transaction_id: str | Unset = UNSET
    payment_method: str | Unset = UNSET
    reference: str | Unset = UNSET
    reference_date: FuzzyDate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_token = self.account_token

        bbps_configuration_id = self.bbps_configuration_id

        bbps_transaction_id = self.bbps_transaction_id

        check_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_date, Unset):
            check_date = self.check_date.to_dict()

        check_number = self.check_number

        checkout_transaction_id = self.checkout_transaction_id

        payment_method = self.payment_method

        reference = self.reference

        reference_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_date, Unset):
            reference_date = self.reference_date.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_token is not UNSET:
            field_dict["account_token"] = account_token
        if bbps_configuration_id is not UNSET:
            field_dict["bbps_configuration_id"] = bbps_configuration_id
        if bbps_transaction_id is not UNSET:
            field_dict["bbps_transaction_id"] = bbps_transaction_id
        if check_date is not UNSET:
            field_dict["check_date"] = check_date
        if check_number is not UNSET:
            field_dict["check_number"] = check_number
        if checkout_transaction_id is not UNSET:
            field_dict["checkout_transaction_id"] = checkout_transaction_id
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        account_token = d.pop("account_token", UNSET)

        bbps_configuration_id = d.pop("bbps_configuration_id", UNSET)

        bbps_transaction_id = d.pop("bbps_transaction_id", UNSET)

        _check_date = d.pop("check_date", UNSET)
        check_date: FuzzyDate | Unset
        if isinstance(_check_date, Unset):
            check_date = UNSET
        else:
            check_date = FuzzyDate.from_dict(_check_date)

        check_number = d.pop("check_number", UNSET)

        checkout_transaction_id = d.pop("checkout_transaction_id", UNSET)

        payment_method = d.pop("payment_method", UNSET)

        reference = d.pop("reference", UNSET)

        _reference_date = d.pop("reference_date", UNSET)
        reference_date: FuzzyDate | Unset
        if isinstance(_reference_date, Unset):
            reference_date = UNSET
        else:
            reference_date = FuzzyDate.from_dict(_reference_date)

        payment_read = cls(
            account_token=account_token,
            bbps_configuration_id=bbps_configuration_id,
            bbps_transaction_id=bbps_transaction_id,
            check_date=check_date,
            check_number=check_number,
            checkout_transaction_id=checkout_transaction_id,
            payment_method=payment_method,
            reference=reference,
            reference_date=reference_date,
        )

        payment_read.additional_properties = d
        return payment_read

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

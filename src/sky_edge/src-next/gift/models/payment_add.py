from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="PaymentAdd")


@_attrs_define
class PaymentAdd:
    """Donors can use a variety of methods — such as Cash, Personal check, Credit card, and Direct debit — to pay for
    gifts.

        Attributes:
            account_token (str | Unset): The account token. Must parse to a valid, non-empty GUID. Only applies to payment
                methods of <i>CreditCard</i> and <i>DirectDebit</i>. When adding a recurring gift, an account token must be
                provided for each <code>payments</code> object.
            bbps_configuration_id (str | Unset): The bbps configuration ID. Must parse to a valid, non-empty GUID. Only
                applies to payment methods of <i>CreditCard</i> and <i>DirectDebit</i>.
            bbps_transaction_id (str | Unset): The bbps transaction ID. Must parse to a valid, non-empty GUID. Only applies
                to payment methods of <i>CreditCard</i> and <i>DirectDebit</i>. When adding a recurring gift payment, either a
                <code>bbps_transaction_id</code> or <code>checkout_transaction_id</code> must be provided for each
                <code>payments</code> object.
            check_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            check_number (str | Unset): The check number. Only applies to payment method of <i>PersonalCheck</i>. Character
                limit: 20.
            checkout_transaction_id (str | Unset): The checkout transaction ID. Must parse to a valid, non-empty GUID. Only
                applies to payment methods of <i>CreditCard</i> and <i>DirectDebit</i>. When adding a recurring gift payment,
                either a <code>bbps_transaction_id</code> or <code>checkout_transaction_id</code> must be provided for each
                <code>payments</code> object.
            charge_transaction (bool | Unset): Whether or not to charge the checkout transaction. Only applies when a
                "CheckoutTransactionId" is supplied.
            payment_method (str | Unset): The payment method. Available values <a href="#PaymentMethods">are listed
                below</a>. For donations, the payment method can be <i>Cash</i>, <i>CreditCard</i>, <i>PersonalCheck</i>,
                <i>DirectDebit</i>, <i>Other</i>, <i>PayPal</i>, or <i>Venmo</i>. For recurring gifts and recurring gift
                payments, the payment method must be <i>CreditCard</i> or <i>DirectDebit</i>.
            reason (str | Unset): Optional. The Reason Code for this payment. Available values are <i>Approved</i>,
                <i>HardReject</i>, <i>Held</i>, and <i>SoftReject</i>.
            reference (str | Unset): The reference. Only applies to payment method of <i>Other</i>.
            reference_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            rejection_details (str | Unset): The detail for why a payment was rejected. Generally comes from the gateway.
                This value will be ignored if reason is not set to <i>HardReject</i>, <i>Held</i>, or <i>SoftReject</i>.
    """

    account_token: str | Unset = UNSET
    bbps_configuration_id: str | Unset = UNSET
    bbps_transaction_id: str | Unset = UNSET
    check_date: FuzzyDate | Unset = UNSET
    check_number: str | Unset = UNSET
    checkout_transaction_id: str | Unset = UNSET
    charge_transaction: bool | Unset = UNSET
    payment_method: str | Unset = UNSET
    reason: str | Unset = UNSET
    reference: str | Unset = UNSET
    reference_date: FuzzyDate | Unset = UNSET
    rejection_details: str | Unset = UNSET
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

        charge_transaction = self.charge_transaction

        payment_method = self.payment_method

        reason = self.reason

        reference = self.reference

        reference_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_date, Unset):
            reference_date = self.reference_date.to_dict()

        rejection_details = self.rejection_details

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
        if charge_transaction is not UNSET:
            field_dict["charge_transaction"] = charge_transaction
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reference is not UNSET:
            field_dict["reference"] = reference
        if reference_date is not UNSET:
            field_dict["reference_date"] = reference_date
        if rejection_details is not UNSET:
            field_dict["rejection_details"] = rejection_details

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

        charge_transaction = d.pop("charge_transaction", UNSET)

        payment_method = d.pop("payment_method", UNSET)

        reason = d.pop("reason", UNSET)

        reference = d.pop("reference", UNSET)

        _reference_date = d.pop("reference_date", UNSET)
        reference_date: FuzzyDate | Unset
        if isinstance(_reference_date, Unset):
            reference_date = UNSET
        else:
            reference_date = FuzzyDate.from_dict(_reference_date)

        rejection_details = d.pop("rejection_details", UNSET)

        payment_add = cls(
            account_token=account_token,
            bbps_configuration_id=bbps_configuration_id,
            bbps_transaction_id=bbps_transaction_id,
            check_date=check_date,
            check_number=check_number,
            checkout_transaction_id=checkout_transaction_id,
            charge_transaction=charge_transaction,
            payment_method=payment_method,
            reason=reason,
            reference=reference,
            reference_date=reference_date,
            rejection_details=rejection_details,
        )

        payment_add.additional_properties = d
        return payment_add

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

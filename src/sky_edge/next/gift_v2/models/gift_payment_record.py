from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.gift_payment_record_payment_method import GiftPaymentRecordPaymentMethod
from ..models.gift_payment_record_processing_status import (
    GiftPaymentRecordProcessingStatus,
)

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.fuzzy_date import FuzzyDate
    from ..models.pad_mandate import PadMandate
    from ..models.payment_account_details import PaymentAccountDetails


T = TypeVar("T", bound="GiftPaymentRecord")


@_attrs_define
class GiftPaymentRecord:
    """A payment for a gift being added.

    Attributes:
        gift_legacy_id (None | str | Unset): The legacy ID of the payment's associated gift. Example: 12345.
        amount (Currency | Unset): An amount denominated in a specific currency.
        method (GiftPaymentRecordPaymentMethod | Unset): The payment method. Example: Cash.
        account_details (PaymentAccountDetails | Unset): Account details for credit card and direct debit accounts
            tokenized in BB Payment Services.
        account_token (None | str | Unset): The account token from BBPS. Example: 3e8f5c58-737d-4255-abde-9cfe236c230e.
        authorization_code (None | str | Unset): The authorization code, for credit card payments. Example: 54321.
        check_dt (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        check_number (None | str | Unset): The check number, for check and direct debit payments. Example: 2001.
        checkout_transaction_id (None | Unset | UUID): The checkout transaction ID from BB Checkout. Example:
            6781faab-0eeb-41b2-ba1e-cdfd20669f81.
        bbps_transaction_id (None | Unset | UUID): The BBPS transaction ID from BB Checkout or BB Payment Services.
            Example: edcd3d4c-116b-4f33-9462-dcdcfaf49eea.
        configuration_id (None | Unset | UUID): The Payment Configuration ID used for this transaction. Example:
            ca5b9a59-633c-40e8-9242-81d59b83a29d.
        reference_dt (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        reference_number (None | str | Unset): The reference number. Example: 555-6666.
        charge_transaction (bool | None | Unset): True if the transaction should be completed. Requires a Checkout
            Transaction ID.
        pad_mandates (list[PadMandate] | None | Unset): The URLs of the mandates.
        processing_status (GiftPaymentRecordProcessingStatus | Unset): Gets or sets the direct debit processing status.
    """

    gift_legacy_id: None | str | Unset = UNSET
    amount: Currency | Unset = UNSET
    method: GiftPaymentRecordPaymentMethod | Unset = UNSET
    account_details: PaymentAccountDetails | Unset = UNSET
    account_token: None | str | Unset = UNSET
    authorization_code: None | str | Unset = UNSET
    check_dt: FuzzyDate | Unset = UNSET
    check_number: None | str | Unset = UNSET
    checkout_transaction_id: None | Unset | UUID = UNSET
    bbps_transaction_id: None | Unset | UUID = UNSET
    configuration_id: None | Unset | UUID = UNSET
    reference_dt: FuzzyDate | Unset = UNSET
    reference_number: None | str | Unset = UNSET
    charge_transaction: bool | None | Unset = UNSET
    pad_mandates: list[PadMandate] | None | Unset = UNSET
    processing_status: GiftPaymentRecordProcessingStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_legacy_id: None | str | Unset
        if isinstance(self.gift_legacy_id, Unset):
            gift_legacy_id = UNSET
        else:
            gift_legacy_id = self.gift_legacy_id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        method: str | Unset = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        account_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_details, Unset):
            account_details = self.account_details.to_dict()

        account_token: None | str | Unset
        if isinstance(self.account_token, Unset):
            account_token = UNSET
        else:
            account_token = self.account_token

        authorization_code: None | str | Unset
        if isinstance(self.authorization_code, Unset):
            authorization_code = UNSET
        else:
            authorization_code = self.authorization_code

        check_dt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_dt, Unset):
            check_dt = self.check_dt.to_dict()

        check_number: None | str | Unset
        if isinstance(self.check_number, Unset):
            check_number = UNSET
        else:
            check_number = self.check_number

        checkout_transaction_id: None | str | Unset
        if isinstance(self.checkout_transaction_id, Unset):
            checkout_transaction_id = UNSET
        elif isinstance(self.checkout_transaction_id, UUID):
            checkout_transaction_id = str(self.checkout_transaction_id)
        else:
            checkout_transaction_id = self.checkout_transaction_id

        bbps_transaction_id: None | str | Unset
        if isinstance(self.bbps_transaction_id, Unset):
            bbps_transaction_id = UNSET
        elif isinstance(self.bbps_transaction_id, UUID):
            bbps_transaction_id = str(self.bbps_transaction_id)
        else:
            bbps_transaction_id = self.bbps_transaction_id

        configuration_id: None | str | Unset
        if isinstance(self.configuration_id, Unset):
            configuration_id = UNSET
        elif isinstance(self.configuration_id, UUID):
            configuration_id = str(self.configuration_id)
        else:
            configuration_id = self.configuration_id

        reference_dt: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reference_dt, Unset):
            reference_dt = self.reference_dt.to_dict()

        reference_number: None | str | Unset
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

        charge_transaction: bool | None | Unset
        if isinstance(self.charge_transaction, Unset):
            charge_transaction = UNSET
        else:
            charge_transaction = self.charge_transaction

        pad_mandates: list[dict[str, Any]] | None | Unset
        if isinstance(self.pad_mandates, Unset):
            pad_mandates = UNSET
        elif isinstance(self.pad_mandates, list):
            pad_mandates = []
            for pad_mandates_type_0_item_data in self.pad_mandates:
                pad_mandates_type_0_item = pad_mandates_type_0_item_data.to_dict()
                pad_mandates.append(pad_mandates_type_0_item)

        else:
            pad_mandates = self.pad_mandates

        processing_status: str | Unset = UNSET
        if not isinstance(self.processing_status, Unset):
            processing_status = self.processing_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_legacy_id is not UNSET:
            field_dict["gift_legacy_id"] = gift_legacy_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if method is not UNSET:
            field_dict["method"] = method
        if account_details is not UNSET:
            field_dict["account_details"] = account_details
        if account_token is not UNSET:
            field_dict["account_token"] = account_token
        if authorization_code is not UNSET:
            field_dict["authorization_code"] = authorization_code
        if check_dt is not UNSET:
            field_dict["check_dt"] = check_dt
        if check_number is not UNSET:
            field_dict["check_number"] = check_number
        if checkout_transaction_id is not UNSET:
            field_dict["checkout_transaction_id"] = checkout_transaction_id
        if bbps_transaction_id is not UNSET:
            field_dict["bbps_transaction_id"] = bbps_transaction_id
        if configuration_id is not UNSET:
            field_dict["configuration_id"] = configuration_id
        if reference_dt is not UNSET:
            field_dict["reference_dt"] = reference_dt
        if reference_number is not UNSET:
            field_dict["reference_number"] = reference_number
        if charge_transaction is not UNSET:
            field_dict["charge_transaction"] = charge_transaction
        if pad_mandates is not UNSET:
            field_dict["pad_mandates"] = pad_mandates
        if processing_status is not UNSET:
            field_dict["processing_status"] = processing_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.fuzzy_date import FuzzyDate
        from ..models.pad_mandate import PadMandate
        from ..models.payment_account_details import PaymentAccountDetails

        d = dict(src_dict)

        def _parse_gift_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_legacy_id = _parse_gift_legacy_id(d.pop("gift_legacy_id", UNSET))

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        _method = d.pop("method", UNSET)
        method: GiftPaymentRecordPaymentMethod | Unset
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = GiftPaymentRecordPaymentMethod(_method)

        _account_details = d.pop("account_details", UNSET)
        account_details: PaymentAccountDetails | Unset
        if isinstance(_account_details, Unset):
            account_details = UNSET
        else:
            account_details = PaymentAccountDetails.from_dict(_account_details)

        def _parse_account_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_token = _parse_account_token(d.pop("account_token", UNSET))

        def _parse_authorization_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorization_code = _parse_authorization_code(
            d.pop("authorization_code", UNSET)
        )

        _check_dt = d.pop("check_dt", UNSET)
        check_dt: FuzzyDate | Unset
        if isinstance(_check_dt, Unset):
            check_dt = UNSET
        else:
            check_dt = FuzzyDate.from_dict(_check_dt)

        def _parse_check_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_number = _parse_check_number(d.pop("check_number", UNSET))

        def _parse_checkout_transaction_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checkout_transaction_id_type_0 = UUID(data)

                return checkout_transaction_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        checkout_transaction_id = _parse_checkout_transaction_id(
            d.pop("checkout_transaction_id", UNSET)
        )

        def _parse_bbps_transaction_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                bbps_transaction_id_type_0 = UUID(data)

                return bbps_transaction_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        bbps_transaction_id = _parse_bbps_transaction_id(
            d.pop("bbps_transaction_id", UNSET)
        )

        def _parse_configuration_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                configuration_id_type_0 = UUID(data)

                return configuration_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        configuration_id = _parse_configuration_id(d.pop("configuration_id", UNSET))

        _reference_dt = d.pop("reference_dt", UNSET)
        reference_dt: FuzzyDate | Unset
        if isinstance(_reference_dt, Unset):
            reference_dt = UNSET
        else:
            reference_dt = FuzzyDate.from_dict(_reference_dt)

        def _parse_reference_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference_number = _parse_reference_number(d.pop("reference_number", UNSET))

        def _parse_charge_transaction(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        charge_transaction = _parse_charge_transaction(
            d.pop("charge_transaction", UNSET)
        )

        def _parse_pad_mandates(data: object) -> list[PadMandate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pad_mandates_type_0 = []
                _pad_mandates_type_0 = data
                for pad_mandates_type_0_item_data in _pad_mandates_type_0:
                    pad_mandates_type_0_item = PadMandate.from_dict(
                        pad_mandates_type_0_item_data
                    )

                    pad_mandates_type_0.append(pad_mandates_type_0_item)

                return pad_mandates_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PadMandate] | None | Unset, data)

        pad_mandates = _parse_pad_mandates(d.pop("pad_mandates", UNSET))

        _processing_status = d.pop("processing_status", UNSET)
        processing_status: GiftPaymentRecordProcessingStatus | Unset
        if isinstance(_processing_status, Unset):
            processing_status = UNSET
        else:
            processing_status = GiftPaymentRecordProcessingStatus(_processing_status)

        gift_payment_record = cls(
            gift_legacy_id=gift_legacy_id,
            amount=amount,
            method=method,
            account_details=account_details,
            account_token=account_token,
            authorization_code=authorization_code,
            check_dt=check_dt,
            check_number=check_number,
            checkout_transaction_id=checkout_transaction_id,
            bbps_transaction_id=bbps_transaction_id,
            configuration_id=configuration_id,
            reference_dt=reference_dt,
            reference_number=reference_number,
            charge_transaction=charge_transaction,
            pad_mandates=pad_mandates,
            processing_status=processing_status,
        )

        return gift_payment_record

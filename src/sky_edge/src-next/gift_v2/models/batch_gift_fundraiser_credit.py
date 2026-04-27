from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.batch_gift_fundraiser_credit_recognition_credit_type import BatchGiftFundraiserCreditRecognitionCreditType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="BatchGiftFundraiserCredit")


@_attrs_define
class BatchGiftFundraiserCredit:
    """A fundraiser credit on a batch gift

    Attributes:
        batch_gift_id (None | str | Unset): ID of the batch gift to which this credit belongs
        batch_id (None | str | Unset): ID of the batch to which this credit belongs
        amount (Currency | Unset): An amount denominated in a specific currency.
        constituent_id (None | str | Unset): The identifier of the recipient of the recognition credit. Example: 280.
        constituent_name (None | str | Unset): Name of the constituent being recognized Example: Robert Hernandez.
        legacy_id (None | str | Unset): The legacy identifier of the recognition credit. Example: 12345.
        credit_type (BatchGiftFundraiserCreditRecognitionCreditType | Unset): The type of recognition credit. Currently
            supports Fundraiser credits and Soft credits. Example: SoftCredit.
        sequence (int | None | Unset): The sequence number for the recognition credit. Example: 1.
    """

    batch_gift_id: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    amount: Currency | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    constituent_name: None | str | Unset = UNSET
    legacy_id: None | str | Unset = UNSET
    credit_type: BatchGiftFundraiserCreditRecognitionCreditType | Unset = UNSET
    sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        batch_gift_id: None | str | Unset
        if isinstance(self.batch_gift_id, Unset):
            batch_gift_id = UNSET
        else:
            batch_gift_id = self.batch_gift_id

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        constituent_name: None | str | Unset
        if isinstance(self.constituent_name, Unset):
            constituent_name = UNSET
        else:
            constituent_name = self.constituent_name

        legacy_id: None | str | Unset
        if isinstance(self.legacy_id, Unset):
            legacy_id = UNSET
        else:
            legacy_id = self.legacy_id

        credit_type: str | Unset = UNSET
        if not isinstance(self.credit_type, Unset):
            credit_type = self.credit_type.value

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if batch_gift_id is not UNSET:
            field_dict["batch_gift_id"] = batch_gift_id
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if constituent_name is not UNSET:
            field_dict["constituent_name"] = constituent_name
        if legacy_id is not UNSET:
            field_dict["legacy_id"] = legacy_id
        if credit_type is not UNSET:
            field_dict["credit_type"] = credit_type
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)

        def _parse_batch_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_gift_id = _parse_batch_gift_id(d.pop("batch_gift_id", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_constituent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_name = _parse_constituent_name(d.pop("constituent_name", UNSET))

        def _parse_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legacy_id = _parse_legacy_id(d.pop("legacy_id", UNSET))

        _credit_type = d.pop("credit_type", UNSET)
        credit_type: BatchGiftFundraiserCreditRecognitionCreditType | Unset
        if isinstance(_credit_type, Unset):
            credit_type = UNSET
        else:
            credit_type = BatchGiftFundraiserCreditRecognitionCreditType(_credit_type)

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        batch_gift_fundraiser_credit = cls(
            batch_gift_id=batch_gift_id,
            batch_id=batch_id,
            amount=amount,
            constituent_id=constituent_id,
            constituent_name=constituent_name,
            legacy_id=legacy_id,
            credit_type=credit_type,
            sequence=sequence,
        )

        return batch_gift_fundraiser_credit

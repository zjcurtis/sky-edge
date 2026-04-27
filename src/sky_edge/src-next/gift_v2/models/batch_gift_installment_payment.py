from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_constituent import GiftConstituent


T = TypeVar("T", bound="BatchGiftInstallmentPayment")


@_attrs_define
class BatchGiftInstallmentPayment:
    """Installment payment for a pledge or recurring gift paid by a batch gift

    Attributes:
        id (None | str | Unset): System ID of this batch gift installment payment
        amount (float | None | Unset): Amount of this installment payment
        batch_id (None | str | Unset): System ID of the batch to which this installment payment belongs
        batch_gift_id (None | str | Unset): System ID of the batch gift to which this installment payment belongs
        installment_id (None | str | Unset): System ID of the installment paid by this batch installment payment
        pledge_id (None | str | Unset): System ID of the pledge gift paid by this batch installment payment
        payment_id (None | str | Unset): Payment ID of this batch installment payment.
        pledge_constituent (GiftConstituent | Unset): The constituent who makes a gift.
        pledge_is_automated (bool | None | Unset): Flag indicating if this installment payment is for an automated
            pledge.
    """

    id: None | str | Unset = UNSET
    amount: float | None | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    batch_gift_id: None | str | Unset = UNSET
    installment_id: None | str | Unset = UNSET
    pledge_id: None | str | Unset = UNSET
    payment_id: None | str | Unset = UNSET
    pledge_constituent: GiftConstituent | Unset = UNSET
    pledge_is_automated: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        batch_gift_id: None | str | Unset
        if isinstance(self.batch_gift_id, Unset):
            batch_gift_id = UNSET
        else:
            batch_gift_id = self.batch_gift_id

        installment_id: None | str | Unset
        if isinstance(self.installment_id, Unset):
            installment_id = UNSET
        else:
            installment_id = self.installment_id

        pledge_id: None | str | Unset
        if isinstance(self.pledge_id, Unset):
            pledge_id = UNSET
        else:
            pledge_id = self.pledge_id

        payment_id: None | str | Unset
        if isinstance(self.payment_id, Unset):
            payment_id = UNSET
        else:
            payment_id = self.payment_id

        pledge_constituent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pledge_constituent, Unset):
            pledge_constituent = self.pledge_constituent.to_dict()

        pledge_is_automated: bool | None | Unset
        if isinstance(self.pledge_is_automated, Unset):
            pledge_is_automated = UNSET
        else:
            pledge_is_automated = self.pledge_is_automated

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if batch_gift_id is not UNSET:
            field_dict["batch_gift_id"] = batch_gift_id
        if installment_id is not UNSET:
            field_dict["installment_id"] = installment_id
        if pledge_id is not UNSET:
            field_dict["pledge_id"] = pledge_id
        if payment_id is not UNSET:
            field_dict["payment_id"] = payment_id
        if pledge_constituent is not UNSET:
            field_dict["pledge_constituent"] = pledge_constituent
        if pledge_is_automated is not UNSET:
            field_dict["pledge_is_automated"] = pledge_is_automated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_constituent import GiftConstituent

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        def _parse_batch_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_gift_id = _parse_batch_gift_id(d.pop("batch_gift_id", UNSET))

        def _parse_installment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installment_id = _parse_installment_id(d.pop("installment_id", UNSET))

        def _parse_pledge_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pledge_id = _parse_pledge_id(d.pop("pledge_id", UNSET))

        def _parse_payment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_id = _parse_payment_id(d.pop("payment_id", UNSET))

        _pledge_constituent = d.pop("pledge_constituent", UNSET)
        pledge_constituent: GiftConstituent | Unset
        if isinstance(_pledge_constituent, Unset):
            pledge_constituent = UNSET
        else:
            pledge_constituent = GiftConstituent.from_dict(_pledge_constituent)

        def _parse_pledge_is_automated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        pledge_is_automated = _parse_pledge_is_automated(d.pop("pledge_is_automated", UNSET))

        batch_gift_installment_payment = cls(
            id=id,
            amount=amount,
            batch_id=batch_id,
            batch_gift_id=batch_gift_id,
            installment_id=installment_id,
            pledge_id=pledge_id,
            payment_id=payment_id,
            pledge_constituent=pledge_constituent,
            pledge_is_automated=pledge_is_automated,
        )

        return batch_gift_installment_payment

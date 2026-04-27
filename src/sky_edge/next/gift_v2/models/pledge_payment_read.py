from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="PledgePaymentRead")


@_attrs_define
class PledgePaymentRead:
    """Represents information for a pledge payment.

    Attributes:
        installment_id (None | str | Unset): The identifier of the installment for this payment.
        payment_gift_id (None | str | Unset): The gift record identifier for this payment.
        amount_applied (Currency | Unset): An amount denominated in a specific currency.
    """

    installment_id: None | str | Unset = UNSET
    payment_gift_id: None | str | Unset = UNSET
    amount_applied: Currency | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        installment_id: None | str | Unset
        if isinstance(self.installment_id, Unset):
            installment_id = UNSET
        else:
            installment_id = self.installment_id

        payment_gift_id: None | str | Unset
        if isinstance(self.payment_gift_id, Unset):
            payment_gift_id = UNSET
        else:
            payment_gift_id = self.payment_gift_id

        amount_applied: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount_applied, Unset):
            amount_applied = self.amount_applied.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if installment_id is not UNSET:
            field_dict["installment_id"] = installment_id
        if payment_gift_id is not UNSET:
            field_dict["payment_gift_id"] = payment_gift_id
        if amount_applied is not UNSET:
            field_dict["amount_applied"] = amount_applied

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)

        def _parse_installment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installment_id = _parse_installment_id(d.pop("installment_id", UNSET))

        def _parse_payment_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_gift_id = _parse_payment_gift_id(d.pop("payment_gift_id", UNSET))

        _amount_applied = d.pop("amount_applied", UNSET)
        amount_applied: Currency | Unset
        if isinstance(_amount_applied, Unset):
            amount_applied = UNSET
        else:
            amount_applied = Currency.from_dict(_amount_applied)

        pledge_payment_read = cls(
            installment_id=installment_id,
            payment_gift_id=payment_gift_id,
            amount_applied=amount_applied,
        )

        return pledge_payment_read

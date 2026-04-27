from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ApplyPaymentInstallment")


@_attrs_define
class ApplyPaymentInstallment:
    """Represents the details provided when applying a payment to an installment.

    Attributes:
        installment_id (str): The identifier for the installment to apply the payment. Example: 34567.
        amount_applied (float): The amount to apply to the specified installment. Example: 25.
    """

    installment_id: str
    amount_applied: float

    def to_dict(self) -> dict[str, Any]:
        installment_id = self.installment_id

        amount_applied = self.amount_applied

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "installment_id": installment_id,
                "amount_applied": amount_applied,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        installment_id = d.pop("installment_id")

        amount_applied = d.pop("amount_applied")

        apply_payment_installment = cls(
            installment_id=installment_id,
            amount_applied=amount_applied,
        )

        return apply_payment_installment

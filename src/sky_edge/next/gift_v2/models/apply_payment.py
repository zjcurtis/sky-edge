from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.apply_payment_installment import ApplyPaymentInstallment


T = TypeVar("T", bound="ApplyPayment")


@_attrs_define
class ApplyPayment:
    """The payment to apply to an installment when adding a pledge payment gift

    Attributes:
        installments (list[ApplyPaymentInstallment] | None | Unset): A collection of installments the payment should be
            applied to
        parent_id (None | str | Unset): The identifier for the payment's parent gift Example: 12345.
        concurrency_id (None | str | Unset): The concurrency ID for this pledge. Retrieved from the GET endpoint.
            Example: 217f8ca6-8e10-4a6f-b1e0-5f186afa1ba7.
    """

    installments: list[ApplyPaymentInstallment] | None | Unset = UNSET
    parent_id: None | str | Unset = UNSET
    concurrency_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        installments: list[dict[str, Any]] | None | Unset
        if isinstance(self.installments, Unset):
            installments = UNSET
        elif isinstance(self.installments, list):
            installments = []
            for installments_type_0_item_data in self.installments:
                installments_type_0_item = installments_type_0_item_data.to_dict()
                installments.append(installments_type_0_item)

        else:
            installments = self.installments

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        concurrency_id: None | str | Unset
        if isinstance(self.concurrency_id, Unset):
            concurrency_id = UNSET
        else:
            concurrency_id = self.concurrency_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if installments is not UNSET:
            field_dict["installments"] = installments
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if concurrency_id is not UNSET:
            field_dict["concurrency_id"] = concurrency_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apply_payment_installment import ApplyPaymentInstallment

        d = dict(src_dict)

        def _parse_installments(
            data: object,
        ) -> list[ApplyPaymentInstallment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                installments_type_0 = []
                _installments_type_0 = data
                for installments_type_0_item_data in _installments_type_0:
                    installments_type_0_item = ApplyPaymentInstallment.from_dict(
                        installments_type_0_item_data
                    )

                    installments_type_0.append(installments_type_0_item)

                return installments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApplyPaymentInstallment] | None | Unset, data)

        installments = _parse_installments(d.pop("installments", UNSET))

        def _parse_parent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_concurrency_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        concurrency_id = _parse_concurrency_id(d.pop("concurrency_id", UNSET))

        apply_payment = cls(
            installments=installments,
            parent_id=parent_id,
            concurrency_id=concurrency_id,
        )

        return apply_payment

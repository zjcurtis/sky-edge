from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pledge_payment_read import PledgePaymentRead


T = TypeVar("T", bound="PledgePaymentsRead")


@_attrs_define
class PledgePaymentsRead:
    """Pledge payment information for a pledge gift.

    Attributes:
        pledge_id (None | str | Unset): The gift identifier of the parent pledge gift.
        pledge_payments (list[PledgePaymentRead] | None | Unset): A collection of pledge payments for the pledge.
    """

    pledge_id: None | str | Unset = UNSET
    pledge_payments: list[PledgePaymentRead] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        pledge_id: None | str | Unset
        if isinstance(self.pledge_id, Unset):
            pledge_id = UNSET
        else:
            pledge_id = self.pledge_id

        pledge_payments: list[dict[str, Any]] | None | Unset
        if isinstance(self.pledge_payments, Unset):
            pledge_payments = UNSET
        elif isinstance(self.pledge_payments, list):
            pledge_payments = []
            for pledge_payments_type_0_item_data in self.pledge_payments:
                pledge_payments_type_0_item = pledge_payments_type_0_item_data.to_dict()
                pledge_payments.append(pledge_payments_type_0_item)

        else:
            pledge_payments = self.pledge_payments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pledge_id is not UNSET:
            field_dict["pledge_id"] = pledge_id
        if pledge_payments is not UNSET:
            field_dict["pledge_payments"] = pledge_payments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pledge_payment_read import PledgePaymentRead

        d = dict(src_dict)

        def _parse_pledge_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pledge_id = _parse_pledge_id(d.pop("pledge_id", UNSET))

        def _parse_pledge_payments(
            data: object,
        ) -> list[PledgePaymentRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pledge_payments_type_0 = []
                _pledge_payments_type_0 = data
                for pledge_payments_type_0_item_data in _pledge_payments_type_0:
                    pledge_payments_type_0_item = PledgePaymentRead.from_dict(
                        pledge_payments_type_0_item_data
                    )

                    pledge_payments_type_0.append(pledge_payments_type_0_item)

                return pledge_payments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PledgePaymentRead] | None | Unset, data)

        pledge_payments = _parse_pledge_payments(d.pop("pledge_payments", UNSET))

        pledge_payments_read = cls(
            pledge_id=pledge_id,
            pledge_payments=pledge_payments,
        )

        return pledge_payments_read

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="SoftCreditRead")


@_attrs_define
class SoftCreditRead:
    """Soft credits allow you to recognize and track the indirect contributions of constituents such as spouses who
    influence the gifts of other constituents.

        Attributes:
            id (str | Unset): The immutable system record ID of the soft credit.
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the soft credit.
            gift_id (str | Unset): The immutable system record ID of the gift associated with the soft credit.
    """

    id: str | Unset = UNSET
    amount: Currency | Unset = UNSET
    constituent_id: str | Unset = UNSET
    gift_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        constituent_id = self.constituent_id

        gift_id = self.gift_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        constituent_id = d.pop("constituent_id", UNSET)

        gift_id = d.pop("gift_id", UNSET)

        soft_credit_read = cls(
            id=id,
            amount=amount,
            constituent_id=constituent_id,
            gift_id=gift_id,
        )

        soft_credit_read.additional_properties = d
        return soft_credit_read

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

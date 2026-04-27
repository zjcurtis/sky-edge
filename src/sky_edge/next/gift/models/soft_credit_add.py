from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="SoftCreditAdd")


@_attrs_define
class SoftCreditAdd:
    """Soft credits allow you to recognize and track the indirect contributions of constituents such as spouses who
    influence the gifts of other constituents.

        Attributes:
            amount (Currency): For consistency, currency is configured at the organization level. This ensures that all
                monetary amounts are consistent, regardless of where they are entered or viewed.
            constituent_id (str): The immutable system record ID of the constituent associated with the soft credit.
    """

    amount: Currency
    constituent_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount.to_dict()

        constituent_id = self.constituent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "constituent_id": constituent_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        amount = Currency.from_dict(d.pop("amount"))

        constituent_id = d.pop("constituent_id")

        soft_credit_add = cls(
            amount=amount,
            constituent_id=constituent_id,
        )

        soft_credit_add.additional_properties = d
        return soft_credit_add

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

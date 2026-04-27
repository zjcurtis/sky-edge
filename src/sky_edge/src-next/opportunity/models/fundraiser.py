from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="Fundraiser")


@_attrs_define
class Fundraiser:
    """Fundraiser constituents interact with other constituents and prospects on behalf of your organization to cultivate
    relationships and advance opportunities to secure major gifts. When the target constituent fulfills an opportunity
    ask, the fundraiser can receive credit to track performance and foster fundraising accomplishments.

        Attributes:
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the fundraiser.
            credit_amount (Currency | Unset): For consistency, currency is configured at the organization level. This
                ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
    """

    constituent_id: str | Unset = UNSET
    credit_amount: Currency | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        credit_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credit_amount, Unset):
            credit_amount = self.credit_amount.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if credit_amount is not UNSET:
            field_dict["credit_amount"] = credit_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        constituent_id = d.pop("constituent_id", UNSET)

        _credit_amount = d.pop("credit_amount", UNSET)
        credit_amount: Currency | Unset
        if isinstance(_credit_amount, Unset):
            credit_amount = UNSET
        else:
            credit_amount = Currency.from_dict(_credit_amount)

        fundraiser = cls(
            constituent_id=constituent_id,
            credit_amount=credit_amount,
        )

        fundraiser.additional_properties = d
        return fundraiser

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

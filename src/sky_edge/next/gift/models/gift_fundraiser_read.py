from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="GiftFundraiserRead")


@_attrs_define
class GiftFundraiserRead:
    """Fundraiser constituents interact with other constituents and prospects on behalf of your organization to cultivate
    relationships and request donations. When a constituent makes a donation, the fundraiser can receive credit to track
    performance and foster fundraising accomplishments.

        Attributes:
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            constituent_id (str | Unset): The immutable constituent system record ID for the fundraiser associated with the
                gift.
    """

    amount: Currency | Unset = UNSET
    constituent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        constituent_id = self.constituent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        constituent_id = d.pop("constituent_id", UNSET)

        gift_fundraiser_read = cls(
            amount=amount,
            constituent_id=constituent_id,
        )

        gift_fundraiser_read.additional_properties = d
        return gift_fundraiser_read

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

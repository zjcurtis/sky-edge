from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="GiftSplitAdd")


@_attrs_define
class GiftSplitAdd:
    """Not all gifts serve a single purpose. Gift splits track donor wishes and allow you to divide gifts among multiple
    campaigns, funds, and appeals.

        Attributes:
            amount (Currency): For consistency, currency is configured at the organization level. This ensures that all
                monetary amounts are consistent, regardless of where they are entered or viewed.
            fund_id (str): The immutable system record ID of the fund associated with the gift split.
            appeal_id (str | Unset): The immutable system record ID of the appeal associated with the gift split.
            campaign_id (str | Unset): The immutable system record ID of the campaign associated with the gift split.
            package_id (str | Unset): The immutable system record ID of the package associated with the gift split.
    """

    amount: Currency
    fund_id: str
    appeal_id: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    package_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount.to_dict()

        fund_id = self.fund_id

        appeal_id = self.appeal_id

        campaign_id = self.campaign_id

        package_id = self.package_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "fund_id": fund_id,
            }
        )
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if package_id is not UNSET:
            field_dict["package_id"] = package_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        amount = Currency.from_dict(d.pop("amount"))

        fund_id = d.pop("fund_id")

        appeal_id = d.pop("appeal_id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        package_id = d.pop("package_id", UNSET)

        gift_split_add = cls(
            amount=amount,
            fund_id=fund_id,
            appeal_id=appeal_id,
            campaign_id=campaign_id,
            package_id=package_id,
        )

        gift_split_add.additional_properties = d
        return gift_split_add

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

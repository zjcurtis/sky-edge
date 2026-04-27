from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="GiftSplitRead")


@_attrs_define
class GiftSplitRead:
    """Not all gifts serve a single purpose. Gift splits track donor wishes and allow you to divide gifts among multiple
    campaigns, funds, and appeals.

        Attributes:
            id (str | Unset): The immutable system record ID of the gift split.
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            appeal_id (str | Unset): The immutable system record ID of the appeal associated with the gift split.
            campaign_id (str | Unset): The immutable system record ID of the campaign associated with the gift split.
            fund_id (str | Unset): The immutable system record ID of the fund associated with the gift split.
            gift_aid_amount (Currency | Unset): For consistency, currency is configured at the organization level. This
                ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            gift_aid_qualification_status (str | Unset): The gift aid qualification status of the gift split. Available
                values are: <i>Qualified</i>, and <i>NotQualified</i>. For the UK only.
            package_id (str | Unset): The immutable system record ID of the package associated with the gift split.
    """

    id: str | Unset = UNSET
    amount: Currency | Unset = UNSET
    appeal_id: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    fund_id: str | Unset = UNSET
    gift_aid_amount: Currency | Unset = UNSET
    gift_aid_qualification_status: str | Unset = UNSET
    package_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        appeal_id = self.appeal_id

        campaign_id = self.campaign_id

        fund_id = self.fund_id

        gift_aid_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_aid_amount, Unset):
            gift_aid_amount = self.gift_aid_amount.to_dict()

        gift_aid_qualification_status = self.gift_aid_qualification_status

        package_id = self.package_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if gift_aid_amount is not UNSET:
            field_dict["gift_aid_amount"] = gift_aid_amount
        if gift_aid_qualification_status is not UNSET:
            field_dict["gift_aid_qualification_status"] = gift_aid_qualification_status
        if package_id is not UNSET:
            field_dict["package_id"] = package_id

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

        appeal_id = d.pop("appeal_id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        fund_id = d.pop("fund_id", UNSET)

        _gift_aid_amount = d.pop("gift_aid_amount", UNSET)
        gift_aid_amount: Currency | Unset
        if isinstance(_gift_aid_amount, Unset):
            gift_aid_amount = UNSET
        else:
            gift_aid_amount = Currency.from_dict(_gift_aid_amount)

        gift_aid_qualification_status = d.pop("gift_aid_qualification_status", UNSET)

        package_id = d.pop("package_id", UNSET)

        gift_split_read = cls(
            id=id,
            amount=amount,
            appeal_id=appeal_id,
            campaign_id=campaign_id,
            fund_id=fund_id,
            gift_aid_amount=gift_aid_amount,
            gift_aid_qualification_status=gift_aid_qualification_status,
            package_id=package_id,
        )

        gift_split_read.additional_properties = d
        return gift_split_read

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

from ..models.goal_edit_type import GoalEditType

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="GoalEdit")


@_attrs_define
class GoalEdit:
    """To help motivate fundraisers and track their effectiveness, your organization may set goal amounts to raise toward
    funds, campaigns, or appeals.

        Attributes:
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            appeal_id (str | Unset): The immutable system record ID of the appeal associated with the fundraiser goal.
            campaign_id (str | Unset): The immutable system record ID of the campaign associated with the fundraiser goal.
            fund_id (str | Unset): The immutable system record ID of the fund associated with the fundraiser goal.
            type_ (GoalEditType | Unset): The fundraiser goal type. Available values are <i>Campaign</i>, <i>Fund</i>,
                <i>UnspecifiedCategory</i>, and <i>Appeal</i>.  This property cannot be set to null.
            unspecified_category_name (str | Unset): The unspecified category name for the fundraiser goal. Available values
                are the active entries in the <a href="https://developer.sky.blackbaud.com/docs/services/58bdd6c8d7dcde06046081d
                7/operations/ListFundraiserGoalCategories"><b>Solicitor Goal Categories</b></a> table.
    """

    amount: Currency | Unset = UNSET
    appeal_id: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    fund_id: str | Unset = UNSET
    type_: GoalEditType | Unset = UNSET
    unspecified_category_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        appeal_id = self.appeal_id

        campaign_id = self.campaign_id

        fund_id = self.fund_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        unspecified_category_name = self.unspecified_category_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if unspecified_category_name is not UNSET:
            field_dict["unspecified_category_name"] = unspecified_category_name

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

        appeal_id = d.pop("appeal_id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        fund_id = d.pop("fund_id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: GoalEditType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GoalEditType(_type_)

        unspecified_category_name = d.pop("unspecified_category_name", UNSET)

        goal_edit = cls(
            amount=amount,
            appeal_id=appeal_id,
            campaign_id=campaign_id,
            fund_id=fund_id,
            type_=type_,
            unspecified_category_name=unspecified_category_name,
        )

        goal_edit.additional_properties = d
        return goal_edit

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

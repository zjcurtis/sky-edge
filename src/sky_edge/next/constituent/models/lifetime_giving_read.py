from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="LifetimeGivingRead")


@_attrs_define
class LifetimeGivingRead:
    """Lifetime giving represents cumulative information about giving history throughout a constituent’s association with
    your organization.

        Attributes:
            consecutive_years_given (int | Unset): This computed field calculates the number of consecutive years the
                constituent has given.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the lifetime
                giving.
            total_committed_matching_gifts (Currency | Unset): For consistency, currency is configured at the organization
                level. This ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            total_giving (Currency | Unset): For consistency, currency is configured at the organization level. This ensures
                that all monetary amounts are consistent, regardless of where they are entered or viewed.
            total_pledge_balance (Currency | Unset): For consistency, currency is configured at the organization level. This
                ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            total_received_giving (Currency | Unset): For consistency, currency is configured at the organization level.
                This ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            total_received_matching_gifts (Currency | Unset): For consistency, currency is configured at the organization
                level. This ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            total_soft_credits (Currency | Unset): For consistency, currency is configured at the organization level. This
                ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            total_years_given (int | Unset): This computed field calculates the total number of years the constituent has
                given.
    """

    consecutive_years_given: int | Unset = UNSET
    constituent_id: str | Unset = UNSET
    total_committed_matching_gifts: Currency | Unset = UNSET
    total_giving: Currency | Unset = UNSET
    total_pledge_balance: Currency | Unset = UNSET
    total_received_giving: Currency | Unset = UNSET
    total_received_matching_gifts: Currency | Unset = UNSET
    total_soft_credits: Currency | Unset = UNSET
    total_years_given: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consecutive_years_given = self.consecutive_years_given

        constituent_id = self.constituent_id

        total_committed_matching_gifts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_committed_matching_gifts, Unset):
            total_committed_matching_gifts = (
                self.total_committed_matching_gifts.to_dict()
            )

        total_giving: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_giving, Unset):
            total_giving = self.total_giving.to_dict()

        total_pledge_balance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_pledge_balance, Unset):
            total_pledge_balance = self.total_pledge_balance.to_dict()

        total_received_giving: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_received_giving, Unset):
            total_received_giving = self.total_received_giving.to_dict()

        total_received_matching_gifts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_received_matching_gifts, Unset):
            total_received_matching_gifts = self.total_received_matching_gifts.to_dict()

        total_soft_credits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_soft_credits, Unset):
            total_soft_credits = self.total_soft_credits.to_dict()

        total_years_given = self.total_years_given

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consecutive_years_given is not UNSET:
            field_dict["consecutive_years_given"] = consecutive_years_given
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if total_committed_matching_gifts is not UNSET:
            field_dict["total_committed_matching_gifts"] = (
                total_committed_matching_gifts
            )
        if total_giving is not UNSET:
            field_dict["total_giving"] = total_giving
        if total_pledge_balance is not UNSET:
            field_dict["total_pledge_balance"] = total_pledge_balance
        if total_received_giving is not UNSET:
            field_dict["total_received_giving"] = total_received_giving
        if total_received_matching_gifts is not UNSET:
            field_dict["total_received_matching_gifts"] = total_received_matching_gifts
        if total_soft_credits is not UNSET:
            field_dict["total_soft_credits"] = total_soft_credits
        if total_years_given is not UNSET:
            field_dict["total_years_given"] = total_years_given

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)
        consecutive_years_given = d.pop("consecutive_years_given", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _total_committed_matching_gifts = d.pop("total_committed_matching_gifts", UNSET)
        total_committed_matching_gifts: Currency | Unset
        if isinstance(_total_committed_matching_gifts, Unset):
            total_committed_matching_gifts = UNSET
        else:
            total_committed_matching_gifts = Currency.from_dict(
                _total_committed_matching_gifts
            )

        _total_giving = d.pop("total_giving", UNSET)
        total_giving: Currency | Unset
        if isinstance(_total_giving, Unset):
            total_giving = UNSET
        else:
            total_giving = Currency.from_dict(_total_giving)

        _total_pledge_balance = d.pop("total_pledge_balance", UNSET)
        total_pledge_balance: Currency | Unset
        if isinstance(_total_pledge_balance, Unset):
            total_pledge_balance = UNSET
        else:
            total_pledge_balance = Currency.from_dict(_total_pledge_balance)

        _total_received_giving = d.pop("total_received_giving", UNSET)
        total_received_giving: Currency | Unset
        if isinstance(_total_received_giving, Unset):
            total_received_giving = UNSET
        else:
            total_received_giving = Currency.from_dict(_total_received_giving)

        _total_received_matching_gifts = d.pop("total_received_matching_gifts", UNSET)
        total_received_matching_gifts: Currency | Unset
        if isinstance(_total_received_matching_gifts, Unset):
            total_received_matching_gifts = UNSET
        else:
            total_received_matching_gifts = Currency.from_dict(
                _total_received_matching_gifts
            )

        _total_soft_credits = d.pop("total_soft_credits", UNSET)
        total_soft_credits: Currency | Unset
        if isinstance(_total_soft_credits, Unset):
            total_soft_credits = UNSET
        else:
            total_soft_credits = Currency.from_dict(_total_soft_credits)

        total_years_given = d.pop("total_years_given", UNSET)

        lifetime_giving_read = cls(
            consecutive_years_given=consecutive_years_given,
            constituent_id=constituent_id,
            total_committed_matching_gifts=total_committed_matching_gifts,
            total_giving=total_giving,
            total_pledge_balance=total_pledge_balance,
            total_received_giving=total_received_giving,
            total_received_matching_gifts=total_received_matching_gifts,
            total_soft_credits=total_soft_credits,
            total_years_given=total_years_given,
        )

        lifetime_giving_read.additional_properties = d
        return lifetime_giving_read

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

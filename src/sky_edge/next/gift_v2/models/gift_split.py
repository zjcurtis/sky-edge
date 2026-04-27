from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.currency import Currency


T = TypeVar("T", bound="GiftSplit")


@_attrs_define
class GiftSplit:
    """A gift's split.

    Attributes:
        id (None | str | Unset): The ID of the split. Example: 12345.
        amount (Currency | Unset): An amount denominated in a specific currency.
        fund_id (None | str | Unset): The ID of the fund to apply the amount to. Example: 1234.
        campaign_id (None | str | Unset): The ID of the campaign to apply the amount to. Example: 1234.
        appeal_id (None | str | Unset): The ID of the appeal to apply the amount to. Example: 1234.
        package_id (None | str | Unset): The ID of the package to apply the amount to. Example: 1234.
        donor_covered (bool | None | Unset): True if split represents donor covering some portion of the processing
            fees.
    """

    id: None | str | Unset = UNSET
    amount: Currency | Unset = UNSET
    fund_id: None | str | Unset = UNSET
    campaign_id: None | str | Unset = UNSET
    appeal_id: None | str | Unset = UNSET
    package_id: None | str | Unset = UNSET
    donor_covered: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        fund_id: None | str | Unset
        if isinstance(self.fund_id, Unset):
            fund_id = UNSET
        else:
            fund_id = self.fund_id

        campaign_id: None | str | Unset
        if isinstance(self.campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = self.campaign_id

        appeal_id: None | str | Unset
        if isinstance(self.appeal_id, Unset):
            appeal_id = UNSET
        else:
            appeal_id = self.appeal_id

        package_id: None | str | Unset
        if isinstance(self.package_id, Unset):
            package_id = UNSET
        else:
            package_id = self.package_id

        donor_covered: bool | None | Unset
        if isinstance(self.donor_covered, Unset):
            donor_covered = UNSET
        else:
            donor_covered = self.donor_covered

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if donor_covered is not UNSET:
            field_dict["donor_covered"] = donor_covered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        def _parse_fund_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fund_id = _parse_fund_id(d.pop("fund_id", UNSET))

        def _parse_campaign_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign_id = _parse_campaign_id(d.pop("campaign_id", UNSET))

        def _parse_appeal_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appeal_id = _parse_appeal_id(d.pop("appeal_id", UNSET))

        def _parse_package_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_id = _parse_package_id(d.pop("package_id", UNSET))

        def _parse_donor_covered(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        donor_covered = _parse_donor_covered(d.pop("donor_covered", UNSET))

        gift_split = cls(
            id=id,
            amount=amount,
            fund_id=fund_id,
            campaign_id=campaign_id,
            appeal_id=appeal_id,
            package_id=package_id,
            donor_covered=donor_covered,
        )

        return gift_split

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.splits_gift_aid_qualification_method import SplitsGiftAidQualificationMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="Splits")


@_attrs_define
class Splits:
    """Represents the gift split

    Attributes:
        gift_split_id (int | Unset): The immutable system record ID of the gift split.
        campaign_id (int | None | Unset): The campaign ID associated with the campaign table.
        fund_id (int | Unset): The fund ID associated with the fund table.
        appeal_id (int | None | Unset): The appeal ID associated with the appeal table.
        package_id (int | None | Unset): The package ID associated with the package table.
        amount (float | Unset): The amount which gift split represents.
        gift_aid_qualification_method (SplitsGiftAidQualificationMethod | Unset): Specifies the qualification methods
            for determining gift aid.
        campaign (None | str | Unset): Indicates campaign for the record.
        fund (None | str | Unset): Indicates fund for the record.
        appeal (None | str | Unset): Indicates appeal for the record.
        package (None | str | Unset): Indicates package for the record.
    """

    gift_split_id: int | Unset = UNSET
    campaign_id: int | None | Unset = UNSET
    fund_id: int | Unset = UNSET
    appeal_id: int | None | Unset = UNSET
    package_id: int | None | Unset = UNSET
    amount: float | Unset = UNSET
    gift_aid_qualification_method: SplitsGiftAidQualificationMethod | Unset = UNSET
    campaign: None | str | Unset = UNSET
    fund: None | str | Unset = UNSET
    appeal: None | str | Unset = UNSET
    package: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_split_id = self.gift_split_id

        campaign_id: int | None | Unset
        if isinstance(self.campaign_id, Unset):
            campaign_id = UNSET
        else:
            campaign_id = self.campaign_id

        fund_id = self.fund_id

        appeal_id: int | None | Unset
        if isinstance(self.appeal_id, Unset):
            appeal_id = UNSET
        else:
            appeal_id = self.appeal_id

        package_id: int | None | Unset
        if isinstance(self.package_id, Unset):
            package_id = UNSET
        else:
            package_id = self.package_id

        amount = self.amount

        gift_aid_qualification_method: str | Unset = UNSET
        if not isinstance(self.gift_aid_qualification_method, Unset):
            gift_aid_qualification_method = self.gift_aid_qualification_method.value

        campaign: None | str | Unset
        if isinstance(self.campaign, Unset):
            campaign = UNSET
        else:
            campaign = self.campaign

        fund: None | str | Unset
        if isinstance(self.fund, Unset):
            fund = UNSET
        else:
            fund = self.fund

        appeal: None | str | Unset
        if isinstance(self.appeal, Unset):
            appeal = UNSET
        else:
            appeal = self.appeal

        package: None | str | Unset
        if isinstance(self.package, Unset):
            package = UNSET
        else:
            package = self.package

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_split_id is not UNSET:
            field_dict["gift_split_id"] = gift_split_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if fund_id is not UNSET:
            field_dict["fund_id"] = fund_id
        if appeal_id is not UNSET:
            field_dict["appeal_id"] = appeal_id
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if gift_aid_qualification_method is not UNSET:
            field_dict["gift_aid_qualification_method"] = gift_aid_qualification_method
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if fund is not UNSET:
            field_dict["fund"] = fund
        if appeal is not UNSET:
            field_dict["appeal"] = appeal
        if package is not UNSET:
            field_dict["package"] = package

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_split_id = d.pop("gift_split_id", UNSET)

        def _parse_campaign_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        campaign_id = _parse_campaign_id(d.pop("campaign_id", UNSET))

        fund_id = d.pop("fund_id", UNSET)

        def _parse_appeal_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        appeal_id = _parse_appeal_id(d.pop("appeal_id", UNSET))

        def _parse_package_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        package_id = _parse_package_id(d.pop("package_id", UNSET))

        amount = d.pop("amount", UNSET)

        _gift_aid_qualification_method = d.pop("gift_aid_qualification_method", UNSET)
        gift_aid_qualification_method: SplitsGiftAidQualificationMethod | Unset
        if isinstance(_gift_aid_qualification_method, Unset):
            gift_aid_qualification_method = UNSET
        else:
            gift_aid_qualification_method = SplitsGiftAidQualificationMethod(_gift_aid_qualification_method)

        def _parse_campaign(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        campaign = _parse_campaign(d.pop("campaign", UNSET))

        def _parse_fund(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fund = _parse_fund(d.pop("fund", UNSET))

        def _parse_appeal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appeal = _parse_appeal(d.pop("appeal", UNSET))

        def _parse_package(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package = _parse_package(d.pop("package", UNSET))

        splits = cls(
            gift_split_id=gift_split_id,
            campaign_id=campaign_id,
            fund_id=fund_id,
            appeal_id=appeal_id,
            package_id=package_id,
            amount=amount,
            gift_aid_qualification_method=gift_aid_qualification_method,
            campaign=campaign,
            fund=fund,
            appeal=appeal,
            package=package,
        )

        return splits

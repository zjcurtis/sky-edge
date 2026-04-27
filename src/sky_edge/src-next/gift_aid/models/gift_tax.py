from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.gift_tax_gift_aid_qualification_method import GiftTaxGiftAidQualificationMethod
from ..models.gift_tax_gift_aid_qualification_status import GiftTaxGiftAidQualificationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.splits import Splits


T = TypeVar("T", bound="GiftTax")


@_attrs_define
class GiftTax:
    """Represents the gift tax

    Attributes:
        id (int | Unset): The immutable system record ID of the gift tax.
        constituent_id (int | Unset): The constituent ID of the individual.
        gift_aid_qualification_method (GiftTaxGiftAidQualificationMethod | Unset): Specifies the qualification methods
            for determining gift aid.
        gift_aid_qualification_status (GiftTaxGiftAidQualificationStatus | Unset): Specifies the GiftAid qualification
            status.
        gift_date (datetime.date | Unset): Refers the date of Gift.
        claim_number (None | str | Unset): Refers gift claim number.
        tax_claim_amount (float | Unset): Refers tax claim amount.
        gift_splits (list[Splits] | None | Unset): Represents the gift splits.
    """

    id: int | Unset = UNSET
    constituent_id: int | Unset = UNSET
    gift_aid_qualification_method: GiftTaxGiftAidQualificationMethod | Unset = UNSET
    gift_aid_qualification_status: GiftTaxGiftAidQualificationStatus | Unset = UNSET
    gift_date: datetime.date | Unset = UNSET
    claim_number: None | str | Unset = UNSET
    tax_claim_amount: float | Unset = UNSET
    gift_splits: list[Splits] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constituent_id = self.constituent_id

        gift_aid_qualification_method: str | Unset = UNSET
        if not isinstance(self.gift_aid_qualification_method, Unset):
            gift_aid_qualification_method = self.gift_aid_qualification_method.value

        gift_aid_qualification_status: str | Unset = UNSET
        if not isinstance(self.gift_aid_qualification_status, Unset):
            gift_aid_qualification_status = self.gift_aid_qualification_status.value

        gift_date: str | Unset = UNSET
        if not isinstance(self.gift_date, Unset):
            gift_date = self.gift_date.isoformat()

        claim_number: None | str | Unset
        if isinstance(self.claim_number, Unset):
            claim_number = UNSET
        else:
            claim_number = self.claim_number

        tax_claim_amount = self.tax_claim_amount

        gift_splits: list[dict[str, Any]] | None | Unset
        if isinstance(self.gift_splits, Unset):
            gift_splits = UNSET
        elif isinstance(self.gift_splits, list):
            gift_splits = []
            for gift_splits_type_0_item_data in self.gift_splits:
                gift_splits_type_0_item = gift_splits_type_0_item_data.to_dict()
                gift_splits.append(gift_splits_type_0_item)

        else:
            gift_splits = self.gift_splits

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if gift_aid_qualification_method is not UNSET:
            field_dict["gift_aid_qualification_method"] = gift_aid_qualification_method
        if gift_aid_qualification_status is not UNSET:
            field_dict["gift_aid_qualification_status"] = gift_aid_qualification_status
        if gift_date is not UNSET:
            field_dict["gift_date"] = gift_date
        if claim_number is not UNSET:
            field_dict["claim_number"] = claim_number
        if tax_claim_amount is not UNSET:
            field_dict["tax_claim_amount"] = tax_claim_amount
        if gift_splits is not UNSET:
            field_dict["gift_splits"] = gift_splits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.splits import Splits

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _gift_aid_qualification_method = d.pop("gift_aid_qualification_method", UNSET)
        gift_aid_qualification_method: GiftTaxGiftAidQualificationMethod | Unset
        if isinstance(_gift_aid_qualification_method, Unset):
            gift_aid_qualification_method = UNSET
        else:
            gift_aid_qualification_method = GiftTaxGiftAidQualificationMethod(_gift_aid_qualification_method)

        _gift_aid_qualification_status = d.pop("gift_aid_qualification_status", UNSET)
        gift_aid_qualification_status: GiftTaxGiftAidQualificationStatus | Unset
        if isinstance(_gift_aid_qualification_status, Unset):
            gift_aid_qualification_status = UNSET
        else:
            gift_aid_qualification_status = GiftTaxGiftAidQualificationStatus(_gift_aid_qualification_status)

        _gift_date = d.pop("gift_date", UNSET)
        gift_date: datetime.date | Unset
        if isinstance(_gift_date, Unset):
            gift_date = UNSET
        else:
            gift_date = isoparse(_gift_date).date()

        def _parse_claim_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_number = _parse_claim_number(d.pop("claim_number", UNSET))

        tax_claim_amount = d.pop("tax_claim_amount", UNSET)

        def _parse_gift_splits(data: object) -> list[Splits] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gift_splits_type_0 = []
                _gift_splits_type_0 = data
                for gift_splits_type_0_item_data in _gift_splits_type_0:
                    gift_splits_type_0_item = Splits.from_dict(gift_splits_type_0_item_data)

                    gift_splits_type_0.append(gift_splits_type_0_item)

                return gift_splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Splits] | None | Unset, data)

        gift_splits = _parse_gift_splits(d.pop("gift_splits", UNSET))

        gift_tax = cls(
            id=id,
            constituent_id=constituent_id,
            gift_aid_qualification_method=gift_aid_qualification_method,
            gift_aid_qualification_status=gift_aid_qualification_status,
            gift_date=gift_date,
            claim_number=claim_number,
            tax_claim_amount=tax_claim_amount,
            gift_splits=gift_splits,
        )

        return gift_tax

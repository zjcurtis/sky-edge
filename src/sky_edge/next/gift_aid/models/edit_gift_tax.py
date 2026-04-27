from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.edit_gift_tax_gift_aid_qualification_method import (
    EditGiftTaxGiftAidQualificationMethod,
)

T = TypeVar("T", bound="EditGiftTax")


@_attrs_define
class EditGiftTax:
    """Gift Tax edit model

    Attributes:
        gift_aid_q_method (EditGiftTaxGiftAidQualificationMethod | Unset): Specifies the qualification methods for
            determining gift aid.
        claim_number (None | str | Unset): Claim number
    """

    gift_aid_q_method: EditGiftTaxGiftAidQualificationMethod | Unset = UNSET
    claim_number: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_aid_q_method: str | Unset = UNSET
        if not isinstance(self.gift_aid_q_method, Unset):
            gift_aid_q_method = self.gift_aid_q_method.value

        claim_number: None | str | Unset
        if isinstance(self.claim_number, Unset):
            claim_number = UNSET
        else:
            claim_number = self.claim_number

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_aid_q_method is not UNSET:
            field_dict["gift_aid_q_method"] = gift_aid_q_method
        if claim_number is not UNSET:
            field_dict["claim_number"] = claim_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _gift_aid_q_method = d.pop("gift_aid_q_method", UNSET)
        gift_aid_q_method: EditGiftTaxGiftAidQualificationMethod | Unset
        if isinstance(_gift_aid_q_method, Unset):
            gift_aid_q_method = UNSET
        else:
            gift_aid_q_method = EditGiftTaxGiftAidQualificationMethod(
                _gift_aid_q_method
            )

        def _parse_claim_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_number = _parse_claim_number(d.pop("claim_number", UNSET))

        edit_gift_tax = cls(
            gift_aid_q_method=gift_aid_q_method,
            claim_number=claim_number,
        )

        return edit_gift_tax

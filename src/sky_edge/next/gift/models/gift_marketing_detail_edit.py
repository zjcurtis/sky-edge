from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="GiftMarketingDetailEdit")


@_attrs_define
class GiftMarketingDetailEdit:
    """Represents marketing information for a gift.

    Attributes:
        finder_number (int | Unset): Gets or sets the gift's finder number. The finder number cannot be negative.
        mailing_id (str | Unset): Gets or sets the gift's mailing identifier.
        marketing_source_code (str | Unset): Gets or sets the gift's marketing source code. Character limit: 255.
    """

    finder_number: int | Unset = UNSET
    mailing_id: str | Unset = UNSET
    marketing_source_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        finder_number = self.finder_number

        mailing_id = self.mailing_id

        marketing_source_code = self.marketing_source_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if finder_number is not UNSET:
            field_dict["finder_number"] = finder_number
        if mailing_id is not UNSET:
            field_dict["mailing_id"] = mailing_id
        if marketing_source_code is not UNSET:
            field_dict["marketing_source_code"] = marketing_source_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        finder_number = d.pop("finder_number", UNSET)

        mailing_id = d.pop("mailing_id", UNSET)

        marketing_source_code = d.pop("marketing_source_code", UNSET)

        gift_marketing_detail_edit = cls(
            finder_number=finder_number,
            mailing_id=mailing_id,
            marketing_source_code=marketing_source_code,
        )

        gift_marketing_detail_edit.additional_properties = d
        return gift_marketing_detail_edit

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

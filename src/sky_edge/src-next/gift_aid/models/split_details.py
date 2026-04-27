from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.split_details_gift_aid_qualification_method import SplitDetailsGiftAidQualificationMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="SplitDetails")


@_attrs_define
class SplitDetails:
    """Gift splits

    Attributes:
        gift_split_id (int): The immutable system gift split ID.
        gift_aid_qualification_method (SplitDetailsGiftAidQualificationMethod | Unset): Specifies the qualification
            methods for determining gift aid.
    """

    gift_split_id: int
    gift_aid_qualification_method: SplitDetailsGiftAidQualificationMethod | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_split_id = self.gift_split_id

        gift_aid_qualification_method: str | Unset = UNSET
        if not isinstance(self.gift_aid_qualification_method, Unset):
            gift_aid_qualification_method = self.gift_aid_qualification_method.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_split_id": gift_split_id,
            }
        )
        if gift_aid_qualification_method is not UNSET:
            field_dict["gift_aid_qualification_method"] = gift_aid_qualification_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_split_id = d.pop("gift_split_id")

        _gift_aid_qualification_method = d.pop("gift_aid_qualification_method", UNSET)
        gift_aid_qualification_method: SplitDetailsGiftAidQualificationMethod | Unset
        if isinstance(_gift_aid_qualification_method, Unset):
            gift_aid_qualification_method = UNSET
        else:
            gift_aid_qualification_method = SplitDetailsGiftAidQualificationMethod(_gift_aid_qualification_method)

        split_details = cls(
            gift_split_id=gift_split_id,
            gift_aid_qualification_method=gift_aid_qualification_method,
        )

        return split_details

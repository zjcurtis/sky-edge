from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.split_details import SplitDetails


T = TypeVar("T", bound="EditGiftSplitsTax")


@_attrs_define
class EditGiftSplitsTax:
    """Gift splits tax edit model

    Attributes:
        claim_number (None | str | Unset): Claim number
        split_details (list[SplitDetails] | None | Unset): Required list of gift split to update
    """

    claim_number: None | str | Unset = UNSET
    split_details: list[SplitDetails] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        claim_number: None | str | Unset
        if isinstance(self.claim_number, Unset):
            claim_number = UNSET
        else:
            claim_number = self.claim_number

        split_details: list[dict[str, Any]] | None | Unset
        if isinstance(self.split_details, Unset):
            split_details = UNSET
        elif isinstance(self.split_details, list):
            split_details = []
            for split_details_type_0_item_data in self.split_details:
                split_details_type_0_item = split_details_type_0_item_data.to_dict()
                split_details.append(split_details_type_0_item)

        else:
            split_details = self.split_details

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if claim_number is not UNSET:
            field_dict["claim_number"] = claim_number
        if split_details is not UNSET:
            field_dict["split_details"] = split_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.split_details import SplitDetails

        d = dict(src_dict)

        def _parse_claim_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        claim_number = _parse_claim_number(d.pop("claim_number", UNSET))

        def _parse_split_details(data: object) -> list[SplitDetails] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                split_details_type_0 = []
                _split_details_type_0 = data
                for split_details_type_0_item_data in _split_details_type_0:
                    split_details_type_0_item = SplitDetails.from_dict(split_details_type_0_item_data)

                    split_details_type_0.append(split_details_type_0_item)

                return split_details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SplitDetails] | None | Unset, data)

        split_details = _parse_split_details(d.pop("split_details", UNSET))

        edit_gift_splits_tax = cls(
            claim_number=claim_number,
            split_details=split_details,
        )

        return edit_gift_splits_tax

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.planned_gift_beneficiary_response import PlannedGiftBeneficiaryResponse


T = TypeVar("T", bound="PlannedGiftBeneficiaryListResponse")


@_attrs_define
class PlannedGiftBeneficiaryListResponse:
    """Represents the paginated list response for planned gift beneficiaries.

    Attributes:
        count (int): The total number of beneficiaries.
        offset (int): The number of records that were skipped in the current request.
        limit (int): The maximum number of records that were requested.
        beneficiaries (list[PlannedGiftBeneficiaryResponse]): The list of planned gift beneficiaries.
    """

    count: int
    offset: int
    limit: int
    beneficiaries: list[PlannedGiftBeneficiaryResponse]

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        offset = self.offset

        limit = self.limit

        beneficiaries = []
        for beneficiaries_item_data in self.beneficiaries:
            beneficiaries_item = beneficiaries_item_data.to_dict()
            beneficiaries.append(beneficiaries_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "offset": offset,
                "limit": limit,
                "beneficiaries": beneficiaries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.planned_gift_beneficiary_response import PlannedGiftBeneficiaryResponse

        d = dict(src_dict)
        count = d.pop("count")

        offset = d.pop("offset")

        limit = d.pop("limit")

        beneficiaries = []
        _beneficiaries = d.pop("beneficiaries")
        for beneficiaries_item_data in _beneficiaries:
            beneficiaries_item = PlannedGiftBeneficiaryResponse.from_dict(beneficiaries_item_data)

            beneficiaries.append(beneficiaries_item)

        planned_gift_beneficiary_list_response = cls(
            count=count,
            offset=offset,
            limit=limit,
            beneficiaries=beneficiaries,
        )

        return planned_gift_beneficiary_list_response

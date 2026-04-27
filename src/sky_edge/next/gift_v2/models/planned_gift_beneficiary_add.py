from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="PlannedGiftBeneficiaryAdd")


@_attrs_define
class PlannedGiftBeneficiaryAdd:
    """Model for adding a new planned gift beneficiary.

    Attributes:
        type_of_relationship (str): The type of relationship. Valid values: "None" (self-beneficiary), "Individual",
            "Organization", "Financial", "Education".
        beneficiary_type (str): The beneficiary type. Valid values depend on the gift's vehicle type.
        relationship_id (None | str | Unset): The relationship record identifier. Required when type_of_relationship is
            not "None".
    """

    type_of_relationship: str
    beneficiary_type: str
    relationship_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_of_relationship = self.type_of_relationship

        beneficiary_type = self.beneficiary_type

        relationship_id: None | str | Unset
        if isinstance(self.relationship_id, Unset):
            relationship_id = UNSET
        else:
            relationship_id = self.relationship_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type_of_relationship": type_of_relationship,
                "beneficiary_type": beneficiary_type,
            }
        )
        if relationship_id is not UNSET:
            field_dict["relationship_id"] = relationship_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_of_relationship = d.pop("type_of_relationship")

        beneficiary_type = d.pop("beneficiary_type")

        def _parse_relationship_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship_id = _parse_relationship_id(d.pop("relationship_id", UNSET))

        planned_gift_beneficiary_add = cls(
            type_of_relationship=type_of_relationship,
            beneficiary_type=beneficiary_type,
            relationship_id=relationship_id,
        )

        return planned_gift_beneficiary_add

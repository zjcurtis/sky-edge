from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry
    from ..models.currency import Currency


T = TypeVar("T", bound="PlannedGiftAssetResponse")


@_attrs_define
class PlannedGiftAssetResponse:
    """Represents a single planned gift asset in the API response.

    Attributes:
        id (None | str): The unique identifier of the asset.
        asset_type (CodeTableEntry): A predefined entry in a code table.
        amount (Currency): An amount denominated in a specific currency.
        cost_basis (Currency): An amount denominated in a specific currency.
        sequence (int): The sequence order of the asset within the gift.
        description (None | str | Unset): The description of the asset.
    """

    id: None | str
    asset_type: CodeTableEntry
    amount: Currency
    cost_basis: Currency
    sequence: int
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        asset_type = self.asset_type.to_dict()

        amount = self.amount.to_dict()

        cost_basis = self.cost_basis.to_dict()

        sequence = self.sequence

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "asset_type": asset_type,
                "amount": amount,
                "cost_basis": cost_basis,
                "sequence": sequence,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry
        from ..models.currency import Currency

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        asset_type = CodeTableEntry.from_dict(d.pop("asset_type"))

        amount = Currency.from_dict(d.pop("amount"))

        cost_basis = Currency.from_dict(d.pop("cost_basis"))

        sequence = d.pop("sequence")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        planned_gift_asset_response = cls(
            id=id,
            asset_type=asset_type,
            amount=amount,
            cost_basis=cost_basis,
            sequence=sequence,
            description=description,
        )

        return planned_gift_asset_response

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry
    from ..models.currency import Currency


T = TypeVar("T", bound="PlannedGiftAssetAdd")


@_attrs_define
class PlannedGiftAssetAdd:
    """Model for adding a new planned gift asset.

    Attributes:
        asset_type (CodeTableEntry): A predefined entry in a code table.
        description (None | str | Unset): Description of the asset.
        amount (Currency | Unset): An amount denominated in a specific currency.
        cost_basis (Currency | Unset): An amount denominated in a specific currency.
    """

    asset_type: CodeTableEntry
    description: None | str | Unset = UNSET
    amount: Currency | Unset = UNSET
    cost_basis: Currency | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_type = self.asset_type.to_dict()

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        cost_basis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cost_basis, Unset):
            cost_basis = self.cost_basis.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "asset_type": asset_type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if amount is not UNSET:
            field_dict["amount"] = amount
        if cost_basis is not UNSET:
            field_dict["cost_basis"] = cost_basis

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry
        from ..models.currency import Currency

        d = dict(src_dict)
        asset_type = CodeTableEntry.from_dict(d.pop("asset_type"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        _cost_basis = d.pop("cost_basis", UNSET)
        cost_basis: Currency | Unset
        if isinstance(_cost_basis, Unset):
            cost_basis = UNSET
        else:
            cost_basis = Currency.from_dict(_cost_basis)

        planned_gift_asset_add = cls(
            asset_type=asset_type,
            description=description,
            amount=amount,
            cost_basis=cost_basis,
        )

        return planned_gift_asset_add

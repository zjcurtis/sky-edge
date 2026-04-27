from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry
    from ..models.currency import Currency


T = TypeVar("T", bound="PlannedGiftAssetEdit")


@_attrs_define
class PlannedGiftAssetEdit:
    """Model for editing an existing planned gift asset. All fields are optional for PATCH semantics.
    Null fields indicate the value should not be changed.

        Attributes:
            asset_type (CodeTableEntry | Unset): A predefined entry in a code table.
            description (None | str | Unset): Description of the asset. When provided (even as null), the description is
                updated.
                When omitted from the request, the description is left unchanged.
            amount (Currency | Unset): An amount denominated in a specific currency.
            cost_basis (Currency | Unset): An amount denominated in a specific currency.
    """

    asset_type: CodeTableEntry | Unset = UNSET
    description: None | str | Unset = UNSET
    amount: Currency | Unset = UNSET
    cost_basis: Currency | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        asset_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
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

        field_dict.update({})
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
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
        _asset_type = d.pop("asset_type", UNSET)
        asset_type: CodeTableEntry | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = CodeTableEntry.from_dict(_asset_type)

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

        planned_gift_asset_edit = cls(
            asset_type=asset_type,
            description=description,
            amount=amount,
            cost_basis=cost_basis,
        )

        return planned_gift_asset_edit

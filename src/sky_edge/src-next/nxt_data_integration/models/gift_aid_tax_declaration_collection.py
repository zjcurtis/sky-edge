from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_aid_tax_declaration import GiftAidTaxDeclaration


T = TypeVar("T", bound="GiftAidTaxDeclarationCollection")


@_attrs_define
class GiftAidTaxDeclarationCollection:
    """
    Attributes:
        count (int | Unset):
        value (list[GiftAidTaxDeclaration] | None | Unset):
    """

    count: int | Unset = UNSET
    value: list[GiftAidTaxDeclaration] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        value: list[dict[str, Any]] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = []
            for value_type_0_item_data in self.value:
                value_type_0_item = value_type_0_item_data.to_dict()
                value.append(value_type_0_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_aid_tax_declaration import GiftAidTaxDeclaration

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_value(data: object) -> list[GiftAidTaxDeclaration] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = []
                _value_type_0 = data
                for value_type_0_item_data in _value_type_0:
                    value_type_0_item = GiftAidTaxDeclaration.from_dict(value_type_0_item_data)

                    value_type_0.append(value_type_0_item)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftAidTaxDeclaration] | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        gift_aid_tax_declaration_collection = cls(
            count=count,
            value=value,
        )

        return gift_aid_tax_declaration_collection

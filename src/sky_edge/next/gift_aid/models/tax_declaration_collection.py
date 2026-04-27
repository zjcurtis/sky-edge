from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tax_declaration import TaxDeclaration


T = TypeVar("T", bound="TaxDeclarationCollection")


@_attrs_define
class TaxDeclarationCollection:
    """Tax declaration collection

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        tax_declarations (list[TaxDeclaration] | None | Unset): The list of tax declaration.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    tax_declarations: list[TaxDeclaration] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        tax_declarations: list[dict[str, Any]] | None | Unset
        if isinstance(self.tax_declarations, Unset):
            tax_declarations = UNSET
        elif isinstance(self.tax_declarations, list):
            tax_declarations = []
            for tax_declarations_type_0_item_data in self.tax_declarations:
                tax_declarations_type_0_item = (
                    tax_declarations_type_0_item_data.to_dict()
                )
                tax_declarations.append(tax_declarations_type_0_item)

        else:
            tax_declarations = self.tax_declarations

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if tax_declarations is not UNSET:
            field_dict["tax_declarations"] = tax_declarations
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tax_declaration import TaxDeclaration

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_tax_declarations(
            data: object,
        ) -> list[TaxDeclaration] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tax_declarations_type_0 = []
                _tax_declarations_type_0 = data
                for tax_declarations_type_0_item_data in _tax_declarations_type_0:
                    tax_declarations_type_0_item = TaxDeclaration.from_dict(
                        tax_declarations_type_0_item_data
                    )

                    tax_declarations_type_0.append(tax_declarations_type_0_item)

                return tax_declarations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TaxDeclaration] | None | Unset, data)

        tax_declarations = _parse_tax_declarations(d.pop("tax_declarations", UNSET))

        count = d.pop("count", UNSET)

        tax_declaration_collection = cls(
            offset=offset,
            limit=limit,
            tax_declarations=tax_declarations,
            count=count,
        )

        return tax_declaration_collection

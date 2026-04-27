from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tribute_acknowledgee_add import TributeAcknowledgeeAdd


T = TypeVar("T", bound="TributeAdd")


@_attrs_define
class TributeAdd:
    """An object representing an existing tribute record to add with a gift.

    Attributes:
        id (str): The system record ID of the tribute.
        tribute_acknowledgees (list[TributeAcknowledgeeAdd] | Unset): The acknowledgees for this tribute record to add
            with a gift tribute.
    """

    id: str
    tribute_acknowledgees: list[TributeAcknowledgeeAdd] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tribute_acknowledgees: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tribute_acknowledgees, Unset):
            tribute_acknowledgees = []
            for tribute_acknowledgees_item_data in self.tribute_acknowledgees:
                tribute_acknowledgees_item = tribute_acknowledgees_item_data.to_dict()
                tribute_acknowledgees.append(tribute_acknowledgees_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if tribute_acknowledgees is not UNSET:
            field_dict["tribute_acknowledgees"] = tribute_acknowledgees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tribute_acknowledgee_add import TributeAcknowledgeeAdd

        d = dict(src_dict)
        id = d.pop("id")

        _tribute_acknowledgees = d.pop("tribute_acknowledgees", UNSET)
        tribute_acknowledgees: list[TributeAcknowledgeeAdd] | Unset = UNSET
        if _tribute_acknowledgees is not UNSET:
            tribute_acknowledgees = []
            for tribute_acknowledgees_item_data in _tribute_acknowledgees:
                tribute_acknowledgees_item = TributeAcknowledgeeAdd.from_dict(
                    tribute_acknowledgees_item_data
                )

                tribute_acknowledgees.append(tribute_acknowledgees_item)

        tribute_add = cls(
            id=id,
            tribute_acknowledgees=tribute_acknowledgees,
        )

        tribute_add.additional_properties = d
        return tribute_add

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

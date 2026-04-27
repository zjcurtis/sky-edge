from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tribute_acknowledgee_lookup import TributeAcknowledgeeLookup


T = TypeVar("T", bound="TributeLookup")


@_attrs_define
class TributeLookup:
    """A tribute to add.

    Attributes:
        id (None | str | Unset): The system record ID of the tribute.
        tribute_acknowledgees (list[TributeAcknowledgeeLookup] | None | Unset): The acknowledgees for this tribute
            record to add with a gift tribute.
    """

    id: None | str | Unset = UNSET
    tribute_acknowledgees: list[TributeAcknowledgeeLookup] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        tribute_acknowledgees: list[dict[str, Any]] | None | Unset
        if isinstance(self.tribute_acknowledgees, Unset):
            tribute_acknowledgees = UNSET
        elif isinstance(self.tribute_acknowledgees, list):
            tribute_acknowledgees = []
            for tribute_acknowledgees_type_0_item_data in self.tribute_acknowledgees:
                tribute_acknowledgees_type_0_item = tribute_acknowledgees_type_0_item_data.to_dict()
                tribute_acknowledgees.append(tribute_acknowledgees_type_0_item)

        else:
            tribute_acknowledgees = self.tribute_acknowledgees

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tribute_acknowledgees is not UNSET:
            field_dict["tribute_acknowledgees"] = tribute_acknowledgees

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tribute_acknowledgee_lookup import TributeAcknowledgeeLookup

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_tribute_acknowledgees(data: object) -> list[TributeAcknowledgeeLookup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tribute_acknowledgees_type_0 = []
                _tribute_acknowledgees_type_0 = data
                for tribute_acknowledgees_type_0_item_data in _tribute_acknowledgees_type_0:
                    tribute_acknowledgees_type_0_item = TributeAcknowledgeeLookup.from_dict(
                        tribute_acknowledgees_type_0_item_data
                    )

                    tribute_acknowledgees_type_0.append(tribute_acknowledgees_type_0_item)

                return tribute_acknowledgees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TributeAcknowledgeeLookup] | None | Unset, data)

        tribute_acknowledgees = _parse_tribute_acknowledgees(d.pop("tribute_acknowledgees", UNSET))

        tribute_lookup = cls(
            id=id,
            tribute_acknowledgees=tribute_acknowledgees,
        )

        return tribute_lookup

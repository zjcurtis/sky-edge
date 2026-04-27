from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.gift_tribute_acknowledge_status import GiftTributeAcknowledgeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftTribute")


@_attrs_define
class GiftTribute:
    """A gift tribute record in Raiser's Edge.

    Attributes:
        id (int | Unset): The system record ID of the gift tribute.
        gift_id (int | Unset): The system record ID of the gift.
        tribute_id (int | Unset): The system record ID of the tribute.
        tribute_type (int | None | Unset): The tribute type.
        import_id (None | str | Unset): The import ID of thte gift tribute.
        acknowledge (GiftTributeAcknowledgeStatus | Unset): The gift tribute acknowledge status.
        sequence (int | Unset): The numeric sequence associated with the gift tribute.
    """

    id: int | Unset = UNSET
    gift_id: int | Unset = UNSET
    tribute_id: int | Unset = UNSET
    tribute_type: int | None | Unset = UNSET
    import_id: None | str | Unset = UNSET
    acknowledge: GiftTributeAcknowledgeStatus | Unset = UNSET
    sequence: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        gift_id = self.gift_id

        tribute_id = self.tribute_id

        tribute_type: int | None | Unset
        if isinstance(self.tribute_type, Unset):
            tribute_type = UNSET
        else:
            tribute_type = self.tribute_type

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        acknowledge: str | Unset = UNSET
        if not isinstance(self.acknowledge, Unset):
            acknowledge = self.acknowledge.value

        sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gift_id is not UNSET:
            field_dict["gift_id"] = gift_id
        if tribute_id is not UNSET:
            field_dict["tribute_id"] = tribute_id
        if tribute_type is not UNSET:
            field_dict["tribute_type"] = tribute_type
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if acknowledge is not UNSET:
            field_dict["acknowledge"] = acknowledge
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        gift_id = d.pop("gift_id", UNSET)

        tribute_id = d.pop("tribute_id", UNSET)

        def _parse_tribute_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tribute_type = _parse_tribute_type(d.pop("tribute_type", UNSET))

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        _acknowledge = d.pop("acknowledge", UNSET)
        acknowledge: GiftTributeAcknowledgeStatus | Unset
        if isinstance(_acknowledge, Unset):
            acknowledge = UNSET
        else:
            acknowledge = GiftTributeAcknowledgeStatus(_acknowledge)

        sequence = d.pop("sequence", UNSET)

        gift_tribute = cls(
            id=id,
            gift_id=gift_id,
            tribute_id=tribute_id,
            tribute_type=tribute_type,
            import_id=import_id,
            acknowledge=acknowledge,
            sequence=sequence,
        )

        return gift_tribute

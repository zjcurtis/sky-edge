from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftTributeCreate")


@_attrs_define
class GiftTributeCreate:
    """Represents the properties of a new Gift Tribute record in Raiser's Edge.

    Attributes:
        gift_id (int): The system record ID of the gift.
        tribute_id (int): The system record ID of the tribute.
        import_id (None | str | Unset): The import ID of the gift tribute record.
    """

    gift_id: int
    tribute_id: int
    import_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_id = self.gift_id

        tribute_id = self.tribute_id

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "gift_id": gift_id,
                "tribute_id": tribute_id,
            }
        )
        if import_id is not UNSET:
            field_dict["import_id"] = import_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_id = d.pop("gift_id")

        tribute_id = d.pop("tribute_id")

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        gift_tribute_create = cls(
            gift_id=gift_id,
            tribute_id=tribute_id,
            import_id=import_id,
        )

        return gift_tribute_create

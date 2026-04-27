from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="TributeAcknowledgeeCreate")


@_attrs_define
class TributeAcknowledgeeCreate:
    """
    Attributes:
        tribute_id (int):
        relationship_id (int | None | Unset):
        letter_id (int | None | Unset):
        sequence (int | None | Unset):
        import_id (None | str | Unset):
    """

    tribute_id: int
    relationship_id: int | None | Unset = UNSET
    letter_id: int | None | Unset = UNSET
    sequence: int | None | Unset = UNSET
    import_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tribute_id = self.tribute_id

        relationship_id: int | None | Unset
        if isinstance(self.relationship_id, Unset):
            relationship_id = UNSET
        else:
            relationship_id = self.relationship_id

        letter_id: int | None | Unset
        if isinstance(self.letter_id, Unset):
            letter_id = UNSET
        else:
            letter_id = self.letter_id

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tribute_id": tribute_id,
            }
        )
        if relationship_id is not UNSET:
            field_dict["relationship_id"] = relationship_id
        if letter_id is not UNSET:
            field_dict["letter_id"] = letter_id
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if import_id is not UNSET:
            field_dict["import_id"] = import_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tribute_id = d.pop("tribute_id")

        def _parse_relationship_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        relationship_id = _parse_relationship_id(d.pop("relationship_id", UNSET))

        def _parse_letter_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        letter_id = _parse_letter_id(d.pop("letter_id", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        tribute_acknowledgee_create = cls(
            tribute_id=tribute_id,
            relationship_id=relationship_id,
            letter_id=letter_id,
            sequence=sequence,
            import_id=import_id,
        )

        return tribute_acknowledgee_create

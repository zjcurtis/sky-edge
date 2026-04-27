from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="TributeAcknowledgee")


@_attrs_define
class TributeAcknowledgee:
    """A record from the dbo.TRIBUTE_ACKNOWLEDGEE table in Raiser's Edge

    Attributes:
        id (int | Unset): The tribute acknowledgee ID.
        tribute_id (int | Unset): The ID of the tribute this acknowledgee is for.
        relationships_id (int | None | Unset): The relationship ID of the acknowledgee. If null, this represents a self-
            acknowledgee.
        letter (int | None | Unset): The code table entry id of the letter for this acknowledgee.
        sequence (int | None | Unset): Order this acknowledgee appears on the tribute.
        import_id (None | str | Unset): Import ID of this acknowledgee.
    """

    id: int | Unset = UNSET
    tribute_id: int | Unset = UNSET
    relationships_id: int | None | Unset = UNSET
    letter: int | None | Unset = UNSET
    sequence: int | None | Unset = UNSET
    import_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tribute_id = self.tribute_id

        relationships_id: int | None | Unset
        if isinstance(self.relationships_id, Unset):
            relationships_id = UNSET
        else:
            relationships_id = self.relationships_id

        letter: int | None | Unset
        if isinstance(self.letter, Unset):
            letter = UNSET
        else:
            letter = self.letter

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

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tribute_id is not UNSET:
            field_dict["tribute_id"] = tribute_id
        if relationships_id is not UNSET:
            field_dict["relationships_id"] = relationships_id
        if letter is not UNSET:
            field_dict["letter"] = letter
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if import_id is not UNSET:
            field_dict["import_id"] = import_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tribute_id = d.pop("tribute_id", UNSET)

        def _parse_relationships_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        relationships_id = _parse_relationships_id(d.pop("relationships_id", UNSET))

        def _parse_letter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        letter = _parse_letter(d.pop("letter", UNSET))

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

        tribute_acknowledgee = cls(
            id=id,
            tribute_id=tribute_id,
            relationships_id=relationships_id,
            letter=letter,
            sequence=sequence,
            import_id=import_id,
        )

        return tribute_acknowledgee

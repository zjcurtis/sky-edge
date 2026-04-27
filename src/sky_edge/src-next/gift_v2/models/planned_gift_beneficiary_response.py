from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="PlannedGiftBeneficiaryResponse")


@_attrs_define
class PlannedGiftBeneficiaryResponse:
    """Represents a single planned gift beneficiary in the API response.

    Attributes:
        id (None | str): The unique identifier of the beneficiary record.
        gift_id (None | str): The gift identifier.
        relationship_type (None | str): The relationship type.
        beneficiary_type (None | str): The beneficiary type.
        constituent_relationship_id (None | str | Unset): The constituent relationship identifier.
        constituent_bank_id (None | str | Unset): The constituent bank identifier.
        constituent_education_id (None | str | Unset): The constituent education identifier.
        constituent_id (None | str | Unset): The resolved constituent identifier.
        name (None | str | Unset): The display name of the constituent.
        first_name (None | str | Unset): The first name of the constituent.
        last_name (None | str | Unset): The last name of the constituent.
        relation_code (CodeTableEntry | Unset): A predefined entry in a code table.
        position (None | str | Unset): The position from the constituent relationship.
        reciprocal_relation_code (CodeTableEntry | Unset): A predefined entry in a code table.
        notes (None | str | Unset): Notes from the constituent relationship.
        date_from (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        date_to (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        sequence (int | None | Unset): The sequence order.
    """

    id: None | str
    gift_id: None | str
    relationship_type: None | str
    beneficiary_type: None | str
    constituent_relationship_id: None | str | Unset = UNSET
    constituent_bank_id: None | str | Unset = UNSET
    constituent_education_id: None | str | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    relation_code: CodeTableEntry | Unset = UNSET
    position: None | str | Unset = UNSET
    reciprocal_relation_code: CodeTableEntry | Unset = UNSET
    notes: None | str | Unset = UNSET
    date_from: FuzzyDate | Unset = UNSET
    date_to: FuzzyDate | Unset = UNSET
    sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        gift_id: None | str
        gift_id = self.gift_id

        relationship_type: None | str
        relationship_type = self.relationship_type

        beneficiary_type: None | str
        beneficiary_type = self.beneficiary_type

        constituent_relationship_id: None | str | Unset
        if isinstance(self.constituent_relationship_id, Unset):
            constituent_relationship_id = UNSET
        else:
            constituent_relationship_id = self.constituent_relationship_id

        constituent_bank_id: None | str | Unset
        if isinstance(self.constituent_bank_id, Unset):
            constituent_bank_id = UNSET
        else:
            constituent_bank_id = self.constituent_bank_id

        constituent_education_id: None | str | Unset
        if isinstance(self.constituent_education_id, Unset):
            constituent_education_id = UNSET
        else:
            constituent_education_id = self.constituent_education_id

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        relation_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation_code, Unset):
            relation_code = self.relation_code.to_dict()

        position: None | str | Unset
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        reciprocal_relation_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reciprocal_relation_code, Unset):
            reciprocal_relation_code = self.reciprocal_relation_code.to_dict()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        date_from: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_from, Unset):
            date_from = self.date_from.to_dict()

        date_to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_to, Unset):
            date_to = self.date_to.to_dict()

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "gift_id": gift_id,
                "relationship_type": relationship_type,
                "beneficiary_type": beneficiary_type,
            }
        )
        if constituent_relationship_id is not UNSET:
            field_dict["constituent_relationship_id"] = constituent_relationship_id
        if constituent_bank_id is not UNSET:
            field_dict["constituent_bank_id"] = constituent_bank_id
        if constituent_education_id is not UNSET:
            field_dict["constituent_education_id"] = constituent_education_id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if relation_code is not UNSET:
            field_dict["relation_code"] = relation_code
        if position is not UNSET:
            field_dict["position"] = position
        if reciprocal_relation_code is not UNSET:
            field_dict["reciprocal_relation_code"] = reciprocal_relation_code
        if notes is not UNSET:
            field_dict["notes"] = notes
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_gift_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gift_id = _parse_gift_id(d.pop("gift_id"))

        def _parse_relationship_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relationship_type = _parse_relationship_type(d.pop("relationship_type"))

        def _parse_beneficiary_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        beneficiary_type = _parse_beneficiary_type(d.pop("beneficiary_type"))

        def _parse_constituent_relationship_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_relationship_id = _parse_constituent_relationship_id(d.pop("constituent_relationship_id", UNSET))

        def _parse_constituent_bank_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_bank_id = _parse_constituent_bank_id(d.pop("constituent_bank_id", UNSET))

        def _parse_constituent_education_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_education_id = _parse_constituent_education_id(d.pop("constituent_education_id", UNSET))

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        _relation_code = d.pop("relation_code", UNSET)
        relation_code: CodeTableEntry | Unset
        if isinstance(_relation_code, Unset):
            relation_code = UNSET
        else:
            relation_code = CodeTableEntry.from_dict(_relation_code)

        def _parse_position(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        position = _parse_position(d.pop("position", UNSET))

        _reciprocal_relation_code = d.pop("reciprocal_relation_code", UNSET)
        reciprocal_relation_code: CodeTableEntry | Unset
        if isinstance(_reciprocal_relation_code, Unset):
            reciprocal_relation_code = UNSET
        else:
            reciprocal_relation_code = CodeTableEntry.from_dict(_reciprocal_relation_code)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _date_from = d.pop("date_from", UNSET)
        date_from: FuzzyDate | Unset
        if isinstance(_date_from, Unset):
            date_from = UNSET
        else:
            date_from = FuzzyDate.from_dict(_date_from)

        _date_to = d.pop("date_to", UNSET)
        date_to: FuzzyDate | Unset
        if isinstance(_date_to, Unset):
            date_to = UNSET
        else:
            date_to = FuzzyDate.from_dict(_date_to)

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        planned_gift_beneficiary_response = cls(
            id=id,
            gift_id=gift_id,
            relationship_type=relationship_type,
            beneficiary_type=beneficiary_type,
            constituent_relationship_id=constituent_relationship_id,
            constituent_bank_id=constituent_bank_id,
            constituent_education_id=constituent_education_id,
            constituent_id=constituent_id,
            name=name,
            first_name=first_name,
            last_name=last_name,
            relation_code=relation_code,
            position=position,
            reciprocal_relation_code=reciprocal_relation_code,
            notes=notes,
            date_from=date_from,
            date_to=date_to,
            sequence=sequence,
        )

        return planned_gift_beneficiary_response

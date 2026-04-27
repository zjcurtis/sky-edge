from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="TributeCreate")


@_attrs_define
class TributeCreate:
    """A Tribute record from the dbo.Tribute table in Raiser's Edge.

    Attributes:
        tribute_type_id (int): The tribute type code ID.
        constituent_record_id (int): The system record ID of the constituent.
        description (None | str | Unset): The tribute description.
        start_date (FuzzyDate | Unset):
        end_date (FuzzyDate | Unset):
        notes (None | str | Unset): The tribute notes.
        is_active (bool | Unset): The active status of the tribute.
        import_id (None | str | Unset): The import id of the tribute.
        default_fund_id (int | None | Unset): The default fund ID.
    """

    tribute_type_id: int
    constituent_record_id: int
    description: None | str | Unset = UNSET
    start_date: FuzzyDate | Unset = UNSET
    end_date: FuzzyDate | Unset = UNSET
    notes: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    import_id: None | str | Unset = UNSET
    default_fund_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tribute_type_id = self.tribute_type_id

        constituent_record_id = self.constituent_record_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        start_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.to_dict()

        end_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.to_dict()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        is_active = self.is_active

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        default_fund_id: int | None | Unset
        if isinstance(self.default_fund_id, Unset):
            default_fund_id = UNSET
        else:
            default_fund_id = self.default_fund_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "tribute_type_id": tribute_type_id,
                "constituent_record_id": constituent_record_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if default_fund_id is not UNSET:
            field_dict["default_fund_id"] = default_fund_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        tribute_type_id = d.pop("tribute_type_id")

        constituent_record_id = d.pop("constituent_record_id")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _start_date = d.pop("start_date", UNSET)
        start_date: FuzzyDate | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = FuzzyDate.from_dict(_start_date)

        _end_date = d.pop("end_date", UNSET)
        end_date: FuzzyDate | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = FuzzyDate.from_dict(_end_date)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        is_active = d.pop("is_active", UNSET)

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        def _parse_default_fund_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_fund_id = _parse_default_fund_id(d.pop("default_fund_id", UNSET))

        tribute_create = cls(
            tribute_type_id=tribute_type_id,
            constituent_record_id=constituent_record_id,
            description=description,
            start_date=start_date,
            end_date=end_date,
            notes=notes,
            is_active=is_active,
            import_id=import_id,
            default_fund_id=default_fund_id,
        )

        return tribute_create

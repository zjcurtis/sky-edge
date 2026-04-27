from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="Tribute")


@_attrs_define
class Tribute:
    """A Code Table record from the dbo.Tribute table in Raiser's Edge.

    Attributes:
        id (int | Unset): The tribute ID.
        tribute_type_id (int | Unset): The tribute type code ID.
        tribute_type_name (None | str | Unset): The tribute type name
        description (None | str | Unset): The tribute description.
        start_date (FuzzyDate | Unset):
        end_date (FuzzyDate | Unset):
        notes (None | str | Unset): The tribute notes.
        is_active (bool | Unset): The active status of the tribute.
        sequence (int | None | Unset): The sequence of the tribute.
        constituent_record_id (int | Unset): The system record ID of the constituent.
        last_changed_by_id (int | None | Unset): The ID of the user who last changed the tribute.
        date_added (datetime.datetime | None | Unset): The date that the tribute was added.
        date_changed (datetime.datetime | None | Unset): The date that the tribute was changed.
        import_id (None | str | Unset): The import id of the tribute.
        added_by_id (int | None | Unset): The ID of the user who added the tribute.
        default_fund_id (int | None | Unset): The default fund ID.
    """

    id: int | Unset = UNSET
    tribute_type_id: int | Unset = UNSET
    tribute_type_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    start_date: FuzzyDate | Unset = UNSET
    end_date: FuzzyDate | Unset = UNSET
    notes: None | str | Unset = UNSET
    is_active: bool | Unset = UNSET
    sequence: int | None | Unset = UNSET
    constituent_record_id: int | Unset = UNSET
    last_changed_by_id: int | None | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    date_changed: datetime.datetime | None | Unset = UNSET
    import_id: None | str | Unset = UNSET
    added_by_id: int | None | Unset = UNSET
    default_fund_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tribute_type_id = self.tribute_type_id

        tribute_type_name: None | str | Unset
        if isinstance(self.tribute_type_name, Unset):
            tribute_type_name = UNSET
        else:
            tribute_type_name = self.tribute_type_name

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

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        constituent_record_id = self.constituent_record_id

        last_changed_by_id: int | None | Unset
        if isinstance(self.last_changed_by_id, Unset):
            last_changed_by_id = UNSET
        else:
            last_changed_by_id = self.last_changed_by_id

        date_added: None | str | Unset
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        date_changed: None | str | Unset
        if isinstance(self.date_changed, Unset):
            date_changed = UNSET
        elif isinstance(self.date_changed, datetime.datetime):
            date_changed = self.date_changed.isoformat()
        else:
            date_changed = self.date_changed

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        added_by_id: int | None | Unset
        if isinstance(self.added_by_id, Unset):
            added_by_id = UNSET
        else:
            added_by_id = self.added_by_id

        default_fund_id: int | None | Unset
        if isinstance(self.default_fund_id, Unset):
            default_fund_id = UNSET
        else:
            default_fund_id = self.default_fund_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tribute_type_id is not UNSET:
            field_dict["tribute_type_id"] = tribute_type_id
        if tribute_type_name is not UNSET:
            field_dict["tribute_type_name"] = tribute_type_name
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
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if constituent_record_id is not UNSET:
            field_dict["constituent_record_id"] = constituent_record_id
        if last_changed_by_id is not UNSET:
            field_dict["last_changed_by_id"] = last_changed_by_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_changed is not UNSET:
            field_dict["date_changed"] = date_changed
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if added_by_id is not UNSET:
            field_dict["added_by_id"] = added_by_id
        if default_fund_id is not UNSET:
            field_dict["default_fund_id"] = default_fund_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tribute_type_id = d.pop("tribute_type_id", UNSET)

        def _parse_tribute_type_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_type_name = _parse_tribute_type_name(d.pop("tribute_type_name", UNSET))

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

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        constituent_record_id = d.pop("constituent_record_id", UNSET)

        def _parse_last_changed_by_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_changed_by_id = _parse_last_changed_by_id(
            d.pop("last_changed_by_id", UNSET)
        )

        def _parse_date_added(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        def _parse_date_changed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_changed_type_0 = isoparse(data)

                return date_changed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_changed = _parse_date_changed(d.pop("date_changed", UNSET))

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        def _parse_added_by_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        added_by_id = _parse_added_by_id(d.pop("added_by_id", UNSET))

        def _parse_default_fund_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        default_fund_id = _parse_default_fund_id(d.pop("default_fund_id", UNSET))

        tribute = cls(
            id=id,
            tribute_type_id=tribute_type_id,
            tribute_type_name=tribute_type_name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            notes=notes,
            is_active=is_active,
            sequence=sequence,
            constituent_record_id=constituent_record_id,
            last_changed_by_id=last_changed_by_id,
            date_added=date_added,
            date_changed=date_changed,
            import_id=import_id,
            added_by_id=added_by_id,
            default_fund_id=default_fund_id,
        )

        return tribute

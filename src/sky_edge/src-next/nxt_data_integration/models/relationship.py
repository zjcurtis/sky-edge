from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Relationship")


@_attrs_define
class Relationship:
    """
    Attributes:
        relation_id (int | Unset):
        relation_description (None | str | Unset):
        relationship_type (None | str | Unset):
        reciprocal_relationship_type (None | str | Unset):
        date_from (datetime.datetime | None | Unset):
        date_to (datetime.datetime | None | Unset):
        notes (None | str | Unset):
    """

    relation_id: int | Unset = UNSET
    relation_description: None | str | Unset = UNSET
    relationship_type: None | str | Unset = UNSET
    reciprocal_relationship_type: None | str | Unset = UNSET
    date_from: datetime.datetime | None | Unset = UNSET
    date_to: datetime.datetime | None | Unset = UNSET
    notes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        relation_id = self.relation_id

        relation_description: None | str | Unset
        if isinstance(self.relation_description, Unset):
            relation_description = UNSET
        else:
            relation_description = self.relation_description

        relationship_type: None | str | Unset
        if isinstance(self.relationship_type, Unset):
            relationship_type = UNSET
        else:
            relationship_type = self.relationship_type

        reciprocal_relationship_type: None | str | Unset
        if isinstance(self.reciprocal_relationship_type, Unset):
            reciprocal_relationship_type = UNSET
        else:
            reciprocal_relationship_type = self.reciprocal_relationship_type

        date_from: None | str | Unset
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        elif isinstance(self.date_from, datetime.datetime):
            date_from = self.date_from.isoformat()
        else:
            date_from = self.date_from

        date_to: None | str | Unset
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        elif isinstance(self.date_to, datetime.datetime):
            date_to = self.date_to.isoformat()
        else:
            date_to = self.date_to

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if relation_id is not UNSET:
            field_dict["relation_id"] = relation_id
        if relation_description is not UNSET:
            field_dict["relation_description"] = relation_description
        if relationship_type is not UNSET:
            field_dict["relationship_type"] = relationship_type
        if reciprocal_relationship_type is not UNSET:
            field_dict["reciprocal_relationship_type"] = reciprocal_relationship_type
        if date_from is not UNSET:
            field_dict["date_from"] = date_from
        if date_to is not UNSET:
            field_dict["date_to"] = date_to
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        relation_id = d.pop("relation_id", UNSET)

        def _parse_relation_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relation_description = _parse_relation_description(d.pop("relation_description", UNSET))

        def _parse_relationship_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship_type = _parse_relationship_type(d.pop("relationship_type", UNSET))

        def _parse_reciprocal_relationship_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reciprocal_relationship_type = _parse_reciprocal_relationship_type(d.pop("reciprocal_relationship_type", UNSET))

        def _parse_date_from(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_type_0 = isoparse(data)

                return date_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_from = _parse_date_from(d.pop("date_from", UNSET))

        def _parse_date_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_to_type_0 = isoparse(data)

                return date_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_to = _parse_date_to(d.pop("date_to", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        relationship = cls(
            relation_id=relation_id,
            relation_description=relation_description,
            relationship_type=relationship_type,
            reciprocal_relationship_type=reciprocal_relationship_type,
            date_from=date_from,
            date_to=date_to,
            notes=notes,
        )

        return relationship

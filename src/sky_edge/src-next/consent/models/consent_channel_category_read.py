from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consent_solicit_code_assignment_read import ConsentSolicitCodeAssignmentRead


T = TypeVar("T", bound="ConsentChannelCategoryRead")


@_attrs_define
class ConsentChannelCategoryRead:
    """Represents the consent channel category.

    Attributes:
        id (None | str | Unset): The consent channel category identifier
        category_id (None | str | Unset): The category identifier
        category (None | str | Unset): The category name for the mapped category.
        inactive (bool | None | Unset): Flag indicating whether or not the consent channel category is currently
            inactive
        solicit_code_assignments (list[ConsentSolicitCodeAssignmentRead] | None | Unset): The list of solicit code
            assignment.
    """

    id: None | str | Unset = UNSET
    category_id: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    inactive: bool | None | Unset = UNSET
    solicit_code_assignments: list[ConsentSolicitCodeAssignmentRead] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        inactive: bool | None | Unset
        if isinstance(self.inactive, Unset):
            inactive = UNSET
        else:
            inactive = self.inactive

        solicit_code_assignments: list[dict[str, Any]] | None | Unset
        if isinstance(self.solicit_code_assignments, Unset):
            solicit_code_assignments = UNSET
        elif isinstance(self.solicit_code_assignments, list):
            solicit_code_assignments = []
            for solicit_code_assignments_type_0_item_data in self.solicit_code_assignments:
                solicit_code_assignments_type_0_item = solicit_code_assignments_type_0_item_data.to_dict()
                solicit_code_assignments.append(solicit_code_assignments_type_0_item)

        else:
            solicit_code_assignments = self.solicit_code_assignments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category is not UNSET:
            field_dict["category"] = category
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if solicit_code_assignments is not UNSET:
            field_dict["solicit_code_assignments"] = solicit_code_assignments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_solicit_code_assignment_read import ConsentSolicitCodeAssignmentRead

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_inactive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inactive = _parse_inactive(d.pop("inactive", UNSET))

        def _parse_solicit_code_assignments(data: object) -> list[ConsentSolicitCodeAssignmentRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                solicit_code_assignments_type_0 = []
                _solicit_code_assignments_type_0 = data
                for solicit_code_assignments_type_0_item_data in _solicit_code_assignments_type_0:
                    solicit_code_assignments_type_0_item = ConsentSolicitCodeAssignmentRead.from_dict(
                        solicit_code_assignments_type_0_item_data
                    )

                    solicit_code_assignments_type_0.append(solicit_code_assignments_type_0_item)

                return solicit_code_assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConsentSolicitCodeAssignmentRead] | None | Unset, data)

        solicit_code_assignments = _parse_solicit_code_assignments(d.pop("solicit_code_assignments", UNSET))

        consent_channel_category_read = cls(
            id=id,
            category_id=category_id,
            category=category,
            inactive=inactive,
            solicit_code_assignments=solicit_code_assignments,
        )

        return consent_channel_category_read

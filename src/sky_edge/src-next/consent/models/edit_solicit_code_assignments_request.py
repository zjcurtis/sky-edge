from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consent_solicit_code_assignment_write import ConsentSolicitCodeAssignmentWrite


T = TypeVar("T", bound="EditSolicitCodeAssignmentsRequest")


@_attrs_define
class EditSolicitCodeAssignmentsRequest:
    """Represents a request to edit solicit code assignments for a specific category.

    Attributes:
        category (None | str | Unset): The optional category identifier or description.
        solicit_code_assignments (list[ConsentSolicitCodeAssignmentWrite] | None | Unset): The collection of solicit
            code assignments to be updated for the specified category.
    """

    category: None | str | Unset = UNSET
    solicit_code_assignments: list[ConsentSolicitCodeAssignmentWrite] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

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
        if category is not UNSET:
            field_dict["category"] = category
        if solicit_code_assignments is not UNSET:
            field_dict["solicit_code_assignments"] = solicit_code_assignments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_solicit_code_assignment_write import ConsentSolicitCodeAssignmentWrite

        d = dict(src_dict)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_solicit_code_assignments(data: object) -> list[ConsentSolicitCodeAssignmentWrite] | None | Unset:
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
                    solicit_code_assignments_type_0_item = ConsentSolicitCodeAssignmentWrite.from_dict(
                        solicit_code_assignments_type_0_item_data
                    )

                    solicit_code_assignments_type_0.append(solicit_code_assignments_type_0_item)

                return solicit_code_assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConsentSolicitCodeAssignmentWrite] | None | Unset, data)

        solicit_code_assignments = _parse_solicit_code_assignments(d.pop("solicit_code_assignments", UNSET))

        edit_solicit_code_assignments_request = cls(
            category=category,
            solicit_code_assignments=solicit_code_assignments,
        )

        return edit_solicit_code_assignments_request

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.consent_solicit_code_assignment_read_add_remove import (
    ConsentSolicitCodeAssignmentReadAddRemove,
)
from ..models.consent_solicit_code_assignment_read_response import (
    ConsentSolicitCodeAssignmentReadResponse,
)

T = TypeVar("T", bound="ConsentSolicitCodeAssignmentRead")


@_attrs_define
class ConsentSolicitCodeAssignmentRead:
    """Represents the consent solicit code assignment.

    Attributes:
        solicit_code (None | str | Unset): The solicit code name for the solicit code assignment.
        response (ConsentSolicitCodeAssignmentReadResponse | Unset): The response of solicit opt in or opt
            out.<p>Members:</p><ul><li><i>OptIn</i></li><li><i>OptOut</i></li></ul>
        add_remove (ConsentSolicitCodeAssignmentReadAddRemove | Unset): The add remove solicit
            response.<p>Members:</p><ul><li><i>Add</i></li><li><i>Remove</i></li></ul>
    """

    solicit_code: None | str | Unset = UNSET
    response: ConsentSolicitCodeAssignmentReadResponse | Unset = UNSET
    add_remove: ConsentSolicitCodeAssignmentReadAddRemove | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        solicit_code: None | str | Unset
        if isinstance(self.solicit_code, Unset):
            solicit_code = UNSET
        else:
            solicit_code = self.solicit_code

        response: str | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.value

        add_remove: str | Unset = UNSET
        if not isinstance(self.add_remove, Unset):
            add_remove = self.add_remove.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if solicit_code is not UNSET:
            field_dict["solicit_code"] = solicit_code
        if response is not UNSET:
            field_dict["response"] = response
        if add_remove is not UNSET:
            field_dict["add_remove"] = add_remove

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_solicit_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        solicit_code = _parse_solicit_code(d.pop("solicit_code", UNSET))

        _response = d.pop("response", UNSET)
        response: ConsentSolicitCodeAssignmentReadResponse | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = ConsentSolicitCodeAssignmentReadResponse(_response)

        _add_remove = d.pop("add_remove", UNSET)
        add_remove: ConsentSolicitCodeAssignmentReadAddRemove | Unset
        if isinstance(_add_remove, Unset):
            add_remove = UNSET
        else:
            add_remove = ConsentSolicitCodeAssignmentReadAddRemove(_add_remove)

        consent_solicit_code_assignment_read = cls(
            solicit_code=solicit_code,
            response=response,
            add_remove=add_remove,
        )

        return consent_solicit_code_assignment_read

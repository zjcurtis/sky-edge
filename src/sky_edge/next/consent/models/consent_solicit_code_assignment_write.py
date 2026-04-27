from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.consent_solicit_code_assignment_write_add_remove import (
    ConsentSolicitCodeAssignmentWriteAddRemove,
)
from ..models.consent_solicit_code_assignment_write_response import (
    ConsentSolicitCodeAssignmentWriteResponse,
)

T = TypeVar("T", bound="ConsentSolicitCodeAssignmentWrite")


@_attrs_define
class ConsentSolicitCodeAssignmentWrite:
    """Represents a request to write a consent solicit code assignment.

    Attributes:
        response (ConsentSolicitCodeAssignmentWriteResponse): The consent response that will trigger this solicit code
            assignment<p>Members:</p><ul><li><i>OptIn</i> - Opt-in</li><li><i>OptOut</i> - Opt-out</li><li><i>NoResponse</i>
            - No response</li></ul>
        add_remove (ConsentSolicitCodeAssignmentWriteAddRemove): Add/Remove the solicit code when the given consent
            response is received.<p>Members:</p><ul><li><i>Add</i> - Add.</li><li><i>Remove</i> - Remove.</li></ul>
        solicit_code (str): The solicit code name
        sequence (int | None | Unset): Optional sequence number for the solicit code assignment.
    """

    response: ConsentSolicitCodeAssignmentWriteResponse
    add_remove: ConsentSolicitCodeAssignmentWriteAddRemove
    solicit_code: str
    sequence: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        response = self.response.value

        add_remove = self.add_remove.value

        solicit_code = self.solicit_code

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "response": response,
                "add_remove": add_remove,
                "solicit_code": solicit_code,
            }
        )
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        response = ConsentSolicitCodeAssignmentWriteResponse(d.pop("response"))

        add_remove = ConsentSolicitCodeAssignmentWriteAddRemove(d.pop("add_remove"))

        solicit_code = d.pop("solicit_code")

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        consent_solicit_code_assignment_write = cls(
            response=response,
            add_remove=add_remove,
            solicit_code=solicit_code,
            sequence=sequence,
        )

        return consent_solicit_code_assignment_write

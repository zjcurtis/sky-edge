from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.consent_channel_category_write_channel import (
    ConsentChannelCategoryWriteChannel,
)

if TYPE_CHECKING:
    from ..models.consent_solicit_code_assignment_write import (
        ConsentSolicitCodeAssignmentWrite,
    )


T = TypeVar("T", bound="ConsentChannelCategoryWrite")


@_attrs_define
class ConsentChannelCategoryWrite:
    """Represents a request to configure a consent channel category.

    Attributes:
        channel (ConsentChannelCategoryWriteChannel): The channel<p>Members:</p><ul><li><i>Email</i> -
            Email</li><li><i>Mail</i> - Mail</li><li><i>SMS</i> - SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i>
            - AutoPhone</li><li><i>Social</i> - Social media</li><li><i>DataProcessing</i> - Data
            processing</li><li><i>Other</i> - Other</li></ul>
        category (str): The category name or system identifier
        solicit_code_assignments (list[ConsentSolicitCodeAssignmentWrite] | None | Unset): Collection of consent solicit
            code assignments to be configured for the channel category.
    """

    channel: ConsentChannelCategoryWriteChannel
    category: str
    solicit_code_assignments: list[ConsentSolicitCodeAssignmentWrite] | None | Unset = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        category = self.category

        solicit_code_assignments: list[dict[str, Any]] | None | Unset
        if isinstance(self.solicit_code_assignments, Unset):
            solicit_code_assignments = UNSET
        elif isinstance(self.solicit_code_assignments, list):
            solicit_code_assignments = []
            for (
                solicit_code_assignments_type_0_item_data
            ) in self.solicit_code_assignments:
                solicit_code_assignments_type_0_item = (
                    solicit_code_assignments_type_0_item_data.to_dict()
                )
                solicit_code_assignments.append(solicit_code_assignments_type_0_item)

        else:
            solicit_code_assignments = self.solicit_code_assignments

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channel": channel,
                "category": category,
            }
        )
        if solicit_code_assignments is not UNSET:
            field_dict["solicit_code_assignments"] = solicit_code_assignments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_solicit_code_assignment_write import (
            ConsentSolicitCodeAssignmentWrite,
        )

        d = dict(src_dict)
        channel = ConsentChannelCategoryWriteChannel(d.pop("channel"))

        category = d.pop("category")

        def _parse_solicit_code_assignments(
            data: object,
        ) -> list[ConsentSolicitCodeAssignmentWrite] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                solicit_code_assignments_type_0 = []
                _solicit_code_assignments_type_0 = data
                for (
                    solicit_code_assignments_type_0_item_data
                ) in _solicit_code_assignments_type_0:
                    solicit_code_assignments_type_0_item = (
                        ConsentSolicitCodeAssignmentWrite.from_dict(
                            solicit_code_assignments_type_0_item_data
                        )
                    )

                    solicit_code_assignments_type_0.append(
                        solicit_code_assignments_type_0_item
                    )

                return solicit_code_assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConsentSolicitCodeAssignmentWrite] | None | Unset, data)

        solicit_code_assignments = _parse_solicit_code_assignments(
            d.pop("solicit_code_assignments", UNSET)
        )

        consent_channel_category_write = cls(
            channel=channel,
            category=category,
            solicit_code_assignments=solicit_code_assignments,
        )

        return consent_channel_category_write

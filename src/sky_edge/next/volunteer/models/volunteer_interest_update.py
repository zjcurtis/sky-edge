from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="VolunteerInterestUpdate")


@_attrs_define
class VolunteerInterestUpdate:
    """Represents volunteer interest update information for a volunteer

    Attributes:
        interest (None | str | Unset): Gets or sets the interest description (code table entry name).
            For PATCH semantics: null means keep current value, empty string means clear the value.
    """

    interest: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        interest: None | str | Unset
        if isinstance(self.interest, Unset):
            interest = UNSET
        else:
            interest = self.interest

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if interest is not UNSET:
            field_dict["interest"] = interest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_interest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interest = _parse_interest(d.pop("interest", UNSET))

        volunteer_interest_update = cls(
            interest=interest,
        )

        return volunteer_interest_update

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry


T = TypeVar("T", bound="MembershipBenefitCreate")


@_attrs_define
class MembershipBenefitCreate:
    """Create memberships and Benefit

    Attributes:
        benefit (CodeTableEntry | Unset): A predefined entry in a code table.
        count (int | None | Unset): Benefit Count
        unit_cost (float | Unset): Unit cost
        total_benefit_value (float | None | Unset): Total benefit value
        sent (None | str | Unset): The date was sent or fulfilled
        comments (None | str | Unset): User text associated with the record.
    """

    benefit: CodeTableEntry | Unset = UNSET
    count: int | None | Unset = UNSET
    unit_cost: float | Unset = UNSET
    total_benefit_value: float | None | Unset = UNSET
    sent: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        benefit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.benefit, Unset):
            benefit = self.benefit.to_dict()

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        unit_cost = self.unit_cost

        total_benefit_value: float | None | Unset
        if isinstance(self.total_benefit_value, Unset):
            total_benefit_value = UNSET
        else:
            total_benefit_value = self.total_benefit_value

        sent: None | str | Unset
        if isinstance(self.sent, Unset):
            sent = UNSET
        else:
            sent = self.sent

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if benefit is not UNSET:
            field_dict["benefit"] = benefit
        if count is not UNSET:
            field_dict["count"] = count
        if unit_cost is not UNSET:
            field_dict["unit_cost"] = unit_cost
        if total_benefit_value is not UNSET:
            field_dict["total_benefit_value"] = total_benefit_value
        if sent is not UNSET:
            field_dict["sent"] = sent
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry

        d = dict(src_dict)
        _benefit = d.pop("benefit", UNSET)
        benefit: CodeTableEntry | Unset
        if isinstance(_benefit, Unset):
            benefit = UNSET
        else:
            benefit = CodeTableEntry.from_dict(_benefit)

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        unit_cost = d.pop("unit_cost", UNSET)

        def _parse_total_benefit_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_benefit_value = _parse_total_benefit_value(
            d.pop("total_benefit_value", UNSET)
        )

        def _parse_sent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sent = _parse_sent(d.pop("sent", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        membership_benefit_create = cls(
            benefit=benefit,
            count=count,
            unit_cost=unit_cost,
            total_benefit_value=total_benefit_value,
            sent=sent,
            comments=comments,
        )

        return membership_benefit_create

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipBenefit")


@_attrs_define
class MembershipBenefit:
    """Membership benefits

    Attributes:
        benefits_id (int | Unset): Benefits ID
        benefit (None | str | Unset): Benefits Description
        count (int | None | Unset): Nullable field  Count
        unit_cost (float | Unset): Unit cost
        total_benefit_value (float | Unset): Total benefit value
        currency_symbol (None | str | Unset): Non Nullable field currency symbol
        sent (None | str | Unset): Nullable field sent with length 8 varchar
        comments (None | str | Unset): Nullable field comments with length 255 varchar
    """

    benefits_id: int | Unset = UNSET
    benefit: None | str | Unset = UNSET
    count: int | None | Unset = UNSET
    unit_cost: float | Unset = UNSET
    total_benefit_value: float | Unset = UNSET
    currency_symbol: None | str | Unset = UNSET
    sent: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        benefits_id = self.benefits_id

        benefit: None | str | Unset
        if isinstance(self.benefit, Unset):
            benefit = UNSET
        else:
            benefit = self.benefit

        count: int | None | Unset
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        unit_cost = self.unit_cost

        total_benefit_value = self.total_benefit_value

        currency_symbol: None | str | Unset
        if isinstance(self.currency_symbol, Unset):
            currency_symbol = UNSET
        else:
            currency_symbol = self.currency_symbol

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
        if benefits_id is not UNSET:
            field_dict["benefits_id"] = benefits_id
        if benefit is not UNSET:
            field_dict["benefit"] = benefit
        if count is not UNSET:
            field_dict["count"] = count
        if unit_cost is not UNSET:
            field_dict["unit_cost"] = unit_cost
        if total_benefit_value is not UNSET:
            field_dict["total_benefit_value"] = total_benefit_value
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if sent is not UNSET:
            field_dict["sent"] = sent
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        benefits_id = d.pop("benefits_id", UNSET)

        def _parse_benefit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        benefit = _parse_benefit(d.pop("benefit", UNSET))

        def _parse_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        count = _parse_count(d.pop("count", UNSET))

        unit_cost = d.pop("unit_cost", UNSET)

        total_benefit_value = d.pop("total_benefit_value", UNSET)

        def _parse_currency_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency_symbol = _parse_currency_symbol(d.pop("currency_symbol", UNSET))

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

        membership_benefit = cls(
            benefits_id=benefits_id,
            benefit=benefit,
            count=count,
            unit_cost=unit_cost,
            total_benefit_value=total_benefit_value,
            currency_symbol=currency_symbol,
            sent=sent,
            comments=comments,
        )

        return membership_benefit

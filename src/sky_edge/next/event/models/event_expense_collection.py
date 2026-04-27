from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_expense import EventExpense


T = TypeVar("T", bound="EventExpenseCollection")


@_attrs_define
class EventExpenseCollection:
    """Defines a collection of expenses for an event.

    Attributes:
        total_budgeted (float | Unset): The sum of the budgeted amounts.
        total_expense (float | Unset): The sum of the expense amounts.
        over_under (float | Unset): The difference between the total expense and the total budgeted.
        count (int | Unset): The total number of items in the collection before limit/offset.
        value (list[EventExpense] | None | Unset): The set of items included in the response. This may be a subset of
            the items in the collection.
    """

    total_budgeted: float | Unset = UNSET
    total_expense: float | Unset = UNSET
    over_under: float | Unset = UNSET
    count: int | Unset = UNSET
    value: list[EventExpense] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total_budgeted = self.total_budgeted

        total_expense = self.total_expense

        over_under = self.over_under

        count = self.count

        value: list[dict[str, Any]] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = []
            for value_type_0_item_data in self.value:
                value_type_0_item = value_type_0_item_data.to_dict()
                value.append(value_type_0_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if total_budgeted is not UNSET:
            field_dict["total_budgeted"] = total_budgeted
        if total_expense is not UNSET:
            field_dict["total_expense"] = total_expense
        if over_under is not UNSET:
            field_dict["over_under"] = over_under
        if count is not UNSET:
            field_dict["count"] = count
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_expense import EventExpense

        d = dict(src_dict)
        total_budgeted = d.pop("total_budgeted", UNSET)

        total_expense = d.pop("total_expense", UNSET)

        over_under = d.pop("over_under", UNSET)

        count = d.pop("count", UNSET)

        def _parse_value(data: object) -> list[EventExpense] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = []
                _value_type_0 = data
                for value_type_0_item_data in _value_type_0:
                    value_type_0_item = EventExpense.from_dict(value_type_0_item_data)

                    value_type_0.append(value_type_0_item)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventExpense] | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        event_expense_collection = cls(
            total_budgeted=total_budgeted,
            total_expense=total_expense,
            over_under=over_under,
            count=count,
            value=value,
        )

        return event_expense_collection

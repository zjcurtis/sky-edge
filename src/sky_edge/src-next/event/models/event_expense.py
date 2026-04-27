from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expense_type import ExpenseType
    from ..models.fuzzy_date import FuzzyDate
    from ..models.vendor import Vendor


T = TypeVar("T", bound="EventExpense")


@_attrs_define
class EventExpense:
    """Defines a data model for an event expense.

    Attributes:
        id (None | str | Unset): The ID of the event expense.
        expense_type (ExpenseType | Unset): Expense type is the custom type for the event expense.
        budgeted (float | Unset): The budgeted amount of the event expense.
        expense (float | Unset): The amount of the event expense.
        paid (float | Unset): The amount paid of the event expense.
        date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
            (with no year indicated).
        comments (None | str | Unset): The comments of the event expense.
        vendor (Vendor | Unset): Vendor details of event expense.
    """

    id: None | str | Unset = UNSET
    expense_type: ExpenseType | Unset = UNSET
    budgeted: float | Unset = UNSET
    expense: float | Unset = UNSET
    paid: float | Unset = UNSET
    date: FuzzyDate | Unset = UNSET
    comments: None | str | Unset = UNSET
    vendor: Vendor | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        expense_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expense_type, Unset):
            expense_type = self.expense_type.to_dict()

        budgeted = self.budgeted

        expense = self.expense

        paid = self.paid

        date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        vendor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if expense_type is not UNSET:
            field_dict["expense_type"] = expense_type
        if budgeted is not UNSET:
            field_dict["budgeted"] = budgeted
        if expense is not UNSET:
            field_dict["expense"] = expense
        if paid is not UNSET:
            field_dict["paid"] = paid
        if date is not UNSET:
            field_dict["date"] = date
        if comments is not UNSET:
            field_dict["comments"] = comments
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expense_type import ExpenseType
        from ..models.fuzzy_date import FuzzyDate
        from ..models.vendor import Vendor

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _expense_type = d.pop("expense_type", UNSET)
        expense_type: ExpenseType | Unset
        if isinstance(_expense_type, Unset):
            expense_type = UNSET
        else:
            expense_type = ExpenseType.from_dict(_expense_type)

        budgeted = d.pop("budgeted", UNSET)

        expense = d.pop("expense", UNSET)

        paid = d.pop("paid", UNSET)

        _date = d.pop("date", UNSET)
        date: FuzzyDate | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FuzzyDate.from_dict(_date)

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        _vendor = d.pop("vendor", UNSET)
        vendor: Vendor | Unset
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = Vendor.from_dict(_vendor)

        event_expense = cls(
            id=id,
            expense_type=expense_type,
            budgeted=budgeted,
            expense=expense,
            paid=paid,
            date=date,
            comments=comments,
            vendor=vendor,
        )

        return event_expense

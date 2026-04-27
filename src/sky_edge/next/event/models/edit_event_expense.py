from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.expense_type_lookup import ExpenseTypeLookup
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="EditEventExpense")


@_attrs_define
class EditEventExpense:
    """An event expense is a debt incurred from hosting an event.

    Attributes:
        expense_type (ExpenseTypeLookup | Unset): Expense type look up model.
        expense_amount (float | Unset): The amount spent for the event.
        budgeted_amount (float | Unset): The budgeted amount for the event expense.
        amount_paid (float | Unset): The amount paid to the vendor.
        expense_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
            February 9 (with no year indicated).
        vendor_id (None | str | Unset): The participant ID of the vendor.
        comments (None | str | Unset): Quick reference information pinned to the expense's record.
    """

    expense_type: ExpenseTypeLookup | Unset = UNSET
    expense_amount: float | Unset = UNSET
    budgeted_amount: float | Unset = UNSET
    amount_paid: float | Unset = UNSET
    expense_date: FuzzyDate | Unset = UNSET
    vendor_id: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        expense_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expense_type, Unset):
            expense_type = self.expense_type.to_dict()

        expense_amount = self.expense_amount

        budgeted_amount = self.budgeted_amount

        amount_paid = self.amount_paid

        expense_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expense_date, Unset):
            expense_date = self.expense_date.to_dict()

        vendor_id: None | str | Unset
        if isinstance(self.vendor_id, Unset):
            vendor_id = UNSET
        else:
            vendor_id = self.vendor_id

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if expense_type is not UNSET:
            field_dict["expense_type"] = expense_type
        if expense_amount is not UNSET:
            field_dict["expense_amount"] = expense_amount
        if budgeted_amount is not UNSET:
            field_dict["budgeted_amount"] = budgeted_amount
        if amount_paid is not UNSET:
            field_dict["amount_paid"] = amount_paid
        if expense_date is not UNSET:
            field_dict["expense_date"] = expense_date
        if vendor_id is not UNSET:
            field_dict["vendor_id"] = vendor_id
        if comments is not UNSET:
            field_dict["comments"] = comments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.expense_type_lookup import ExpenseTypeLookup
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        _expense_type = d.pop("expense_type", UNSET)
        expense_type: ExpenseTypeLookup | Unset
        if isinstance(_expense_type, Unset):
            expense_type = UNSET
        else:
            expense_type = ExpenseTypeLookup.from_dict(_expense_type)

        expense_amount = d.pop("expense_amount", UNSET)

        budgeted_amount = d.pop("budgeted_amount", UNSET)

        amount_paid = d.pop("amount_paid", UNSET)

        _expense_date = d.pop("expense_date", UNSET)
        expense_date: FuzzyDate | Unset
        if isinstance(_expense_date, Unset):
            expense_date = UNSET
        else:
            expense_date = FuzzyDate.from_dict(_expense_date)

        def _parse_vendor_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vendor_id = _parse_vendor_id(d.pop("vendor_id", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        edit_event_expense = cls(
            expense_type=expense_type,
            expense_amount=expense_amount,
            budgeted_amount=budgeted_amount,
            amount_paid=amount_paid,
            expense_date=expense_date,
            vendor_id=vendor_id,
            comments=comments,
        )

        return edit_event_expense

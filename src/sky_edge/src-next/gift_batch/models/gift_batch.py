from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftBatch")


@_attrs_define
class GiftBatch:
    """Represents the gift batch object

    Attributes:
        id (None | str | Unset): The batch identifier
        actual_amount (float | None | Unset): The actual batch amount
        batch_description (None | str | Unset): The batch description
        batch_number (None | str | Unset): The batch number
        added_by (None | str | Unset): The user who created the batch
        date_added (datetime.datetime | None | Unset): The date the batch was created. Includes an offset from UTC in <a
            href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
        has_exceptions (bool | None | Unset): Indicates whether the batch has exceptions
        approved (bool | None | Unset): Indicates whether the batch is approved
        number_of_gifts (int | None | Unset): The actual number of gifts in the batch
        projected_amount (float | None | Unset): The projected amount
        projected_number_of_gifts (int | None | Unset): The projected number of gifts
    """

    id: None | str | Unset = UNSET
    actual_amount: float | None | Unset = UNSET
    batch_description: None | str | Unset = UNSET
    batch_number: None | str | Unset = UNSET
    added_by: None | str | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    has_exceptions: bool | None | Unset = UNSET
    approved: bool | None | Unset = UNSET
    number_of_gifts: int | None | Unset = UNSET
    projected_amount: float | None | Unset = UNSET
    projected_number_of_gifts: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        actual_amount: float | None | Unset
        if isinstance(self.actual_amount, Unset):
            actual_amount = UNSET
        else:
            actual_amount = self.actual_amount

        batch_description: None | str | Unset
        if isinstance(self.batch_description, Unset):
            batch_description = UNSET
        else:
            batch_description = self.batch_description

        batch_number: None | str | Unset
        if isinstance(self.batch_number, Unset):
            batch_number = UNSET
        else:
            batch_number = self.batch_number

        added_by: None | str | Unset
        if isinstance(self.added_by, Unset):
            added_by = UNSET
        else:
            added_by = self.added_by

        date_added: None | str | Unset
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        has_exceptions: bool | None | Unset
        if isinstance(self.has_exceptions, Unset):
            has_exceptions = UNSET
        else:
            has_exceptions = self.has_exceptions

        approved: bool | None | Unset
        if isinstance(self.approved, Unset):
            approved = UNSET
        else:
            approved = self.approved

        number_of_gifts: int | None | Unset
        if isinstance(self.number_of_gifts, Unset):
            number_of_gifts = UNSET
        else:
            number_of_gifts = self.number_of_gifts

        projected_amount: float | None | Unset
        if isinstance(self.projected_amount, Unset):
            projected_amount = UNSET
        else:
            projected_amount = self.projected_amount

        projected_number_of_gifts: int | None | Unset
        if isinstance(self.projected_number_of_gifts, Unset):
            projected_number_of_gifts = UNSET
        else:
            projected_number_of_gifts = self.projected_number_of_gifts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if actual_amount is not UNSET:
            field_dict["actual_amount"] = actual_amount
        if batch_description is not UNSET:
            field_dict["batch_description"] = batch_description
        if batch_number is not UNSET:
            field_dict["batch_number"] = batch_number
        if added_by is not UNSET:
            field_dict["added_by"] = added_by
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if has_exceptions is not UNSET:
            field_dict["has_exceptions"] = has_exceptions
        if approved is not UNSET:
            field_dict["approved"] = approved
        if number_of_gifts is not UNSET:
            field_dict["number_of_gifts"] = number_of_gifts
        if projected_amount is not UNSET:
            field_dict["projected_amount"] = projected_amount
        if projected_number_of_gifts is not UNSET:
            field_dict["projected_number_of_gifts"] = projected_number_of_gifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_actual_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        actual_amount = _parse_actual_amount(d.pop("actual_amount", UNSET))

        def _parse_batch_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_description = _parse_batch_description(d.pop("batch_description", UNSET))

        def _parse_batch_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_number = _parse_batch_number(d.pop("batch_number", UNSET))

        def _parse_added_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by = _parse_added_by(d.pop("added_by", UNSET))

        def _parse_date_added(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        def _parse_has_exceptions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_exceptions = _parse_has_exceptions(d.pop("has_exceptions", UNSET))

        def _parse_approved(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        approved = _parse_approved(d.pop("approved", UNSET))

        def _parse_number_of_gifts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_gifts = _parse_number_of_gifts(d.pop("number_of_gifts", UNSET))

        def _parse_projected_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        projected_amount = _parse_projected_amount(d.pop("projected_amount", UNSET))

        def _parse_projected_number_of_gifts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        projected_number_of_gifts = _parse_projected_number_of_gifts(d.pop("projected_number_of_gifts", UNSET))

        gift_batch = cls(
            id=id,
            actual_amount=actual_amount,
            batch_description=batch_description,
            batch_number=batch_number,
            added_by=added_by,
            date_added=date_added,
            has_exceptions=has_exceptions,
            approved=approved,
            number_of_gifts=number_of_gifts,
            projected_amount=projected_amount,
            projected_number_of_gifts=projected_number_of_gifts,
        )

        return gift_batch

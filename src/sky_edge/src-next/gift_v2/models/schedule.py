from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.schedule_schedule_frequency import ScheduleScheduleFrequency
from ..types import UNSET, Unset

T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    """A gift schedule.

    Attributes:
        next_installment_date (datetime.datetime | None | Unset): The date of the next scheduled installment. Read only.
        frequency (ScheduleScheduleFrequency | Unset): The frequency of the gift schedule.
            Pledge gifts cannot have EVERY_SIX_MONTHS, EVERY_FOUR_WEEKS, or Weekly frequencies. Instead, use an Irregular
            frequency.
            Recurring gifts cannot have Single or Irregular frequencies. Consider a different gift type. Example: Monthly.
        start_date (datetime.datetime | None | Unset): The date that the gift schedule starts.
        end_date (datetime.datetime | None | Unset): The date that the gift schedule ends.
        number_of_installments (int | None | Unset): The number of installments on the pledge schedule.
    """

    next_installment_date: datetime.datetime | None | Unset = UNSET
    frequency: ScheduleScheduleFrequency | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    number_of_installments: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        next_installment_date: None | str | Unset
        if isinstance(self.next_installment_date, Unset):
            next_installment_date = UNSET
        elif isinstance(self.next_installment_date, datetime.datetime):
            next_installment_date = self.next_installment_date.isoformat()
        else:
            next_installment_date = self.next_installment_date

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        number_of_installments: int | None | Unset
        if isinstance(self.number_of_installments, Unset):
            number_of_installments = UNSET
        else:
            number_of_installments = self.number_of_installments

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if next_installment_date is not UNSET:
            field_dict["next_installment_date"] = next_installment_date
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if number_of_installments is not UNSET:
            field_dict["number_of_installments"] = number_of_installments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_next_installment_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_installment_date_type_0 = isoparse(data)

                return next_installment_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        next_installment_date = _parse_next_installment_date(d.pop("next_installment_date", UNSET))

        _frequency = d.pop("frequency", UNSET)
        frequency: ScheduleScheduleFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = ScheduleScheduleFrequency(_frequency)

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_number_of_installments(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        number_of_installments = _parse_number_of_installments(d.pop("number_of_installments", UNSET))

        schedule = cls(
            next_installment_date=next_installment_date,
            frequency=frequency,
            start_date=start_date,
            end_date=end_date,
            number_of_installments=number_of_installments,
        )

        return schedule

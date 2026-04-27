from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipDetails")


@_attrs_define
class MembershipDetails:
    """This contains stored membership details.

    Attributes:
        dues (float | None | Unset): The dues amount.
        category_name (None | str | Unset): The membership category name.
        program_name (None | str | Unset): The membership program name.
        sub_category_name (None | str | Unset): The membership subcategory name.
        last_renewed_date (datetime.date | None | Unset): The date the membership was last renewed.
        last_dropped_date (datetime.date | None | Unset): The date the membership was last dropped.
        next_renewal_date (datetime.date | None | Unset): The date the membership next renewal.
        joined_date (datetime.date | Unset): The date the membership began.
        total_years (int | None | Unset): The total number of years of membership
        times_renewed (int | None | Unset): The number of times the membership was renewed.
        consec_years (int | None | Unset): The number of consecutive membership years.
        constituent_id (None | str | Unset): The constituent ID associated with the membership.
        notes (None | str | Unset): Membership notes.
    """

    dues: float | None | Unset = UNSET
    category_name: None | str | Unset = UNSET
    program_name: None | str | Unset = UNSET
    sub_category_name: None | str | Unset = UNSET
    last_renewed_date: datetime.date | None | Unset = UNSET
    last_dropped_date: datetime.date | None | Unset = UNSET
    next_renewal_date: datetime.date | None | Unset = UNSET
    joined_date: datetime.date | Unset = UNSET
    total_years: int | None | Unset = UNSET
    times_renewed: int | None | Unset = UNSET
    consec_years: int | None | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dues: float | None | Unset
        if isinstance(self.dues, Unset):
            dues = UNSET
        else:
            dues = self.dues

        category_name: None | str | Unset
        if isinstance(self.category_name, Unset):
            category_name = UNSET
        else:
            category_name = self.category_name

        program_name: None | str | Unset
        if isinstance(self.program_name, Unset):
            program_name = UNSET
        else:
            program_name = self.program_name

        sub_category_name: None | str | Unset
        if isinstance(self.sub_category_name, Unset):
            sub_category_name = UNSET
        else:
            sub_category_name = self.sub_category_name

        last_renewed_date: None | str | Unset
        if isinstance(self.last_renewed_date, Unset):
            last_renewed_date = UNSET
        elif isinstance(self.last_renewed_date, datetime.date):
            last_renewed_date = self.last_renewed_date.isoformat()
        else:
            last_renewed_date = self.last_renewed_date

        last_dropped_date: None | str | Unset
        if isinstance(self.last_dropped_date, Unset):
            last_dropped_date = UNSET
        elif isinstance(self.last_dropped_date, datetime.date):
            last_dropped_date = self.last_dropped_date.isoformat()
        else:
            last_dropped_date = self.last_dropped_date

        next_renewal_date: None | str | Unset
        if isinstance(self.next_renewal_date, Unset):
            next_renewal_date = UNSET
        elif isinstance(self.next_renewal_date, datetime.date):
            next_renewal_date = self.next_renewal_date.isoformat()
        else:
            next_renewal_date = self.next_renewal_date

        joined_date: str | Unset = UNSET
        if not isinstance(self.joined_date, Unset):
            joined_date = self.joined_date.isoformat()

        total_years: int | None | Unset
        if isinstance(self.total_years, Unset):
            total_years = UNSET
        else:
            total_years = self.total_years

        times_renewed: int | None | Unset
        if isinstance(self.times_renewed, Unset):
            times_renewed = UNSET
        else:
            times_renewed = self.times_renewed

        consec_years: int | None | Unset
        if isinstance(self.consec_years, Unset):
            consec_years = UNSET
        else:
            consec_years = self.consec_years

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dues is not UNSET:
            field_dict["dues"] = dues
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if program_name is not UNSET:
            field_dict["program_name"] = program_name
        if sub_category_name is not UNSET:
            field_dict["sub_category_name"] = sub_category_name
        if last_renewed_date is not UNSET:
            field_dict["last_renewed_date"] = last_renewed_date
        if last_dropped_date is not UNSET:
            field_dict["last_dropped_date"] = last_dropped_date
        if next_renewal_date is not UNSET:
            field_dict["next_renewal_date"] = next_renewal_date
        if joined_date is not UNSET:
            field_dict["joined_date"] = joined_date
        if total_years is not UNSET:
            field_dict["total_years"] = total_years
        if times_renewed is not UNSET:
            field_dict["times_renewed"] = times_renewed
        if consec_years is not UNSET:
            field_dict["consec_years"] = consec_years
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_dues(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dues = _parse_dues(d.pop("dues", UNSET))

        def _parse_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_name = _parse_category_name(d.pop("category_name", UNSET))

        def _parse_program_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        program_name = _parse_program_name(d.pop("program_name", UNSET))

        def _parse_sub_category_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_category_name = _parse_sub_category_name(d.pop("sub_category_name", UNSET))

        def _parse_last_renewed_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_renewed_date_type_0 = isoparse(data).date()

                return last_renewed_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_renewed_date = _parse_last_renewed_date(d.pop("last_renewed_date", UNSET))

        def _parse_last_dropped_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_dropped_date_type_0 = isoparse(data).date()

                return last_dropped_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        last_dropped_date = _parse_last_dropped_date(d.pop("last_dropped_date", UNSET))

        def _parse_next_renewal_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_renewal_date_type_0 = isoparse(data).date()

                return next_renewal_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        next_renewal_date = _parse_next_renewal_date(d.pop("next_renewal_date", UNSET))

        _joined_date = d.pop("joined_date", UNSET)
        joined_date: datetime.date | Unset
        if isinstance(_joined_date, Unset):
            joined_date = UNSET
        else:
            joined_date = isoparse(_joined_date).date()

        def _parse_total_years(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_years = _parse_total_years(d.pop("total_years", UNSET))

        def _parse_times_renewed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        times_renewed = _parse_times_renewed(d.pop("times_renewed", UNSET))

        def _parse_consec_years(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        consec_years = _parse_consec_years(d.pop("consec_years", UNSET))

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        membership_details = cls(
            dues=dues,
            category_name=category_name,
            program_name=program_name,
            sub_category_name=sub_category_name,
            last_renewed_date=last_renewed_date,
            last_dropped_date=last_dropped_date,
            next_renewal_date=next_renewal_date,
            joined_date=joined_date,
            total_years=total_years,
            times_renewed=times_renewed,
            consec_years=consec_years,
            constituent_id=constituent_id,
            notes=notes,
        )

        return membership_details

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ConstituentSolicitCodeAdd")


@_attrs_define
class ConstituentSolicitCodeAdd:
    """Solicit codes provide guidance on how to contact constituents. These rules describe instructions and restrictions
    about when to reach out to constituents and how to tailor communications to honor their requests.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the solicit code.
            solicit_code (str): Communication instructions and/or restrictions for a constituent. Available values can be
                obtained from the <a href="https://developer.sky.blackbaud.com/docs/services/communication-
                preference/operations/ListSolicitCodes">Solicit Codes List</a>.
            end_date (datetime.datetime | None | Unset): The end date of the solicit code. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            start_date (datetime.datetime | None | Unset): The start date of the solicit code. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
    """

    constituent_id: str
    solicit_code: str
    end_date: datetime.datetime | None | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        solicit_code = self.solicit_code

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "constituent_id": constituent_id,
                "solicit_code": solicit_code,
            }
        )
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        solicit_code = d.pop("solicit_code")

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

        constituent_solicit_code_add = cls(
            constituent_id=constituent_id,
            solicit_code=solicit_code,
            end_date=end_date,
            start_date=start_date,
        )

        return constituent_solicit_code_add

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ConstituentSolicitCodeRead")


@_attrs_define
class ConstituentSolicitCodeRead:
    """Solicit codes provide guidance on how to contact constituents. These rules describe instructions and restrictions
    about when to reach out to constituents and how to tailor communications to honor their requests.

        Attributes:
            id (None | str | Unset): The immutable system record ID of the constituent solicit code.
            constituent_id (None | str | Unset): The immutable system record ID of the constituent associated with the
                solicit code.
            end_date (datetime.datetime | None | Unset): The end date of the solicit code. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            solicit_code (None | str | Unset): Communication instructions and/or restrictions for a constituent. Available
                values can be obtained from the <a href="https://developer.sky.blackbaud.com/docs/services/communication-
                preference/operations/ListSolicitCodes">Solicit Codes List</a>.
            start_date (datetime.datetime | None | Unset): The start date of the solicit code. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
    """

    id: None | str | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    solicit_code: None | str | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        solicit_code: None | str | Unset
        if isinstance(self.solicit_code, Unset):
            solicit_code = UNSET
        else:
            solicit_code = self.solicit_code

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if solicit_code is not UNSET:
            field_dict["solicit_code"] = solicit_code
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

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

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

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

        def _parse_solicit_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        solicit_code = _parse_solicit_code(d.pop("solicit_code", UNSET))

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

        constituent_solicit_code_read = cls(
            id=id,
            constituent_id=constituent_id,
            end_date=end_date,
            solicit_code=solicit_code,
            start_date=start_date,
        )

        return constituent_solicit_code_read

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConstituentAppealEdit")


@_attrs_define
class ConstituentAppealEdit:
    """A record from the dbo.CONSTITUENT_APPEALS table in Raiser's Edge.

    Attributes:
        appeal_description (str): The appeal description; used to look up the appeal record ID.
        package_description (None | str | Unset): The package description; used to look up the package record ID.
        response_description (None | str | Unset): The long description of the response for the constituent appeal.
        comments (None | str | Unset): The comments associated with the constituent appeal.
        appeal_date (datetime.date | None | Unset): The date for the constituent appeal.
        mailing_id (int | None | Unset): The mailing ID of the constituent appeal.
        market_finder_number (None | str | Unset): The market finder number associated with the constituent appeal.
        marketing_segment (None | str | Unset): The marketing segment associated with the constituent appeal.
        marketing_source_code (None | str | Unset): The marketing source code associated with the constituent appeal.
    """

    appeal_description: str
    package_description: None | str | Unset = UNSET
    response_description: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    appeal_date: datetime.date | None | Unset = UNSET
    mailing_id: int | None | Unset = UNSET
    market_finder_number: None | str | Unset = UNSET
    marketing_segment: None | str | Unset = UNSET
    marketing_source_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        appeal_description = self.appeal_description

        package_description: None | str | Unset
        if isinstance(self.package_description, Unset):
            package_description = UNSET
        else:
            package_description = self.package_description

        response_description: None | str | Unset
        if isinstance(self.response_description, Unset):
            response_description = UNSET
        else:
            response_description = self.response_description

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        appeal_date: None | str | Unset
        if isinstance(self.appeal_date, Unset):
            appeal_date = UNSET
        elif isinstance(self.appeal_date, datetime.date):
            appeal_date = self.appeal_date.isoformat()
        else:
            appeal_date = self.appeal_date

        mailing_id: int | None | Unset
        if isinstance(self.mailing_id, Unset):
            mailing_id = UNSET
        else:
            mailing_id = self.mailing_id

        market_finder_number: None | str | Unset
        if isinstance(self.market_finder_number, Unset):
            market_finder_number = UNSET
        else:
            market_finder_number = self.market_finder_number

        marketing_segment: None | str | Unset
        if isinstance(self.marketing_segment, Unset):
            marketing_segment = UNSET
        else:
            marketing_segment = self.marketing_segment

        marketing_source_code: None | str | Unset
        if isinstance(self.marketing_source_code, Unset):
            marketing_source_code = UNSET
        else:
            marketing_source_code = self.marketing_source_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "appeal_description": appeal_description,
            }
        )
        if package_description is not UNSET:
            field_dict["package_description"] = package_description
        if response_description is not UNSET:
            field_dict["response_description"] = response_description
        if comments is not UNSET:
            field_dict["comments"] = comments
        if appeal_date is not UNSET:
            field_dict["appeal_date"] = appeal_date
        if mailing_id is not UNSET:
            field_dict["mailing_id"] = mailing_id
        if market_finder_number is not UNSET:
            field_dict["market_finder_number"] = market_finder_number
        if marketing_segment is not UNSET:
            field_dict["marketing_segment"] = marketing_segment
        if marketing_source_code is not UNSET:
            field_dict["marketing_source_code"] = marketing_source_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appeal_description = d.pop("appeal_description")

        def _parse_package_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        package_description = _parse_package_description(d.pop("package_description", UNSET))

        def _parse_response_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_description = _parse_response_description(d.pop("response_description", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        def _parse_appeal_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                appeal_date_type_0 = isoparse(data).date()

                return appeal_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        appeal_date = _parse_appeal_date(d.pop("appeal_date", UNSET))

        def _parse_mailing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mailing_id = _parse_mailing_id(d.pop("mailing_id", UNSET))

        def _parse_market_finder_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_finder_number = _parse_market_finder_number(d.pop("market_finder_number", UNSET))

        def _parse_marketing_segment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marketing_segment = _parse_marketing_segment(d.pop("marketing_segment", UNSET))

        def _parse_marketing_source_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marketing_source_code = _parse_marketing_source_code(d.pop("marketing_source_code", UNSET))

        constituent_appeal_edit = cls(
            appeal_description=appeal_description,
            package_description=package_description,
            response_description=response_description,
            comments=comments,
            appeal_date=appeal_date,
            mailing_id=mailing_id,
            market_finder_number=market_finder_number,
            marketing_segment=marketing_segment,
            marketing_source_code=marketing_source_code,
        )

        return constituent_appeal_edit

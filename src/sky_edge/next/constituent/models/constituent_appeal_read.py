from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appeal_read import AppealRead
    from ..models.package_read import PackageRead


T = TypeVar("T", bound="ConstituentAppealRead")


@_attrs_define
class ConstituentAppealRead:
    """Constituent appeals are the solicitations received by a constituent to bring in gifts, such as direct mailings,
    phonathons, auctions, or gala events.

        Attributes:
            id (str | Unset): The immutable system record ID of the constituent appeal.
            appeal (AppealRead | Unset): Appeals are solicitations to generate gifts, such as direct mailings, online
                donation pages, phonathons, auctions, and events.
            comments (str | Unset): User comments for the constituent appeal.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the appeal.
            date (datetime.datetime | Unset): The constituent appeal date. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            finder_number (str | Unset): The Marketing finder number for the constituent appeal.
            mailing_id (str | Unset): The user-defined mailing identifier for the constituent appeal.
            marketing_segment (str | Unset): The marketing segment for the constituent appeal.
            marketing_source_code (str | Unset): The Marketing source code for the constituent appeal.
            package (PackageRead | Unset): Packages contain content and other items for the appeals that organizations use
                to solicit gifts.
            response (str | Unset): The response for the constituent appeal.
    """

    id: str | Unset = UNSET
    appeal: AppealRead | Unset = UNSET
    comments: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    finder_number: str | Unset = UNSET
    mailing_id: str | Unset = UNSET
    marketing_segment: str | Unset = UNSET
    marketing_source_code: str | Unset = UNSET
    package: PackageRead | Unset = UNSET
    response: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        appeal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.appeal, Unset):
            appeal = self.appeal.to_dict()

        comments = self.comments

        constituent_id = self.constituent_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        finder_number = self.finder_number

        mailing_id = self.mailing_id

        marketing_segment = self.marketing_segment

        marketing_source_code = self.marketing_source_code

        package: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        response = self.response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if appeal is not UNSET:
            field_dict["appeal"] = appeal
        if comments is not UNSET:
            field_dict["comments"] = comments
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date is not UNSET:
            field_dict["date"] = date
        if finder_number is not UNSET:
            field_dict["finder_number"] = finder_number
        if mailing_id is not UNSET:
            field_dict["mailing_id"] = mailing_id
        if marketing_segment is not UNSET:
            field_dict["marketing_segment"] = marketing_segment
        if marketing_source_code is not UNSET:
            field_dict["marketing_source_code"] = marketing_source_code
        if package is not UNSET:
            field_dict["package"] = package
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appeal_read import AppealRead
        from ..models.package_read import PackageRead

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _appeal = d.pop("appeal", UNSET)
        appeal: AppealRead | Unset
        if isinstance(_appeal, Unset):
            appeal = UNSET
        else:
            appeal = AppealRead.from_dict(_appeal)

        comments = d.pop("comments", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        finder_number = d.pop("finder_number", UNSET)

        mailing_id = d.pop("mailing_id", UNSET)

        marketing_segment = d.pop("marketing_segment", UNSET)

        marketing_source_code = d.pop("marketing_source_code", UNSET)

        _package = d.pop("package", UNSET)
        package: PackageRead | Unset
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = PackageRead.from_dict(_package)

        response = d.pop("response", UNSET)

        constituent_appeal_read = cls(
            id=id,
            appeal=appeal,
            comments=comments,
            constituent_id=constituent_id,
            date=date,
            finder_number=finder_number,
            mailing_id=mailing_id,
            marketing_segment=marketing_segment,
            marketing_source_code=marketing_source_code,
            package=package,
            response=response,
        )

        constituent_appeal_read.additional_properties = d
        return constituent_appeal_read

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

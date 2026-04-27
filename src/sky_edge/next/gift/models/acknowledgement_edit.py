from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="AcknowledgementEdit")


@_attrs_define
class AcknowledgementEdit:
    """Acknowledgement letters foster relationships with donors and show appreciation for their contributions. It is
    important to keep track of the acknowledgement status of gifts to ensure that each one gets a well-deserved thank
    you.

        Attributes:
            date (datetime.datetime | Unset): The date associated with the acknowledgement. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            letter (str | Unset): The letter associated with the acknowledgement.
            status (str | Unset): The status of the acknowledgement. Available values are: <i>ACKNOWLEDGED</i>,
                <i>NEEDSACKNOWLEDGEMENT</i>, and <i>DONOTACKNOWLEDGE.</i>
                When <code>acknowledgement_status</code> is set to <i>DONOTACKNOWLEDGE</i>, <code>acknowledgement_letter</code>
                and <code>acknowledgement_date</code> should be null.
                When it is set to <i>NEEDSACKNOWLEDGEMENT</i>, <code>acknowledgement_date</code> should be null.
    """

    date: datetime.datetime | Unset = UNSET
    letter: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        letter = self.letter

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if letter is not UNSET:
            field_dict["letter"] = letter
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        letter = d.pop("letter", UNSET)

        status = d.pop("status", UNSET)

        acknowledgement_edit = cls(
            date=date,
            letter=letter,
            status=status,
        )

        acknowledgement_edit.additional_properties = d
        return acknowledgement_edit

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

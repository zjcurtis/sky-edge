from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentEdit")


@_attrs_define
class AttachmentEdit:
    """Many cultivation activities collect related collateral, such as correspondence and prospect research. Attachments
    can save this data on the appropriate record to maintain a complete view of those activities.

        Attributes:
            date (datetime.datetime | Unset): The date of the attachment. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43-04:00</i>. This property
                cannot be set to null.
            name (str | Unset): The name of the attachment. Character limit: 150.
            tags (list[str] | Unset): The tags associated with the attachment. Tags supplement the attachment’s name and
                description and identify it based on how an organization categorizes attachments. Available values are the
                entries in the <b>Document Tags</b> table. Character limit: 100.
            url (str | Unset): The URL for the attachment. You can only edit the URL for link attachments. This property
                cannot be set to null.
    """

    date: datetime.datetime | Unset = UNSET
    name: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        name = self.name

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if url is not UNSET:
            field_dict["url"] = url

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

        name = d.pop("name", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        url = d.pop("url", UNSET)

        attachment_edit = cls(
            date=date,
            name=name,
            tags=tags,
            url=url,
        )

        attachment_edit.additional_properties = d
        return attachment_edit

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

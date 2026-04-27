from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="EditAttachment")


@_attrs_define
class EditAttachment:
    """A link or a physical attachment for an event. Physical attachments are uploaded files such as images, PDFs, or Word
    documents that are saved locally or on the network. They are stored and managed in the system. Link attachments are
    links to files such as images, blog posts, or YouTube videos that are online or in a cloud storage account. They are
    stored and managed externally.

        Attributes:
            tags (list[str] | None | Unset): The tags associated with the attachment. Tags supplement the attachment’s name
                and description and identify it based on how an organization categorizes attachments. Available values are the
                entries in the <b>Document Tags</b> table. Character limit: 100.
            date (datetime.date | Unset): The date of the attachment. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>. This property defaults to the
                current date if not supplied.
            name (None | str | Unset): The name of the attachment. Character limit: 150.
            url (None | str | Unset): The URL for the attachment. This is required for link attachments but does not apply
                to physical attachments.
    """

    tags: list[str] | None | Unset = UNSET
    date: datetime.date | Unset = UNSET
    name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tags: list[str] | None | Unset
        if isinstance(self.tags, Unset):
            tags = UNSET
        elif isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if date is not UNSET:
            field_dict["date"] = date
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_tags(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tags = _parse_tags(d.pop("tags", UNSET))

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        edit_attachment = cls(
            tags=tags,
            date=date,
            name=name,
            url=url,
        )

        return edit_attachment

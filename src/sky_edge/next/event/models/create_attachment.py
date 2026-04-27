from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.create_attachment_type import CreateAttachmentType

T = TypeVar("T", bound="CreateAttachment")


@_attrs_define
class CreateAttachment:
    """A link or a physical attachment for an event. Physical attachments are uploaded files such as images, PDFs, or Word
    documents that are saved locally or on the network. They are stored and managed in the system. Link attachments are
    links to files such as images, blog posts, or YouTube videos that are online or in a cloud storage account. They are
    stored and managed externally.

        Attributes:
            type_ (CreateAttachmentType): The attachment type.<p>Available values:</p><ul><li><i>Link</i> - Link attachments
                are links to files, such as images, blog posts, or YouTube videos, that are online or in a cloud storage
                account. They are stored and managed externally.</li><li><i>Physical</i> - Physical attachments are uploaded
                files, such as images, PDFs, or Word documents, that are saved locally or on the network. They are stored and
                managed in the system.</li></ul>
            tags (list[str] | None | Unset): The tags associated with the attachment. Tags supplement the attachment’s name
                and description and identify it based on how an organization categorizes attachments. Available values are the
                entries in the <b>Document Tags</b> table. Character limit: 100.
            date (datetime.date | Unset): The date of the attachment. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format</a>: <i>1969-11-21</i>. This property defaults to the
                current date if not supplied.
            name (None | str | Unset): The name of the attachment. Character limit: 150.
            url (None | str | Unset): The URL for the attachment. This is required for link attachments but does not apply
                to physical attachments.
            file_id (None | str | Unset): The identifier of the file. Character limit: 36. For physical attachments only.
            file_name (None | str | Unset): The file name. For physical attachments only.
            thumbnail_id (None | str | Unset): The identifier of the thumbnail. Character limit: 36. For physical
                attachments only.
    """

    type_: CreateAttachmentType
    tags: list[str] | None | Unset = UNSET
    date: datetime.date | Unset = UNSET
    name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    file_id: None | str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    thumbnail_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

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

        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        else:
            file_id = self.file_id

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        thumbnail_id: None | str | Unset
        if isinstance(self.thumbnail_id, Unset):
            thumbnail_id = UNSET
        else:
            thumbnail_id = self.thumbnail_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if date is not UNSET:
            field_dict["date"] = date
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if thumbnail_id is not UNSET:
            field_dict["thumbnail_id"] = thumbnail_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CreateAttachmentType(d.pop("type"))

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

        def _parse_file_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_thumbnail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_id = _parse_thumbnail_id(d.pop("thumbnail_id", UNSET))

        create_attachment = cls(
            type_=type_,
            tags=tags,
            date=date,
            name=name,
            url=url,
            file_id=file_id,
            file_name=file_name,
            thumbnail_id=thumbnail_id,
        )

        return create_attachment

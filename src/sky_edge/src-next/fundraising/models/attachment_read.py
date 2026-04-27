from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attachment_read_type import AttachmentReadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentRead")


@_attrs_define
class AttachmentRead:
    """Many cultivation activities collect related collateral, such as correspondence and prospect research. Attachments
    can save this data on the appropriate record to maintain a complete view of those activities.

        Attributes:
            id (str | Unset): The immutable system record ID of the attachment.
            content_type (str | Unset): The content type. For physical attachments only.
            date (datetime.datetime | Unset): The date of the attachment. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43-04:00</i>.
            file_id (str | Unset): The identifier of the file.
            file_name (str | Unset): The file name. For physical attachments only.
            file_size (int | Unset): The file size in bytes. For physical attachments only.
            name (str | Unset): The name of the attachment.
            parent_id (str | Unset): The parent object's immutable system record ID.
            tags (list[str] | Unset): The tags associated with the attachment. Tags supplement the attachment’s name and
                description and identify it based on how an organization categorizes attachments. Available values are the
                entries in the <b>Document Tags</b> table.
            thumbnail_id (str | Unset): The identifier of the thumbnail. For physical attachments that are images only.
            thumbnail_url (str | Unset): The URL for a thumbnail. For physical attachments that are images only. Contains a
                time-bound signature that limits access to 30 minutes.
            type_ (AttachmentReadType | Unset): The attachment type. Available values are <i>Link</i> and <i>Physical</i>.
                Physical attachments are uploaded files such as images, PDFs, or Word documents that are saved locally or on the
                network. They are stored and managed in the system. Link attachments are links to files such as images, blog
                posts, or YouTube videos that are online or in a cloud storage account. They are stored and managed externally.
            url (str | Unset): The URL for the attachment. The URL for a physical attachment contains a time-bound signature
                that limits access to 30 minutes.
    """

    id: str | Unset = UNSET
    content_type: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    file_id: str | Unset = UNSET
    file_name: str | Unset = UNSET
    file_size: int | Unset = UNSET
    name: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    thumbnail_id: str | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    type_: AttachmentReadType | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content_type = self.content_type

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        file_id = self.file_id

        file_name = self.file_name

        file_size = self.file_size

        name = self.name

        parent_id = self.parent_id

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        thumbnail_id = self.thumbnail_id

        thumbnail_url = self.thumbnail_url

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if date is not UNSET:
            field_dict["date"] = date
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if thumbnail_id is not UNSET:
            field_dict["thumbnail_id"] = thumbnail_id
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        content_type = d.pop("content_type", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        file_id = d.pop("file_id", UNSET)

        file_name = d.pop("file_name", UNSET)

        file_size = d.pop("file_size", UNSET)

        name = d.pop("name", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        thumbnail_id = d.pop("thumbnail_id", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: AttachmentReadType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AttachmentReadType(_type_)

        url = d.pop("url", UNSET)

        attachment_read = cls(
            id=id,
            content_type=content_type,
            date=date,
            file_id=file_id,
            file_name=file_name,
            file_size=file_size,
            name=name,
            parent_id=parent_id,
            tags=tags,
            thumbnail_id=thumbnail_id,
            thumbnail_url=thumbnail_url,
            type_=type_,
            url=url,
        )

        attachment_read.additional_properties = d
        return attachment_read

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

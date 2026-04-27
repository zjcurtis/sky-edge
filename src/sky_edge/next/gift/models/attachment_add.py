from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.attachment_add_type import AttachmentAddType

T = TypeVar("T", bound="AttachmentAdd")


@_attrs_define
class AttachmentAdd:
    """Many cultivation activities collect related collateral, such as correspondence and prospect research. Attachments
    can save this data on the appropriate record to maintain a complete view of those activities.

        Attributes:
            parent_id (str): The parent object's immutable system record ID.
            type_ (AttachmentAddType): The attachment type. Available values are <i>Link</i> and <i>Physical</i>. Physical
                attachments are uploaded files such as images, PDFs, or Word documents that are saved locally or on the network.
                They are stored and managed in the system. Link attachments are links to files such as images, blog posts, or
                YouTube videos that are online or in a cloud storage account. They are stored and managed externally.
            date (datetime.datetime | Unset): The date of the attachment. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format:</a><i>1969-11-21T10:29:43-04:00</i>. This property
                defaults to the current date and time if not supplied.
            file_id (str | Unset): The identifier of the file. Character limit: 36. For physical attachments only.
            file_name (str | Unset): The name of the file. Character limit: 255. For physical attachments only.
            name (str | Unset): The name of the attachment. Character limit: 150.
            tags (list[str] | Unset): The tags associated with the attachment. Tags supplement the attachment’s name and
                description and identify it based on how an organization categorizes attachments. Available values are the
                entries in the <b>Document Tags</b> table. Character limit: 100.
            thumbnail_id (str | Unset): The identifier of the thumbnail. Character limit: 36. For physical attachments only.
            url (str | Unset): The URL for the attachment. This is required for link attachments but does not apply to
                physical attachments.
    """

    parent_id: str
    type_: AttachmentAddType
    date: datetime.datetime | Unset = UNSET
    file_id: str | Unset = UNSET
    file_name: str | Unset = UNSET
    name: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    thumbnail_id: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_id = self.parent_id

        type_ = self.type_.value

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        file_id = self.file_id

        file_name = self.file_name

        name = self.name

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        thumbnail_id = self.thumbnail_id

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent_id": parent_id,
                "type": type_,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if name is not UNSET:
            field_dict["name"] = name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if thumbnail_id is not UNSET:
            field_dict["thumbnail_id"] = thumbnail_id
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_id = d.pop("parent_id")

        type_ = AttachmentAddType(d.pop("type"))

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        file_id = d.pop("file_id", UNSET)

        file_name = d.pop("file_name", UNSET)

        name = d.pop("name", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        thumbnail_id = d.pop("thumbnail_id", UNSET)

        url = d.pop("url", UNSET)

        attachment_add = cls(
            parent_id=parent_id,
            type_=type_,
            date=date,
            file_id=file_id,
            file_name=file_name,
            name=name,
            tags=tags,
            thumbnail_id=thumbnail_id,
            url=url,
        )

        attachment_add.additional_properties = d
        return attachment_add

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

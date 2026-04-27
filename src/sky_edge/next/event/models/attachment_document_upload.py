from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="AttachmentDocumentUpload")


@_attrs_define
class AttachmentDocumentUpload:
    """An object that represents the physical attachment to upload.
    An attachment is information you save to a record, such as images, PDFs, or Word files.

        Attributes:
            file_name (str): The file name. For physical attachments only.
            upload_thumbnail (bool | None | Unset): Indicates that a thumbnail needs to be created.
    """

    file_name: str
    upload_thumbnail: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        upload_thumbnail: bool | None | Unset
        if isinstance(self.upload_thumbnail, Unset):
            upload_thumbnail = UNSET
        else:
            upload_thumbnail = self.upload_thumbnail

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file_name": file_name,
            }
        )
        if upload_thumbnail is not UNSET:
            field_dict["upload_thumbnail"] = upload_thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("file_name")

        def _parse_upload_thumbnail(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upload_thumbnail = _parse_upload_thumbnail(d.pop("upload_thumbnail", UNSET))

        attachment_document_upload = cls(
            file_name=file_name,
            upload_thumbnail=upload_thumbnail,
        )

        return attachment_document_upload

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.attachment_file_request_metadata import (
    AttachmentFileRequestMetadata,
)

T = TypeVar("T", bound="AttachmentFileDefinition")


@_attrs_define
class AttachmentFileDefinition:
    """Contains metadata for uploading a document and unique document identifier for physical attachments.

    Attributes:
        file_id (None | str | Unset): The identifier of the file.
        file_upload_request (AttachmentFileRequestMetadata | Unset): The AttachmentFileRequestMetadata entity specifies
            metadata for requests to upload physical
            attachments, including the URL for files, headers and the HTTP method to use.
        thumbnail_id (None | str | Unset): The identifier of the thumbnail.
        thumbnail_upload_request (AttachmentFileRequestMetadata | Unset): The AttachmentFileRequestMetadata entity
            specifies metadata for requests to upload physical
            attachments, including the URL for files, headers and the HTTP method to use.
    """

    file_id: None | str | Unset = UNSET
    file_upload_request: AttachmentFileRequestMetadata | Unset = UNSET
    thumbnail_id: None | str | Unset = UNSET
    thumbnail_upload_request: AttachmentFileRequestMetadata | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        else:
            file_id = self.file_id

        file_upload_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_upload_request, Unset):
            file_upload_request = self.file_upload_request.to_dict()

        thumbnail_id: None | str | Unset
        if isinstance(self.thumbnail_id, Unset):
            thumbnail_id = UNSET
        else:
            thumbnail_id = self.thumbnail_id

        thumbnail_upload_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_upload_request, Unset):
            thumbnail_upload_request = self.thumbnail_upload_request.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_upload_request is not UNSET:
            field_dict["file_upload_request"] = file_upload_request
        if thumbnail_id is not UNSET:
            field_dict["thumbnail_id"] = thumbnail_id
        if thumbnail_upload_request is not UNSET:
            field_dict["thumbnail_upload_request"] = thumbnail_upload_request

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_file_request_metadata import (
            AttachmentFileRequestMetadata,
        )

        d = dict(src_dict)

        def _parse_file_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        _file_upload_request = d.pop("file_upload_request", UNSET)
        file_upload_request: AttachmentFileRequestMetadata | Unset
        if isinstance(_file_upload_request, Unset):
            file_upload_request = UNSET
        else:
            file_upload_request = AttachmentFileRequestMetadata.from_dict(
                _file_upload_request
            )

        def _parse_thumbnail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_id = _parse_thumbnail_id(d.pop("thumbnail_id", UNSET))

        _thumbnail_upload_request = d.pop("thumbnail_upload_request", UNSET)
        thumbnail_upload_request: AttachmentFileRequestMetadata | Unset
        if isinstance(_thumbnail_upload_request, Unset):
            thumbnail_upload_request = UNSET
        else:
            thumbnail_upload_request = AttachmentFileRequestMetadata.from_dict(
                _thumbnail_upload_request
            )

        attachment_file_definition = cls(
            file_id=file_id,
            file_upload_request=file_upload_request,
            thumbnail_id=thumbnail_id,
            thumbnail_upload_request=thumbnail_upload_request,
        )

        return attachment_file_definition

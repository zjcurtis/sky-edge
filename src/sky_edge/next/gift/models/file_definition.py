from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_meta_data import RequestMetaData


T = TypeVar("T", bound="FileDefinition")


@_attrs_define
class FileDefinition:
    """Contains metadata for uploading a document and unique document identifier for physical attachments.

    Attributes:
        file_id (str | Unset): The identifier of the file.
        file_upload_request (RequestMetaData | Unset): The RequestMetadata entity specifies metadata for requests to
            upload physical attachments, including the URL for files, headers and the HTTP method to use.
        thumbnail_id (str | Unset): The identifier of the thumbnail.
        thumbnail_upload_request (RequestMetaData | Unset): The RequestMetadata entity specifies metadata for requests
            to upload physical attachments, including the URL for files, headers and the HTTP method to use.
    """

    file_id: str | Unset = UNSET
    file_upload_request: RequestMetaData | Unset = UNSET
    thumbnail_id: str | Unset = UNSET
    thumbnail_upload_request: RequestMetaData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        file_upload_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_upload_request, Unset):
            file_upload_request = self.file_upload_request.to_dict()

        thumbnail_id = self.thumbnail_id

        thumbnail_upload_request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.thumbnail_upload_request, Unset):
            thumbnail_upload_request = self.thumbnail_upload_request.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        from ..models.request_meta_data import RequestMetaData

        d = dict(src_dict)
        file_id = d.pop("file_id", UNSET)

        _file_upload_request = d.pop("file_upload_request", UNSET)
        file_upload_request: RequestMetaData | Unset
        if isinstance(_file_upload_request, Unset):
            file_upload_request = UNSET
        else:
            file_upload_request = RequestMetaData.from_dict(_file_upload_request)

        thumbnail_id = d.pop("thumbnail_id", UNSET)

        _thumbnail_upload_request = d.pop("thumbnail_upload_request", UNSET)
        thumbnail_upload_request: RequestMetaData | Unset
        if isinstance(_thumbnail_upload_request, Unset):
            thumbnail_upload_request = UNSET
        else:
            thumbnail_upload_request = RequestMetaData.from_dict(
                _thumbnail_upload_request
            )

        file_definition = cls(
            file_id=file_id,
            file_upload_request=file_upload_request,
            thumbnail_id=thumbnail_id,
            thumbnail_upload_request=thumbnail_upload_request,
        )

        file_definition.additional_properties = d
        return file_definition

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

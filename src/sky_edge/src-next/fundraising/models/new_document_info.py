from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewDocumentInfo")


@_attrs_define
class NewDocumentInfo:
    """Cultivation activities often result in physical collateral such as images, PDFs, or Word files. The New Document
    entity allows you to upload these files to maintain a holistic view of target constituents.

        Attributes:
            file_name (str | Unset): The file name. For physical attachments only.
            upload_thumbnail (bool | Unset): Indicates that a thumbnail needs to be created.
    """

    file_name: str | Unset = UNSET
    upload_thumbnail: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        upload_thumbnail = self.upload_thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if upload_thumbnail is not UNSET:
            field_dict["upload_thumbnail"] = upload_thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("file_name", UNSET)

        upload_thumbnail = d.pop("upload_thumbnail", UNSET)

        new_document_info = cls(
            file_name=file_name,
            upload_thumbnail=upload_thumbnail,
        )

        new_document_info.additional_properties = d
        return new_document_info

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

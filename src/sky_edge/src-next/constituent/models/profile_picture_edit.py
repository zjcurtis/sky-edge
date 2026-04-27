from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfilePictureEdit")


@_attrs_define
class ProfilePictureEdit:
    """Profile pictures are photos or images such as selfies or company logos that help identify constituents and
    personalize relationships. Profile pictures can be PNG, BMP, or JPG image files uploaded via the web view.

        Attributes:
            document_id (UUID): The document identifier.
            file_name (str): The name of the file.
            thumbnail_id (UUID | Unset): The thumbnail document identifier.
    """

    document_id: UUID
    file_name: str
    thumbnail_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_id = str(self.document_id)

        file_name = self.file_name

        thumbnail_id: str | Unset = UNSET
        if not isinstance(self.thumbnail_id, Unset):
            thumbnail_id = str(self.thumbnail_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_id": document_id,
                "file_name": file_name,
            }
        )
        if thumbnail_id is not UNSET:
            field_dict["thumbnail_id"] = thumbnail_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_id = UUID(d.pop("document_id"))

        file_name = d.pop("file_name")

        _thumbnail_id = d.pop("thumbnail_id", UNSET)
        thumbnail_id: UUID | Unset
        if isinstance(_thumbnail_id, Unset):
            thumbnail_id = UNSET
        else:
            thumbnail_id = UUID(_thumbnail_id)

        profile_picture_edit = cls(
            document_id=document_id,
            file_name=file_name,
            thumbnail_id=thumbnail_id,
        )

        profile_picture_edit.additional_properties = d
        return profile_picture_edit

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfilePictureRead")


@_attrs_define
class ProfilePictureRead:
    """Profile pictures are photos or images such as selfies or company logos that help identify constituents and
    personalize relationships. Profile pictures can be PNG, BMP, or JPG image files uploaded via the web view.

        Attributes:
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the profile
                picture.
            thumbnail_url (str | Unset): The URL for a thumbnail of the profile picture. Contains a time-bound signature
                that limits access to 30 minutes.
            url (str | Unset): The URL for the profile picture. The URL contains a time-bound signature that limits access
                to 30 minutes.
    """

    constituent_id: str | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        thumbnail_url = self.thumbnail_url

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        url = d.pop("url", UNSET)

        profile_picture_read = cls(
            constituent_id=constituent_id,
            thumbnail_url=thumbnail_url,
            url=url,
        )

        profile_picture_read.additional_properties = d
        return profile_picture_read

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

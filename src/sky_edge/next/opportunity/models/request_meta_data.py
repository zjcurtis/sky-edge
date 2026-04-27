from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.header import Header


T = TypeVar("T", bound="RequestMetaData")


@_attrs_define
class RequestMetaData:
    """The RequestMetadata entity specifies metadata for requests to upload physical attachments, including the URL for
    files, headers and the HTTP method to use.

        Attributes:
            headers (list[Header] | Unset): The headers to supply when making the request.
            method (str | Unset): The http method to use for the request.
            url (str | Unset): The url to use for the request.
    """

    headers: list[Header] | Unset = UNSET
    method: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)

        method = self.method

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if method is not UNSET:
            field_dict["method"] = method
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.header import Header

        d = dict(src_dict)
        _headers = d.pop("headers", UNSET)
        headers: list[Header] | Unset = UNSET
        if _headers is not UNSET:
            headers = []
            for headers_item_data in _headers:
                headers_item = Header.from_dict(headers_item_data)

                headers.append(headers_item)

        method = d.pop("method", UNSET)

        url = d.pop("url", UNSET)

        request_meta_data = cls(
            headers=headers,
            method=method,
            url=url,
        )

        request_meta_data.additional_properties = d
        return request_meta_data

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

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="EditJobResponse")


@_attrs_define
class EditJobResponse:
    """Contract object returned when editing an existing job.

    Attributes:
        file_upload_uri (None | str | Unset): The file upload URI for the edited job.
    """

    file_upload_uri: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_upload_uri: None | str | Unset
        if isinstance(self.file_upload_uri, Unset):
            file_upload_uri = UNSET
        else:
            file_upload_uri = self.file_upload_uri

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_upload_uri is not UNSET:
            field_dict["file_upload_uri"] = file_upload_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_upload_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_upload_uri = _parse_file_upload_uri(d.pop("file_upload_uri", UNSET))

        edit_job_response = cls(
            file_upload_uri=file_upload_uri,
        )

        return edit_job_response

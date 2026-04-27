from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ImportFileUploadInformation")


@_attrs_define
class ImportFileUploadInformation:
    """Contract object returned getting a new file upload URI for an import job.

    Attributes:
        file_upload_uri (None | str): The file upload URI for the job.
    """

    file_upload_uri: None | str

    def to_dict(self) -> dict[str, Any]:
        file_upload_uri: None | str
        file_upload_uri = self.file_upload_uri

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file_upload_uri": file_upload_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_upload_uri(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_upload_uri = _parse_file_upload_uri(d.pop("file_upload_uri"))

        import_file_upload_information = cls(
            file_upload_uri=file_upload_uri,
        )

        return import_file_upload_information

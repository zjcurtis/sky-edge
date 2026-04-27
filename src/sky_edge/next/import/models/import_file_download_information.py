from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ImportFileDownloadInformation")


@_attrs_define
class ImportFileDownloadInformation:
    """Contract object returned when getting a file download URI for an import job.

    Attributes:
        file_download_uri (None | str): The file download URI for the job.
    """

    file_download_uri: None | str

    def to_dict(self) -> dict[str, Any]:
        file_download_uri: None | str
        file_download_uri = self.file_download_uri

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file_download_uri": file_download_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_download_uri(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_download_uri = _parse_file_download_uri(d.pop("file_download_uri"))

        import_file_download_information = cls(
            file_download_uri=file_download_uri,
        )

        return import_file_download_information

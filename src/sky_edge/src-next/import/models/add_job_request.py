from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AddJobRequest")


@_attrs_define
class AddJobRequest:
    """The contract object for adding an import job.

    Attributes:
        file_name (str): The name of the file to be imported by this job
    """

    file_name: str

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "file_name": file_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_name = d.pop("file_name")

        add_job_request = cls(
            file_name=file_name,
        )

        return add_job_request

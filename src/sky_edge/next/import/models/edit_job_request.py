from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="EditJobRequest")


@_attrs_define
class EditJobRequest:
    """The contract object for editing an import job.

    Attributes:
        file_name (None | str | Unset): The name of the file to be imported by this job.
    """

    file_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_name is not UNSET:
            field_dict["file_name"] = file_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        edit_job_request = cls(
            file_name=file_name,
        )

        return edit_job_request

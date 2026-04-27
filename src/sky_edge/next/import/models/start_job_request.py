from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="StartJobRequest")


@_attrs_define
class StartJobRequest:
    """The contract object for starting an import job.

    Attributes:
        job_id (str): The ID of the job to start.
    """

    job_id: str

    def to_dict(self) -> dict[str, Any]:
        job_id = self.job_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "job_id": job_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = d.pop("job_id")

        start_job_request = cls(
            job_id=job_id,
        )

        return start_job_request

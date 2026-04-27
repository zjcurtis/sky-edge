from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.job_status import JobStatus

T = TypeVar("T", bound="StartJobResponse")


@_attrs_define
class StartJobResponse:
    """Contract object returned when starting a job.

    Attributes:
        status (JobStatus | Unset): The status of an import job.<p>Members:</p><ul><li><i>Pending</i></li><li><i>Enqueue
            d</i></li><li><i>Starting</i></li><li><i>Running</i></li><li><i>Completed</i></li><li><i>CompletedWithExceptions
            </i></li><li><i>Failed</i></li></ul>
    """

    status: JobStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobStatus(_status)

        start_job_response = cls(
            status=status,
        )

        return start_job_response

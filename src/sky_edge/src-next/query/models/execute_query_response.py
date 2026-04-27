from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.query_job_status import QueryJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecuteQueryResponse")


@_attrs_define
class ExecuteQueryResponse:
    """Response model for StartQueryExecutionJobByID and StartQueryExecutionJob

    Attributes:
        id (str): The job identifier
        status (QueryJobStatus | Unset): Represents the status of the query job<p>Members:</p><ul><li><i>Pending</i> -
            The job has been queued but has not yet started running.</li><li><i>Running</i> - The job is
            running.</li><li><i>Completed</i> - The job successfully completed.</li><li><i>Failed</i> - The job
            failed.</li><li><i>Cancelling</i> - Job cancellation has been requested.  The job may still complete
            successfully from this state.</li><li><i>Cancelled</i> - The job was cancelled.</li><li><i>Throttled</i> - The
            job has been throttled.  The job will run when space is available.</li></ul>
        message (None | str | Unset): A message associated with the response
    """

    id: str
    status: QueryJobStatus | Unset = UNSET
    message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        _status = d.pop("status", UNSET)
        status: QueryJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = QueryJobStatus(_status)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        execute_query_response = cls(
            id=id,
            status=status,
            message=message,
        )

        return execute_query_response

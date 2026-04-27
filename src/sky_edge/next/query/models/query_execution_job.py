from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.query_job_status import QueryJobStatus

T = TypeVar("T", bound="QueryExecutionJob")


@_attrs_define
class QueryExecutionJob:
    """A background job for executing a query

    Attributes:
        id (None | str | Unset): The job ID
        status (QueryJobStatus | Unset): Represents the status of the query job<p>Members:</p><ul><li><i>Pending</i> -
            The job has been queued but has not yet started running.</li><li><i>Running</i> - The job is
            running.</li><li><i>Completed</i> - The job successfully completed.</li><li><i>Failed</i> - The job
            failed.</li><li><i>Cancelling</i> - Job cancellation has been requested.  The job may still complete
            successfully from this state.</li><li><i>Cancelled</i> - The job was cancelled.</li><li><i>Throttled</i> - The
            job has been throttled.  The job will run when space is available.</li></ul>
        sas_uri (None | str | Unset): SAS URI for accessing the query results.
            The URI functions as a secure credential to access the query results, and thus should be considered a secret
            unique value.
            Sharing this URI with anyone is strongly discouraged, and as a best practice, avoid persisting the URI beyond
            processing the job result.
            The URI will expire after 15 minutes.
        row_count (int | None | Unset): The number of rows found by the query
    """

    id: None | str | Unset = UNSET
    status: QueryJobStatus | Unset = UNSET
    sas_uri: None | str | Unset = UNSET
    row_count: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        sas_uri: None | str | Unset
        if isinstance(self.sas_uri, Unset):
            sas_uri = UNSET
        else:
            sas_uri = self.sas_uri

        row_count: int | None | Unset
        if isinstance(self.row_count, Unset):
            row_count = UNSET
        else:
            row_count = self.row_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if sas_uri is not UNSET:
            field_dict["sas_uri"] = sas_uri
        if row_count is not UNSET:
            field_dict["row_count"] = row_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _status = d.pop("status", UNSET)
        status: QueryJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = QueryJobStatus(_status)

        def _parse_sas_uri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sas_uri = _parse_sas_uri(d.pop("sas_uri", UNSET))

        def _parse_row_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        row_count = _parse_row_count(d.pop("row_count", UNSET))

        query_execution_job = cls(
            id=id,
            status=status,
            sas_uri=sas_uri,
            row_count=row_count,
        )

        return query_execution_job

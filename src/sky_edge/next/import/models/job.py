from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.job_status import JobStatus

T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """Summary information for import jobs.

    Attributes:
        id (None | str): The ID of the job.
        file_name (None | str): The file name of the job.
        status (JobStatus): The status of an import job.<p>Members:</p><ul><li><i>Pending</i></li><li><i>Enqueued</i></l
            i><li><i>Starting</i></li><li><i>Running</i></li><li><i>Completed</i></li><li><i>CompletedWithExceptions</i></li
            ><li><i>Failed</i></li></ul>
        added_by (None | str): The ID of the user who created the job.
        date_added (datetime.datetime): Date and time when the job was created.
        sequence (int | None | Unset): The sequence number of the job.
        rows_processed (int | None | Unset): The number of rows in the job's file.
        rows_committed (int | None | Unset): The number of rows committed by this job to date.
        rows_rejected (int | None | Unset): The number of invalid rows for the job.
        exception_count (int | None | Unset): The number of unaddressed exceptions for the job.
        run_duration (int | None | Unset): The duration of the job in seconds. Null if the job has not been run yet or
            if start_date or end_date is missing.
        start_date (datetime.datetime | None | Unset): Date and time when the job started.
        end_date (datetime.datetime | None | Unset): Date and time when the job ended.
        failure_message (None | str | Unset): The message associated with a failed job.
        date_modified (datetime.datetime | None | Unset): Date and time when the job was last changed.
    """

    id: None | str
    file_name: None | str
    status: JobStatus
    added_by: None | str
    date_added: datetime.datetime
    sequence: int | None | Unset = UNSET
    rows_processed: int | None | Unset = UNSET
    rows_committed: int | None | Unset = UNSET
    rows_rejected: int | None | Unset = UNSET
    exception_count: int | None | Unset = UNSET
    run_duration: int | None | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    failure_message: None | str | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        file_name: None | str
        file_name = self.file_name

        status = self.status.value

        added_by: None | str
        added_by = self.added_by

        date_added = self.date_added.isoformat()

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        rows_processed: int | None | Unset
        if isinstance(self.rows_processed, Unset):
            rows_processed = UNSET
        else:
            rows_processed = self.rows_processed

        rows_committed: int | None | Unset
        if isinstance(self.rows_committed, Unset):
            rows_committed = UNSET
        else:
            rows_committed = self.rows_committed

        rows_rejected: int | None | Unset
        if isinstance(self.rows_rejected, Unset):
            rows_rejected = UNSET
        else:
            rows_rejected = self.rows_rejected

        exception_count: int | None | Unset
        if isinstance(self.exception_count, Unset):
            exception_count = UNSET
        else:
            exception_count = self.exception_count

        run_duration: int | None | Unset
        if isinstance(self.run_duration, Unset):
            run_duration = UNSET
        else:
            run_duration = self.run_duration

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        failure_message: None | str | Unset
        if isinstance(self.failure_message, Unset):
            failure_message = UNSET
        else:
            failure_message = self.failure_message

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "file_name": file_name,
                "status": status,
                "added_by": added_by,
                "date_added": date_added,
            }
        )
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if rows_processed is not UNSET:
            field_dict["rows_processed"] = rows_processed
        if rows_committed is not UNSET:
            field_dict["rows_committed"] = rows_committed
        if rows_rejected is not UNSET:
            field_dict["rows_rejected"] = rows_rejected
        if exception_count is not UNSET:
            field_dict["exception_count"] = exception_count
        if run_duration is not UNSET:
            field_dict["run_duration"] = run_duration
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if failure_message is not UNSET:
            field_dict["failure_message"] = failure_message
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_file_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        file_name = _parse_file_name(d.pop("file_name"))

        status = JobStatus(d.pop("status"))

        def _parse_added_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        added_by = _parse_added_by(d.pop("added_by"))

        date_added = isoparse(d.pop("date_added"))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_rows_processed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rows_processed = _parse_rows_processed(d.pop("rows_processed", UNSET))

        def _parse_rows_committed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rows_committed = _parse_rows_committed(d.pop("rows_committed", UNSET))

        def _parse_rows_rejected(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rows_rejected = _parse_rows_rejected(d.pop("rows_rejected", UNSET))

        def _parse_exception_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exception_count = _parse_exception_count(d.pop("exception_count", UNSET))

        def _parse_run_duration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        run_duration = _parse_run_duration(d.pop("run_duration", UNSET))

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        def _parse_failure_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        failure_message = _parse_failure_message(d.pop("failure_message", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = isoparse(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        job = cls(
            id=id,
            file_name=file_name,
            status=status,
            added_by=added_by,
            date_added=date_added,
            sequence=sequence,
            rows_processed=rows_processed,
            rows_committed=rows_committed,
            rows_rejected=rows_rejected,
            exception_count=exception_count,
            run_duration=run_duration,
            start_date=start_date,
            end_date=end_date,
            failure_message=failure_message,
            date_modified=date_modified,
        )

        return job

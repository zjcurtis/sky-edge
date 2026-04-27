from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job import Job


T = TypeVar("T", bound="GetJobsResult")


@_attrs_define
class GetJobsResult:
    """A collection of job summaries.

    Attributes:
        count (int): The total number of jobs matching the filter.
        limit (int): The limit on the get jobs request.
        jobs (list[Job] | None): A collection of job summaries.
        continuation_token (None | str | Unset): A value will be returned here if not all possible results have been
            returned.
            To get the next page of results, make another request with this token and the same request criteria.
    """

    count: int
    limit: int
    jobs: list[Job] | None
    continuation_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        limit = self.limit

        jobs: list[dict[str, Any]] | None
        if isinstance(self.jobs, list):
            jobs = []
            for jobs_type_0_item_data in self.jobs:
                jobs_type_0_item = jobs_type_0_item_data.to_dict()
                jobs.append(jobs_type_0_item)

        else:
            jobs = self.jobs

        continuation_token: None | str | Unset
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "count": count,
                "limit": limit,
                "jobs": jobs,
            }
        )
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job import Job

        d = dict(src_dict)
        count = d.pop("count")

        limit = d.pop("limit")

        def _parse_jobs(data: object) -> list[Job] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                jobs_type_0 = []
                _jobs_type_0 = data
                for jobs_type_0_item_data in _jobs_type_0:
                    jobs_type_0_item = Job.from_dict(jobs_type_0_item_data)

                    jobs_type_0.append(jobs_type_0_item)

                return jobs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Job] | None, data)

        jobs = _parse_jobs(d.pop("jobs"))

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(d.pop("continuation_token", UNSET))

        get_jobs_result = cls(
            count=count,
            limit=limit,
            jobs=jobs,
            continuation_token=continuation_token,
        )

        return get_jobs_result

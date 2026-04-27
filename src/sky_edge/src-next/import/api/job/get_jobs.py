from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_jobs_400_response_types import GetJobs400ResponseTypes
from ...models.get_jobs_result import GetJobsResult
from ...models.job_status import JobStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: JobStatus | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["continuation_token"] = continuation_token

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetJobs400ResponseTypes | GetJobsResult | None:
    if response.status_code == 200:
        response_200 = GetJobsResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetJobs400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetJobs400ResponseTypes | GetJobsResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: JobStatus | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[Any | GetJobs400ResponseTypes | GetJobsResult]:
    """Get jobs (PREVIEW)

     Gets import jobs for the current environment.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        status (JobStatus | Unset): The status of an import job.<p>Members:</p><ul><li><i>Pending<
            /i></li><li><i>Enqueued</i></li><li><i>Starting</i></li><li><i>Running</i></li><li><i>Comp
            leted</i></li><li><i>CompletedWithExceptions</i></li><li><i>Failed</i></li></ul>
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetJobs400ResponseTypes | GetJobsResult]
    """

    kwargs = _get_kwargs(
        status=status,
        continuation_token=continuation_token,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    status: JobStatus | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Any | GetJobs400ResponseTypes | GetJobsResult | None:
    """Get jobs (PREVIEW)

     Gets import jobs for the current environment.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        status (JobStatus | Unset): The status of an import job.<p>Members:</p><ul><li><i>Pending<
            /i></li><li><i>Enqueued</i></li><li><i>Starting</i></li><li><i>Running</i></li><li><i>Comp
            leted</i></li><li><i>CompletedWithExceptions</i></li><li><i>Failed</i></li></ul>
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetJobs400ResponseTypes | GetJobsResult
    """

    return sync_detailed(
        client=client,
        status=status,
        continuation_token=continuation_token,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: JobStatus | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Response[Any | GetJobs400ResponseTypes | GetJobsResult]:
    """Get jobs (PREVIEW)

     Gets import jobs for the current environment.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        status (JobStatus | Unset): The status of an import job.<p>Members:</p><ul><li><i>Pending<
            /i></li><li><i>Enqueued</i></li><li><i>Starting</i></li><li><i>Running</i></li><li><i>Comp
            leted</i></li><li><i>CompletedWithExceptions</i></li><li><i>Failed</i></li></ul>
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetJobs400ResponseTypes | GetJobsResult]
    """

    kwargs = _get_kwargs(
        status=status,
        continuation_token=continuation_token,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: JobStatus | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 100,
) -> Any | GetJobs400ResponseTypes | GetJobsResult | None:
    """Get jobs (PREVIEW)

     Gets import jobs for the current environment.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        status (JobStatus | Unset): The status of an import job.<p>Members:</p><ul><li><i>Pending<
            /i></li><li><i>Enqueued</i></li><li><i>Starting</i></li><li><i>Running</i></li><li><i>Comp
            leted</i></li><li><i>CompletedWithExceptions</i></li><li><i>Failed</i></li></ul>
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetJobs400ResponseTypes | GetJobsResult
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            continuation_token=continuation_token,
            limit=limit,
        )
    ).parsed

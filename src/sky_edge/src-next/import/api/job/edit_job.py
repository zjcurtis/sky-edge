from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_job_400_response_types import EditJob400ResponseTypes
from ...models.edit_job_request import EditJobRequest
from ...models.edit_job_response import EditJobResponse
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    job_id: str,
    *,
    body: EditJobRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/jobs/{job_id}".format(
            job_id=quote(str(job_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = EditJobResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EditJob400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 412:
        response_412 = ProblemDetails.from_dict(response.json())

        return response_412

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditJobRequest | Unset = UNSET,
) -> Response[Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails]:
    """Edit a job (PREVIEW)

     Edits an import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        job_id (str):
        body (EditJobRequest | Unset): The contract object for editing an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditJobRequest | Unset = UNSET,
) -> Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails | None:
    """Edit a job (PREVIEW)

     Edits an import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        job_id (str):
        body (EditJobRequest | Unset): The contract object for editing an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails
    """

    return sync_detailed(
        job_id=job_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditJobRequest | Unset = UNSET,
) -> Response[Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails]:
    """Edit a job (PREVIEW)

     Edits an import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        job_id (str):
        body (EditJobRequest | Unset): The contract object for editing an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        job_id=job_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditJobRequest | Unset = UNSET,
) -> Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails | None:
    """Edit a job (PREVIEW)

     Edits an import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        job_id (str):
        body (EditJobRequest | Unset): The contract object for editing an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EditJob400ResponseTypes | EditJobResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            job_id=job_id,
            client=client,
            body=body,
        )
    ).parsed

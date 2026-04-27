from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.start_job_400_response_types import StartJob400ResponseTypes
from ...models.start_job_request import StartJobRequest
from ...models.start_job_response import StartJobResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: StartJobRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/jobs/start",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse | None:
    if response.status_code == 200:
        response_200 = StartJobResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = StartJob400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartJobRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse]:
    """Start a job (PREVIEW)

     Starts a pending import job. Call this after the import file has been uploaded.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (StartJobRequest | Unset): The contract object for starting an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: StartJobRequest | Unset = UNSET,
) -> Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse | None:
    """Start a job (PREVIEW)

     Starts a pending import job. Call this after the import file has been uploaded.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (StartJobRequest | Unset): The contract object for starting an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartJobRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse]:
    """Start a job (PREVIEW)

     Starts a pending import job. Call this after the import file has been uploaded.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (StartJobRequest | Unset): The contract object for starting an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: StartJobRequest | Unset = UNSET,
) -> Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse | None:
    """Start a job (PREVIEW)

     Starts a pending import job. Call this after the import file has been uploaded.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (StartJobRequest | Unset): The contract object for starting an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | StartJob400ResponseTypes | StartJobResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

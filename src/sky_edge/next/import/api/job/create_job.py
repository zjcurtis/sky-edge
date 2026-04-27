from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.add_job_request import AddJobRequest
from ...models.add_job_response import AddJobResponse
from ...models.create_job_400_response_types import CreateJob400ResponseTypes


def _get_kwargs(
    *,
    body: AddJobRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/jobs",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddJobResponse | Any | CreateJob400ResponseTypes | None:
    if response.status_code == 200:
        response_200 = AddJobResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateJob400ResponseTypes.from_dict(response.json())

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
) -> Response[AddJobResponse | Any | CreateJob400ResponseTypes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddJobRequest | Unset = UNSET,
) -> Response[AddJobResponse | Any | CreateJob400ResponseTypes]:
    """Create a job (PREVIEW)

     Creates a new import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (AddJobRequest | Unset): The contract object for adding an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddJobResponse | Any | CreateJob400ResponseTypes]
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
    body: AddJobRequest | Unset = UNSET,
) -> AddJobResponse | Any | CreateJob400ResponseTypes | None:
    """Create a job (PREVIEW)

     Creates a new import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (AddJobRequest | Unset): The contract object for adding an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddJobResponse | Any | CreateJob400ResponseTypes
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AddJobRequest | Unset = UNSET,
) -> Response[AddJobResponse | Any | CreateJob400ResponseTypes]:
    """Create a job (PREVIEW)

     Creates a new import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (AddJobRequest | Unset): The contract object for adding an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddJobResponse | Any | CreateJob400ResponseTypes]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AddJobRequest | Unset = UNSET,
) -> AddJobResponse | Any | CreateJob400ResponseTypes | None:
    """Create a job (PREVIEW)

     Creates a new import job.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (AddJobRequest | Unset): The contract object for adding an import job.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddJobResponse | Any | CreateJob400ResponseTypes
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

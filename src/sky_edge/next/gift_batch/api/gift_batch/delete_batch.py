from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.bad_request_response_problem_details import (
    BadRequestResponseProblemDetails,
)


def _get_kwargs(
    batch_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/giftbatches/{batch_id}".format(
            batch_id=quote(str(batch_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequestResponseProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = BadRequestResponseProblemDetails.from_dict(response.json())

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
) -> Response[Any | BadRequestResponseProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BadRequestResponseProblemDetails]:
    """Delete gift batch

     Deletes a gift batch.

    Args:
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequestResponseProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | BadRequestResponseProblemDetails | None:
    """Delete gift batch

     Deletes a gift batch.

    Args:
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequestResponseProblemDetails
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BadRequestResponseProblemDetails]:
    """Delete gift batch

     Deletes a gift batch.

    Args:
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequestResponseProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | BadRequestResponseProblemDetails | None:
    """Delete gift batch

     Deletes a gift batch.

    Args:
        batch_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequestResponseProblemDetails
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
        )
    ).parsed

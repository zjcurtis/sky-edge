from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_response_problem_details import BadRequestResponseProblemDetails
from ...models.create_batch import CreateBatch
from ...models.created_batch import CreatedBatch
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateBatch | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/giftbatches",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequestResponseProblemDetails | CreatedBatch | None:
    if response.status_code == 200:
        response_200 = CreatedBatch.from_dict(response.json())

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
) -> Response[Any | BadRequestResponseProblemDetails | CreatedBatch]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBatch | Unset = UNSET,
) -> Response[Any | BadRequestResponseProblemDetails | CreatedBatch]:
    """Create gift batch

     Creates a gift batch.

    Args:
        body (CreateBatch | Unset): Defines fields for a batch to be added to the data store

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequestResponseProblemDetails | CreatedBatch]
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
    body: CreateBatch | Unset = UNSET,
) -> Any | BadRequestResponseProblemDetails | CreatedBatch | None:
    """Create gift batch

     Creates a gift batch.

    Args:
        body (CreateBatch | Unset): Defines fields for a batch to be added to the data store

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequestResponseProblemDetails | CreatedBatch
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBatch | Unset = UNSET,
) -> Response[Any | BadRequestResponseProblemDetails | CreatedBatch]:
    """Create gift batch

     Creates a gift batch.

    Args:
        body (CreateBatch | Unset): Defines fields for a batch to be added to the data store

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequestResponseProblemDetails | CreatedBatch]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBatch | Unset = UNSET,
) -> Any | BadRequestResponseProblemDetails | CreatedBatch | None:
    """Create gift batch

     Creates a gift batch.

    Args:
        body (CreateBatch | Unset): Defines fields for a batch to be added to the data store

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequestResponseProblemDetails | CreatedBatch
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

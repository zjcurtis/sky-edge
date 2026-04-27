from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.batch_gift_read import BatchGiftRead
from ...models.get_batch_gift_400_response_types_problem_details import GetBatchGift400ResponseTypesProblemDetails
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    batch_gift_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/batchgifts/{batch_gift_id}".format(
            batch_gift_id=quote(str(batch_gift_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BatchGiftRead.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetBatchGift400ResponseTypesProblemDetails.from_dict(response.json())

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
) -> Response[Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails]:
    """Get Batch Gift (PREVIEW)

     Returns a single batch gift by ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_gift_id=batch_gift_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails | None:
    """Get Batch Gift (PREVIEW)

     Returns a single batch gift by ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails
    """

    return sync_detailed(
        batch_gift_id=batch_gift_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails]:
    """Get Batch Gift (PREVIEW)

     Returns a single batch gift by ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_gift_id=batch_gift_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails | None:
    """Get Batch Gift (PREVIEW)

     Returns a single batch gift by ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BatchGiftRead | GetBatchGift400ResponseTypesProblemDetails | ProblemDetails
    """

    return (
        await asyncio_detailed(
            batch_gift_id=batch_gift_id,
            client=client,
        )
    ).parsed

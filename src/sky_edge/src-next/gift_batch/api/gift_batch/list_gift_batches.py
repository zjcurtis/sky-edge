from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gift_batch_collection import GiftBatchCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
    added_by: str | Unset = UNSET,
    search_text: str | Unset = UNSET,
    approved: bool | Unset = UNSET,
    has_exceptions: bool | Unset = UNSET,
    batch_number: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["added_by"] = added_by

    params["search_text"] = search_text

    params["approved"] = approved

    params["has_exceptions"] = has_exceptions

    params["batch_number"] = batch_number

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/giftbatches",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GiftBatchCollection | None:
    if response.status_code == 200:
        response_200 = GiftBatchCollection.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GiftBatchCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
    added_by: str | Unset = UNSET,
    search_text: str | Unset = UNSET,
    approved: bool | Unset = UNSET,
    has_exceptions: bool | Unset = UNSET,
    batch_number: str | Unset = UNSET,
) -> Response[Any | GiftBatchCollection]:
    """List gift batches

     Returns a list of gift batches.

    Args:
        limit (int | Unset):  Default: 500.
        offset (int | Unset):
        added_by (str | Unset):
        search_text (str | Unset):
        approved (bool | Unset):
        has_exceptions (bool | Unset):
        batch_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftBatchCollection]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        added_by=added_by,
        search_text=search_text,
        approved=approved,
        has_exceptions=has_exceptions,
        batch_number=batch_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
    added_by: str | Unset = UNSET,
    search_text: str | Unset = UNSET,
    approved: bool | Unset = UNSET,
    has_exceptions: bool | Unset = UNSET,
    batch_number: str | Unset = UNSET,
) -> Any | GiftBatchCollection | None:
    """List gift batches

     Returns a list of gift batches.

    Args:
        limit (int | Unset):  Default: 500.
        offset (int | Unset):
        added_by (str | Unset):
        search_text (str | Unset):
        approved (bool | Unset):
        has_exceptions (bool | Unset):
        batch_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftBatchCollection
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        added_by=added_by,
        search_text=search_text,
        approved=approved,
        has_exceptions=has_exceptions,
        batch_number=batch_number,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
    added_by: str | Unset = UNSET,
    search_text: str | Unset = UNSET,
    approved: bool | Unset = UNSET,
    has_exceptions: bool | Unset = UNSET,
    batch_number: str | Unset = UNSET,
) -> Response[Any | GiftBatchCollection]:
    """List gift batches

     Returns a list of gift batches.

    Args:
        limit (int | Unset):  Default: 500.
        offset (int | Unset):
        added_by (str | Unset):
        search_text (str | Unset):
        approved (bool | Unset):
        has_exceptions (bool | Unset):
        batch_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftBatchCollection]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        added_by=added_by,
        search_text=search_text,
        approved=approved,
        has_exceptions=has_exceptions,
        batch_number=batch_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
    added_by: str | Unset = UNSET,
    search_text: str | Unset = UNSET,
    approved: bool | Unset = UNSET,
    has_exceptions: bool | Unset = UNSET,
    batch_number: str | Unset = UNSET,
) -> Any | GiftBatchCollection | None:
    """List gift batches

     Returns a list of gift batches.

    Args:
        limit (int | Unset):  Default: 500.
        offset (int | Unset):
        added_by (str | Unset):
        search_text (str | Unset):
        approved (bool | Unset):
        has_exceptions (bool | Unset):
        batch_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftBatchCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            added_by=added_by,
            search_text=search_text,
            approved=approved,
            has_exceptions=has_exceptions,
            batch_number=batch_number,
        )
    ).parsed

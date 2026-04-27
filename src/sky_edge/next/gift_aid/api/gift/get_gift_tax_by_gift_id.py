from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.gift_tax import GiftTax
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    gift_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/gifts/{gift_id}/giftaid".format(
            gift_id=quote(str(gift_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GiftTax | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = GiftTax.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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
) -> Response[Any | GiftTax | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GiftTax | ProblemDetails]:
    """Get gift record with gift splits by gift ID (PREVIEW)

     Get single gift by gift ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftTax | ProblemDetails]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GiftTax | ProblemDetails | None:
    """Get gift record with gift splits by gift ID (PREVIEW)

     Get single gift by gift ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftTax | ProblemDetails
    """

    return sync_detailed(
        gift_id=gift_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GiftTax | ProblemDetails]:
    """Get gift record with gift splits by gift ID (PREVIEW)

     Get single gift by gift ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftTax | ProblemDetails]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GiftTax | ProblemDetails | None:
    """Get gift record with gift splits by gift ID (PREVIEW)

     Get single gift by gift ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftTax | ProblemDetails
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
        )
    ).parsed

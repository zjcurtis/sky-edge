from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gift_id_map import GiftIdMap
from ...types import Response


def _get_kwargs(
    giftlookupid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/giftidmap/{giftlookupid}".format(
            giftlookupid=quote(str(giftlookupid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | GiftIdMap | None:
    if response.status_code == 200:
        response_200 = GiftIdMap.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | GiftIdMap]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    giftlookupid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GiftIdMap]:
    """Get a gift record id from gift lookup id

     Returns a gift system record id mapping for a given gift lookup id.

    Args:
        giftlookupid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftIdMap]
    """

    kwargs = _get_kwargs(
        giftlookupid=giftlookupid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    giftlookupid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GiftIdMap | None:
    """Get a gift record id from gift lookup id

     Returns a gift system record id mapping for a given gift lookup id.

    Args:
        giftlookupid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftIdMap
    """

    return sync_detailed(
        giftlookupid=giftlookupid,
        client=client,
    ).parsed


async def asyncio_detailed(
    giftlookupid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GiftIdMap]:
    """Get a gift record id from gift lookup id

     Returns a gift system record id mapping for a given gift lookup id.

    Args:
        giftlookupid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftIdMap]
    """

    kwargs = _get_kwargs(
        giftlookupid=giftlookupid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    giftlookupid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GiftIdMap | None:
    """Get a gift record id from gift lookup id

     Returns a gift system record id mapping for a given gift lookup id.

    Args:
        giftlookupid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftIdMap
    """

    return (
        await asyncio_detailed(
            giftlookupid=giftlookupid,
            client=client,
        )
    ).parsed

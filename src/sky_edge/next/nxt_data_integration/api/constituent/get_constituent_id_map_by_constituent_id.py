from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.constituent_id_map import ConstituentIdMap


def _get_kwargs(
    constituentid: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/constituentidmap/{constituentid}".format(
            constituentid=quote(str(constituentid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConstituentIdMap | None:
    if response.status_code == 200:
        response_200 = ConstituentIdMap.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ConstituentIdMap]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituentid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ConstituentIdMap]:
    """Get a constituent record id from constituent id

     Returns a constituent system record id mapping for a given constituent id.

    Args:
        constituentid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentIdMap]
    """

    kwargs = _get_kwargs(
        constituentid=constituentid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituentid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ConstituentIdMap | None:
    """Get a constituent record id from constituent id

     Returns a constituent system record id mapping for a given constituent id.

    Args:
        constituentid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentIdMap
    """

    return sync_detailed(
        constituentid=constituentid,
        client=client,
    ).parsed


async def asyncio_detailed(
    constituentid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ConstituentIdMap]:
    """Get a constituent record id from constituent id

     Returns a constituent system record id mapping for a given constituent id.

    Args:
        constituentid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentIdMap]
    """

    kwargs = _get_kwargs(
        constituentid=constituentid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituentid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ConstituentIdMap | None:
    """Get a constituent record id from constituent id

     Returns a constituent system record id mapping for a given constituent id.

    Args:
        constituentid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentIdMap
    """

    return (
        await asyncio_detailed(
            constituentid=constituentid,
            client=client,
        )
    ).parsed

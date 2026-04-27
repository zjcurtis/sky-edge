from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tribute import Tribute
from ...types import Response


def _get_kwargs(
    importid: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/tribute/importid/{importid}".format(
            importid=quote(str(importid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Tribute | None:
    if response.status_code == 200:
        response_200 = Tribute.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Tribute]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    importid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Tribute]:
    """Get a tribute by import id

     Returns details about a tribute.

    Args:
        importid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Tribute]
    """

    kwargs = _get_kwargs(
        importid=importid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    importid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Tribute | None:
    """Get a tribute by import id

     Returns details about a tribute.

    Args:
        importid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Tribute
    """

    return sync_detailed(
        importid=importid,
        client=client,
    ).parsed


async def asyncio_detailed(
    importid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | Tribute]:
    """Get a tribute by import id

     Returns details about a tribute.

    Args:
        importid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Tribute]
    """

    kwargs = _get_kwargs(
        importid=importid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    importid: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | Tribute | None:
    """Get a tribute by import id

     Returns details about a tribute.

    Args:
        importid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Tribute
    """

    return (
        await asyncio_detailed(
            importid=importid,
            client=client,
        )
    ).parsed

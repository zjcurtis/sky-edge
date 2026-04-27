from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.table_entry import TableEntry


def _get_kwargs(
    code_table_id: str,
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/codetables/{code_table_id}/tableentries/{id}".format(
            code_table_id=quote(str(code_table_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TableEntry | None:
    if response.status_code == 200:
        response_200 = TableEntry.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | TableEntry]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code_table_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TableEntry]:
    """Get a table entry (PREVIEW)

     Returns details about a table entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        code_table_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TableEntry]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    code_table_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TableEntry | None:
    """Get a table entry (PREVIEW)

     Returns details about a table entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        code_table_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TableEntry
    """

    return sync_detailed(
        code_table_id=code_table_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    code_table_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TableEntry]:
    """Get a table entry (PREVIEW)

     Returns details about a table entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        code_table_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TableEntry]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    code_table_id: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TableEntry | None:
    """Get a table entry (PREVIEW)

     Returns details about a table entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        code_table_id (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TableEntry
    """

    return (
        await asyncio_detailed(
            code_table_id=code_table_id,
            id=id,
            client=client,
        )
    ).parsed

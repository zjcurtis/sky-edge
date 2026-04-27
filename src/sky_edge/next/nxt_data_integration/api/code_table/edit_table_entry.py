from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.table_entry_edit import TableEntryEdit


def _get_kwargs(
    code_table_id: int,
    id: int,
    *,
    body: TableEntryEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/re/codetables/{code_table_id}/tableentries/{id}".format(
            code_table_id=quote(str(code_table_id), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code_table_id: int,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TableEntryEdit | Unset = UNSET,
) -> Response[Any]:
    """Edit a table entry

     Edit the details about a table entry.

    Args:
        code_table_id (int):
        id (int):
        body (TableEntryEdit | Unset): RE7 Table entry record edit class from the dbo.TableEntries
            table in Raiser's Edge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    code_table_id: int,
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TableEntryEdit | Unset = UNSET,
) -> Response[Any]:
    """Edit a table entry

     Edit the details about a table entry.

    Args:
        code_table_id (int):
        id (int):
        body (TableEntryEdit | Unset): RE7 Table entry record edit class from the dbo.TableEntries
            table in Raiser's Edge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

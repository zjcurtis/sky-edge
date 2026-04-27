from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_response import PostResponse
from ...models.table_entry_create import TableEntryCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    code_table_id: int,
    *,
    body: TableEntryCreate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/re/codetables/{code_table_id}/tableentries".format(
            code_table_id=quote(str(code_table_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PostResponse | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code_table_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TableEntryCreate | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Create a table entry

     Creates a new table entry.

    Args:
        code_table_id (int):
        body (TableEntryCreate | Unset): An Table Entry record from the dbo.TableEntries table in
            Raiser's Edge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    code_table_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TableEntryCreate | Unset = UNSET,
) -> Any | PostResponse | None:
    """Create a table entry

     Creates a new table entry.

    Args:
        code_table_id (int):
        body (TableEntryCreate | Unset): An Table Entry record from the dbo.TableEntries table in
            Raiser's Edge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return sync_detailed(
        code_table_id=code_table_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    code_table_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TableEntryCreate | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Create a table entry

     Creates a new table entry.

    Args:
        code_table_id (int):
        body (TableEntryCreate | Unset): An Table Entry record from the dbo.TableEntries table in
            Raiser's Edge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    code_table_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: TableEntryCreate | Unset = UNSET,
) -> Any | PostResponse | None:
    """Create a table entry

     Creates a new table entry.

    Args:
        code_table_id (int):
        body (TableEntryCreate | Unset): An Table Entry record from the dbo.TableEntries table in
            Raiser's Edge.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return (
        await asyncio_detailed(
            code_table_id=code_table_id,
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.table_entry_collection import TableEntryCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    code_table_id: int,
    *,
    long_description: str | Unset = UNSET,
    short_description: str | Unset = UNSET,
    numeric_value: float | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["long_description"] = long_description

    params["short_description"] = short_description

    params["numeric_value"] = numeric_value

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/codetables/{code_table_id}/tableentries".format(
            code_table_id=quote(str(code_table_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TableEntryCollection | None:
    if response.status_code == 200:
        response_200 = TableEntryCollection.from_dict(response.json())

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
) -> Response[Any | TableEntryCollection]:
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
    long_description: str | Unset = UNSET,
    short_description: str | Unset = UNSET,
    numeric_value: float | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | TableEntryCollection]:
    """Get table entries list

     Returns a list of table entries.

    Args:
        code_table_id (int):
        long_description (str | Unset):
        short_description (str | Unset):
        numeric_value (float | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TableEntryCollection]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        long_description=long_description,
        short_description=short_description,
        numeric_value=numeric_value,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    code_table_id: int,
    *,
    client: AuthenticatedClient | Client,
    long_description: str | Unset = UNSET,
    short_description: str | Unset = UNSET,
    numeric_value: float | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | TableEntryCollection | None:
    """Get table entries list

     Returns a list of table entries.

    Args:
        code_table_id (int):
        long_description (str | Unset):
        short_description (str | Unset):
        numeric_value (float | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TableEntryCollection
    """

    return sync_detailed(
        code_table_id=code_table_id,
        client=client,
        long_description=long_description,
        short_description=short_description,
        numeric_value=numeric_value,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    code_table_id: int,
    *,
    client: AuthenticatedClient | Client,
    long_description: str | Unset = UNSET,
    short_description: str | Unset = UNSET,
    numeric_value: float | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | TableEntryCollection]:
    """Get table entries list

     Returns a list of table entries.

    Args:
        code_table_id (int):
        long_description (str | Unset):
        short_description (str | Unset):
        numeric_value (float | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TableEntryCollection]
    """

    kwargs = _get_kwargs(
        code_table_id=code_table_id,
        long_description=long_description,
        short_description=short_description,
        numeric_value=numeric_value,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    code_table_id: int,
    *,
    client: AuthenticatedClient | Client,
    long_description: str | Unset = UNSET,
    short_description: str | Unset = UNSET,
    numeric_value: float | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | TableEntryCollection | None:
    """Get table entries list

     Returns a list of table entries.

    Args:
        code_table_id (int):
        long_description (str | Unset):
        short_description (str | Unset):
        numeric_value (float | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TableEntryCollection
    """

    return (
        await asyncio_detailed(
            code_table_id=code_table_id,
            client=client,
            long_description=long_description,
            short_description=short_description,
            numeric_value=numeric_value,
            include_inactive=include_inactive,
            limit=limit,
            offset=offset,
        )
    ).parsed

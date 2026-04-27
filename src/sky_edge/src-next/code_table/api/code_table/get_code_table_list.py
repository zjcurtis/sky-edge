from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.code_table_category import CodeTableCategory
from ...models.code_table_collection import CodeTableCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    search: str | Unset = UNSET,
    category: CodeTableCategory | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["search"] = search

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category.value

    params["category"] = json_category

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/codetables",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CodeTableCollection | None:
    if response.status_code == 200:
        response_200 = CodeTableCollection.from_dict(response.json())

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
) -> Response[Any | CodeTableCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    search: str | Unset = UNSET,
    category: CodeTableCategory | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | CodeTableCollection]:
    """Get code table list (PREVIEW)

     Returns a list of code tables.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        name (str | Unset):
        search (str | Unset):
        category (CodeTableCategory | Unset): The code table categories available. Certain
            categories are product module dependent.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CodeTableCollection]
    """

    kwargs = _get_kwargs(
        name=name,
        search=search,
        category=category,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    search: str | Unset = UNSET,
    category: CodeTableCategory | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | CodeTableCollection | None:
    """Get code table list (PREVIEW)

     Returns a list of code tables.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        name (str | Unset):
        search (str | Unset):
        category (CodeTableCategory | Unset): The code table categories available. Certain
            categories are product module dependent.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CodeTableCollection
    """

    return sync_detailed(
        client=client,
        name=name,
        search=search,
        category=category,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    search: str | Unset = UNSET,
    category: CodeTableCategory | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | CodeTableCollection]:
    """Get code table list (PREVIEW)

     Returns a list of code tables.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        name (str | Unset):
        search (str | Unset):
        category (CodeTableCategory | Unset): The code table categories available. Certain
            categories are product module dependent.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CodeTableCollection]
    """

    kwargs = _get_kwargs(
        name=name,
        search=search,
        category=category,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    search: str | Unset = UNSET,
    category: CodeTableCategory | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | CodeTableCollection | None:
    """Get code table list (PREVIEW)

     Returns a list of code tables.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        name (str | Unset):
        search (str | Unset):
        category (CodeTableCategory | Unset): The code table categories available. Certain
            categories are product module dependent.
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CodeTableCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            search=search,
            category=category,
            limit=limit,
            offset=offset,
        )
    ).parsed

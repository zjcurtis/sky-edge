from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.list_model import ListModel


def _get_kwargs(
    list_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lists/{list_id}".format(
            list_id=quote(str(list_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListModel | None:
    if response.status_code == 200:
        response_200 = ListModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListModel]:
    """Gets a list (PREVIEW)

     Returns a saved list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListModel]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ListModel | None:
    """Gets a list (PREVIEW)

     Returns a saved list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListModel
    """

    return sync_detailed(
        list_id=list_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ListModel]:
    """Gets a list (PREVIEW)

     Returns a saved list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListModel]
    """

    kwargs = _get_kwargs(
        list_id=list_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    list_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> ListModel | None:
    """Gets a list (PREVIEW)

     Returns a saved list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        list_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListModel
    """

    return (
        await asyncio_detailed(
            list_id=list_id,
            client=client,
        )
    ).parsed

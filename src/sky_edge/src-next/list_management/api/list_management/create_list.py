from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_model import ListModel
from ...models.save_list_request import SaveListRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SaveListRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/lists",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListModel | None:
    if response.status_code == 200:
        response_200 = ListModel.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SaveListRequest | Unset = UNSET,
) -> Response[ListModel]:
    """Creates a new list (PREVIEW)

     Saves a new list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (SaveListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SaveListRequest | Unset = UNSET,
) -> ListModel | None:
    """Creates a new list (PREVIEW)

     Saves a new list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (SaveListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SaveListRequest | Unset = UNSET,
) -> Response[ListModel]:
    """Creates a new list (PREVIEW)

     Saves a new list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (SaveListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SaveListRequest | Unset = UNSET,
) -> ListModel | None:
    """Creates a new list (PREVIEW)

     Saves a new list

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (SaveListRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

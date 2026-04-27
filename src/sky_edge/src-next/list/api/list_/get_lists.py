from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_collection_of_list import ApiCollectionOfList
from ...models.get_lists_list_type import GetListsListType
from ...types import UNSET, Response


def _get_kwargs(
    *,
    list_type: GetListsListType,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_list_type = list_type.value
    params["list_type"] = json_list_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/lists",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfList | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfList.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApiCollectionOfList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    list_type: GetListsListType,
) -> Response[Any | ApiCollectionOfList]:
    """Get a list of lists

     Returns a list of lists for the given list type

    Args:
        list_type (GetListsListType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfList]
    """

    kwargs = _get_kwargs(
        list_type=list_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    list_type: GetListsListType,
) -> Any | ApiCollectionOfList | None:
    """Get a list of lists

     Returns a list of lists for the given list type

    Args:
        list_type (GetListsListType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfList
    """

    return sync_detailed(
        client=client,
        list_type=list_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    list_type: GetListsListType,
) -> Response[Any | ApiCollectionOfList]:
    """Get a list of lists

     Returns a list of lists for the given list type

    Args:
        list_type (GetListsListType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfList]
    """

    kwargs = _get_kwargs(
        list_type=list_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    list_type: GetListsListType,
) -> Any | ApiCollectionOfList | None:
    """Get a list of lists

     Returns a list of lists for the given list type

    Args:
        list_type (GetListsListType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfList
    """

    return (
        await asyncio_detailed(
            client=client,
            list_type=list_type,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expense_type_collection import ExpenseTypeCollection
from ...models.service_error import ServiceError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_inactive: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_inactive"] = include_inactive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/expensetypes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExpenseTypeCollection | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = ExpenseTypeCollection.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = ServiceError.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExpenseTypeCollection | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Response[ExpenseTypeCollection | list[ServiceError]]:
    """Get expense types (PREVIEW)

     Returns a collection of expense types.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpenseTypeCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> ExpenseTypeCollection | list[ServiceError] | None:
    """Get expense types (PREVIEW)

     Returns a collection of expense types.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpenseTypeCollection | list[ServiceError]
    """

    return sync_detailed(
        client=client,
        include_inactive=include_inactive,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Response[ExpenseTypeCollection | list[ServiceError]]:
    """Get expense types (PREVIEW)

     Returns a collection of expense types.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExpenseTypeCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        include_inactive=include_inactive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> ExpenseTypeCollection | list[ServiceError] | None:
    """Get expense types (PREVIEW)

     Returns a collection of expense types.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExpenseTypeCollection | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            client=client,
            include_inactive=include_inactive,
        )
    ).parsed

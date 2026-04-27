from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.event_expense import EventExpense
from ...models.service_error import ServiceError


def _get_kwargs(
    expense_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/expenses/{expense_id}".format(
            expense_id=quote(str(expense_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventExpense | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = EventExpense.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ServiceError.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = ServiceError.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403

    if response.status_code == 404:
        response_404 = []
        _response_404 = response.json()
        for response_404_item_data in _response_404:
            response_404_item = ServiceError.from_dict(response_404_item_data)

            response_404.append(response_404_item)

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EventExpense | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    expense_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EventExpense | list[ServiceError]]:
    """Gets an event expense. (PREVIEW)

     Returns an event expense for a given expense ID.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        expense_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventExpense | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        expense_id=expense_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    expense_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EventExpense | list[ServiceError] | None:
    """Gets an event expense. (PREVIEW)

     Returns an event expense for a given expense ID.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        expense_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventExpense | list[ServiceError]
    """

    return sync_detailed(
        expense_id=expense_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    expense_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EventExpense | list[ServiceError]]:
    """Gets an event expense. (PREVIEW)

     Returns an event expense for a given expense ID.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        expense_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventExpense | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        expense_id=expense_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    expense_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EventExpense | list[ServiceError] | None:
    """Gets an event expense. (PREVIEW)

     Returns an event expense for a given expense ID.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        expense_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventExpense | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            expense_id=expense_id,
            client=client,
        )
    ).parsed

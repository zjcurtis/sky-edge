from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_event_expense_request import CreateEventExpenseRequest
from ...models.id_response import IdResponse
from ...models.service_error import ServiceError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_id: str,
    *,
    body: CreateEventExpenseRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/events/{event_id}/expenses".format(
            event_id=quote(str(event_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IdResponse | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = IdResponse.from_dict(response.json())

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
) -> Response[IdResponse | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventExpenseRequest | Unset = UNSET,
) -> Response[IdResponse | list[ServiceError]]:
    """Create an event expense (PREVIEW)

     Create an event expense.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        event_id (str):
        body (CreateEventExpenseRequest | Unset): An event expense is a debt incurred from hosting
            an event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdResponse | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventExpenseRequest | Unset = UNSET,
) -> IdResponse | list[ServiceError] | None:
    """Create an event expense (PREVIEW)

     Create an event expense.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        event_id (str):
        body (CreateEventExpenseRequest | Unset): An event expense is a debt incurred from hosting
            an event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdResponse | list[ServiceError]
    """

    return sync_detailed(
        event_id=event_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventExpenseRequest | Unset = UNSET,
) -> Response[IdResponse | list[ServiceError]]:
    """Create an event expense (PREVIEW)

     Create an event expense.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        event_id (str):
        body (CreateEventExpenseRequest | Unset): An event expense is a debt incurred from hosting
            an event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IdResponse | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        event_id=event_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateEventExpenseRequest | Unset = UNSET,
) -> IdResponse | list[ServiceError] | None:
    """Create an event expense (PREVIEW)

     Create an event expense.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        event_id (str):
        body (CreateEventExpenseRequest | Unset): An event expense is a debt incurred from hosting
            an event.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IdResponse | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            event_id=event_id,
            client=client,
            body=body,
        )
    ).parsed

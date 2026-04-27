from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_list_from_ids_request import CreateListFromIdsRequest
from ...models.create_list_from_ids_response import CreateListFromIdsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateListFromIdsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/createlistfromids",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateListFromIdsResponse | None:
    if response.status_code == 200:
        response_200 = CreateListFromIdsResponse.from_dict(response.json())

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
) -> Response[Any | CreateListFromIdsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateListFromIdsRequest | Unset = UNSET,
) -> Response[Any | CreateListFromIdsResponse]:
    """Create a list from set of identifiers

     Creates a new list filtered to the specified set of identifiers. Returns a unique identifier for the
    new list The <code>name</code> parameter must be unique and not in use on an existing list. The
    <code>ids</code> parameter is limited to 100,000 identifiers. The <code>name</code> parameter is
    limited to 50 characters

    Args:
        body (CreateListFromIdsRequest | Unset): Represents a request to create a list filtered to
            a set of unique record identifiers

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateListFromIdsResponse]
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
    body: CreateListFromIdsRequest | Unset = UNSET,
) -> Any | CreateListFromIdsResponse | None:
    """Create a list from set of identifiers

     Creates a new list filtered to the specified set of identifiers. Returns a unique identifier for the
    new list The <code>name</code> parameter must be unique and not in use on an existing list. The
    <code>ids</code> parameter is limited to 100,000 identifiers. The <code>name</code> parameter is
    limited to 50 characters

    Args:
        body (CreateListFromIdsRequest | Unset): Represents a request to create a list filtered to
            a set of unique record identifiers

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateListFromIdsResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateListFromIdsRequest | Unset = UNSET,
) -> Response[Any | CreateListFromIdsResponse]:
    """Create a list from set of identifiers

     Creates a new list filtered to the specified set of identifiers. Returns a unique identifier for the
    new list The <code>name</code> parameter must be unique and not in use on an existing list. The
    <code>ids</code> parameter is limited to 100,000 identifiers. The <code>name</code> parameter is
    limited to 50 characters

    Args:
        body (CreateListFromIdsRequest | Unset): Represents a request to create a list filtered to
            a set of unique record identifiers

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateListFromIdsResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateListFromIdsRequest | Unset = UNSET,
) -> Any | CreateListFromIdsResponse | None:
    """Create a list from set of identifiers

     Creates a new list filtered to the specified set of identifiers. Returns a unique identifier for the
    new list The <code>name</code> parameter must be unique and not in use on an existing list. The
    <code>ids</code> parameter is limited to 100,000 identifiers. The <code>name</code> parameter is
    limited to 50 characters

    Args:
        body (CreateListFromIdsRequest | Unset): Represents a request to create a list filtered to
            a set of unique record identifiers

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateListFromIdsResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

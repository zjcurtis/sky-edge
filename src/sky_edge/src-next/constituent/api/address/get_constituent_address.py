from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_read_extended import AddressReadExtended
from ...types import Response


def _get_kwargs(
    address_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/addresses/{address_id}".format(
            address_id=quote(str(address_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddressReadExtended | Any | None:
    if response.status_code == 200:
        response_200 = AddressReadExtended.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddressReadExtended | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AddressReadExtended | Any]:
    """Address

     Returns a constituent address.

    Args:
        address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressReadExtended | Any]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AddressReadExtended | Any | None:
    """Address

     Returns a constituent address.

    Args:
        address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressReadExtended | Any
    """

    return sync_detailed(
        address_id=address_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AddressReadExtended | Any]:
    """Address

     Returns a constituent address.

    Args:
        address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressReadExtended | Any]
    """

    kwargs = _get_kwargs(
        address_id=address_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    address_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AddressReadExtended | Any | None:
    """Address

     Returns a constituent address.

    Args:
        address_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressReadExtended | Any
    """

    return (
        await asyncio_detailed(
            address_id=address_id,
            client=client,
        )
    ).parsed

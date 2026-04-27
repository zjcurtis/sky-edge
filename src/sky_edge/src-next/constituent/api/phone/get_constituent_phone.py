from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.phone_read import PhoneRead
from ...types import Response


def _get_kwargs(
    phone_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/phones/{phone_id}".format(
            phone_id=quote(str(phone_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PhoneRead | None:
    if response.status_code == 200:
        response_200 = PhoneRead.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PhoneRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    phone_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PhoneRead]:
    """Phone (Get)

     Returns a single phone.

    Args:
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PhoneRead]
    """

    kwargs = _get_kwargs(
        phone_id=phone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    phone_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PhoneRead | None:
    """Phone (Get)

     Returns a single phone.

    Args:
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PhoneRead
    """

    return sync_detailed(
        phone_id=phone_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    phone_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PhoneRead]:
    """Phone (Get)

     Returns a single phone.

    Args:
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PhoneRead]
    """

    kwargs = _get_kwargs(
        phone_id=phone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    phone_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | PhoneRead | None:
    """Phone (Get)

     Returns a single phone.

    Args:
        phone_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PhoneRead
    """

    return (
        await asyncio_detailed(
            phone_id=phone_id,
            client=client,
        )
    ).parsed

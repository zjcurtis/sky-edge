from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.fund_read import FundRead


def _get_kwargs(
    fund_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/funds/{fund_id}".format(
            fund_id=quote(str(fund_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FundRead | None:
    if response.status_code == 200:
        response_200 = FundRead.from_dict(response.json())

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
) -> Response[Any | FundRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fund_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | FundRead]:
    """Fund (Get)

     Returns information about the fund with the specified ID.

    Args:
        fund_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FundRead]
    """

    kwargs = _get_kwargs(
        fund_id=fund_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fund_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | FundRead | None:
    """Fund (Get)

     Returns information about the fund with the specified ID.

    Args:
        fund_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FundRead
    """

    return sync_detailed(
        fund_id=fund_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fund_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | FundRead]:
    """Fund (Get)

     Returns information about the fund with the specified ID.

    Args:
        fund_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FundRead]
    """

    kwargs = _get_kwargs(
        fund_id=fund_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fund_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | FundRead | None:
    """Fund (Get)

     Returns information about the fund with the specified ID.

    Args:
        fund_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FundRead
    """

    return (
        await asyncio_detailed(
            fund_id=fund_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fund_collection import FundCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    fund_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["fund_id"] = fund_id

    params["description"] = description

    params["include_inactive"] = include_inactive

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/funds",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | FundCollection | None:
    if response.status_code == 200:
        response_200 = FundCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FundCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    fund_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | FundCollection]:
    """Get fund list

     Returns a list of funds.

    Args:
        fund_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FundCollection]
    """

    kwargs = _get_kwargs(
        fund_id=fund_id,
        description=description,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    fund_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | FundCollection | None:
    """Get fund list

     Returns a list of funds.

    Args:
        fund_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FundCollection
    """

    return sync_detailed(
        client=client,
        fund_id=fund_id,
        description=description,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    fund_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | FundCollection]:
    """Get fund list

     Returns a list of funds.

    Args:
        fund_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FundCollection]
    """

    kwargs = _get_kwargs(
        fund_id=fund_id,
        description=description,
        include_inactive=include_inactive,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    fund_id: str | Unset = UNSET,
    description: str | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | FundCollection | None:
    """Get fund list

     Returns a list of funds.

    Args:
        fund_id (str | Unset):
        description (str | Unset):
        include_inactive (bool | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FundCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            fund_id=fund_id,
            description=description,
            include_inactive=include_inactive,
            limit=limit,
            offset=offset,
        )
    ).parsed

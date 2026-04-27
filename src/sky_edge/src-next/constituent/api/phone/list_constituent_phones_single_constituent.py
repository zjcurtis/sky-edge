from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_collection_of_phone_read import ApiCollectionOfPhoneRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    constituent_id: str,
    *,
    include_inactive: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_inactive"] = include_inactive

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/{constituent_id}/phones".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfPhoneRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfPhoneRead.from_dict(response.json())

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
) -> Response[Any | ApiCollectionOfPhoneRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Response[Any | ApiCollectionOfPhoneRead]:
    """Phone list (Single constituent)

     Returns a list of phones for a constituent.

    Args:
        constituent_id (str):
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfPhoneRead]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        include_inactive=include_inactive,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Any | ApiCollectionOfPhoneRead | None:
    """Phone list (Single constituent)

     Returns a list of phones for a constituent.

    Args:
        constituent_id (str):
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfPhoneRead
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
        include_inactive=include_inactive,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Response[Any | ApiCollectionOfPhoneRead]:
    """Phone list (Single constituent)

     Returns a list of phones for a constituent.

    Args:
        constituent_id (str):
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfPhoneRead]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        include_inactive=include_inactive,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_inactive: bool | Unset = UNSET,
) -> Any | ApiCollectionOfPhoneRead | None:
    """Phone list (Single constituent)

     Returns a list of phones for a constituent.

    Args:
        constituent_id (str):
        include_inactive (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfPhoneRead
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            include_inactive=include_inactive,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tribute_acknowledgee_collection import TributeAcknowledgeeCollection
from ...types import Response


def _get_kwargs(
    tribute_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/re/tribute/{tribute_id}/acknowledgees".format(
            tribute_id=quote(str(tribute_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | TributeAcknowledgeeCollection | None:
    if response.status_code == 200:
        response_200 = TributeAcknowledgeeCollection.from_dict(response.json())

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
) -> Response[Any | TributeAcknowledgeeCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tribute_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TributeAcknowledgeeCollection]:
    """Get tribute acknowledgees by tribute id

     Returns a list of tribute acknowledgees for the given tribute.

    Args:
        tribute_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TributeAcknowledgeeCollection]
    """

    kwargs = _get_kwargs(
        tribute_id=tribute_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tribute_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TributeAcknowledgeeCollection | None:
    """Get tribute acknowledgees by tribute id

     Returns a list of tribute acknowledgees for the given tribute.

    Args:
        tribute_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TributeAcknowledgeeCollection
    """

    return sync_detailed(
        tribute_id=tribute_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tribute_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | TributeAcknowledgeeCollection]:
    """Get tribute acknowledgees by tribute id

     Returns a list of tribute acknowledgees for the given tribute.

    Args:
        tribute_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | TributeAcknowledgeeCollection]
    """

    kwargs = _get_kwargs(
        tribute_id=tribute_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tribute_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Any | TributeAcknowledgeeCollection | None:
    """Get tribute acknowledgees by tribute id

     Returns a list of tribute acknowledgees for the given tribute.

    Args:
        tribute_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | TributeAcknowledgeeCollection
    """

    return (
        await asyncio_detailed(
            tribute_id=tribute_id,
            client=client,
        )
    ).parsed

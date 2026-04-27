from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appeal_read import AppealRead
from ...types import Response


def _get_kwargs(
    appeal_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/appeals/{appeal_id}".format(
            appeal_id=quote(str(appeal_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | AppealRead | None:
    if response.status_code == 200:
        response_200 = AppealRead.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | AppealRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    appeal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | AppealRead]:
    """Appeal (Get)

     Returns information about the appeal with the specified ID.

    Args:
        appeal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AppealRead]
    """

    kwargs = _get_kwargs(
        appeal_id=appeal_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    appeal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | AppealRead | None:
    """Appeal (Get)

     Returns information about the appeal with the specified ID.

    Args:
        appeal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AppealRead
    """

    return sync_detailed(
        appeal_id=appeal_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    appeal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | AppealRead]:
    """Appeal (Get)

     Returns information about the appeal with the specified ID.

    Args:
        appeal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AppealRead]
    """

    kwargs = _get_kwargs(
        appeal_id=appeal_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    appeal_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | AppealRead | None:
    """Appeal (Get)

     Returns information about the appeal with the specified ID.

    Args:
        appeal_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AppealRead
    """

    return (
        await asyncio_detailed(
            appeal_id=appeal_id,
            client=client,
        )
    ).parsed

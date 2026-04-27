from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constituent_code_read import ConstituentCodeRead
from ...types import Response


def _get_kwargs(
    constituent_code_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/constituentcodes/{constituent_code_id}".format(
            constituent_code_id=quote(str(constituent_code_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConstituentCodeRead | None:
    if response.status_code == 200:
        response_200 = ConstituentCodeRead.from_dict(response.json())

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
) -> Response[Any | ConstituentCodeRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituent_code_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ConstituentCodeRead]:
    """Constituent code (Get)

     Returns a constituent code.

    Args:
        constituent_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentCodeRead]
    """

    kwargs = _get_kwargs(
        constituent_code_id=constituent_code_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_code_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ConstituentCodeRead | None:
    """Constituent code (Get)

     Returns a constituent code.

    Args:
        constituent_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentCodeRead
    """

    return sync_detailed(
        constituent_code_id=constituent_code_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    constituent_code_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ConstituentCodeRead]:
    """Constituent code (Get)

     Returns a constituent code.

    Args:
        constituent_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentCodeRead]
    """

    kwargs = _get_kwargs(
        constituent_code_id=constituent_code_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_code_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ConstituentCodeRead | None:
    """Constituent code (Get)

     Returns a constituent code.

    Args:
        constituent_code_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentCodeRead
    """

    return (
        await asyncio_detailed(
            constituent_code_id=constituent_code_id,
            client=client,
        )
    ).parsed

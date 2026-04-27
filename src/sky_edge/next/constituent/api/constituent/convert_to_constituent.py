from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.non_constituent_conversion import NonConstituentConversion
from ...models.post_response import PostResponse


def _get_kwargs(
    non_constituent_id: str,
    *,
    body: NonConstituentConversion | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/constituents/convert/{non_constituent_id}".format(
            non_constituent_id=quote(str(non_constituent_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostResponse | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

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
) -> Response[Any | PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    non_constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NonConstituentConversion | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Constituent (Convert)

     Converts a non-constituent to a constituent.

    Args:
        non_constituent_id (str):
        body (NonConstituentConversion | Unset): The non-constituent conversion object holds
            constituent codes to apply during the conversion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
    """

    kwargs = _get_kwargs(
        non_constituent_id=non_constituent_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    non_constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NonConstituentConversion | Unset = UNSET,
) -> Any | PostResponse | None:
    """Constituent (Convert)

     Converts a non-constituent to a constituent.

    Args:
        non_constituent_id (str):
        body (NonConstituentConversion | Unset): The non-constituent conversion object holds
            constituent codes to apply during the conversion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return sync_detailed(
        non_constituent_id=non_constituent_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    non_constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NonConstituentConversion | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Constituent (Convert)

     Converts a non-constituent to a constituent.

    Args:
        non_constituent_id (str):
        body (NonConstituentConversion | Unset): The non-constituent conversion object holds
            constituent codes to apply during the conversion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
    """

    kwargs = _get_kwargs(
        non_constituent_id=non_constituent_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    non_constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NonConstituentConversion | Unset = UNSET,
) -> Any | PostResponse | None:
    """Constituent (Convert)

     Converts a non-constituent to a constituent.

    Args:
        non_constituent_id (str):
        body (NonConstituentConversion | Unset): The non-constituent conversion object holds
            constituent codes to apply during the conversion.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return (
        await asyncio_detailed(
            non_constituent_id=non_constituent_id,
            client=client,
            body=body,
        )
    ).parsed

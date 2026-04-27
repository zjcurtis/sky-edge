from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.constituent_code_add import ConstituentCodeAdd
from ...models.post_response import PostResponse


def _get_kwargs(
    *,
    body: ConstituentCodeAdd | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/constituentcodes",
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

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
    *,
    client: AuthenticatedClient | Client,
    body: ConstituentCodeAdd | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Constituent code (Create)

     Creates a constituent code for a constituent.

    Args:
        body (ConstituentCodeAdd | Unset): Constituent codes define the high-level affiliations
            between constituents and your organization — such as Board member, Vendor, and Volunteer —
            to provide context for why constituents are in the database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
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
    body: ConstituentCodeAdd | Unset = UNSET,
) -> Any | PostResponse | None:
    """Constituent code (Create)

     Creates a constituent code for a constituent.

    Args:
        body (ConstituentCodeAdd | Unset): Constituent codes define the high-level affiliations
            between constituents and your organization — such as Board member, Vendor, and Volunteer —
            to provide context for why constituents are in the database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConstituentCodeAdd | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Constituent code (Create)

     Creates a constituent code for a constituent.

    Args:
        body (ConstituentCodeAdd | Unset): Constituent codes define the high-level affiliations
            between constituents and your organization — such as Board member, Vendor, and Volunteer —
            to provide context for why constituents are in the database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConstituentCodeAdd | Unset = UNSET,
) -> Any | PostResponse | None:
    """Constituent code (Create)

     Creates a constituent code for a constituent.

    Args:
        body (ConstituentCodeAdd | Unset): Constituent codes define the high-level affiliations
            between constituents and your organization — such as Board member, Vendor, and Volunteer —
            to provide context for why constituents are in the database.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

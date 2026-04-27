from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.post_response import PostResponse
from ...models.volunteer_interest_add import VolunteerInterestAdd


def _get_kwargs(
    *,
    body: VolunteerInterestAdd | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/volunteers/interests",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostResponse | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VolunteerInterestAdd | Unset = UNSET,
) -> Response[PostResponse]:
    """Create a volunteer interest (PREVIEW)

     Adds a new interest entry to the specified constituent.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (VolunteerInterestAdd | Unset): Represents a request to add an interest for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse]
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
    body: VolunteerInterestAdd | Unset = UNSET,
) -> PostResponse | None:
    """Create a volunteer interest (PREVIEW)

     Adds a new interest entry to the specified constituent.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (VolunteerInterestAdd | Unset): Represents a request to add an interest for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VolunteerInterestAdd | Unset = UNSET,
) -> Response[PostResponse]:
    """Create a volunteer interest (PREVIEW)

     Adds a new interest entry to the specified constituent.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (VolunteerInterestAdd | Unset): Represents a request to add an interest for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VolunteerInterestAdd | Unset = UNSET,
) -> PostResponse | None:
    """Create a volunteer interest (PREVIEW)

     Adds a new interest entry to the specified constituent.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (VolunteerInterestAdd | Unset): Represents a request to add an interest for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

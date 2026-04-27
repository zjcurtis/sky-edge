from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.opportunity_read import OpportunityRead


def _get_kwargs(
    opportunity_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/opportunities/{opportunity_id}".format(
            opportunity_id=quote(str(opportunity_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OpportunityRead | None:
    if response.status_code == 200:
        response_200 = OpportunityRead.from_dict(response.json())

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
) -> Response[Any | OpportunityRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | OpportunityRead]:
    """Opportunity (Get)

     Returns information about an opportunity.

    <b>Note:</b> This endpoint returns the status property with a latency of about 10 minutes.

    Args:
        opportunity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpportunityRead]
    """

    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | OpportunityRead | None:
    """Opportunity (Get)

     Returns information about an opportunity.

    <b>Note:</b> This endpoint returns the status property with a latency of about 10 minutes.

    Args:
        opportunity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpportunityRead
    """

    return sync_detailed(
        opportunity_id=opportunity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | OpportunityRead]:
    """Opportunity (Get)

     Returns information about an opportunity.

    <b>Note:</b> This endpoint returns the status property with a latency of about 10 minutes.

    Args:
        opportunity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpportunityRead]
    """

    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | OpportunityRead | None:
    """Opportunity (Get)

     Returns information about an opportunity.

    <b>Note:</b> This endpoint returns the status property with a latency of about 10 minutes.

    Args:
        opportunity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpportunityRead
    """

    return (
        await asyncio_detailed(
            opportunity_id=opportunity_id,
            client=client,
        )
    ).parsed

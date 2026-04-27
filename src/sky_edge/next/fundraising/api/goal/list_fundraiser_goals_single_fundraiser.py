from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.api_collection_goal_read import ApiCollectionGoalRead


def _get_kwargs(
    fundraiser_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/fundraisers/{fundraiser_id}/goals".format(
            fundraiser_id=quote(str(fundraiser_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionGoalRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionGoalRead.from_dict(response.json())

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
) -> Response[Any | ApiCollectionGoalRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fundraiser_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiCollectionGoalRead]:
    """Fundraiser goal list (Single fundraiser)

     Returns a list of fundraiser goals for a fundraiser.

    Args:
        fundraiser_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionGoalRead]
    """

    kwargs = _get_kwargs(
        fundraiser_id=fundraiser_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fundraiser_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiCollectionGoalRead | None:
    """Fundraiser goal list (Single fundraiser)

     Returns a list of fundraiser goals for a fundraiser.

    Args:
        fundraiser_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionGoalRead
    """

    return sync_detailed(
        fundraiser_id=fundraiser_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fundraiser_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiCollectionGoalRead]:
    """Fundraiser goal list (Single fundraiser)

     Returns a list of fundraiser goals for a fundraiser.

    Args:
        fundraiser_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionGoalRead]
    """

    kwargs = _get_kwargs(
        fundraiser_id=fundraiser_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fundraiser_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiCollectionGoalRead | None:
    """Fundraiser goal list (Single fundraiser)

     Returns a list of fundraiser goals for a fundraiser.

    Args:
        fundraiser_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionGoalRead
    """

    return (
        await asyncio_detailed(
            fundraiser_id=fundraiser_id,
            client=client,
        )
    ).parsed

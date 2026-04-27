from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.planned_gift_read import PlannedGiftRead
from ...types import Response


def _get_kwargs(
    gift_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/gifts/{gift_id}/plannedgift".format(
            gift_id=quote(str(gift_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PlannedGiftRead | None:
    if response.status_code == 200:
        response_200 = PlannedGiftRead.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PlannedGiftRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PlannedGiftRead]:
    """Gets a planned gift by its identifier. (PREVIEW)

     Returns the details of a planned gift including vehicle-specific fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlannedGiftRead]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PlannedGiftRead | None:
    """Gets a planned gift by its identifier. (PREVIEW)

     Returns the details of a planned gift including vehicle-specific fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlannedGiftRead
    """

    return sync_detailed(
        gift_id=gift_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[PlannedGiftRead]:
    """Gets a planned gift by its identifier. (PREVIEW)

     Returns the details of a planned gift including vehicle-specific fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlannedGiftRead]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> PlannedGiftRead | None:
    """Gets a planned gift by its identifier. (PREVIEW)

     Returns the details of a planned gift including vehicle-specific fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlannedGiftRead
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.sell_stock_gift_400_response_types_problem_details import SellStockGift400ResponseTypesProblemDetails
from ...models.sold_stock_details_edit import SoldStockDetailsEdit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    gift_id: str,
    *,
    body: SoldStockDetailsEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/gifts/{gift_id}/stock/sell".format(
            gift_id=quote(str(gift_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = SellStockGift400ResponseTypesProblemDetails.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails]:
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
    body: SoldStockDetailsEdit | Unset = UNSET,
) -> Response[Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails]:
    """Sell a stock gift (PREVIEW)

     This updates a stock gift to sold with the given details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (SoldStockDetailsEdit | Unset): Represents the details for selling a stock gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SoldStockDetailsEdit | Unset = UNSET,
) -> Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails | None:
    """Sell a stock gift (PREVIEW)

     This updates a stock gift to sold with the given details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (SoldStockDetailsEdit | Unset): Represents the details for selling a stock gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails
    """

    return sync_detailed(
        gift_id=gift_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SoldStockDetailsEdit | Unset = UNSET,
) -> Response[Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails]:
    """Sell a stock gift (PREVIEW)

     This updates a stock gift to sold with the given details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (SoldStockDetailsEdit | Unset): Represents the details for selling a stock gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SoldStockDetailsEdit | Unset = UNSET,
) -> Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails | None:
    """Sell a stock gift (PREVIEW)

     This updates a stock gift to sold with the given details.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (SoldStockDetailsEdit | Unset): Represents the details for selling a stock gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | SellStockGift400ResponseTypesProblemDetails
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gift_add import GiftAdd
from ...models.gift_add_result import GiftAddResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GiftAdd | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["default_constituency"] = default_constituency

    params["default_soft_credits"] = default_soft_credits

    params["default_fundraiser_credits"] = default_fundraiser_credits

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/gifts",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GiftAddResult | None:
    if response.status_code == 200:
        response_200 = GiftAddResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GiftAddResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GiftAdd | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> Response[GiftAddResult]:
    """Create a gift. (PREVIEW)

     Supported gift types include One-time, pledge, pledge payment, recurring, stock, gift-in-kind, and
    other.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (GiftAdd | Unset): A new gift to be added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GiftAddResult]
    """

    kwargs = _get_kwargs(
        body=body,
        default_constituency=default_constituency,
        default_soft_credits=default_soft_credits,
        default_fundraiser_credits=default_fundraiser_credits,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: GiftAdd | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> GiftAddResult | None:
    """Create a gift. (PREVIEW)

     Supported gift types include One-time, pledge, pledge payment, recurring, stock, gift-in-kind, and
    other.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (GiftAdd | Unset): A new gift to be added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GiftAddResult
    """

    return sync_detailed(
        client=client,
        body=body,
        default_constituency=default_constituency,
        default_soft_credits=default_soft_credits,
        default_fundraiser_credits=default_fundraiser_credits,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GiftAdd | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> Response[GiftAddResult]:
    """Create a gift. (PREVIEW)

     Supported gift types include One-time, pledge, pledge payment, recurring, stock, gift-in-kind, and
    other.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (GiftAdd | Unset): A new gift to be added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GiftAddResult]
    """

    kwargs = _get_kwargs(
        body=body,
        default_constituency=default_constituency,
        default_soft_credits=default_soft_credits,
        default_fundraiser_credits=default_fundraiser_credits,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: GiftAdd | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> GiftAddResult | None:
    """Create a gift. (PREVIEW)

     Supported gift types include One-time, pledge, pledge payment, recurring, stock, gift-in-kind, and
    other.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (GiftAdd | Unset): A new gift to be added.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GiftAddResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            default_constituency=default_constituency,
            default_soft_credits=default_soft_credits,
            default_fundraiser_credits=default_fundraiser_credits,
        )
    ).parsed

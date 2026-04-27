from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.amend_gift_result import AmendGiftResult
from ...models.edit_payment_information import EditPaymentInformation


def _get_kwargs(
    gift_id: str,
    *,
    body: EditPaymentInformation | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/recurringgifts/{gift_id}/amendments/paymentinformation".format(
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
) -> AmendGiftResult | None:
    if response.status_code == 200:
        response_200 = AmendGiftResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AmendGiftResult]:
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
    body: EditPaymentInformation | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[AmendGiftResult]:
    """Edit payment information for a recurring gift (PREVIEW)

     Edits payment information for a recurring gift paid by credit card.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        if_match (str | Unset):
        body (EditPaymentInformation | Unset): Information to edit payment information for a gift

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AmendGiftResult]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditPaymentInformation | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> AmendGiftResult | None:
    """Edit payment information for a recurring gift (PREVIEW)

     Edits payment information for a recurring gift paid by credit card.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        if_match (str | Unset):
        body (EditPaymentInformation | Unset): Information to edit payment information for a gift

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AmendGiftResult
    """

    return sync_detailed(
        gift_id=gift_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditPaymentInformation | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> Response[AmendGiftResult]:
    """Edit payment information for a recurring gift (PREVIEW)

     Edits payment information for a recurring gift paid by credit card.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        if_match (str | Unset):
        body (EditPaymentInformation | Unset): Information to edit payment information for a gift

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AmendGiftResult]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EditPaymentInformation | Unset = UNSET,
    if_match: str | Unset = UNSET,
) -> AmendGiftResult | None:
    """Edit payment information for a recurring gift (PREVIEW)

     Edits payment information for a recurring gift paid by credit card.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        if_match (str | Unset):
        body (EditPaymentInformation | Unset): Information to edit payment information for a gift

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AmendGiftResult
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed

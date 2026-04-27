from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    gift_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/gifts/{gift_id}".format(
            gift_id=quote(str(gift_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 409:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
) -> Response[Any]:
    """Gift (Delete)

     Deletes a gift.
    If a gift was added in database view or added through the API with the <code>is_manual</code> flag
    set to true, you can only delete it if it is a recurring gift, recurring gift payment, or pledge.
    You can delete gifts added via web view except for any recurring gift payment.
    Recurring gifts added via web view cannot be deleted if their current status is Active or Held.
    Pledge gifts added via web view or added through the API with the <code>is_manual</code> flag set to
    false cannot be deleted if their payment method is Credit card or Direct debit.
    Regardless of type, you can’t delete a gift if it has:
    <ul><li>claimed Gift Aid</li><li>a payment with a live transaction ID</li><li>a GL distribution
    record</li><li>an adjustment</li><li>a matching gift</li><li>a pledge payment record or an
    uncommitted pledge payment in a batch</li><li>a recurring gift payment record or an uncommitted
    recurring gift payment in a batch</li><li>a write-off</li><li>receipt history</li><li>a receipt
    status of Receipted</li></ul>

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Gift (Delete)

     Deletes a gift.
    If a gift was added in database view or added through the API with the <code>is_manual</code> flag
    set to true, you can only delete it if it is a recurring gift, recurring gift payment, or pledge.
    You can delete gifts added via web view except for any recurring gift payment.
    Recurring gifts added via web view cannot be deleted if their current status is Active or Held.
    Pledge gifts added via web view or added through the API with the <code>is_manual</code> flag set to
    false cannot be deleted if their payment method is Credit card or Direct debit.
    Regardless of type, you can’t delete a gift if it has:
    <ul><li>claimed Gift Aid</li><li>a payment with a live transaction ID</li><li>a GL distribution
    record</li><li>an adjustment</li><li>a matching gift</li><li>a pledge payment record or an
    uncommitted pledge payment in a batch</li><li>a recurring gift payment record or an uncommitted
    recurring gift payment in a batch</li><li>a write-off</li><li>receipt history</li><li>a receipt
    status of Receipted</li></ul>

    Args:
        gift_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

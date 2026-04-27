from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pledge_installments_add import PledgeInstallmentsAdd
from ...models.pledge_installments_add_result import PledgeInstallmentsAddResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    gift_id: str,
    *,
    body: PledgeInstallmentsAdd | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/gifts/{gift_id}/installments".format(
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
) -> PledgeInstallmentsAddResult | None:
    if response.status_code == 200:
        response_200 = PledgeInstallmentsAddResult.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PledgeInstallmentsAddResult]:
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
    body: PledgeInstallmentsAdd | Unset = UNSET,
) -> Response[PledgeInstallmentsAddResult]:
    """Add pledge installments (PREVIEW)

     This adds installments to an existing pledge gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PledgeInstallmentsAdd | Unset): Adds multiple pledge installments to a pledge gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PledgeInstallmentsAddResult]
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
    body: PledgeInstallmentsAdd | Unset = UNSET,
) -> PledgeInstallmentsAddResult | None:
    """Add pledge installments (PREVIEW)

     This adds installments to an existing pledge gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PledgeInstallmentsAdd | Unset): Adds multiple pledge installments to a pledge gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PledgeInstallmentsAddResult
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
    body: PledgeInstallmentsAdd | Unset = UNSET,
) -> Response[PledgeInstallmentsAddResult]:
    """Add pledge installments (PREVIEW)

     This adds installments to an existing pledge gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PledgeInstallmentsAdd | Unset): Adds multiple pledge installments to a pledge gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PledgeInstallmentsAddResult]
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
    body: PledgeInstallmentsAdd | Unset = UNSET,
) -> PledgeInstallmentsAddResult | None:
    """Add pledge installments (PREVIEW)

     This adds installments to an existing pledge gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PledgeInstallmentsAdd | Unset): Adds multiple pledge installments to a pledge gift.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PledgeInstallmentsAddResult
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
            body=body,
        )
    ).parsed

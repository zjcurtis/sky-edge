from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pledge_installments_add import PledgeInstallmentsAdd
from ...models.pledge_schedule import PledgeSchedule
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PledgeSchedule | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/gifts/generateinstallments",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PledgeInstallmentsAdd | None:
    if response.status_code == 200:
        response_200 = PledgeInstallmentsAdd.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PledgeInstallmentsAdd]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PledgeSchedule | Unset = UNSET,
) -> Response[PledgeInstallmentsAdd]:
    """Generate pledge installments from schedule (PREVIEW)

     This generates the installments for a given schedule.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (PledgeSchedule | Unset): Represents a pledge schedule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PledgeInstallmentsAdd]
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
    body: PledgeSchedule | Unset = UNSET,
) -> PledgeInstallmentsAdd | None:
    """Generate pledge installments from schedule (PREVIEW)

     This generates the installments for a given schedule.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (PledgeSchedule | Unset): Represents a pledge schedule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PledgeInstallmentsAdd
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PledgeSchedule | Unset = UNSET,
) -> Response[PledgeInstallmentsAdd]:
    """Generate pledge installments from schedule (PREVIEW)

     This generates the installments for a given schedule.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (PledgeSchedule | Unset): Represents a pledge schedule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PledgeInstallmentsAdd]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PledgeSchedule | Unset = UNSET,
) -> PledgeInstallmentsAdd | None:
    """Generate pledge installments from schedule (PREVIEW)

     This generates the installments for a given schedule.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        body (PledgeSchedule | Unset): Represents a pledge schedule

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PledgeInstallmentsAdd
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

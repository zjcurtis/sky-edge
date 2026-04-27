from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.planned_gift_beneficiary_add import PlannedGiftBeneficiaryAdd
from ...models.planned_gift_beneficiary_created import PlannedGiftBeneficiaryCreated
from ...types import UNSET, Response, Unset


def _get_kwargs(
    gift_id: str,
    *,
    body: PlannedGiftBeneficiaryAdd | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/gifts/{gift_id}/plannedgift/beneficiaries".format(
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
) -> PlannedGiftBeneficiaryCreated | None:
    if response.status_code == 200:
        response_200 = PlannedGiftBeneficiaryCreated.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PlannedGiftBeneficiaryCreated]:
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
    body: PlannedGiftBeneficiaryAdd | Unset = UNSET,
) -> Response[PlannedGiftBeneficiaryCreated]:
    """Adds a new beneficiary to a planned gift. (PREVIEW)

     Creates a new beneficiary record and associates it with the specified planned gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PlannedGiftBeneficiaryAdd | Unset): Model for adding a new planned gift beneficiary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlannedGiftBeneficiaryCreated]
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
    body: PlannedGiftBeneficiaryAdd | Unset = UNSET,
) -> PlannedGiftBeneficiaryCreated | None:
    """Adds a new beneficiary to a planned gift. (PREVIEW)

     Creates a new beneficiary record and associates it with the specified planned gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PlannedGiftBeneficiaryAdd | Unset): Model for adding a new planned gift beneficiary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlannedGiftBeneficiaryCreated
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
    body: PlannedGiftBeneficiaryAdd | Unset = UNSET,
) -> Response[PlannedGiftBeneficiaryCreated]:
    """Adds a new beneficiary to a planned gift. (PREVIEW)

     Creates a new beneficiary record and associates it with the specified planned gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PlannedGiftBeneficiaryAdd | Unset): Model for adding a new planned gift beneficiary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlannedGiftBeneficiaryCreated]
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
    body: PlannedGiftBeneficiaryAdd | Unset = UNSET,
) -> PlannedGiftBeneficiaryCreated | None:
    """Adds a new beneficiary to a planned gift. (PREVIEW)

     Creates a new beneficiary record and associates it with the specified planned gift.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        body (PlannedGiftBeneficiaryAdd | Unset): Model for adding a new planned gift beneficiary.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlannedGiftBeneficiaryCreated
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
            body=body,
        )
    ).parsed

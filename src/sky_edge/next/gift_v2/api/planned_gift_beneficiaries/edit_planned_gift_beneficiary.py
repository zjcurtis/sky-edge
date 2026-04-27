from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.planned_gift_beneficiary_edit import PlannedGiftBeneficiaryEdit


def _get_kwargs(
    gift_id: str,
    beneficiary_id: str,
    *,
    body: PlannedGiftBeneficiaryEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/gifts/{gift_id}/plannedgift/beneficiaries/{beneficiary_id}".format(
            gift_id=quote(str(gift_id), safe=""),
            beneficiary_id=quote(str(beneficiary_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gift_id: str,
    beneficiary_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlannedGiftBeneficiaryEdit | Unset = UNSET,
) -> Response[Any]:
    """Edits an existing beneficiary on a planned gift. (PREVIEW)

     Updates the specified fields on an existing planned gift beneficiary. Only the provided fields are
    updated; omitted fields retain their current values.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        beneficiary_id (str):
        body (PlannedGiftBeneficiaryEdit | Unset): Model for editing an existing planned gift
            beneficiary. All fields are optional for PATCH semantics.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        beneficiary_id=beneficiary_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    gift_id: str,
    beneficiary_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlannedGiftBeneficiaryEdit | Unset = UNSET,
) -> Response[Any]:
    """Edits an existing beneficiary on a planned gift. (PREVIEW)

     Updates the specified fields on an existing planned gift beneficiary. Only the provided fields are
    updated; omitted fields retain their current values.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        gift_id (str):
        beneficiary_id (str):
        body (PlannedGiftBeneficiaryEdit | Unset): Model for editing an existing planned gift
            beneficiary. All fields are optional for PATCH semantics.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        beneficiary_id=beneficiary_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

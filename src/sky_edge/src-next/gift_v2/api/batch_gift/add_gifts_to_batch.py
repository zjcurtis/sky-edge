from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_edit_batch_gift_400_response_types_problem_details import (
    AddEditBatchGift400ResponseTypesProblemDetails,
)
from ...models.add_gifts_to_batch_result import AddGiftsToBatchResult
from ...models.batch_gift_add_with_tribute_lookup import BatchGiftAddWithTributeLookup
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    batch_id: str,
    *,
    body: list[BatchGiftAddWithTributeLookup] | Unset = UNSET,
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
        "url": "/v2/batchgifts/{batch_id}".format(
            batch_id=quote(str(batch_id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for body_item_data in body:
            body_item = body_item_data.to_dict()
            _kwargs["json"].append(body_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = AddGiftsToBatchResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddEditBatchGift400ResponseTypesProblemDetails.from_dict(response.json())

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
) -> Response[AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BatchGiftAddWithTributeLookup] | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> Response[AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails]:
    """Add Gifts to Batch (PREVIEW)

     Add multiple gifts to an existing unapproved batch

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_id (str):
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (list[BatchGiftAddWithTributeLookup] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
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
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BatchGiftAddWithTributeLookup] | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails | None:
    """Add Gifts to Batch (PREVIEW)

     Add multiple gifts to an existing unapproved batch

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_id (str):
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (list[BatchGiftAddWithTributeLookup] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        body=body,
        default_constituency=default_constituency,
        default_soft_credits=default_soft_credits,
        default_fundraiser_credits=default_fundraiser_credits,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BatchGiftAddWithTributeLookup] | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> Response[AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails]:
    """Add Gifts to Batch (PREVIEW)

     Add multiple gifts to an existing unapproved batch

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_id (str):
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (list[BatchGiftAddWithTributeLookup] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
        default_constituency=default_constituency,
        default_soft_credits=default_soft_credits,
        default_fundraiser_credits=default_fundraiser_credits,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: list[BatchGiftAddWithTributeLookup] | Unset = UNSET,
    default_constituency: bool | Unset = UNSET,
    default_soft_credits: bool | Unset = UNSET,
    default_fundraiser_credits: bool | Unset = UNSET,
) -> AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails | None:
    """Add Gifts to Batch (PREVIEW)

     Add multiple gifts to an existing unapproved batch

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_id (str):
        default_constituency (bool | Unset):
        default_soft_credits (bool | Unset):
        default_fundraiser_credits (bool | Unset):
        body (list[BatchGiftAddWithTributeLookup] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddEditBatchGift400ResponseTypesProblemDetails | AddGiftsToBatchResult | Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            body=body,
            default_constituency=default_constituency,
            default_soft_credits=default_soft_credits,
            default_fundraiser_credits=default_fundraiser_credits,
        )
    ).parsed

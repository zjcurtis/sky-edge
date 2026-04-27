from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.add_edit_batch_gift_400_response_types_problem_details import (
    AddEditBatchGift400ResponseTypesProblemDetails,
)
from ...models.batch_gift_edit import BatchGiftEdit
from ...models.gift_validation_errors import GiftValidationErrors
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    batch_gift_id: str,
    *,
    body: BatchGiftEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v2/batchgifts/{batch_gift_id}".format(
            batch_gift_id=quote(str(batch_gift_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AddEditBatchGift400ResponseTypesProblemDetails
    | Any
    | GiftValidationErrors
    | ProblemDetails
    | None
):
    if response.status_code == 200:
        response_200 = GiftValidationErrors.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddEditBatchGift400ResponseTypesProblemDetails.from_dict(
            response.json()
        )

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
) -> Response[
    AddEditBatchGift400ResponseTypesProblemDetails
    | Any
    | GiftValidationErrors
    | ProblemDetails
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BatchGiftEdit | Unset = UNSET,
) -> Response[
    AddEditBatchGift400ResponseTypesProblemDetails
    | Any
    | GiftValidationErrors
    | ProblemDetails
]:
    """Edit Batch Gift (PREVIEW)

     Updates a batch gift

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):
        body (BatchGiftEdit | Unset): A batch gift to be edited, only including fields that can be
            changed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddEditBatchGift400ResponseTypesProblemDetails | Any | GiftValidationErrors | ProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_gift_id=batch_gift_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BatchGiftEdit | Unset = UNSET,
) -> (
    AddEditBatchGift400ResponseTypesProblemDetails
    | Any
    | GiftValidationErrors
    | ProblemDetails
    | None
):
    """Edit Batch Gift (PREVIEW)

     Updates a batch gift

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):
        body (BatchGiftEdit | Unset): A batch gift to be edited, only including fields that can be
            changed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddEditBatchGift400ResponseTypesProblemDetails | Any | GiftValidationErrors | ProblemDetails
    """

    return sync_detailed(
        batch_gift_id=batch_gift_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BatchGiftEdit | Unset = UNSET,
) -> Response[
    AddEditBatchGift400ResponseTypesProblemDetails
    | Any
    | GiftValidationErrors
    | ProblemDetails
]:
    """Edit Batch Gift (PREVIEW)

     Updates a batch gift

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):
        body (BatchGiftEdit | Unset): A batch gift to be edited, only including fields that can be
            changed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddEditBatchGift400ResponseTypesProblemDetails | Any | GiftValidationErrors | ProblemDetails]
    """

    kwargs = _get_kwargs(
        batch_gift_id=batch_gift_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BatchGiftEdit | Unset = UNSET,
) -> (
    AddEditBatchGift400ResponseTypesProblemDetails
    | Any
    | GiftValidationErrors
    | ProblemDetails
    | None
):
    """Edit Batch Gift (PREVIEW)

     Updates a batch gift

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        batch_gift_id (str):
        body (BatchGiftEdit | Unset): A batch gift to be edited, only including fields that can be
            changed

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddEditBatchGift400ResponseTypesProblemDetails | Any | GiftValidationErrors | ProblemDetails
    """

    return (
        await asyncio_detailed(
            batch_gift_id=batch_gift_id,
            client=client,
            body=body,
        )
    ).parsed

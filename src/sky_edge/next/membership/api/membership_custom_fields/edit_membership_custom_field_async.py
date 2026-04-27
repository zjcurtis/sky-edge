from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.bad_request_400_response_types import BadRequest400ResponseTypes
from ...models.custom_field_update import CustomFieldUpdate
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    member_junction_id: str,
    custom_field_id: str,
    *,
    body: CustomFieldUpdate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/memberships/{member_junction_id}/customfield/{custom_field_id}".format(
            member_junction_id=quote(str(member_junction_id), safe=""),
            custom_field_id=quote(str(custom_field_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequest400ResponseTypes | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = BadRequest400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

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
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    member_junction_id: str,
    custom_field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldUpdate | Unset = UNSET,
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails]:
    """Edit membership custom field (PREVIEW)

     Edit membership custom field.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        custom_field_id (str):
        body (CustomFieldUpdate | Unset): While records provide many fields to track information,
            organizations often require additional details. To track this specialized information, use
            custom fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
        custom_field_id=custom_field_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_junction_id: str,
    custom_field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldUpdate | Unset = UNSET,
) -> Any | BadRequest400ResponseTypes | ProblemDetails | None:
    """Edit membership custom field (PREVIEW)

     Edit membership custom field.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        custom_field_id (str):
        body (CustomFieldUpdate | Unset): While records provide many fields to track information,
            organizations often require additional details. To track this specialized information, use
            custom fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | ProblemDetails
    """

    return sync_detailed(
        member_junction_id=member_junction_id,
        custom_field_id=custom_field_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    member_junction_id: str,
    custom_field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldUpdate | Unset = UNSET,
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails]:
    """Edit membership custom field (PREVIEW)

     Edit membership custom field.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        custom_field_id (str):
        body (CustomFieldUpdate | Unset): While records provide many fields to track information,
            organizations often require additional details. To track this specialized information, use
            custom fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
        custom_field_id=custom_field_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_junction_id: str,
    custom_field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldUpdate | Unset = UNSET,
) -> Any | BadRequest400ResponseTypes | ProblemDetails | None:
    """Edit membership custom field (PREVIEW)

     Edit membership custom field.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        custom_field_id (str):
        body (CustomFieldUpdate | Unset): While records provide many fields to track information,
            organizations often require additional details. To track this specialized information, use
            custom fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | ProblemDetails
    """

    return (
        await asyncio_detailed(
            member_junction_id=member_junction_id,
            custom_field_id=custom_field_id,
            client=client,
            body=body,
        )
    ).parsed

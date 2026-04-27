from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.edit_channel_solicit_code_assignments_channel import (
    EditChannelSolicitCodeAssignmentsChannel,
)
from ...models.edit_solicit_code_assignments_request import (
    EditSolicitCodeAssignmentsRequest,
)
from ...models.problem_details import ProblemDetails
from ...models.update_solicit_code_assignments_400_response_types import (
    UpdateSolicitCodeAssignments400ResponseTypes,
)


def _get_kwargs(
    channel: EditChannelSolicitCodeAssignmentsChannel,
    *,
    body: EditSolicitCodeAssignmentsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/configuration/channels/{channel}/solicitcodeassignments".format(
            channel=quote(str(channel), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = UpdateSolicitCodeAssignments400ResponseTypes.from_dict(
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
) -> Response[Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel: EditChannelSolicitCodeAssignmentsChannel,
    *,
    client: AuthenticatedClient | Client,
    body: EditSolicitCodeAssignmentsRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes]:
    """Edit channel solicit code assignments.

     Edit channel solicit code assignments for the given channel and optional category.

    Args:
        channel (EditChannelSolicitCodeAssignmentsChannel): Consent
            channels<p>Members:</p><ul><li><i>Email</i> - Email</li><li><i>Mail</i> -
            Mail</li><li><i>SMS</i> - SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i> -
            AutoPhone</li><li><i>Social</i> - Social media</li><li><i>DataProcessing</i> - Data
            processing</li><li><i>Other</i> - Other</li></ul>
        body (EditSolicitCodeAssignmentsRequest | Unset): Represents a request to edit solicit
            code assignments for a specific category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes]
    """

    kwargs = _get_kwargs(
        channel=channel,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel: EditChannelSolicitCodeAssignmentsChannel,
    *,
    client: AuthenticatedClient | Client,
    body: EditSolicitCodeAssignmentsRequest | Unset = UNSET,
) -> Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes | None:
    """Edit channel solicit code assignments.

     Edit channel solicit code assignments for the given channel and optional category.

    Args:
        channel (EditChannelSolicitCodeAssignmentsChannel): Consent
            channels<p>Members:</p><ul><li><i>Email</i> - Email</li><li><i>Mail</i> -
            Mail</li><li><i>SMS</i> - SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i> -
            AutoPhone</li><li><i>Social</i> - Social media</li><li><i>DataProcessing</i> - Data
            processing</li><li><i>Other</i> - Other</li></ul>
        body (EditSolicitCodeAssignmentsRequest | Unset): Represents a request to edit solicit
            code assignments for a specific category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes
    """

    return sync_detailed(
        channel=channel,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    channel: EditChannelSolicitCodeAssignmentsChannel,
    *,
    client: AuthenticatedClient | Client,
    body: EditSolicitCodeAssignmentsRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes]:
    """Edit channel solicit code assignments.

     Edit channel solicit code assignments for the given channel and optional category.

    Args:
        channel (EditChannelSolicitCodeAssignmentsChannel): Consent
            channels<p>Members:</p><ul><li><i>Email</i> - Email</li><li><i>Mail</i> -
            Mail</li><li><i>SMS</i> - SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i> -
            AutoPhone</li><li><i>Social</i> - Social media</li><li><i>DataProcessing</i> - Data
            processing</li><li><i>Other</i> - Other</li></ul>
        body (EditSolicitCodeAssignmentsRequest | Unset): Represents a request to edit solicit
            code assignments for a specific category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes]
    """

    kwargs = _get_kwargs(
        channel=channel,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel: EditChannelSolicitCodeAssignmentsChannel,
    *,
    client: AuthenticatedClient | Client,
    body: EditSolicitCodeAssignmentsRequest | Unset = UNSET,
) -> Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes | None:
    """Edit channel solicit code assignments.

     Edit channel solicit code assignments for the given channel and optional category.

    Args:
        channel (EditChannelSolicitCodeAssignmentsChannel): Consent
            channels<p>Members:</p><ul><li><i>Email</i> - Email</li><li><i>Mail</i> -
            Mail</li><li><i>SMS</i> - SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i> -
            AutoPhone</li><li><i>Social</i> - Social media</li><li><i>DataProcessing</i> - Data
            processing</li><li><i>Other</i> - Other</li></ul>
        body (EditSolicitCodeAssignmentsRequest | Unset): Represents a request to edit solicit
            code assignments for a specific category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | UpdateSolicitCodeAssignments400ResponseTypes
    """

    return (
        await asyncio_detailed(
            channel=channel,
            client=client,
            body=body,
        )
    ).parsed

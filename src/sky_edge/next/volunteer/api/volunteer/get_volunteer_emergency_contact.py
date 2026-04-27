from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.emergency_contact import EmergencyContact
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    constituent_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/volunteers/{constituent_id}/emergencycontact".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmergencyContact | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = EmergencyContact.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EmergencyContact | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EmergencyContact | ProblemDetails]:
    """Get emergency contact (PREVIEW)

     Returns the emergency contact information for the specified volunteer/constituent. Returns an empty
    response if the constituent has no emergency contact data.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmergencyContact | ProblemDetails]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EmergencyContact | ProblemDetails | None:
    """Get emergency contact (PREVIEW)

     Returns the emergency contact information for the specified volunteer/constituent. Returns an empty
    response if the constituent has no emergency contact data.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmergencyContact | ProblemDetails
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EmergencyContact | ProblemDetails]:
    """Get emergency contact (PREVIEW)

     Returns the emergency contact information for the specified volunteer/constituent. Returns an empty
    response if the constituent has no emergency contact data.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmergencyContact | ProblemDetails]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EmergencyContact | ProblemDetails | None:
    """Get emergency contact (PREVIEW)

     Returns the emergency contact information for the specified volunteer/constituent. Returns an empty
    response if the constituent has no emergency contact data.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmergencyContact | ProblemDetails
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
        )
    ).parsed

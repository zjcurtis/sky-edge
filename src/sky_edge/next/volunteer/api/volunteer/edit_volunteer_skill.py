from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.problem_details import ProblemDetails
from ...models.volunteer_skill_update import VolunteerSkillUpdate


def _get_kwargs(
    volunteer_skill_id: str,
    *,
    body: VolunteerSkillUpdate | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/volunteers/skills/{volunteer_skill_id}".format(
            volunteer_skill_id=quote(str(volunteer_skill_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    volunteer_skill_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VolunteerSkillUpdate | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Update a volunteer skill (PREVIEW)

     Updates an existing volunteer skill/experience entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        volunteer_skill_id (str):
        body (VolunteerSkillUpdate | Unset): Represents volunteer skill update information for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        volunteer_skill_id=volunteer_skill_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    volunteer_skill_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VolunteerSkillUpdate | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Update a volunteer skill (PREVIEW)

     Updates an existing volunteer skill/experience entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        volunteer_skill_id (str):
        body (VolunteerSkillUpdate | Unset): Represents volunteer skill update information for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        volunteer_skill_id=volunteer_skill_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    volunteer_skill_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VolunteerSkillUpdate | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Update a volunteer skill (PREVIEW)

     Updates an existing volunteer skill/experience entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        volunteer_skill_id (str):
        body (VolunteerSkillUpdate | Unset): Represents volunteer skill update information for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        volunteer_skill_id=volunteer_skill_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    volunteer_skill_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: VolunteerSkillUpdate | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Update a volunteer skill (PREVIEW)

     Updates an existing volunteer skill/experience entry.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        volunteer_skill_id (str):
        body (VolunteerSkillUpdate | Unset): Represents volunteer skill update information for a
            volunteer

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            volunteer_skill_id=volunteer_skill_id,
            client=client,
            body=body,
        )
    ).parsed

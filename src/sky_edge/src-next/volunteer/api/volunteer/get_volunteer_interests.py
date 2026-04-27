from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_volunteer_interests_response import GetVolunteerInterestsResponse
from ...types import Response


def _get_kwargs(
    constituent_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/volunteers/{constituent_id}/interests".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetVolunteerInterestsResponse | None:
    if response.status_code == 200:
        response_200 = GetVolunteerInterestsResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetVolunteerInterestsResponse]:
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
) -> Response[GetVolunteerInterestsResponse]:
    """List volunteer interests (PREVIEW)

     Returns a list of interests for the specified volunteer/constituent

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVolunteerInterestsResponse]
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
) -> GetVolunteerInterestsResponse | None:
    """List volunteer interests (PREVIEW)

     Returns a list of interests for the specified volunteer/constituent

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVolunteerInterestsResponse
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetVolunteerInterestsResponse]:
    """List volunteer interests (PREVIEW)

     Returns a list of interests for the specified volunteer/constituent

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetVolunteerInterestsResponse]
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
) -> GetVolunteerInterestsResponse | None:
    """List volunteer interests (PREVIEW)

     Returns a list of interests for the specified volunteer/constituent

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetVolunteerInterestsResponse
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
        )
    ).parsed

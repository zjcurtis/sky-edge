from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_400_response_types import BadRequest400ResponseTypes
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    member_junction_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/memberships/{member_junction_id}".format(
            member_junction_id=quote(str(member_junction_id), safe=""),
        ),
    }

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
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails]:
    """Delete a membership (PREVIEW)

     Deletes a membership.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | BadRequest400ResponseTypes | ProblemDetails | None:
    """Delete a membership (PREVIEW)

     Deletes a membership.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | ProblemDetails
    """

    return sync_detailed(
        member_junction_id=member_junction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails]:
    """Delete a membership (PREVIEW)

     Deletes a membership.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | BadRequest400ResponseTypes | ProblemDetails | None:
    """Delete a membership (PREVIEW)

     Deletes a membership.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | ProblemDetails
    """

    return (
        await asyncio_detailed(
            member_junction_id=member_junction_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_consents_multiple_constituents_400_response_types import (
    CreateConsentsMultipleConstituents400ResponseTypes,
)
from ...models.create_constituent_consents_request import CreateConstituentConsentsRequest
from ...models.identifier_collection import IdentifierCollection
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateConstituentConsentsRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/constituents/consents",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = IdentifierCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateConsentsMultipleConstituents400ResponseTypes.from_dict(response.json())

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
) -> Response[Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConstituentConsentsRequest | Unset = UNSET,
) -> Response[Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails]:
    """Create consents for one or more constituents.

     Create one or more consents for one or more constituents.

    Args:
        body (CreateConstituentConsentsRequest | Unset): Model used by SkyApi to create consent
            records for multiple constituents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConstituentConsentsRequest | Unset = UNSET,
) -> Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails | None:
    """Create consents for one or more constituents.

     Create one or more consents for one or more constituents.

    Args:
        body (CreateConstituentConsentsRequest | Unset): Model used by SkyApi to create consent
            records for multiple constituents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConstituentConsentsRequest | Unset = UNSET,
) -> Response[Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails]:
    """Create consents for one or more constituents.

     Create one or more consents for one or more constituents.

    Args:
        body (CreateConstituentConsentsRequest | Unset): Model used by SkyApi to create consent
            records for multiple constituents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConstituentConsentsRequest | Unset = UNSET,
) -> Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails | None:
    """Create consents for one or more constituents.

     Create one or more consents for one or more constituents.

    Args:
        body (CreateConstituentConsentsRequest | Unset): Model used by SkyApi to create consent
            records for multiple constituents

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateConsentsMultipleConstituents400ResponseTypes | IdentifierCollection | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

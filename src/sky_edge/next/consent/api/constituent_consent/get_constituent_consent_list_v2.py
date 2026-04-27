from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.consent_list_options import ConsentListOptions
from ...models.constituent_consent_read_collection import (
    ConstituentConsentReadCollection,
)
from ...models.get_consent_list_400_response_types import GetConsentList400ResponseTypes


def _get_kwargs(
    *,
    body: ConsentListOptions | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/constituents/consentlist",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes | None:
    if response.status_code == 200:
        response_200 = ConstituentConsentReadCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetConsentList400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentListOptions | Unset = UNSET,
) -> Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]:
    """Get constituent consent list (V2).

     Get a list of constituent consents using POST to work around query string length limitations.

    Args:
        body (ConsentListOptions | Unset): Optional Get constituent consents filters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]
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
    body: ConsentListOptions | Unset = UNSET,
) -> Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes | None:
    """Get constituent consent list (V2).

     Get a list of constituent consents using POST to work around query string length limitations.

    Args:
        body (ConsentListOptions | Unset): Optional Get constituent consents filters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentListOptions | Unset = UNSET,
) -> Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]:
    """Get constituent consent list (V2).

     Get a list of constituent consents using POST to work around query string length limitations.

    Args:
        body (ConsentListOptions | Unset): Optional Get constituent consents filters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentListOptions | Unset = UNSET,
) -> Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes | None:
    """Get constituent consent list (V2).

     Get a list of constituent consents using POST to work around query string length limitations.

    Args:
        body (ConsentListOptions | Unset): Optional Get constituent consents filters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

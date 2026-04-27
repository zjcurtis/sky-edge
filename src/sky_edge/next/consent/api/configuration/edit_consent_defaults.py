from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.consent_defaults import ConsentDefaults


def _get_kwargs(
    *,
    body: ConsentDefaults | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/configuration/defaults",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ConsentDefaults | None:
    if response.status_code == 200:
        response_200 = ConsentDefaults.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConsentDefaults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentDefaults | Unset = UNSET,
) -> Response[ConsentDefaults]:
    """Edit consent defaults.

     Edit the default consent statement and/or privacy policy.

    Args:
        body (ConsentDefaults | Unset): Defines model to represent consent defaults.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsentDefaults]
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
    body: ConsentDefaults | Unset = UNSET,
) -> ConsentDefaults | None:
    """Edit consent defaults.

     Edit the default consent statement and/or privacy policy.

    Args:
        body (ConsentDefaults | Unset): Defines model to represent consent defaults.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsentDefaults
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentDefaults | Unset = UNSET,
) -> Response[ConsentDefaults]:
    """Edit consent defaults.

     Edit the default consent statement and/or privacy policy.

    Args:
        body (ConsentDefaults | Unset): Defines model to represent consent defaults.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsentDefaults]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentDefaults | Unset = UNSET,
) -> ConsentDefaults | None:
    """Edit consent defaults.

     Edit the default consent statement and/or privacy policy.

    Args:
        body (ConsentDefaults | Unset): Defines model to represent consent defaults.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsentDefaults
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

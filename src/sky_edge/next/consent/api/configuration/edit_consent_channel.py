from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.consent_channel_write import ConsentChannelWrite
from ...models.consent_defaults import ConsentDefaults
from ...models.edit_consent_channel_400_response_types import (
    EditConsentChannel400ResponseTypes,
)


def _get_kwargs(
    channel: str,
    *,
    body: ConsentChannelWrite | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/configuration/channels/{channel}".format(
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
) -> ConsentDefaults | EditConsentChannel400ResponseTypes | None:
    if response.status_code == 200:
        response_200 = ConsentDefaults.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = EditConsentChannel400ResponseTypes.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConsentDefaults | EditConsentChannel400ResponseTypes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConsentChannelWrite | Unset = UNSET,
) -> Response[ConsentDefaults | EditConsentChannel400ResponseTypes]:
    """Edit consent channel.

     Edit a consent channel.

    Args:
        channel (str):
        body (ConsentChannelWrite | Unset): Defines a model to represent a consent channel write
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsentDefaults | EditConsentChannel400ResponseTypes]
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
    channel: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConsentChannelWrite | Unset = UNSET,
) -> ConsentDefaults | EditConsentChannel400ResponseTypes | None:
    """Edit consent channel.

     Edit a consent channel.

    Args:
        channel (str):
        body (ConsentChannelWrite | Unset): Defines a model to represent a consent channel write
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsentDefaults | EditConsentChannel400ResponseTypes
    """

    return sync_detailed(
        channel=channel,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    channel: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConsentChannelWrite | Unset = UNSET,
) -> Response[ConsentDefaults | EditConsentChannel400ResponseTypes]:
    """Edit consent channel.

     Edit a consent channel.

    Args:
        channel (str):
        body (ConsentChannelWrite | Unset): Defines a model to represent a consent channel write
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConsentDefaults | EditConsentChannel400ResponseTypes]
    """

    kwargs = _get_kwargs(
        channel=channel,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConsentChannelWrite | Unset = UNSET,
) -> ConsentDefaults | EditConsentChannel400ResponseTypes | None:
    """Edit consent channel.

     Edit a consent channel.

    Args:
        channel (str):
        body (ConsentChannelWrite | Unset): Defines a model to represent a consent channel write
            operation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConsentDefaults | EditConsentChannel400ResponseTypes
    """

    return (
        await asyncio_detailed(
            channel=channel,
            client=client,
            body=body,
        )
    ).parsed

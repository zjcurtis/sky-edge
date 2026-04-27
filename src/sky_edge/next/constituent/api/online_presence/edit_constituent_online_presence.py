from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.online_presence_edit import OnlinePresenceEdit


def _get_kwargs(
    online_presence_id: str,
    *,
    body: OnlinePresenceEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/onlinepresences/{online_presence_id}".format(
            online_presence_id=quote(str(online_presence_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    online_presence_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OnlinePresenceEdit | Unset = UNSET,
) -> Response[Any]:
    """Online presence (Edit)

     Edits a constituent online presence.

    Args:
        online_presence_id (str):
        body (OnlinePresenceEdit | Unset): Online presence entities store a constituent’s social
            media accounts, websites, and other means of reaching out or gaining more information
            about the constituent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        online_presence_id=online_presence_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    online_presence_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OnlinePresenceEdit | Unset = UNSET,
) -> Response[Any]:
    """Online presence (Edit)

     Edits a constituent online presence.

    Args:
        online_presence_id (str):
        body (OnlinePresenceEdit | Unset): Online presence entities store a constituent’s social
            media accounts, websites, and other means of reaching out or gaining more information
            about the constituent.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        online_presence_id=online_presence_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

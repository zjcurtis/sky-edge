from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.parented_note_edit import ParentedNoteEdit


def _get_kwargs(
    note_id: str,
    *,
    body: ParentedNoteEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/actions/notes/{note_id}".format(
            note_id=quote(str(note_id), safe=""),
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
    note_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ParentedNoteEdit | Unset = UNSET,
) -> Response[Any]:
    """Action note (Edit)

     Edits an action note.

    Args:
        note_id (str):
        body (ParentedNoteEdit | Unset): Notes track helpful or important details about
            constituents, gifts, or actions, such as specific interests and special instructions for
            donations. Notes connect you with donors at a more personal level as you cultivate
            relationships and track lessons learned for more effective fundraising.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    note_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ParentedNoteEdit | Unset = UNSET,
) -> Response[Any]:
    """Action note (Edit)

     Edits an action note.

    Args:
        note_id (str):
        body (ParentedNoteEdit | Unset): Notes track helpful or important details about
            constituents, gifts, or actions, such as specific interests and special instructions for
            donations. Notes connect you with donors at a more personal level as you cultivate
            relationships and track lessons learned for more effective fundraising.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        note_id=note_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

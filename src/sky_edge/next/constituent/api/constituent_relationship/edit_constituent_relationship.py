from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.relationship_edit import RelationshipEdit


def _get_kwargs(
    relationship_id: str,
    *,
    body: RelationshipEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/relationships/{relationship_id}".format(
            relationship_id=quote(str(relationship_id), safe=""),
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
    relationship_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationshipEdit | Unset = UNSET,
) -> Response[Any]:
    """Relationship (Edit)

     Edits a relationship for a constituent.
    If a reciprocal relationship exists, it is also modified to reflect the changes. This does not
    include changes to the `comments` property, which is specific to each record and can be modified
    independently on each record.

    Args:
        relationship_id (str):
        body (RelationshipEdit | Unset): Relationships describe connections between constituents
            and other individuals and organizations such as family, friends, and employers. Tracking
            constituent relationships can enhance fundraising efforts and interactions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        relationship_id=relationship_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    relationship_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RelationshipEdit | Unset = UNSET,
) -> Response[Any]:
    """Relationship (Edit)

     Edits a relationship for a constituent.
    If a reciprocal relationship exists, it is also modified to reflect the changes. This does not
    include changes to the `comments` property, which is specific to each record and can be modified
    independently on each record.

    Args:
        relationship_id (str):
        body (RelationshipEdit | Unset): Relationships describe connections between constituents
            and other individuals and organizations such as family, friends, and employers. Tracking
            constituent relationships can enhance fundraising efforts and interactions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        relationship_id=relationship_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.api_collection_of_custom_field_read import ApiCollectionOfCustomFieldRead


def _get_kwargs(
    action_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/actions/{action_id}/customfields".format(
            action_id=quote(str(action_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfCustomFieldRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfCustomFieldRead.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ApiCollectionOfCustomFieldRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiCollectionOfCustomFieldRead]:
    """Action custom field list (Single action)

     Returns a list of custom fields for an action.

    Args:
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfCustomFieldRead]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiCollectionOfCustomFieldRead | None:
    """Action custom field list (Single action)

     Returns a list of custom fields for an action.

    Args:
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfCustomFieldRead
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ApiCollectionOfCustomFieldRead]:
    """Action custom field list (Single action)

     Returns a list of custom fields for an action.

    Args:
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfCustomFieldRead]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | ApiCollectionOfCustomFieldRead | None:
    """Action custom field list (Single action)

     Returns a list of custom fields for an action.

    Args:
        action_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfCustomFieldRead
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
        )
    ).parsed

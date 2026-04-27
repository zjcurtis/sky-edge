from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.alias_add_collection import AliasAddCollection
from ...models.api_collection_of_string import ApiCollectionOfString


def _get_kwargs(
    constituent_id: str,
    *,
    body: AliasAddCollection | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/constituents/{constituent_id}/aliascollection".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfString | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfString.from_dict(response.json())

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
) -> Response[Any | ApiCollectionOfString]:
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
    body: AliasAddCollection | Unset = UNSET,
) -> Response[Any | ApiCollectionOfString]:
    """Alias collection (Create)

     Creates aliases.

    Args:
        constituent_id (str):
        body (AliasAddCollection | Unset): Aliases provide secondary identification for
            individuals or organizations. For example, aliases can be stage names or acronyms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfString]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AliasAddCollection | Unset = UNSET,
) -> Any | ApiCollectionOfString | None:
    """Alias collection (Create)

     Creates aliases.

    Args:
        constituent_id (str):
        body (AliasAddCollection | Unset): Aliases provide secondary identification for
            individuals or organizations. For example, aliases can be stage names or acronyms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfString
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AliasAddCollection | Unset = UNSET,
) -> Response[Any | ApiCollectionOfString]:
    """Alias collection (Create)

     Creates aliases.

    Args:
        constituent_id (str):
        body (AliasAddCollection | Unset): Aliases provide secondary identification for
            individuals or organizations. For example, aliases can be stage names or acronyms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfString]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AliasAddCollection | Unset = UNSET,
) -> Any | ApiCollectionOfString | None:
    """Alias collection (Create)

     Creates aliases.

    Args:
        constituent_id (str):
        body (AliasAddCollection | Unset): Aliases provide secondary identification for
            individuals or organizations. For example, aliases can be stage names or acronyms.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfString
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            body=body,
        )
    ).parsed

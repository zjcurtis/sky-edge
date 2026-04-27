from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.name_format_edit import NameFormatEdit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name_format_id: str,
    *,
    body: NameFormatEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/nameformats/{name_format_id}".format(
            name_format_id=quote(str(name_format_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name_format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NameFormatEdit | Unset = UNSET,
) -> Response[Any]:
    """Name format (Edit)

     Edits a name format for a constituent.

    Args:
        name_format_id (str):
        body (NameFormatEdit | Unset): Name formats define how to address constituents in
            communications. How you refer to individuals sets the tone of your communications with
            them and how well they receive your interactions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        name_format_id=name_format_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    name_format_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: NameFormatEdit | Unset = UNSET,
) -> Response[Any]:
    """Name format (Edit)

     Edits a name format for a constituent.

    Args:
        name_format_id (str):
        body (NameFormatEdit | Unset): Name formats define how to address constituents in
            communications. How you refer to individuals sets the tone of your communications with
            them and how well they receive your interactions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        name_format_id=name_format_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.constituent_edit import ConstituentEdit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    constituent_id: str,
    *,
    body: ConstituentEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/constituents/{constituent_id}".format(
            constituent_id=quote(str(constituent_id), safe=""),
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

    if response.status_code == 403:
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
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConstituentEdit | Unset = UNSET,
) -> Response[Any]:
    """Constituent (Edit)

     Edits a constituent.

    Args:
        constituent_id (str):
        body (ConstituentEdit | Unset): Constituents are the individuals and organizations who
            support your organization by contributing time, money, and resources. The constituent
            entity stores information about donors, prospects, volunteers, general supporters, and
            more.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConstituentEdit | Unset = UNSET,
) -> Response[Any]:
    """Constituent (Edit)

     Edits a constituent.

    Args:
        constituent_id (str):
        body (ConstituentEdit | Unset): Constituents are the individuals and organizations who
            support your organization by contributing time, money, and resources. The constituent
            entity stores information about donors, prospects, volunteers, general supporters, and
            more.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

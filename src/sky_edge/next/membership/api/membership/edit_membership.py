from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.membership_edit import MembershipEdit


def _get_kwargs(
    member_junction_id: str,
    *,
    body: MembershipEdit | Unset = UNSET,
    overwrite_benefits: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["overwrite_benefits"] = overwrite_benefits

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/memberships/{member_junction_id}/editmembershipdetails".format(
            member_junction_id=quote(str(member_junction_id), safe=""),
        ),
        "params": params,
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

    if response.status_code == 401:
        return None

    if response.status_code == 403:
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
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MembershipEdit | Unset = UNSET,
    overwrite_benefits: bool | Unset = False,
) -> Response[Any]:
    """Edit membership detail endpoint (PREVIEW)

     Edit membership detail.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        overwrite_benefits (bool | Unset):  Default: False.
        body (MembershipEdit | Unset): Membership update request model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
        body=body,
        overwrite_benefits=overwrite_benefits,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    member_junction_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MembershipEdit | Unset = UNSET,
    overwrite_benefits: bool | Unset = False,
) -> Response[Any]:
    """Edit membership detail endpoint (PREVIEW)

     Edit membership detail.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        overwrite_benefits (bool | Unset):  Default: False.
        body (MembershipEdit | Unset): Membership update request model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
        body=body,
        overwrite_benefits=overwrite_benefits,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

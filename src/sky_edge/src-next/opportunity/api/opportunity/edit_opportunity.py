from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opportunity_edit import OpportunityEdit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    opportunity_id: str,
    *,
    body: OpportunityEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/opportunities/{opportunity_id}".format(
            opportunity_id=quote(str(opportunity_id), safe=""),
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
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OpportunityEdit | Unset = UNSET,
) -> Response[Any]:
    """Opportunity (Edit)

     Edits an opportunity.

    Args:
        opportunity_id (str):
        body (OpportunityEdit | Unset): Opportunities help you plan and track efforts to build
            relationships with prospects and secure major gifts. They can manage information about
            fundraising activities and the effectiveness of your efforts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    opportunity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OpportunityEdit | Unset = UNSET,
) -> Response[Any]:
    """Opportunity (Edit)

     Edits an opportunity.

    Args:
        opportunity_id (str):
        body (OpportunityEdit | Unset): Opportunities help you plan and track efforts to build
            relationships with prospects and secure major gifts. They can manage information about
            fundraising activities and the effectiveness of your efforts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        opportunity_id=opportunity_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

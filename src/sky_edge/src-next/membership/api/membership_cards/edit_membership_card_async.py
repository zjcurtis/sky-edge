from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_400_response_types import BadRequest400ResponseTypes
from ...models.membership_card import MembershipCard
from ...models.membership_card_edit import MembershipCardEdit
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    member_junction_id: str,
    membership_card_id: str,
    *,
    body: MembershipCardEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/memberships/{member_junction_id}/membershipcards/{membership_card_id}".format(
            member_junction_id=quote(str(member_junction_id), safe=""),
            membership_card_id=quote(str(membership_card_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = MembershipCard.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BadRequest400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    member_junction_id: str,
    membership_card_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MembershipCardEdit | Unset = UNSET,
) -> Response[Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails]:
    """Edit a membership card (PREVIEW)

     Edits a membership card with the specified changes.

    **Note:** Depending on the type of update, you may need to include additional fields in the request
    body. For example:

    - To change the **Valid From** or **Valid To** dates, include `card_expires`.

    - To change the **name on the card**, include `card_member` and `editable`.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        membership_card_id (str):
        body (MembershipCardEdit | Unset): Edit membership card request model for JSON Merge Patch
            operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
        membership_card_id=membership_card_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    member_junction_id: str,
    membership_card_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MembershipCardEdit | Unset = UNSET,
) -> Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails | None:
    """Edit a membership card (PREVIEW)

     Edits a membership card with the specified changes.

    **Note:** Depending on the type of update, you may need to include additional fields in the request
    body. For example:

    - To change the **Valid From** or **Valid To** dates, include `card_expires`.

    - To change the **name on the card**, include `card_member` and `editable`.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        membership_card_id (str):
        body (MembershipCardEdit | Unset): Edit membership card request model for JSON Merge Patch
            operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails
    """

    return sync_detailed(
        member_junction_id=member_junction_id,
        membership_card_id=membership_card_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    member_junction_id: str,
    membership_card_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MembershipCardEdit | Unset = UNSET,
) -> Response[Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails]:
    """Edit a membership card (PREVIEW)

     Edits a membership card with the specified changes.

    **Note:** Depending on the type of update, you may need to include additional fields in the request
    body. For example:

    - To change the **Valid From** or **Valid To** dates, include `card_expires`.

    - To change the **name on the card**, include `card_member` and `editable`.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        membership_card_id (str):
        body (MembershipCardEdit | Unset): Edit membership card request model for JSON Merge Patch
            operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails]
    """

    kwargs = _get_kwargs(
        member_junction_id=member_junction_id,
        membership_card_id=membership_card_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    member_junction_id: str,
    membership_card_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MembershipCardEdit | Unset = UNSET,
) -> Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails | None:
    """Edit a membership card (PREVIEW)

     Edits a membership card with the specified changes.

    **Note:** Depending on the type of update, you may need to include additional fields in the request
    body. For example:

    - To change the **Valid From** or **Valid To** dates, include `card_expires`.

    - To change the **name on the card**, include `card_member` and `editable`.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        member_junction_id (str):
        membership_card_id (str):
        body (MembershipCardEdit | Unset): Edit membership card request model for JSON Merge Patch
            operations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | MembershipCard | ProblemDetails
    """

    return (
        await asyncio_detailed(
            member_junction_id=member_junction_id,
            membership_card_id=membership_card_id,
            client=client,
            body=body,
        )
    ).parsed

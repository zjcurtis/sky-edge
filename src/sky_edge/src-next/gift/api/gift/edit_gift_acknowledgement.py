from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.acknowledgement_edit import AcknowledgementEdit
from ...models.giftacknowledgements_acknowledgement_id_patch_200_application_json_response import (
    GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    acknowledgement_id: str,
    *,
    body: AcknowledgementEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/giftacknowledgements/{acknowledgement_id}".format(
            acknowledgement_id=quote(str(acknowledgement_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse | None:
    if response.status_code == 200:
        response_200 = GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse.from_dict(response.json())

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
) -> Response[Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    acknowledgement_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AcknowledgementEdit | Unset = UNSET,
) -> Response[Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse]:
    """Gift acknowledgement (Edit)

     Edits a gift acknowledgement.

    Args:
        acknowledgement_id (str):
        body (AcknowledgementEdit | Unset): Acknowledgement letters foster relationships with
            donors and show appreciation for their contributions. It is important to keep track of the
            acknowledgement status of gifts to ensure that each one gets a well-deserved thank you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse]
    """

    kwargs = _get_kwargs(
        acknowledgement_id=acknowledgement_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    acknowledgement_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AcknowledgementEdit | Unset = UNSET,
) -> Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse | None:
    """Gift acknowledgement (Edit)

     Edits a gift acknowledgement.

    Args:
        acknowledgement_id (str):
        body (AcknowledgementEdit | Unset): Acknowledgement letters foster relationships with
            donors and show appreciation for their contributions. It is important to keep track of the
            acknowledgement status of gifts to ensure that each one gets a well-deserved thank you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse
    """

    return sync_detailed(
        acknowledgement_id=acknowledgement_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    acknowledgement_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AcknowledgementEdit | Unset = UNSET,
) -> Response[Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse]:
    """Gift acknowledgement (Edit)

     Edits a gift acknowledgement.

    Args:
        acknowledgement_id (str):
        body (AcknowledgementEdit | Unset): Acknowledgement letters foster relationships with
            donors and show appreciation for their contributions. It is important to keep track of the
            acknowledgement status of gifts to ensure that each one gets a well-deserved thank you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse]
    """

    kwargs = _get_kwargs(
        acknowledgement_id=acknowledgement_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    acknowledgement_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AcknowledgementEdit | Unset = UNSET,
) -> Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse | None:
    """Gift acknowledgement (Edit)

     Edits a gift acknowledgement.

    Args:
        acknowledgement_id (str):
        body (AcknowledgementEdit | Unset): Acknowledgement letters foster relationships with
            donors and show appreciation for their contributions. It is important to keep track of the
            acknowledgement status of gifts to ensure that each one gets a well-deserved thank you.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftacknowledgementsAcknowledgementIdPatch200ApplicationJsonResponse
    """

    return (
        await asyncio_detailed(
            acknowledgement_id=acknowledgement_id,
            client=client,
            body=body,
        )
    ).parsed

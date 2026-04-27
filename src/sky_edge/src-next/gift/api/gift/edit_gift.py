from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.gift_edit import GiftEdit
from ...models.gifts_gift_id_patch_200_application_json_response import GiftsGiftIdPatch200ApplicationJsonResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    gift_id: str,
    *,
    body: GiftEdit | Unset = UNSET,
    if_match: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/gifts/{gift_id}".format(
            gift_id=quote(str(gift_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GiftsGiftIdPatch200ApplicationJsonResponse | None:
    if response.status_code == 200:
        response_200 = GiftsGiftIdPatch200ApplicationJsonResponse.from_dict(response.json())

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
) -> Response[Any | GiftsGiftIdPatch200ApplicationJsonResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftEdit | Unset = UNSET,
    if_match: str,
) -> Response[Any | GiftsGiftIdPatch200ApplicationJsonResponse]:
    """Gift (Edit)

     Edits a gift.
    Posted gifts cannot be modified, except to change recurring gift status.

    Args:
        gift_id (str):
        if_match (str):
        body (GiftEdit | Unset): An object that represents the gift to edit.
            Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot
            of information associated with them to ensure that they are properly allocated and
            acknowledged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftsGiftIdPatch200ApplicationJsonResponse]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftEdit | Unset = UNSET,
    if_match: str,
) -> Any | GiftsGiftIdPatch200ApplicationJsonResponse | None:
    """Gift (Edit)

     Edits a gift.
    Posted gifts cannot be modified, except to change recurring gift status.

    Args:
        gift_id (str):
        if_match (str):
        body (GiftEdit | Unset): An object that represents the gift to edit.
            Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot
            of information associated with them to ensure that they are properly allocated and
            acknowledged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftsGiftIdPatch200ApplicationJsonResponse
    """

    return sync_detailed(
        gift_id=gift_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftEdit | Unset = UNSET,
    if_match: str,
) -> Response[Any | GiftsGiftIdPatch200ApplicationJsonResponse]:
    """Gift (Edit)

     Edits a gift.
    Posted gifts cannot be modified, except to change recurring gift status.

    Args:
        gift_id (str):
        if_match (str):
        body (GiftEdit | Unset): An object that represents the gift to edit.
            Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot
            of information associated with them to ensure that they are properly allocated and
            acknowledged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GiftsGiftIdPatch200ApplicationJsonResponse]
    """

    kwargs = _get_kwargs(
        gift_id=gift_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    gift_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftEdit | Unset = UNSET,
    if_match: str,
) -> Any | GiftsGiftIdPatch200ApplicationJsonResponse | None:
    """Gift (Edit)

     Edits a gift.
    Posted gifts cannot be modified, except to change recurring gift status.

    Args:
        gift_id (str):
        if_match (str):
        body (GiftEdit | Unset): An object that represents the gift to edit.
            Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot
            of information associated with them to ensure that they are properly allocated and
            acknowledged.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GiftsGiftIdPatch200ApplicationJsonResponse
    """

    return (
        await asyncio_detailed(
            gift_id=gift_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.custom_field_edit import CustomFieldEdit


def _get_kwargs(
    custom_field_id: str,
    *,
    body: CustomFieldEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/gifts/customfields/{custom_field_id}".format(
            custom_field_id=quote(str(custom_field_id), safe=""),
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
    custom_field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldEdit | Unset = UNSET,
) -> Response[Any]:
    """Gift custom field (Edit)

     Edits a gift custom field.

    Args:
        custom_field_id (str):
        body (CustomFieldEdit | Unset): While records provide many fields to track information,
            organizations often require additional details. To track this specialized information, use
            custom fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    custom_field_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldEdit | Unset = UNSET,
) -> Response[Any]:
    """Gift custom field (Edit)

     Edits a gift custom field.

    Args:
        custom_field_id (str):
        body (CustomFieldEdit | Unset): While records provide many fields to track information,
            organizations often require additional details. To track this specialized information, use
            custom fields.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        custom_field_id=custom_field_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

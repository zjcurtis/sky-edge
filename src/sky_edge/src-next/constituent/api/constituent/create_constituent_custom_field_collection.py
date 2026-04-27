from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_add import CustomFieldAdd
from ...models.post_response import PostResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    constituent_id: str,
    *,
    body: list[CustomFieldAdd] | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/constituents/{constituent_id}/customfieldcollection".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = []
        for componentsschemas_custom_field_add_array_item_data in body:
            componentsschemas_custom_field_add_array_item = componentsschemas_custom_field_add_array_item_data.to_dict()
            _kwargs["json"].append(componentsschemas_custom_field_add_array_item)

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PostResponse | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PostResponse]:
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
    body: list[CustomFieldAdd] | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Constituent custom field collection (Create)

     Creates a collection of constituent custom fields.

    Args:
        constituent_id (str):
        body (list[CustomFieldAdd] | Unset):  Example: [{'category': 'Anniversary', 'comment':
            'Celebrated yearly', 'date': '2007-03-26T00:00:00.0000000+00:00', 'value':
            '1986-01-22T00:00:00.0000000+00:00'}, {'category': 'Favorite color', 'date':
            '2007-03-26T00:00:00.0000000+00:00', 'value': 'Blue'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
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
    body: list[CustomFieldAdd] | Unset = UNSET,
) -> Any | PostResponse | None:
    """Constituent custom field collection (Create)

     Creates a collection of constituent custom fields.

    Args:
        constituent_id (str):
        body (list[CustomFieldAdd] | Unset):  Example: [{'category': 'Anniversary', 'comment':
            'Celebrated yearly', 'date': '2007-03-26T00:00:00.0000000+00:00', 'value':
            '1986-01-22T00:00:00.0000000+00:00'}, {'category': 'Favorite color', 'date':
            '2007-03-26T00:00:00.0000000+00:00', 'value': 'Blue'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
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
    body: list[CustomFieldAdd] | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Constituent custom field collection (Create)

     Creates a collection of constituent custom fields.

    Args:
        constituent_id (str):
        body (list[CustomFieldAdd] | Unset):  Example: [{'category': 'Anniversary', 'comment':
            'Celebrated yearly', 'date': '2007-03-26T00:00:00.0000000+00:00', 'value':
            '1986-01-22T00:00:00.0000000+00:00'}, {'category': 'Favorite color', 'date':
            '2007-03-26T00:00:00.0000000+00:00', 'value': 'Blue'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
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
    body: list[CustomFieldAdd] | Unset = UNSET,
) -> Any | PostResponse | None:
    """Constituent custom field collection (Create)

     Creates a collection of constituent custom fields.

    Args:
        constituent_id (str):
        body (list[CustomFieldAdd] | Unset):  Example: [{'category': 'Anniversary', 'comment':
            'Celebrated yearly', 'date': '2007-03-26T00:00:00.0000000+00:00', 'value':
            '1986-01-22T00:00:00.0000000+00:00'}, {'category': 'Favorite color', 'date':
            '2007-03-26T00:00:00.0000000+00:00', 'value': 'Blue'}].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            body=body,
        )
    ).parsed

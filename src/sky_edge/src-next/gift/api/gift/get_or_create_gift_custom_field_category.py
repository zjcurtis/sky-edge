from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_category_add import CustomFieldCategoryAdd
from ...models.post_response import PostResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CustomFieldCategoryAdd | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/gifts/customfields/categories",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

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
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldCategoryAdd | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Adds custom field Category (GetOrCreate)

     Creates a gift custom field category if it doesn't exist or retrieves the id of the existing
    category.

    Args:
        body (CustomFieldCategoryAdd | Unset): Add a new custom field category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldCategoryAdd | Unset = UNSET,
) -> Any | PostResponse | None:
    """Adds custom field Category (GetOrCreate)

     Creates a gift custom field category if it doesn't exist or retrieves the id of the existing
    category.

    Args:
        body (CustomFieldCategoryAdd | Unset): Add a new custom field category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldCategoryAdd | Unset = UNSET,
) -> Response[Any | PostResponse]:
    """Adds custom field Category (GetOrCreate)

     Creates a gift custom field category if it doesn't exist or retrieves the id of the existing
    category.

    Args:
        body (CustomFieldCategoryAdd | Unset): Add a new custom field category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CustomFieldCategoryAdd | Unset = UNSET,
) -> Any | PostResponse | None:
    """Adds custom field Category (GetOrCreate)

     Creates a gift custom field category if it doesn't exist or retrieves the id of the existing
    category.

    Args:
        body (CustomFieldCategoryAdd | Unset): Add a new custom field category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

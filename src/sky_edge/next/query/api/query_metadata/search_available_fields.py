from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.available_fields_search_error_codes import (
    AvailableFieldsSearchErrorCodes,
)
from ...models.available_fields_search_response import AvailableFieldsSearchResponse
from ...models.query_field_context import QueryFieldContext
from ...models.search_available_fields_module import SearchAvailableFieldsModule
from ...models.search_available_fields_product import SearchAvailableFieldsProduct


def _get_kwargs(
    query_type_id: int,
    *,
    product: SearchAvailableFieldsProduct,
    module: SearchAvailableFieldsModule,
    search_text: str | Unset = UNSET,
    field_context: QueryFieldContext | Unset = UNSET,
    limit: int | Unset = 50,
    continuation_token: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params["search_text"] = search_text

    json_field_context: str | Unset = UNSET
    if not isinstance(field_context, Unset):
        json_field_context = field_context.value

    params["field_context"] = json_field_context

    params["limit"] = limit

    params["continuation_token"] = continuation_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/querytypes/{query_type_id}/availablefields/search".format(
            query_type_id=quote(str(query_type_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse | None:
    if response.status_code == 200:
        response_200 = AvailableFieldsSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AvailableFieldsSearchErrorCodes.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    query_type_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: SearchAvailableFieldsProduct,
    module: SearchAvailableFieldsModule,
    search_text: str | Unset = UNSET,
    field_context: QueryFieldContext | Unset = UNSET,
    limit: int | Unset = 50,
    continuation_token: str | Unset = UNSET,
) -> Response[AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse]:
    """Available field search (PREVIEW)

     Searches for available fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        query_type_id (int):
        product (SearchAvailableFieldsProduct):
        module (SearchAvailableFieldsModule):
        search_text (str | Unset):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>
        limit (int | Unset):  Default: 50.
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse]
    """

    kwargs = _get_kwargs(
        query_type_id=query_type_id,
        product=product,
        module=module,
        search_text=search_text,
        field_context=field_context,
        limit=limit,
        continuation_token=continuation_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    query_type_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: SearchAvailableFieldsProduct,
    module: SearchAvailableFieldsModule,
    search_text: str | Unset = UNSET,
    field_context: QueryFieldContext | Unset = UNSET,
    limit: int | Unset = 50,
    continuation_token: str | Unset = UNSET,
) -> AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse | None:
    """Available field search (PREVIEW)

     Searches for available fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        query_type_id (int):
        product (SearchAvailableFieldsProduct):
        module (SearchAvailableFieldsModule):
        search_text (str | Unset):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>
        limit (int | Unset):  Default: 50.
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse
    """

    return sync_detailed(
        query_type_id=query_type_id,
        client=client,
        product=product,
        module=module,
        search_text=search_text,
        field_context=field_context,
        limit=limit,
        continuation_token=continuation_token,
    ).parsed


async def asyncio_detailed(
    query_type_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: SearchAvailableFieldsProduct,
    module: SearchAvailableFieldsModule,
    search_text: str | Unset = UNSET,
    field_context: QueryFieldContext | Unset = UNSET,
    limit: int | Unset = 50,
    continuation_token: str | Unset = UNSET,
) -> Response[AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse]:
    """Available field search (PREVIEW)

     Searches for available fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        query_type_id (int):
        product (SearchAvailableFieldsProduct):
        module (SearchAvailableFieldsModule):
        search_text (str | Unset):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>
        limit (int | Unset):  Default: 50.
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse]
    """

    kwargs = _get_kwargs(
        query_type_id=query_type_id,
        product=product,
        module=module,
        search_text=search_text,
        field_context=field_context,
        limit=limit,
        continuation_token=continuation_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    query_type_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: SearchAvailableFieldsProduct,
    module: SearchAvailableFieldsModule,
    search_text: str | Unset = UNSET,
    field_context: QueryFieldContext | Unset = UNSET,
    limit: int | Unset = 50,
    continuation_token: str | Unset = UNSET,
) -> AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse | None:
    """Available field search (PREVIEW)

     Searches for available fields.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        query_type_id (int):
        product (SearchAvailableFieldsProduct):
        module (SearchAvailableFieldsModule):
        search_text (str | Unset):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>
        limit (int | Unset):  Default: 50.
        continuation_token (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailableFieldsSearchErrorCodes | AvailableFieldsSearchResponse
    """

    return (
        await asyncio_detailed(
            query_type_id=query_type_id,
            client=client,
            product=product,
            module=module,
            search_text=search_text,
            field_context=field_context,
            limit=limit,
            continuation_token=continuation_token,
        )
    ).parsed

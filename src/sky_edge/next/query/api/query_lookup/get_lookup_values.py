from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.get_lookup_values_module import GetLookupValuesModule
from ...models.get_lookup_values_product import GetLookupValuesProduct
from ...models.get_lookup_values_response import GetLookupValuesResponse
from ...models.problem_details import ProblemDetails


def _get_kwargs(
    query_field_id: int,
    *,
    product: GetLookupValuesProduct,
    module: GetLookupValuesModule,
    unique_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params["unique_id"] = unique_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/queryfields/{query_field_id}/lookupvalues".format(
            query_field_id=quote(str(query_field_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetLookupValuesResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = GetLookupValuesResponse.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

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
) -> Response[GetLookupValuesResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    query_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetLookupValuesProduct,
    module: GetLookupValuesModule,
    unique_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Response[GetLookupValuesResponse | ProblemDetails]:
    """Get lookup values

     Gets the list of lookup values for a field.

    Args:
        query_field_id (int):
        product (GetLookupValuesProduct):
        module (GetLookupValuesModule):
        unique_id (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLookupValuesResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        query_field_id=query_field_id,
        product=product,
        module=module,
        unique_id=unique_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    query_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetLookupValuesProduct,
    module: GetLookupValuesModule,
    unique_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> GetLookupValuesResponse | ProblemDetails | None:
    """Get lookup values

     Gets the list of lookup values for a field.

    Args:
        query_field_id (int):
        product (GetLookupValuesProduct):
        module (GetLookupValuesModule):
        unique_id (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLookupValuesResponse | ProblemDetails
    """

    return sync_detailed(
        query_field_id=query_field_id,
        client=client,
        product=product,
        module=module,
        unique_id=unique_id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    query_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetLookupValuesProduct,
    module: GetLookupValuesModule,
    unique_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Response[GetLookupValuesResponse | ProblemDetails]:
    """Get lookup values

     Gets the list of lookup values for a field.

    Args:
        query_field_id (int):
        product (GetLookupValuesProduct):
        module (GetLookupValuesModule):
        unique_id (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetLookupValuesResponse | ProblemDetails]
    """

    kwargs = _get_kwargs(
        query_field_id=query_field_id,
        product=product,
        module=module,
        unique_id=unique_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    query_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetLookupValuesProduct,
    module: GetLookupValuesModule,
    unique_id: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> GetLookupValuesResponse | ProblemDetails | None:
    """Get lookup values

     Gets the list of lookup values for a field.

    Args:
        query_field_id (int):
        product (GetLookupValuesProduct):
        module (GetLookupValuesModule):
        unique_id (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetLookupValuesResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            query_field_id=query_field_id,
            client=client,
            product=product,
            module=module,
            unique_id=unique_id,
            limit=limit,
            offset=offset,
        )
    ).parsed

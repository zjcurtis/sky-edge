from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response

from ...models.get_fields_response import GetFieldsResponse
from ...models.get_root_nodes_for_query_type_module import (
    GetRootNodesForQueryTypeModule,
)
from ...models.get_root_nodes_for_query_type_product import (
    GetRootNodesForQueryTypeProduct,
)
from ...models.problem_details import ProblemDetails
from ...models.query_definition_service_error_codes import (
    QueryDefinitionServiceErrorCodes,
)


def _get_kwargs(
    query_type_id: int,
    *,
    product: GetRootNodesForQueryTypeProduct,
    module: GetRootNodesForQueryTypeModule,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/querytypes/{query_type_id}/availablefields".format(
            query_type_id=quote(str(query_type_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    if response.status_code == 200:
        response_200 = GetFieldsResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = QueryDefinitionServiceErrorCodes.from_dict(response.json())

        return response_400

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
) -> Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
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
    product: GetRootNodesForQueryTypeProduct,
    module: GetRootNodesForQueryTypeModule,
) -> Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Available fields tree (Root)

     Gets the list of nodes at the root of the available fields tree for a query type.

    Args:
        query_type_id (int):
        product (GetRootNodesForQueryTypeProduct):
        module (GetRootNodesForQueryTypeModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]
    """

    kwargs = _get_kwargs(
        query_type_id=query_type_id,
        product=product,
        module=module,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    query_type_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetRootNodesForQueryTypeProduct,
    module: GetRootNodesForQueryTypeModule,
) -> GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Available fields tree (Root)

     Gets the list of nodes at the root of the available fields tree for a query type.

    Args:
        query_type_id (int):
        product (GetRootNodesForQueryTypeProduct):
        module (GetRootNodesForQueryTypeModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes
    """

    return sync_detailed(
        query_type_id=query_type_id,
        client=client,
        product=product,
        module=module,
    ).parsed


async def asyncio_detailed(
    query_type_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetRootNodesForQueryTypeProduct,
    module: GetRootNodesForQueryTypeModule,
) -> Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Available fields tree (Root)

     Gets the list of nodes at the root of the available fields tree for a query type.

    Args:
        query_type_id (int):
        product (GetRootNodesForQueryTypeProduct):
        module (GetRootNodesForQueryTypeModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]
    """

    kwargs = _get_kwargs(
        query_type_id=query_type_id,
        product=product,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    query_type_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetRootNodesForQueryTypeProduct,
    module: GetRootNodesForQueryTypeModule,
) -> GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Available fields tree (Root)

     Gets the list of nodes at the root of the available fields tree for a query type.

    Args:
        query_type_id (int):
        product (GetRootNodesForQueryTypeProduct):
        module (GetRootNodesForQueryTypeModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes
    """

    return (
        await asyncio_detailed(
            query_type_id=query_type_id,
            client=client,
            product=product,
            module=module,
        )
    ).parsed

from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.get_children_of_summary_field_node_module import (
    GetChildrenOfSummaryFieldNodeModule,
)
from ...models.get_children_of_summary_field_node_product import (
    GetChildrenOfSummaryFieldNodeProduct,
)
from ...models.get_fields_response import GetFieldsResponse
from ...models.problem_details import ProblemDetails
from ...models.query_definition_service_error_codes import (
    QueryDefinitionServiceErrorCodes,
)
from ...models.query_field_context import QueryFieldContext


def _get_kwargs(
    summary_field_id: int,
    node_id: int,
    *,
    product: GetChildrenOfSummaryFieldNodeProduct,
    module: GetChildrenOfSummaryFieldNodeModule,
    field_context: QueryFieldContext | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    json_field_context: str | Unset = UNSET
    if not isinstance(field_context, Unset):
        json_field_context = field_context.value

    params["field_context"] = json_field_context

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/summaryfields/{summary_field_id}/nodes/{node_id}/availablefields".format(
            summary_field_id=quote(str(summary_field_id), safe=""),
            node_id=quote(str(node_id), safe=""),
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
    summary_field_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetChildrenOfSummaryFieldNodeProduct,
    module: GetChildrenOfSummaryFieldNodeModule,
    field_context: QueryFieldContext | Unset = UNSET,
) -> Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Available fields tree for summary field (Node)

     Gets the list of nodes and fields that are children of the specified summary field and node in the
    available fields tree.

    Args:
        summary_field_id (int):
        node_id (int):
        product (GetChildrenOfSummaryFieldNodeProduct):
        module (GetChildrenOfSummaryFieldNodeModule):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]
    """

    kwargs = _get_kwargs(
        summary_field_id=summary_field_id,
        node_id=node_id,
        product=product,
        module=module,
        field_context=field_context,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    summary_field_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetChildrenOfSummaryFieldNodeProduct,
    module: GetChildrenOfSummaryFieldNodeModule,
    field_context: QueryFieldContext | Unset = UNSET,
) -> GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Available fields tree for summary field (Node)

     Gets the list of nodes and fields that are children of the specified summary field and node in the
    available fields tree.

    Args:
        summary_field_id (int):
        node_id (int):
        product (GetChildrenOfSummaryFieldNodeProduct):
        module (GetChildrenOfSummaryFieldNodeModule):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes
    """

    return sync_detailed(
        summary_field_id=summary_field_id,
        node_id=node_id,
        client=client,
        product=product,
        module=module,
        field_context=field_context,
    ).parsed


async def asyncio_detailed(
    summary_field_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetChildrenOfSummaryFieldNodeProduct,
    module: GetChildrenOfSummaryFieldNodeModule,
    field_context: QueryFieldContext | Unset = UNSET,
) -> Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Available fields tree for summary field (Node)

     Gets the list of nodes and fields that are children of the specified summary field and node in the
    available fields tree.

    Args:
        summary_field_id (int):
        node_id (int):
        product (GetChildrenOfSummaryFieldNodeProduct):
        module (GetChildrenOfSummaryFieldNodeModule):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]
    """

    kwargs = _get_kwargs(
        summary_field_id=summary_field_id,
        node_id=node_id,
        product=product,
        module=module,
        field_context=field_context,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    summary_field_id: int,
    node_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetChildrenOfSummaryFieldNodeProduct,
    module: GetChildrenOfSummaryFieldNodeModule,
    field_context: QueryFieldContext | Unset = UNSET,
) -> GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Available fields tree for summary field (Node)

     Gets the list of nodes and fields that are children of the specified summary field and node in the
    available fields tree.

    Args:
        summary_field_id (int):
        node_id (int):
        product (GetChildrenOfSummaryFieldNodeProduct):
        module (GetChildrenOfSummaryFieldNodeModule):
        field_context (QueryFieldContext | Unset): The context (editor tab), often used to handle
            differences in
            how various query fields behave depending how they're
            used.<p>Members:</p><ul><li><i>None</i> - Default</li><li><i>Filter</i> - Filter fields,
            aka criteria</li><li><i>Sort</i> - Sort fields</li><li><i>Select</i> - Select fields, aka
            output</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFieldsResponse | ProblemDetails | QueryDefinitionServiceErrorCodes
    """

    return (
        await asyncio_detailed(
            summary_field_id=summary_field_id,
            node_id=node_id,
            client=client,
            product=product,
            module=module,
            field_context=field_context,
        )
    ).parsed

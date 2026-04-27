from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response

from ...models.get_query_by_id_error_codes import GetQueryByIdErrorCodes
from ...models.get_query_by_id_module import GetQueryByIdModule
from ...models.get_query_by_id_product import GetQueryByIdProduct
from ...models.problem_details import ProblemDetails
from ...models.query_read import QueryRead


def _get_kwargs(
    id: int,
    *,
    product: GetQueryByIdProduct,
    module: GetQueryByIdModule,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/queries/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetQueryByIdErrorCodes | ProblemDetails | QueryRead | None:
    if response.status_code == 200:
        response_200 = QueryRead.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetQueryByIdErrorCodes.from_dict(response.json())

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
) -> Response[GetQueryByIdErrorCodes | ProblemDetails | QueryRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryByIdProduct,
    module: GetQueryByIdModule,
) -> Response[GetQueryByIdErrorCodes | ProblemDetails | QueryRead]:
    """Query

     Gets a query by ID.

    Args:
        id (int):
        product (GetQueryByIdProduct):
        module (GetQueryByIdModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueryByIdErrorCodes | ProblemDetails | QueryRead]
    """

    kwargs = _get_kwargs(
        id=id,
        product=product,
        module=module,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryByIdProduct,
    module: GetQueryByIdModule,
) -> GetQueryByIdErrorCodes | ProblemDetails | QueryRead | None:
    """Query

     Gets a query by ID.

    Args:
        id (int):
        product (GetQueryByIdProduct):
        module (GetQueryByIdModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueryByIdErrorCodes | ProblemDetails | QueryRead
    """

    return sync_detailed(
        id=id,
        client=client,
        product=product,
        module=module,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryByIdProduct,
    module: GetQueryByIdModule,
) -> Response[GetQueryByIdErrorCodes | ProblemDetails | QueryRead]:
    """Query

     Gets a query by ID.

    Args:
        id (int):
        product (GetQueryByIdProduct):
        module (GetQueryByIdModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetQueryByIdErrorCodes | ProblemDetails | QueryRead]
    """

    kwargs = _get_kwargs(
        id=id,
        product=product,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetQueryByIdProduct,
    module: GetQueryByIdModule,
) -> GetQueryByIdErrorCodes | ProblemDetails | QueryRead | None:
    """Query

     Gets a query by ID.

    Args:
        id (int):
        product (GetQueryByIdProduct):
        module (GetQueryByIdModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetQueryByIdErrorCodes | ProblemDetails | QueryRead
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            product=product,
            module=module,
        )
    ).parsed

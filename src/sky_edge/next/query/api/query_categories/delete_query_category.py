from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response

from ...models.delete_query_category_module import DeleteQueryCategoryModule
from ...models.delete_query_category_product import DeleteQueryCategoryProduct
from ...models.problem_details import ProblemDetails
from ...models.query_category_delete_error_codes import QueryCategoryDeleteErrorCodes


def _get_kwargs(
    id: int,
    *,
    product: DeleteQueryCategoryProduct,
    module: DeleteQueryCategoryModule,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/categories/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | QueryCategoryDeleteErrorCodes | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = QueryCategoryDeleteErrorCodes.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ProblemDetails | QueryCategoryDeleteErrorCodes]:
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
    product: DeleteQueryCategoryProduct,
    module: DeleteQueryCategoryModule,
) -> Response[Any | ProblemDetails | QueryCategoryDeleteErrorCodes]:
    """Deletes a query category

     Deletes a query category.

    Args:
        id (int):
        product (DeleteQueryCategoryProduct):
        module (DeleteQueryCategoryModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryCategoryDeleteErrorCodes]
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
    product: DeleteQueryCategoryProduct,
    module: DeleteQueryCategoryModule,
) -> Any | ProblemDetails | QueryCategoryDeleteErrorCodes | None:
    """Deletes a query category

     Deletes a query category.

    Args:
        id (int):
        product (DeleteQueryCategoryProduct):
        module (DeleteQueryCategoryModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryCategoryDeleteErrorCodes
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
    product: DeleteQueryCategoryProduct,
    module: DeleteQueryCategoryModule,
) -> Response[Any | ProblemDetails | QueryCategoryDeleteErrorCodes]:
    """Deletes a query category

     Deletes a query category.

    Args:
        id (int):
        product (DeleteQueryCategoryProduct):
        module (DeleteQueryCategoryModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryCategoryDeleteErrorCodes]
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
    product: DeleteQueryCategoryProduct,
    module: DeleteQueryCategoryModule,
) -> Any | ProblemDetails | QueryCategoryDeleteErrorCodes | None:
    """Deletes a query category

     Deletes a query category.

    Args:
        id (int):
        product (DeleteQueryCategoryProduct):
        module (DeleteQueryCategoryModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryCategoryDeleteErrorCodes
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            product=product,
            module=module,
        )
    ).parsed

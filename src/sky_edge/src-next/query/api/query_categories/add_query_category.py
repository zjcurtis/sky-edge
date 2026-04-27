from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_query_category_module import AddQueryCategoryModule
from ...models.add_query_category_product import AddQueryCategoryProduct
from ...models.post_response import PostResponse
from ...models.problem_details import ProblemDetails
from ...models.query_category_add_error_codes import QueryCategoryAddErrorCodes
from ...models.query_category_write import QueryCategoryWrite
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: QueryCategoryWrite | Unset = UNSET,
    product: AddQueryCategoryProduct,
    module: AddQueryCategoryModule,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/categories",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostResponse | ProblemDetails | QueryCategoryAddErrorCodes | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = QueryCategoryAddErrorCodes.from_dict(response.json())

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
) -> Response[PostResponse | ProblemDetails | QueryCategoryAddErrorCodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueryCategoryWrite | Unset = UNSET,
    product: AddQueryCategoryProduct,
    module: AddQueryCategoryModule,
) -> Response[PostResponse | ProblemDetails | QueryCategoryAddErrorCodes]:
    """Adds a query category.

     Adds a query category.

    Args:
        product (AddQueryCategoryProduct):
        module (AddQueryCategoryModule):
        body (QueryCategoryWrite | Unset): Model for adding a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse | ProblemDetails | QueryCategoryAddErrorCodes]
    """

    kwargs = _get_kwargs(
        body=body,
        product=product,
        module=module,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QueryCategoryWrite | Unset = UNSET,
    product: AddQueryCategoryProduct,
    module: AddQueryCategoryModule,
) -> PostResponse | ProblemDetails | QueryCategoryAddErrorCodes | None:
    """Adds a query category.

     Adds a query category.

    Args:
        product (AddQueryCategoryProduct):
        module (AddQueryCategoryModule):
        body (QueryCategoryWrite | Unset): Model for adding a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse | ProblemDetails | QueryCategoryAddErrorCodes
    """

    return sync_detailed(
        client=client,
        body=body,
        product=product,
        module=module,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueryCategoryWrite | Unset = UNSET,
    product: AddQueryCategoryProduct,
    module: AddQueryCategoryModule,
) -> Response[PostResponse | ProblemDetails | QueryCategoryAddErrorCodes]:
    """Adds a query category.

     Adds a query category.

    Args:
        product (AddQueryCategoryProduct):
        module (AddQueryCategoryModule):
        body (QueryCategoryWrite | Unset): Model for adding a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse | ProblemDetails | QueryCategoryAddErrorCodes]
    """

    kwargs = _get_kwargs(
        body=body,
        product=product,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QueryCategoryWrite | Unset = UNSET,
    product: AddQueryCategoryProduct,
    module: AddQueryCategoryModule,
) -> PostResponse | ProblemDetails | QueryCategoryAddErrorCodes | None:
    """Adds a query category.

     Adds a query category.

    Args:
        product (AddQueryCategoryProduct):
        module (AddQueryCategoryModule):
        body (QueryCategoryWrite | Unset): Model for adding a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse | ProblemDetails | QueryCategoryAddErrorCodes
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            product=product,
            module=module,
        )
    ).parsed

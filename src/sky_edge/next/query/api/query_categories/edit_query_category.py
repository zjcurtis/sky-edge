from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.edit_query_category_module import EditQueryCategoryModule
from ...models.edit_query_category_product import EditQueryCategoryProduct
from ...models.problem_details import ProblemDetails
from ...models.query_category_edit import QueryCategoryEdit
from ...models.query_category_edit_error_codes import QueryCategoryEditErrorCodes


def _get_kwargs(
    id: int,
    *,
    body: QueryCategoryEdit | Unset = UNSET,
    product: EditQueryCategoryProduct,
    module: EditQueryCategoryModule,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/categories/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | QueryCategoryEditErrorCodes | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = QueryCategoryEditErrorCodes.from_dict(response.json())

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
) -> Response[Any | ProblemDetails | QueryCategoryEditErrorCodes]:
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
    body: QueryCategoryEdit | Unset = UNSET,
    product: EditQueryCategoryProduct,
    module: EditQueryCategoryModule,
) -> Response[Any | ProblemDetails | QueryCategoryEditErrorCodes]:
    """Edit a query category.

     Edit a query category.

    Args:
        id (int):
        product (EditQueryCategoryProduct):
        module (EditQueryCategoryModule):
        body (QueryCategoryEdit | Unset): Model used to edit a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryCategoryEditErrorCodes]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
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
    body: QueryCategoryEdit | Unset = UNSET,
    product: EditQueryCategoryProduct,
    module: EditQueryCategoryModule,
) -> Any | ProblemDetails | QueryCategoryEditErrorCodes | None:
    """Edit a query category.

     Edit a query category.

    Args:
        id (int):
        product (EditQueryCategoryProduct):
        module (EditQueryCategoryModule):
        body (QueryCategoryEdit | Unset): Model used to edit a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryCategoryEditErrorCodes
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        product=product,
        module=module,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QueryCategoryEdit | Unset = UNSET,
    product: EditQueryCategoryProduct,
    module: EditQueryCategoryModule,
) -> Response[Any | ProblemDetails | QueryCategoryEditErrorCodes]:
    """Edit a query category.

     Edit a query category.

    Args:
        id (int):
        product (EditQueryCategoryProduct):
        module (EditQueryCategoryModule):
        body (QueryCategoryEdit | Unset): Model used to edit a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryCategoryEditErrorCodes]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        product=product,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: QueryCategoryEdit | Unset = UNSET,
    product: EditQueryCategoryProduct,
    module: EditQueryCategoryModule,
) -> Any | ProblemDetails | QueryCategoryEditErrorCodes | None:
    """Edit a query category.

     Edit a query category.

    Args:
        id (int):
        product (EditQueryCategoryProduct):
        module (EditQueryCategoryModule):
        body (QueryCategoryEdit | Unset): Model used to edit a query category

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryCategoryEditErrorCodes
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            product=product,
            module=module,
        )
    ).parsed

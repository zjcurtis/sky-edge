from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.add_query_module import AddQueryModule
from ...models.add_query_product import AddQueryProduct
from ...models.post_response import PostResponse
from ...models.problem_details import ProblemDetails
from ...models.query_add import QueryAdd
from ...models.query_write_error_codes import QueryWriteErrorCodes


def _get_kwargs(
    *,
    body: QueryAdd | Unset = UNSET,
    product: AddQueryProduct,
    module: AddQueryModule,
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
        "url": "/queries",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostResponse | ProblemDetails | QueryWriteErrorCodes | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = QueryWriteErrorCodes.from_dict(response.json())

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
) -> Response[PostResponse | ProblemDetails | QueryWriteErrorCodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QueryAdd | Unset = UNSET,
    product: AddQueryProduct,
    module: AddQueryModule,
) -> Response[PostResponse | ProblemDetails | QueryWriteErrorCodes]:
    """Query

     Adds a query.

    Args:
        product (AddQueryProduct):
        module (AddQueryModule):
        body (QueryAdd | Unset): Model of a query add

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse | ProblemDetails | QueryWriteErrorCodes]
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
    body: QueryAdd | Unset = UNSET,
    product: AddQueryProduct,
    module: AddQueryModule,
) -> PostResponse | ProblemDetails | QueryWriteErrorCodes | None:
    """Query

     Adds a query.

    Args:
        product (AddQueryProduct):
        module (AddQueryModule):
        body (QueryAdd | Unset): Model of a query add

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse | ProblemDetails | QueryWriteErrorCodes
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
    body: QueryAdd | Unset = UNSET,
    product: AddQueryProduct,
    module: AddQueryModule,
) -> Response[PostResponse | ProblemDetails | QueryWriteErrorCodes]:
    """Query

     Adds a query.

    Args:
        product (AddQueryProduct):
        module (AddQueryModule):
        body (QueryAdd | Unset): Model of a query add

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse | ProblemDetails | QueryWriteErrorCodes]
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
    body: QueryAdd | Unset = UNSET,
    product: AddQueryProduct,
    module: AddQueryModule,
) -> PostResponse | ProblemDetails | QueryWriteErrorCodes | None:
    """Query

     Adds a query.

    Args:
        product (AddQueryProduct):
        module (AddQueryModule):
        body (QueryAdd | Unset): Model of a query add

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse | ProblemDetails | QueryWriteErrorCodes
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            product=product,
            module=module,
        )
    ).parsed

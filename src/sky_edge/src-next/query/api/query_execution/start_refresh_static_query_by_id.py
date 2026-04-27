from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_query_response import ExecuteQueryResponse
from ...models.problem_details import ProblemDetails
from ...models.refresh_static_query_error_codes import RefreshStaticQueryErrorCodes
from ...models.refresh_static_query_request import RefreshStaticQueryRequest
from ...models.start_refresh_static_query_by_id_module import StartRefreshStaticQueryByIDModule
from ...models.start_refresh_static_query_by_id_product import StartRefreshStaticQueryByIDProduct
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RefreshStaticQueryRequest | Unset = UNSET,
    product: StartRefreshStaticQueryByIDProduct,
    module: StartRefreshStaticQueryByIDModule,
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
        "url": "/queries/refreshstaticquery",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes | None:
    if response.status_code == 200:
        response_200 = ExecuteQueryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RefreshStaticQueryErrorCodes.from_dict(response.json())

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
) -> Response[ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshStaticQueryRequest | Unset = UNSET,
    product: StartRefreshStaticQueryByIDProduct,
    module: StartRefreshStaticQueryByIDModule,
) -> Response[ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes]:
    """Refresh static query execution job

     Creates a background job to refresh the saved keys for a static query specified by ID.

    Args:
        product (StartRefreshStaticQueryByIDProduct):
        module (StartRefreshStaticQueryByIDModule):
        body (RefreshStaticQueryRequest | Unset): Request model for refreshing a static query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes]
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
    body: RefreshStaticQueryRequest | Unset = UNSET,
    product: StartRefreshStaticQueryByIDProduct,
    module: StartRefreshStaticQueryByIDModule,
) -> ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes | None:
    """Refresh static query execution job

     Creates a background job to refresh the saved keys for a static query specified by ID.

    Args:
        product (StartRefreshStaticQueryByIDProduct):
        module (StartRefreshStaticQueryByIDModule):
        body (RefreshStaticQueryRequest | Unset): Request model for refreshing a static query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes
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
    body: RefreshStaticQueryRequest | Unset = UNSET,
    product: StartRefreshStaticQueryByIDProduct,
    module: StartRefreshStaticQueryByIDModule,
) -> Response[ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes]:
    """Refresh static query execution job

     Creates a background job to refresh the saved keys for a static query specified by ID.

    Args:
        product (StartRefreshStaticQueryByIDProduct):
        module (StartRefreshStaticQueryByIDModule):
        body (RefreshStaticQueryRequest | Unset): Request model for refreshing a static query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes]
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
    body: RefreshStaticQueryRequest | Unset = UNSET,
    product: StartRefreshStaticQueryByIDProduct,
    module: StartRefreshStaticQueryByIDModule,
) -> ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes | None:
    """Refresh static query execution job

     Creates a background job to refresh the saved keys for a static query specified by ID.

    Args:
        product (StartRefreshStaticQueryByIDProduct):
        module (StartRefreshStaticQueryByIDModule):
        body (RefreshStaticQueryRequest | Unset): Request model for refreshing a static query

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteQueryResponse | ProblemDetails | RefreshStaticQueryErrorCodes
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            product=product,
            module=module,
        )
    ).parsed

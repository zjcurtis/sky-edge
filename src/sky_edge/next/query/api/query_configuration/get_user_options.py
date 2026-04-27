from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response

from ...models.get_user_options_module import GetUserOptionsModule
from ...models.get_user_options_product import GetUserOptionsProduct
from ...models.problem_details import ProblemDetails
from ...models.query_definition_service_error_codes import (
    QueryDefinitionServiceErrorCodes,
)
from ...models.user_options import UserOptions


def _get_kwargs(
    *,
    product: GetUserOptionsProduct,
    module: GetUserOptionsModule,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/configuration/useroptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions | None:
    if response.status_code == 200:
        response_200 = UserOptions.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = QueryDefinitionServiceErrorCodes.from_dict(response.json())

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
) -> Response[ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: GetUserOptionsProduct,
    module: GetUserOptionsModule,
) -> Response[ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions]:
    """Get current user options.

     Get current user options.

    Args:
        product (GetUserOptionsProduct):
        module (GetUserOptionsModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions]
    """

    kwargs = _get_kwargs(
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
    product: GetUserOptionsProduct,
    module: GetUserOptionsModule,
) -> ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions | None:
    """Get current user options.

     Get current user options.

    Args:
        product (GetUserOptionsProduct):
        module (GetUserOptionsModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions
    """

    return sync_detailed(
        client=client,
        product=product,
        module=module,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    product: GetUserOptionsProduct,
    module: GetUserOptionsModule,
) -> Response[ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions]:
    """Get current user options.

     Get current user options.

    Args:
        product (GetUserOptionsProduct):
        module (GetUserOptionsModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions]
    """

    kwargs = _get_kwargs(
        product=product,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    product: GetUserOptionsProduct,
    module: GetUserOptionsModule,
) -> ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions | None:
    """Get current user options.

     Get current user options.

    Args:
        product (GetUserOptionsProduct):
        module (GetUserOptionsModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | QueryDefinitionServiceErrorCodes | UserOptions
    """

    return (
        await asyncio_detailed(
            client=client,
            product=product,
            module=module,
        )
    ).parsed

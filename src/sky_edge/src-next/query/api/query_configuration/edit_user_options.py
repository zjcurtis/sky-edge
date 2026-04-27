from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.edit_user_options_module import EditUserOptionsModule
from ...models.edit_user_options_product import EditUserOptionsProduct
from ...models.problem_details import ProblemDetails
from ...models.query_definition_service_error_codes import QueryDefinitionServiceErrorCodes
from ...models.user_options import UserOptions
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UserOptions | Unset = UNSET,
    product: EditUserOptionsProduct,
    module: EditUserOptionsModule,
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
        "url": "/configuration/useroptions",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserOptions | Unset = UNSET,
    product: EditUserOptionsProduct,
    module: EditUserOptionsModule,
) -> Response[Any | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Edit current user options.

     Edit current user options.

    Args:
        product (EditUserOptionsProduct):
        module (EditUserOptionsModule):
        body (UserOptions | Unset): A set of user options for a given environment + user + product

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryDefinitionServiceErrorCodes]
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
    body: UserOptions | Unset = UNSET,
    product: EditUserOptionsProduct,
    module: EditUserOptionsModule,
) -> Any | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Edit current user options.

     Edit current user options.

    Args:
        product (EditUserOptionsProduct):
        module (EditUserOptionsModule):
        body (UserOptions | Unset): A set of user options for a given environment + user + product

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryDefinitionServiceErrorCodes
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
    body: UserOptions | Unset = UNSET,
    product: EditUserOptionsProduct,
    module: EditUserOptionsModule,
) -> Response[Any | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Edit current user options.

     Edit current user options.

    Args:
        product (EditUserOptionsProduct):
        module (EditUserOptionsModule):
        body (UserOptions | Unset): A set of user options for a given environment + user + product

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryDefinitionServiceErrorCodes]
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
    body: UserOptions | Unset = UNSET,
    product: EditUserOptionsProduct,
    module: EditUserOptionsModule,
) -> Any | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Edit current user options.

     Edit current user options.

    Args:
        product (EditUserOptionsProduct):
        module (EditUserOptionsModule):
        body (UserOptions | Unset): A set of user options for a given environment + user + product

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryDefinitionServiceErrorCodes
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            product=product,
            module=module,
        )
    ).parsed

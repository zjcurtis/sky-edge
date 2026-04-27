from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_query_module import DeleteQueryModule
from ...models.delete_query_product import DeleteQueryProduct
from ...models.problem_details import ProblemDetails
from ...models.query_delete_error_codes import QueryDeleteErrorCodes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    product: DeleteQueryProduct,
    module: DeleteQueryModule,
    perform_delete: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params["perform_delete"] = perform_delete

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/queries/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | QueryDeleteErrorCodes | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = QueryDeleteErrorCodes.from_dict(response.json())

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
) -> Response[Any | ProblemDetails | QueryDeleteErrorCodes]:
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
    product: DeleteQueryProduct,
    module: DeleteQueryModule,
    perform_delete: bool | Unset = False,
) -> Response[Any | ProblemDetails | QueryDeleteErrorCodes]:
    """Query

     Delete a query by ID.

    Args:
        id (int):
        product (DeleteQueryProduct):
        module (DeleteQueryModule):
        perform_delete (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryDeleteErrorCodes]
    """

    kwargs = _get_kwargs(
        id=id,
        product=product,
        module=module,
        perform_delete=perform_delete,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    product: DeleteQueryProduct,
    module: DeleteQueryModule,
    perform_delete: bool | Unset = False,
) -> Any | ProblemDetails | QueryDeleteErrorCodes | None:
    """Query

     Delete a query by ID.

    Args:
        id (int):
        product (DeleteQueryProduct):
        module (DeleteQueryModule):
        perform_delete (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryDeleteErrorCodes
    """

    return sync_detailed(
        id=id,
        client=client,
        product=product,
        module=module,
        perform_delete=perform_delete,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    product: DeleteQueryProduct,
    module: DeleteQueryModule,
    perform_delete: bool | Unset = False,
) -> Response[Any | ProblemDetails | QueryDeleteErrorCodes]:
    """Query

     Delete a query by ID.

    Args:
        id (int):
        product (DeleteQueryProduct):
        module (DeleteQueryModule):
        perform_delete (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | QueryDeleteErrorCodes]
    """

    kwargs = _get_kwargs(
        id=id,
        product=product,
        module=module,
        perform_delete=perform_delete,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    product: DeleteQueryProduct,
    module: DeleteQueryModule,
    perform_delete: bool | Unset = False,
) -> Any | ProblemDetails | QueryDeleteErrorCodes | None:
    """Query

     Delete a query by ID.

    Args:
        id (int):
        product (DeleteQueryProduct):
        module (DeleteQueryModule):
        perform_delete (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | QueryDeleteErrorCodes
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            product=product,
            module=module,
            perform_delete=perform_delete,
        )
    ).parsed

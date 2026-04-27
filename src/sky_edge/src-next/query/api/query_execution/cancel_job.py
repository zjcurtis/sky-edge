from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_job_module import CancelJobModule
from ...models.cancel_job_product import CancelJobProduct
from ...models.post_response import PostResponse
from ...models.problem_details import ProblemDetails
from ...models.query_definition_service_error_codes import QueryDefinitionServiceErrorCodes
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    product: CancelJobProduct,
    module: CancelJobModule,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/jobs/{id}/cancel".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    if response.status_code == 200:
        response_200 = PostResponse.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    product: CancelJobProduct,
    module: CancelJobModule,
) -> Response[PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Cancel query execution job (PREVIEW)

     Updates the job status to cancelling.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        id (str):
        product (CancelJobProduct):
        module (CancelJobModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    product: CancelJobProduct,
    module: CancelJobModule,
) -> PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Cancel query execution job (PREVIEW)

     Updates the job status to cancelling.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        id (str):
        product (CancelJobProduct):
        module (CancelJobModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes
    """

    return sync_detailed(
        id=id,
        client=client,
        product=product,
        module=module,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    product: CancelJobProduct,
    module: CancelJobModule,
) -> Response[PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]:
    """Cancel query execution job (PREVIEW)

     Updates the job status to cancelling.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        id (str):
        product (CancelJobProduct):
        module (CancelJobModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes]
    """

    kwargs = _get_kwargs(
        id=id,
        product=product,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    product: CancelJobProduct,
    module: CancelJobModule,
) -> PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes | None:
    """Cancel query execution job (PREVIEW)

     Updates the job status to cancelling.

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        id (str):
        product (CancelJobProduct):
        module (CancelJobModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostResponse | ProblemDetails | QueryDefinitionServiceErrorCodes
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            product=product,
            module=module,
        )
    ).parsed

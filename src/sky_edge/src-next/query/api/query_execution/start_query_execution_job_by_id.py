from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_query_by_id_error_codes import ExecuteQueryByIdErrorCodes
from ...models.execute_query_by_id_request import ExecuteQueryByIdRequest
from ...models.execute_query_response import ExecuteQueryResponse
from ...models.problem_details import ProblemDetails
from ...models.start_query_execution_job_by_id_module import StartQueryExecutionJobByIDModule
from ...models.start_query_execution_job_by_id_product import StartQueryExecutionJobByIDProduct
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ExecuteQueryByIdRequest | Unset = UNSET,
    product: StartQueryExecutionJobByIDProduct,
    module: StartQueryExecutionJobByIDModule,
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
        "url": "/queries/executebyid",
        "params": params,
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ExecuteQueryResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ExecuteQueryByIdErrorCodes.from_dict(response.json())

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
) -> Response[ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExecuteQueryByIdRequest | Unset = UNSET,
    product: StartQueryExecutionJobByIDProduct,
    module: StartQueryExecutionJobByIDModule,
) -> Response[ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails]:
    """Query execution job (by ID)

     Creates a background job to execute a query specified by ID. For RE requests, the Analysis - Query -
    Export permission is required to use this endpoint.

    Args:
        product (StartQueryExecutionJobByIDProduct):
        module (StartQueryExecutionJobByIDModule):
        body (ExecuteQueryByIdRequest | Unset): Request model for executing a query by ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails]
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
    body: ExecuteQueryByIdRequest | Unset = UNSET,
    product: StartQueryExecutionJobByIDProduct,
    module: StartQueryExecutionJobByIDModule,
) -> ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails | None:
    """Query execution job (by ID)

     Creates a background job to execute a query specified by ID. For RE requests, the Analysis - Query -
    Export permission is required to use this endpoint.

    Args:
        product (StartQueryExecutionJobByIDProduct):
        module (StartQueryExecutionJobByIDModule):
        body (ExecuteQueryByIdRequest | Unset): Request model for executing a query by ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails
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
    body: ExecuteQueryByIdRequest | Unset = UNSET,
    product: StartQueryExecutionJobByIDProduct,
    module: StartQueryExecutionJobByIDModule,
) -> Response[ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails]:
    """Query execution job (by ID)

     Creates a background job to execute a query specified by ID. For RE requests, the Analysis - Query -
    Export permission is required to use this endpoint.

    Args:
        product (StartQueryExecutionJobByIDProduct):
        module (StartQueryExecutionJobByIDModule):
        body (ExecuteQueryByIdRequest | Unset): Request model for executing a query by ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails]
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
    body: ExecuteQueryByIdRequest | Unset = UNSET,
    product: StartQueryExecutionJobByIDProduct,
    module: StartQueryExecutionJobByIDModule,
) -> ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails | None:
    """Query execution job (by ID)

     Creates a background job to execute a query specified by ID. For RE requests, the Analysis - Query -
    Export permission is required to use this endpoint.

    Args:
        product (StartQueryExecutionJobByIDProduct):
        module (StartQueryExecutionJobByIDModule):
        body (ExecuteQueryByIdRequest | Unset): Request model for executing a query by ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteQueryByIdErrorCodes | ExecuteQueryResponse | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            product=product,
            module=module,
        )
    ).parsed

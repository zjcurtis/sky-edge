from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_summary_field_default_filters_module import GetSummaryFieldDefaultFiltersModule
from ...models.get_summary_field_default_filters_product import GetSummaryFieldDefaultFiltersProduct
from ...models.get_summary_field_default_filters_response import GetSummaryFieldDefaultFiltersResponse
from ...models.problem_details import ProblemDetails
from ...models.summary_field_default_filter_error_codes import SummaryFieldDefaultFilterErrorCodes
from ...types import UNSET, Response


def _get_kwargs(
    summary_field_id: int,
    *,
    product: GetSummaryFieldDefaultFiltersProduct,
    module: GetSummaryFieldDefaultFiltersModule,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/summaryfields/{summary_field_id}/defaultfilters".format(
            summary_field_id=quote(str(summary_field_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes | None:
    if response.status_code == 200:
        response_200 = GetSummaryFieldDefaultFiltersResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SummaryFieldDefaultFilterErrorCodes.from_dict(response.json())

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
) -> Response[GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    summary_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetSummaryFieldDefaultFiltersProduct,
    module: GetSummaryFieldDefaultFiltersModule,
) -> Response[GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes]:
    """Default filters for a parameterized summary field

     Gets the list of default filters to apply for the specified summary field that is a parameterized
    summary type.

    Args:
        summary_field_id (int):
        product (GetSummaryFieldDefaultFiltersProduct):
        module (GetSummaryFieldDefaultFiltersModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes]
    """

    kwargs = _get_kwargs(
        summary_field_id=summary_field_id,
        product=product,
        module=module,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    summary_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetSummaryFieldDefaultFiltersProduct,
    module: GetSummaryFieldDefaultFiltersModule,
) -> GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes | None:
    """Default filters for a parameterized summary field

     Gets the list of default filters to apply for the specified summary field that is a parameterized
    summary type.

    Args:
        summary_field_id (int):
        product (GetSummaryFieldDefaultFiltersProduct):
        module (GetSummaryFieldDefaultFiltersModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes
    """

    return sync_detailed(
        summary_field_id=summary_field_id,
        client=client,
        product=product,
        module=module,
    ).parsed


async def asyncio_detailed(
    summary_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetSummaryFieldDefaultFiltersProduct,
    module: GetSummaryFieldDefaultFiltersModule,
) -> Response[GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes]:
    """Default filters for a parameterized summary field

     Gets the list of default filters to apply for the specified summary field that is a parameterized
    summary type.

    Args:
        summary_field_id (int):
        product (GetSummaryFieldDefaultFiltersProduct):
        module (GetSummaryFieldDefaultFiltersModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes]
    """

    kwargs = _get_kwargs(
        summary_field_id=summary_field_id,
        product=product,
        module=module,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    summary_field_id: int,
    *,
    client: AuthenticatedClient | Client,
    product: GetSummaryFieldDefaultFiltersProduct,
    module: GetSummaryFieldDefaultFiltersModule,
) -> GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes | None:
    """Default filters for a parameterized summary field

     Gets the list of default filters to apply for the specified summary field that is a parameterized
    summary type.

    Args:
        summary_field_id (int):
        product (GetSummaryFieldDefaultFiltersProduct):
        module (GetSummaryFieldDefaultFiltersModule):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSummaryFieldDefaultFiltersResponse | ProblemDetails | SummaryFieldDefaultFilterErrorCodes
    """

    return (
        await asyncio_detailed(
            summary_field_id=summary_field_id,
            client=client,
            product=product,
            module=module,
        )
    ).parsed

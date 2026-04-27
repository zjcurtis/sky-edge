from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request_400_response_types import BadRequest400ResponseTypes
from ...models.get_tax_declaration_list_by_constituent_id_sort_direction import (
    GetTaxDeclarationListByConstituentIdSortDirection,
)
from ...models.get_tax_declaration_list_by_constituent_id_tax_declaration_sort_fields import (
    GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields,
)
from ...models.problem_details import ProblemDetails
from ...models.tax_declaration_collection import TaxDeclarationCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    constituent_id: str,
    *,
    sort_direction: GetTaxDeclarationListByConstituentIdSortDirection
    | Unset = GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING,
    sort_by: GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields
    | Unset = GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_sort_direction: str | Unset = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/taxdeclarations/constituents/{constituent_id}".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection | None:
    if response.status_code == 200:
        response_200 = TaxDeclarationCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = BadRequest400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
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
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetTaxDeclarationListByConstituentIdSortDirection
    | Unset = GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING,
    sort_by: GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields
    | Unset = GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection]:
    """Get tax declarations for constituent (PREVIEW)

     Returned tax declarations by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetTaxDeclarationListByConstituentIdSortDirection | Unset):  Default:
            GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING.
        sort_by (GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields | Unset):  Default:
            GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        sort_direction=sort_direction,
        sort_by=sort_by,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetTaxDeclarationListByConstituentIdSortDirection
    | Unset = GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING,
    sort_by: GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields
    | Unset = GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection | None:
    """Get tax declarations for constituent (PREVIEW)

     Returned tax declarations by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetTaxDeclarationListByConstituentIdSortDirection | Unset):  Default:
            GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING.
        sort_by (GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields | Unset):  Default:
            GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
        sort_direction=sort_direction,
        sort_by=sort_by,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetTaxDeclarationListByConstituentIdSortDirection
    | Unset = GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING,
    sort_by: GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields
    | Unset = GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Response[Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection]:
    """Get tax declarations for constituent (PREVIEW)

     Returned tax declarations by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetTaxDeclarationListByConstituentIdSortDirection | Unset):  Default:
            GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING.
        sort_by (GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields | Unset):  Default:
            GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        sort_direction=sort_direction,
        sort_by=sort_by,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    sort_direction: GetTaxDeclarationListByConstituentIdSortDirection
    | Unset = GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING,
    sort_by: GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields
    | Unset = GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE,
    limit: int | Unset = 500,
    offset: int | Unset = 0,
) -> Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection | None:
    """Get tax declarations for constituent (PREVIEW)

     Returned tax declarations by constituent ID

    ***This endpoint is in PREVIEW and may be changed or removed at any time.***

    Args:
        constituent_id (str):
        sort_direction (GetTaxDeclarationListByConstituentIdSortDirection | Unset):  Default:
            GetTaxDeclarationListByConstituentIdSortDirection.ASCENDING.
        sort_by (GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields | Unset):  Default:
            GetTaxDeclarationListByConstituentIdTaxDeclarationSortFields.STARTDATE.
        limit (int | Unset):  Default: 500.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BadRequest400ResponseTypes | ProblemDetails | TaxDeclarationCollection
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            sort_direction=sort_direction,
            sort_by=sort_by,
            limit=limit,
            offset=offset,
        )
    ).parsed

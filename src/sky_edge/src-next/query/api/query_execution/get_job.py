from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.blob_content_disposition import BlobContentDisposition
from ...models.get_job_module import GetJobModule
from ...models.get_job_product import GetJobProduct
from ...models.include_read_url import IncludeReadUrl
from ...models.problem_details import ProblemDetails
from ...models.query_definition_service_error_codes import QueryDefinitionServiceErrorCodes
from ...models.query_execution_job import QueryExecutionJob
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    product: GetJobProduct,
    module: GetJobModule,
    include_read_url: IncludeReadUrl | Unset = UNSET,
    content_disposition: BlobContentDisposition | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_product = product.value
    params["product"] = json_product

    json_module = module.value
    params["module"] = json_module

    json_include_read_url: str | Unset = UNSET
    if not isinstance(include_read_url, Unset):
        json_include_read_url = include_read_url.value

    params["include_read_url"] = json_include_read_url

    json_content_disposition: str | Unset = UNSET
    if not isinstance(content_disposition, Unset):
        json_content_disposition = content_disposition.value

    params["content_disposition"] = json_content_disposition

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/jobs/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob | None:
    if response.status_code == 200:
        response_200 = QueryExecutionJob.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob]:
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
    product: GetJobProduct,
    module: GetJobModule,
    include_read_url: IncludeReadUrl | Unset = UNSET,
    content_disposition: BlobContentDisposition | Unset = UNSET,
) -> Response[ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob]:
    """Query execution job status

     Gets information about a background query execution job. Jobs and query results will be available
    for approximately 30 days after creation. For RE requests, the Analysis - Query - Export permission
    is required to use this endpoint.

    Args:
        id (str):
        product (GetJobProduct):
        module (GetJobModule):
        include_read_url (IncludeReadUrl | Unset): Indicates when the SAS URL to retrieve the
            results should be included on the job response<p>Members:</p><ul><li><i>Never</i> -
            Never</li><li><i>OnceRunning</i> - When the job has status Running or
            Completed</li><li><i>OnceCompleted</i> - When the job has status Completed</li></ul>
        content_disposition (BlobContentDisposition | Unset): Indicates whether the content will
            be displayed inline in the browser or as an attachment<p>Members:</p><ul><li><i>Inline</i>
            - The content will be displayed as a web page or as part of a web
            page</li><li><i>Attachment</i> - The content will be downloaded and saved
            locally</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob]
    """

    kwargs = _get_kwargs(
        id=id,
        product=product,
        module=module,
        include_read_url=include_read_url,
        content_disposition=content_disposition,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    product: GetJobProduct,
    module: GetJobModule,
    include_read_url: IncludeReadUrl | Unset = UNSET,
    content_disposition: BlobContentDisposition | Unset = UNSET,
) -> ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob | None:
    """Query execution job status

     Gets information about a background query execution job. Jobs and query results will be available
    for approximately 30 days after creation. For RE requests, the Analysis - Query - Export permission
    is required to use this endpoint.

    Args:
        id (str):
        product (GetJobProduct):
        module (GetJobModule):
        include_read_url (IncludeReadUrl | Unset): Indicates when the SAS URL to retrieve the
            results should be included on the job response<p>Members:</p><ul><li><i>Never</i> -
            Never</li><li><i>OnceRunning</i> - When the job has status Running or
            Completed</li><li><i>OnceCompleted</i> - When the job has status Completed</li></ul>
        content_disposition (BlobContentDisposition | Unset): Indicates whether the content will
            be displayed inline in the browser or as an attachment<p>Members:</p><ul><li><i>Inline</i>
            - The content will be displayed as a web page or as part of a web
            page</li><li><i>Attachment</i> - The content will be downloaded and saved
            locally</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob
    """

    return sync_detailed(
        id=id,
        client=client,
        product=product,
        module=module,
        include_read_url=include_read_url,
        content_disposition=content_disposition,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    product: GetJobProduct,
    module: GetJobModule,
    include_read_url: IncludeReadUrl | Unset = UNSET,
    content_disposition: BlobContentDisposition | Unset = UNSET,
) -> Response[ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob]:
    """Query execution job status

     Gets information about a background query execution job. Jobs and query results will be available
    for approximately 30 days after creation. For RE requests, the Analysis - Query - Export permission
    is required to use this endpoint.

    Args:
        id (str):
        product (GetJobProduct):
        module (GetJobModule):
        include_read_url (IncludeReadUrl | Unset): Indicates when the SAS URL to retrieve the
            results should be included on the job response<p>Members:</p><ul><li><i>Never</i> -
            Never</li><li><i>OnceRunning</i> - When the job has status Running or
            Completed</li><li><i>OnceCompleted</i> - When the job has status Completed</li></ul>
        content_disposition (BlobContentDisposition | Unset): Indicates whether the content will
            be displayed inline in the browser or as an attachment<p>Members:</p><ul><li><i>Inline</i>
            - The content will be displayed as a web page or as part of a web
            page</li><li><i>Attachment</i> - The content will be downloaded and saved
            locally</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob]
    """

    kwargs = _get_kwargs(
        id=id,
        product=product,
        module=module,
        include_read_url=include_read_url,
        content_disposition=content_disposition,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    product: GetJobProduct,
    module: GetJobModule,
    include_read_url: IncludeReadUrl | Unset = UNSET,
    content_disposition: BlobContentDisposition | Unset = UNSET,
) -> ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob | None:
    """Query execution job status

     Gets information about a background query execution job. Jobs and query results will be available
    for approximately 30 days after creation. For RE requests, the Analysis - Query - Export permission
    is required to use this endpoint.

    Args:
        id (str):
        product (GetJobProduct):
        module (GetJobModule):
        include_read_url (IncludeReadUrl | Unset): Indicates when the SAS URL to retrieve the
            results should be included on the job response<p>Members:</p><ul><li><i>Never</i> -
            Never</li><li><i>OnceRunning</i> - When the job has status Running or
            Completed</li><li><i>OnceCompleted</i> - When the job has status Completed</li></ul>
        content_disposition (BlobContentDisposition | Unset): Indicates whether the content will
            be displayed inline in the browser or as an attachment<p>Members:</p><ul><li><i>Inline</i>
            - The content will be displayed as a web page or as part of a web
            page</li><li><i>Attachment</i> - The content will be downloaded and saved
            locally</li></ul>

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | QueryDefinitionServiceErrorCodes | QueryExecutionJob
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            product=product,
            module=module,
            include_read_url=include_read_url,
            content_disposition=content_disposition,
        )
    ).parsed

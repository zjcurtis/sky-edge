from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.file_definition import FileDefinition
from ...models.new_document_info import NewDocumentInfo


def _get_kwargs(
    *,
    body: NewDocumentInfo | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/documents",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | FileDefinition | None:
    if response.status_code == 200:
        response_200 = FileDefinition.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | FileDefinition]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewDocumentInfo | Unset = UNSET,
) -> Response[Any | FileDefinition]:
    """Document (Create)

     Creates a document upload location and unique document identifier for physical attachments.

    Args:
        body (NewDocumentInfo | Unset): Cultivation activities often result in physical collateral
            such as images, PDFs, or Word files. The New Document entity allows you to upload these
            files to maintain a holistic view of target constituents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileDefinition]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: NewDocumentInfo | Unset = UNSET,
) -> Any | FileDefinition | None:
    """Document (Create)

     Creates a document upload location and unique document identifier for physical attachments.

    Args:
        body (NewDocumentInfo | Unset): Cultivation activities often result in physical collateral
            such as images, PDFs, or Word files. The New Document entity allows you to upload these
            files to maintain a holistic view of target constituents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileDefinition
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: NewDocumentInfo | Unset = UNSET,
) -> Response[Any | FileDefinition]:
    """Document (Create)

     Creates a document upload location and unique document identifier for physical attachments.

    Args:
        body (NewDocumentInfo | Unset): Cultivation activities often result in physical collateral
            such as images, PDFs, or Word files. The New Document entity allows you to upload these
            files to maintain a holistic view of target constituents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FileDefinition]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: NewDocumentInfo | Unset = UNSET,
) -> Any | FileDefinition | None:
    """Document (Create)

     Creates a document upload location and unique document identifier for physical attachments.

    Args:
        body (NewDocumentInfo | Unset): Cultivation activities often result in physical collateral
            such as images, PDFs, or Word files. The New Document entity allows you to upload these
            files to maintain a holistic view of target constituents.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FileDefinition
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

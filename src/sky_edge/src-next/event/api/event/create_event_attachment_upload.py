from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment_document_upload import AttachmentDocumentUpload
from ...models.attachment_file_definition import AttachmentFileDefinition
from ...models.service_error import ServiceError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AttachmentDocumentUpload | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/eventattachmentupload",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AttachmentFileDefinition | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = AttachmentFileDefinition.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ServiceError.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = ServiceError.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AttachmentFileDefinition | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentDocumentUpload | Unset = UNSET,
) -> Response[AttachmentFileDefinition | list[ServiceError]]:
    """Create an event attachment upload

     Creates a document upload location and unique document identifier for physical attachments. Use the
    returned url to upload a physical file for an attachment, then call the Create an event attachment
    endpoint. Maximum file size is 100MB.

    Args:
        body (AttachmentDocumentUpload | Unset): An object that represents the physical attachment
            to upload.
            An attachment is information you save to a record, such as images, PDFs, or Word files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentFileDefinition | list[ServiceError]]
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
    body: AttachmentDocumentUpload | Unset = UNSET,
) -> AttachmentFileDefinition | list[ServiceError] | None:
    """Create an event attachment upload

     Creates a document upload location and unique document identifier for physical attachments. Use the
    returned url to upload a physical file for an attachment, then call the Create an event attachment
    endpoint. Maximum file size is 100MB.

    Args:
        body (AttachmentDocumentUpload | Unset): An object that represents the physical attachment
            to upload.
            An attachment is information you save to a record, such as images, PDFs, or Word files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentFileDefinition | list[ServiceError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentDocumentUpload | Unset = UNSET,
) -> Response[AttachmentFileDefinition | list[ServiceError]]:
    """Create an event attachment upload

     Creates a document upload location and unique document identifier for physical attachments. Use the
    returned url to upload a physical file for an attachment, then call the Create an event attachment
    endpoint. Maximum file size is 100MB.

    Args:
        body (AttachmentDocumentUpload | Unset): An object that represents the physical attachment
            to upload.
            An attachment is information you save to a record, such as images, PDFs, or Word files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachmentFileDefinition | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AttachmentDocumentUpload | Unset = UNSET,
) -> AttachmentFileDefinition | list[ServiceError] | None:
    """Create an event attachment upload

     Creates a document upload location and unique document identifier for physical attachments. Use the
    returned url to upload a physical file for an attachment, then call the Create an event attachment
    endpoint. Maximum file size is 100MB.

    Args:
        body (AttachmentDocumentUpload | Unset): An object that represents the physical attachment
            to upload.
            An attachment is information you save to a record, such as images, PDFs, or Word files.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachmentFileDefinition | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

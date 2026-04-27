from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.education_read import EducationRead


def _get_kwargs(
    education_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/educations/{education_id}".format(
            education_id=quote(str(education_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EducationRead | None:
    if response.status_code == 200:
        response_200 = EducationRead.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EducationRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    education_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | EducationRead]:
    """Education (Get)

     Returns an education record.

    Args:
        education_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EducationRead]
    """

    kwargs = _get_kwargs(
        education_id=education_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    education_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | EducationRead | None:
    """Education (Get)

     Returns an education record.

    Args:
        education_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EducationRead
    """

    return sync_detailed(
        education_id=education_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    education_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | EducationRead]:
    """Education (Get)

     Returns an education record.

    Args:
        education_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EducationRead]
    """

    kwargs = _get_kwargs(
        education_id=education_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    education_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | EducationRead | None:
    """Education (Get)

     Returns an education record.

    Args:
        education_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EducationRead
    """

    return (
        await asyncio_detailed(
            education_id=education_id,
            client=client,
        )
    ).parsed

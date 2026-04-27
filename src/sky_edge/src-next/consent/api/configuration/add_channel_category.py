from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_channel_category_400_response_types import AddChannelCategory400ResponseTypes
from ...models.consent_channel_category_write import ConsentChannelCategoryWrite
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ConsentChannelCategoryWrite | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/configuration/channels",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddChannelCategory400ResponseTypes | Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = AddChannelCategory400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddChannelCategory400ResponseTypes | Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentChannelCategoryWrite | Unset = UNSET,
) -> Response[AddChannelCategory400ResponseTypes | Any | ProblemDetails]:
    """Add channel category.

     Add consent configuration for a channel and category.

    Args:
        body (ConsentChannelCategoryWrite | Unset): Represents a request to configure a consent
            channel category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddChannelCategory400ResponseTypes | Any | ProblemDetails]
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
    body: ConsentChannelCategoryWrite | Unset = UNSET,
) -> AddChannelCategory400ResponseTypes | Any | ProblemDetails | None:
    """Add channel category.

     Add consent configuration for a channel and category.

    Args:
        body (ConsentChannelCategoryWrite | Unset): Represents a request to configure a consent
            channel category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddChannelCategory400ResponseTypes | Any | ProblemDetails
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentChannelCategoryWrite | Unset = UNSET,
) -> Response[AddChannelCategory400ResponseTypes | Any | ProblemDetails]:
    """Add channel category.

     Add consent configuration for a channel and category.

    Args:
        body (ConsentChannelCategoryWrite | Unset): Represents a request to configure a consent
            channel category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddChannelCategory400ResponseTypes | Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConsentChannelCategoryWrite | Unset = UNSET,
) -> AddChannelCategory400ResponseTypes | Any | ProblemDetails | None:
    """Add channel category.

     Add consent configuration for a channel and category.

    Args:
        body (ConsentChannelCategoryWrite | Unset): Represents a request to configure a consent
            channel category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddChannelCategory400ResponseTypes | Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

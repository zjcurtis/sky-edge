from http import HTTPStatus
from typing import Any

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.create_subscription_bad_request_response import (
    CreateSubscriptionBadRequestResponse,
)
from ...models.problem_details import ProblemDetails
from ...models.subscription_created import SubscriptionCreated
from ...models.subscription_request import SubscriptionRequest


def _get_kwargs(
    *,
    body: SubscriptionRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/subscriptions",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated | None:
    if response.status_code == 200:
        response_200 = SubscriptionCreated.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = CreateSubscriptionBadRequestResponse.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 409:
        response_409 = ProblemDetails.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubscriptionRequest | Unset = UNSET,
) -> Response[
    CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated
]:
    """Create a subscription

     Creates a subscription in your application. This subscription is scoped to the Blackbaud Environment
    authorized by your SKY API access token.

    Args:
        body (SubscriptionRequest | Unset): The request for the Webhook subscription.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated]
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
    body: SubscriptionRequest | Unset = UNSET,
) -> CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated | None:
    """Create a subscription

     Creates a subscription in your application. This subscription is scoped to the Blackbaud Environment
    authorized by your SKY API access token.

    Args:
        body (SubscriptionRequest | Unset): The request for the Webhook subscription.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubscriptionRequest | Unset = UNSET,
) -> Response[
    CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated
]:
    """Create a subscription

     Creates a subscription in your application. This subscription is scoped to the Blackbaud Environment
    authorized by your SKY API access token.

    Args:
        body (SubscriptionRequest | Unset): The request for the Webhook subscription.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SubscriptionRequest | Unset = UNSET,
) -> CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated | None:
    """Create a subscription

     Creates a subscription in your application. This subscription is scoped to the Blackbaud Environment
    authorized by your SKY API access token.

    Args:
        body (SubscriptionRequest | Unset): The request for the Webhook subscription.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSubscriptionBadRequestResponse | ProblemDetails | SubscriptionCreated
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

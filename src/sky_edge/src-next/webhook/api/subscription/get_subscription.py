from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_subscription_bad_request_response import GetSubscriptionBadRequestResponse
from ...models.problem_details import ProblemDetails
from ...models.subscription import Subscription
from ...types import Response


def _get_kwargs(
    subscription_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/subscriptions/{subscription_id}".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetSubscriptionBadRequestResponse | ProblemDetails | Subscription | None:
    if response.status_code == 200:
        response_200 = Subscription.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetSubscriptionBadRequestResponse.from_dict(response.json())

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
) -> Response[GetSubscriptionBadRequestResponse | ProblemDetails | Subscription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSubscriptionBadRequestResponse | ProblemDetails | Subscription]:
    """Get a subscription

     Returns subscription information for a specific application and subscription ID. The subscription is
    scoped to the Blackbaud Environment authorized by your SKY API access token.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionBadRequestResponse | ProblemDetails | Subscription]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSubscriptionBadRequestResponse | ProblemDetails | Subscription | None:
    """Get a subscription

     Returns subscription information for a specific application and subscription ID. The subscription is
    scoped to the Blackbaud Environment authorized by your SKY API access token.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionBadRequestResponse | ProblemDetails | Subscription
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GetSubscriptionBadRequestResponse | ProblemDetails | Subscription]:
    """Get a subscription

     Returns subscription information for a specific application and subscription ID. The subscription is
    scoped to the Blackbaud Environment authorized by your SKY API access token.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetSubscriptionBadRequestResponse | ProblemDetails | Subscription]
    """

    kwargs = _get_kwargs(
        subscription_id=subscription_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> GetSubscriptionBadRequestResponse | ProblemDetails | Subscription | None:
    """Get a subscription

     Returns subscription information for a specific application and subscription ID. The subscription is
    scoped to the Blackbaud Environment authorized by your SKY API access token.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetSubscriptionBadRequestResponse | ProblemDetails | Subscription
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import Response

from ...models.problem_details import ProblemDetails
from ...models.send_test_payload_to_subscription_bad_request_response import (
    SendTestPayloadToSubscriptionBadRequestResponse,
)


def _get_kwargs(
    subscription_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/utilities/subscriptions/{subscription_id}/testpayload".format(
            subscription_id=quote(str(subscription_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = SendTestPayloadToSubscriptionBadRequestResponse.from_dict(
            response.json()
        )

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
) -> Response[Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse]:
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
) -> Response[Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse]:
    """Create a subscription test payload

     Sends a test event to your subscription's webhook URL. Use this event to verify that your
    subscription is configured correctly. This payload uses a special event type,
    'com.blackbaud.utility.testpayload.v1', so that your webhook can identify the test.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse]
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
) -> Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse | None:
    """Create a subscription test payload

     Sends a test event to your subscription's webhook URL. Use this event to verify that your
    subscription is configured correctly. This payload uses a special event type,
    'com.blackbaud.utility.testpayload.v1', so that your webhook can identify the test.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse
    """

    return sync_detailed(
        subscription_id=subscription_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    subscription_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse]:
    """Create a subscription test payload

     Sends a test event to your subscription's webhook URL. Use this event to verify that your
    subscription is configured correctly. This payload uses a special event type,
    'com.blackbaud.utility.testpayload.v1', so that your webhook can identify the test.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse]
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
) -> Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse | None:
    """Create a subscription test payload

     Sends a test event to your subscription's webhook URL. Use this event to verify that your
    subscription is configured correctly. This payload uses a special event type,
    'com.blackbaud.utility.testpayload.v1', so that your webhook can identify the test.

    Args:
        subscription_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails | SendTestPayloadToSubscriptionBadRequestResponse
    """

    return (
        await asyncio_detailed(
            subscription_id=subscription_id,
            client=client,
        )
    ).parsed

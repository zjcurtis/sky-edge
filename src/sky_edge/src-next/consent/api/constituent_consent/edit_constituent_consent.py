from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.update_consent_request import UpdateConsentRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    consent_id: str,
    *,
    body: UpdateConsentRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/constituents/consents/{consent_id}".format(
            consent_id=quote(str(consent_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    consent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateConsentRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Edit constituent consent.

     Edit a constituent consent.

    Args:
        consent_id (str):
        body (UpdateConsentRequest | Unset): Defines model to represent update consent request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    consent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateConsentRequest | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Edit constituent consent.

     Edit a constituent consent.

    Args:
        consent_id (str):
        body (UpdateConsentRequest | Unset): Defines model to represent update consent request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        consent_id=consent_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    consent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateConsentRequest | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Edit constituent consent.

     Edit a constituent consent.

    Args:
        consent_id (str):
        body (UpdateConsentRequest | Unset): Defines model to represent update consent request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        consent_id=consent_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    consent_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateConsentRequest | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Edit constituent consent.

     Edit a constituent consent.

    Args:
        consent_id (str):
        body (UpdateConsentRequest | Unset): Defines model to represent update consent request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            consent_id=consent_id,
            client=client,
            body=body,
        )
    ).parsed

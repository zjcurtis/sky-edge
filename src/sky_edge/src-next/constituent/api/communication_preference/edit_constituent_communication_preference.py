from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.communication_preference_edit import CommunicationPreferenceEdit
from ...types import UNSET, Response, Unset


def _get_kwargs(
    communication_preference_id: str,
    *,
    body: CommunicationPreferenceEdit | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/communicationpreferences/{communication_preference_id}".format(
            communication_preference_id=quote(str(communication_preference_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    communication_preference_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CommunicationPreferenceEdit | Unset = UNSET,
) -> Response[Any]:
    r"""Communication preference (Edit)

     Edits a constituent communication preference. This endpoint will be deprecated in a future version
    of the Constituent API. Please reference the equivalent endpoint, <a
    href=\"https://developer.sky.blackbaud.com/docs/services/communication-
    preference/operations/EditConstituentSolicitCode\">Constituent solicit code (Patch)</a>, in the
    Communication Preference API instead.

    Args:
        communication_preference_id (str):
        body (CommunicationPreferenceEdit | Unset): Communication preferences provide guidance on
            how to contact constituents. These rules describe instructions and restrictions about when
            to reach out to constituents and how to tailor communications to honor their requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        communication_preference_id=communication_preference_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    communication_preference_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CommunicationPreferenceEdit | Unset = UNSET,
) -> Response[Any]:
    r"""Communication preference (Edit)

     Edits a constituent communication preference. This endpoint will be deprecated in a future version
    of the Constituent API. Please reference the equivalent endpoint, <a
    href=\"https://developer.sky.blackbaud.com/docs/services/communication-
    preference/operations/EditConstituentSolicitCode\">Constituent solicit code (Patch)</a>, in the
    Communication Preference API instead.

    Args:
        communication_preference_id (str):
        body (CommunicationPreferenceEdit | Unset): Communication preferences provide guidance on
            how to contact constituents. These rules describe instructions and restrictions about when
            to reach out to constituents and how to tailor communications to honor their requests.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        communication_preference_id=communication_preference_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)

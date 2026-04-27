from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_collection_of_communication_preference_read import ApiCollectionOfCommunicationPreferenceRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    constituent_id: str,
    *,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/{constituent_id}/communicationpreferences".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionOfCommunicationPreferenceRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionOfCommunicationPreferenceRead.from_dict(response.json())

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
) -> Response[Any | ApiCollectionOfCommunicationPreferenceRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfCommunicationPreferenceRead]:
    r"""Communication preference list (Single constituent)

     Returns a list of communication preferences for a constituent. This endpoint will be deprecated in a
    future version of the Constituent API. Please reference the equivalent endpoint, <a
    href=\"https://developer.sky.blackbaud.com/docs/services/communication-
    preference/operations/ListConstituentSolicitCodesSingleConstituent\">Constituent solicit code list
    (Single constituent)</a>, in the Communication Preference API instead.

    Args:
        constituent_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfCommunicationPreferenceRead]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfCommunicationPreferenceRead | None:
    r"""Communication preference list (Single constituent)

     Returns a list of communication preferences for a constituent. This endpoint will be deprecated in a
    future version of the Constituent API. Please reference the equivalent endpoint, <a
    href=\"https://developer.sky.blackbaud.com/docs/services/communication-
    preference/operations/ListConstituentSolicitCodesSingleConstituent\">Constituent solicit code list
    (Single constituent)</a>, in the Communication Preference API instead.

    Args:
        constituent_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfCommunicationPreferenceRead
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionOfCommunicationPreferenceRead]:
    r"""Communication preference list (Single constituent)

     Returns a list of communication preferences for a constituent. This endpoint will be deprecated in a
    future version of the Constituent API. Please reference the equivalent endpoint, <a
    href=\"https://developer.sky.blackbaud.com/docs/services/communication-
    preference/operations/ListConstituentSolicitCodesSingleConstituent\">Constituent solicit code list
    (Single constituent)</a>, in the Communication Preference API instead.

    Args:
        constituent_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionOfCommunicationPreferenceRead]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionOfCommunicationPreferenceRead | None:
    r"""Communication preference list (Single constituent)

     Returns a list of communication preferences for a constituent. This endpoint will be deprecated in a
    future version of the Constituent API. Please reference the equivalent endpoint, <a
    href=\"https://developer.sky.blackbaud.com/docs/services/communication-
    preference/operations/ListConstituentSolicitCodesSingleConstituent\">Constituent solicit code list
    (Single constituent)</a>, in the Communication Preference API instead.

    Args:
        constituent_id (str):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionOfCommunicationPreferenceRead
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed

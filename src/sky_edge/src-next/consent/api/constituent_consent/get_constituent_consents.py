import datetime
from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.consent_reads_collection import ConsentReadsCollection
from ...models.get_constituent_consents_400_response_types import GetConstituentConsents400ResponseTypes
from ...models.get_constituent_consents_channels_item import GetConstituentConsentsChannelsItem
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    constituent_id: str,
    *,
    include_history: bool | Unset = UNSET,
    channels: list[GetConstituentConsentsChannelsItem] | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_history"] = include_history

    json_channels: list[str] | Unset = UNSET
    if not isinstance(channels, Unset):
        json_channels = []
        for channels_item_data in channels:
            channels_item = channels_item_data.value
            json_channels.append(channels_item)

    params["channels"] = json_channels

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["from_date"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["to_date"] = json_to_date

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/{constituent_id}/consents".format(
            constituent_id=quote(str(constituent_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ConsentReadsCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetConstituentConsents400ResponseTypes.from_dict(response.json())

        return response_400

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
) -> Response[Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails]:
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
    include_history: bool | Unset = UNSET,
    channels: list[GetConstituentConsentsChannelsItem] | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Response[Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails]:
    """Get constituent consents.

     Get the collection of consents for the specified constituent.

    Args:
        constituent_id (str):
        include_history (bool | Unset):
        channels (list[GetConstituentConsentsChannelsItem] | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        include_history=include_history,
        channels=channels,
        from_date=from_date,
        to_date=to_date,
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
    include_history: bool | Unset = UNSET,
    channels: list[GetConstituentConsentsChannelsItem] | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails | None:
    """Get constituent consents.

     Get the collection of consents for the specified constituent.

    Args:
        constituent_id (str):
        include_history (bool | Unset):
        channels (list[GetConstituentConsentsChannelsItem] | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails
    """

    return sync_detailed(
        constituent_id=constituent_id,
        client=client,
        include_history=include_history,
        channels=channels,
        from_date=from_date,
        to_date=to_date,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_history: bool | Unset = UNSET,
    channels: list[GetConstituentConsentsChannelsItem] | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Response[Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails]:
    """Get constituent consents.

     Get the collection of consents for the specified constituent.

    Args:
        constituent_id (str):
        include_history (bool | Unset):
        channels (list[GetConstituentConsentsChannelsItem] | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails]
    """

    kwargs = _get_kwargs(
        constituent_id=constituent_id,
        include_history=include_history,
        channels=channels,
        from_date=from_date,
        to_date=to_date,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    constituent_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_history: bool | Unset = UNSET,
    channels: list[GetConstituentConsentsChannelsItem] | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails | None:
    """Get constituent consents.

     Get the collection of consents for the specified constituent.

    Args:
        constituent_id (str):
        include_history (bool | Unset):
        channels (list[GetConstituentConsentsChannelsItem] | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConsentReadsCollection | GetConstituentConsents400ResponseTypes | ProblemDetails
    """

    return (
        await asyncio_detailed(
            constituent_id=constituent_id,
            client=client,
            include_history=include_history,
            channels=channels,
            from_date=from_date,
            to_date=to_date,
            limit=limit,
            offset=offset,
        )
    ).parsed

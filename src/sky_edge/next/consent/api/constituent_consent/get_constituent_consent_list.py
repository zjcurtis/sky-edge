import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.constituent_consent_read_collection import (
    ConstituentConsentReadCollection,
)
from ...models.get_consent_list_400_response_types import GetConsentList400ResponseTypes
from ...models.get_constituent_consent_list_category_filter_type import (
    GetConstituentConsentListCategoryFilterType,
)
from ...models.get_constituent_consent_list_channels_item import (
    GetConstituentConsentListChannelsItem,
)
from ...models.get_constituent_consent_list_response import (
    GetConstituentConsentListResponse,
)


def _get_kwargs(
    *,
    channels: list[GetConstituentConsentListChannelsItem] | Unset = UNSET,
    constituent_ids: list[str] | Unset = UNSET,
    category_filter_type: GetConstituentConsentListCategoryFilterType | Unset = UNSET,
    category: str | Unset = UNSET,
    response: GetConstituentConsentListResponse | Unset = UNSET,
    source: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_channels: list[str] | Unset = UNSET
    if not isinstance(channels, Unset):
        json_channels = []
        for channels_item_data in channels:
            channels_item = channels_item_data.value
            json_channels.append(channels_item)

    params["channels"] = json_channels

    json_constituent_ids: list[str] | Unset = UNSET
    if not isinstance(constituent_ids, Unset):
        json_constituent_ids = constituent_ids

    params["constituent_ids"] = json_constituent_ids

    json_category_filter_type: str | Unset = UNSET
    if not isinstance(category_filter_type, Unset):
        json_category_filter_type = category_filter_type.value

    params["category_filter_type"] = json_category_filter_type

    params["category"] = category

    json_response: str | Unset = UNSET
    if not isinstance(response, Unset):
        json_response = response.value

    params["response"] = json_response

    params["source"] = source

    json_from_date: str | Unset = UNSET
    if not isinstance(from_date, Unset):
        json_from_date = from_date.isoformat()
    params["from_date"] = json_from_date

    json_to_date: str | Unset = UNSET
    if not isinstance(to_date, Unset):
        json_to_date = to_date.isoformat()
    params["to_date"] = json_to_date

    params["continuation_token"] = continuation_token

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/constituents/consents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes | None:
    if response.status_code == 200:
        response_200 = ConstituentConsentReadCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetConsentList400ResponseTypes.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    channels: list[GetConstituentConsentListChannelsItem] | Unset = UNSET,
    constituent_ids: list[str] | Unset = UNSET,
    category_filter_type: GetConstituentConsentListCategoryFilterType | Unset = UNSET,
    category: str | Unset = UNSET,
    response: GetConstituentConsentListResponse | Unset = UNSET,
    source: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]:
    """Get constituent consent list.

     Get a list of constituent consents.

    Args:
        channels (list[GetConstituentConsentListChannelsItem] | Unset):
        constituent_ids (list[str] | Unset):
        category_filter_type (GetConstituentConsentListCategoryFilterType | Unset):
        category (str | Unset):
        response (GetConstituentConsentListResponse | Unset):
        source (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]
    """

    kwargs = _get_kwargs(
        channels=channels,
        constituent_ids=constituent_ids,
        category_filter_type=category_filter_type,
        category=category,
        response=response,
        source=source,
        from_date=from_date,
        to_date=to_date,
        continuation_token=continuation_token,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    channels: list[GetConstituentConsentListChannelsItem] | Unset = UNSET,
    constituent_ids: list[str] | Unset = UNSET,
    category_filter_type: GetConstituentConsentListCategoryFilterType | Unset = UNSET,
    category: str | Unset = UNSET,
    response: GetConstituentConsentListResponse | Unset = UNSET,
    source: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes | None:
    """Get constituent consent list.

     Get a list of constituent consents.

    Args:
        channels (list[GetConstituentConsentListChannelsItem] | Unset):
        constituent_ids (list[str] | Unset):
        category_filter_type (GetConstituentConsentListCategoryFilterType | Unset):
        category (str | Unset):
        response (GetConstituentConsentListResponse | Unset):
        source (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes
    """

    return sync_detailed(
        client=client,
        channels=channels,
        constituent_ids=constituent_ids,
        category_filter_type=category_filter_type,
        category=category,
        response=response,
        source=source,
        from_date=from_date,
        to_date=to_date,
        continuation_token=continuation_token,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    channels: list[GetConstituentConsentListChannelsItem] | Unset = UNSET,
    constituent_ids: list[str] | Unset = UNSET,
    category_filter_type: GetConstituentConsentListCategoryFilterType | Unset = UNSET,
    category: str | Unset = UNSET,
    response: GetConstituentConsentListResponse | Unset = UNSET,
    source: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]:
    """Get constituent consent list.

     Get a list of constituent consents.

    Args:
        channels (list[GetConstituentConsentListChannelsItem] | Unset):
        constituent_ids (list[str] | Unset):
        category_filter_type (GetConstituentConsentListCategoryFilterType | Unset):
        category (str | Unset):
        response (GetConstituentConsentListResponse | Unset):
        source (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes]
    """

    kwargs = _get_kwargs(
        channels=channels,
        constituent_ids=constituent_ids,
        category_filter_type=category_filter_type,
        category=category,
        response=response,
        source=source,
        from_date=from_date,
        to_date=to_date,
        continuation_token=continuation_token,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    channels: list[GetConstituentConsentListChannelsItem] | Unset = UNSET,
    constituent_ids: list[str] | Unset = UNSET,
    category_filter_type: GetConstituentConsentListCategoryFilterType | Unset = UNSET,
    category: str | Unset = UNSET,
    response: GetConstituentConsentListResponse | Unset = UNSET,
    source: str | Unset = UNSET,
    from_date: datetime.datetime | Unset = UNSET,
    to_date: datetime.datetime | Unset = UNSET,
    continuation_token: str | Unset = UNSET,
    limit: int | Unset = 500,
    offset: int | Unset = UNSET,
) -> Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes | None:
    """Get constituent consent list.

     Get a list of constituent consents.

    Args:
        channels (list[GetConstituentConsentListChannelsItem] | Unset):
        constituent_ids (list[str] | Unset):
        category_filter_type (GetConstituentConsentListCategoryFilterType | Unset):
        category (str | Unset):
        response (GetConstituentConsentListResponse | Unset):
        source (str | Unset):
        from_date (datetime.datetime | Unset):
        to_date (datetime.datetime | Unset):
        continuation_token (str | Unset):
        limit (int | Unset):  Default: 500.
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ConstituentConsentReadCollection | GetConsentList400ResponseTypes
    """

    return (
        await asyncio_detailed(
            client=client,
            channels=channels,
            constituent_ids=constituent_ids,
            category_filter_type=category_filter_type,
            category=category,
            response=response,
            source=source,
            from_date=from_date,
            to_date=to_date,
            continuation_token=continuation_token,
            limit=limit,
            offset=offset,
        )
    ).parsed

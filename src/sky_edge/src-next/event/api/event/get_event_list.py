import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_list_entry_collection import EventListEntryCollection
from ...models.service_error import ServiceError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    category: str | Unset = UNSET,
    event_id: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    params["lookup_id"] = lookup_id

    params["category"] = category

    params["event_id"] = event_id

    json_start_date_from: str | Unset = UNSET
    if not isinstance(start_date_from, Unset):
        json_start_date_from = start_date_from.isoformat()
    params["start_date_from"] = json_start_date_from

    json_start_date_to: str | Unset = UNSET
    if not isinstance(start_date_to, Unset):
        json_start_date_to = start_date_to.isoformat()
    params["start_date_to"] = json_start_date_to

    json_date_added: str | Unset = UNSET
    if not isinstance(date_added, Unset):
        json_date_added = date_added.isoformat()
    params["date_added"] = json_date_added

    json_last_modified: str | Unset = UNSET
    if not isinstance(last_modified, Unset):
        json_last_modified = last_modified.isoformat()
    params["last_modified"] = json_last_modified

    json_fields: list[str] | Unset = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["include_inactive"] = include_inactive

    params["group"] = group

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/eventlist",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EventListEntryCollection | list[ServiceError] | None:
    if response.status_code == 200:
        response_200 = EventListEntryCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = []
        _response_400 = response.json()
        for response_400_item_data in _response_400:
            response_400_item = ServiceError.from_dict(response_400_item_data)

            response_400.append(response_400_item)

        return response_400

    if response.status_code == 403:
        response_403 = []
        _response_403 = response.json()
        for response_403_item_data in _response_403:
            response_403_item = ServiceError.from_dict(response_403_item_data)

            response_403.append(response_403_item)

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EventListEntryCollection | list[ServiceError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    category: str | Unset = UNSET,
    event_id: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[EventListEntryCollection | list[ServiceError]]:
    """Get event list

     Returns a paginated list of events.

    Args:
        name (str | Unset):
        lookup_id (str | Unset):
        category (str | Unset):
        event_id (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        include_inactive (bool | Unset):
        group (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventListEntryCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        name=name,
        lookup_id=lookup_id,
        category=category,
        event_id=event_id,
        start_date_from=start_date_from,
        start_date_to=start_date_to,
        date_added=date_added,
        last_modified=last_modified,
        fields=fields,
        sort=sort,
        include_inactive=include_inactive,
        group=group,
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
    name: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    category: str | Unset = UNSET,
    event_id: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> EventListEntryCollection | list[ServiceError] | None:
    """Get event list

     Returns a paginated list of events.

    Args:
        name (str | Unset):
        lookup_id (str | Unset):
        category (str | Unset):
        event_id (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        include_inactive (bool | Unset):
        group (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventListEntryCollection | list[ServiceError]
    """

    return sync_detailed(
        client=client,
        name=name,
        lookup_id=lookup_id,
        category=category,
        event_id=event_id,
        start_date_from=start_date_from,
        start_date_to=start_date_to,
        date_added=date_added,
        last_modified=last_modified,
        fields=fields,
        sort=sort,
        include_inactive=include_inactive,
        group=group,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    category: str | Unset = UNSET,
    event_id: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[EventListEntryCollection | list[ServiceError]]:
    """Get event list

     Returns a paginated list of events.

    Args:
        name (str | Unset):
        lookup_id (str | Unset):
        category (str | Unset):
        event_id (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        include_inactive (bool | Unset):
        group (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EventListEntryCollection | list[ServiceError]]
    """

    kwargs = _get_kwargs(
        name=name,
        lookup_id=lookup_id,
        category=category,
        event_id=event_id,
        start_date_from=start_date_from,
        start_date_to=start_date_to,
        date_added=date_added,
        last_modified=last_modified,
        fields=fields,
        sort=sort,
        include_inactive=include_inactive,
        group=group,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    name: str | Unset = UNSET,
    lookup_id: str | Unset = UNSET,
    category: str | Unset = UNSET,
    event_id: str | Unset = UNSET,
    start_date_from: datetime.date | Unset = UNSET,
    start_date_to: datetime.date | Unset = UNSET,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    fields: list[str] | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    include_inactive: bool | Unset = UNSET,
    group: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> EventListEntryCollection | list[ServiceError] | None:
    """Get event list

     Returns a paginated list of events.

    Args:
        name (str | Unset):
        lookup_id (str | Unset):
        category (str | Unset):
        event_id (str | Unset):
        start_date_from (datetime.date | Unset):
        start_date_to (datetime.date | Unset):
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        fields (list[str] | Unset):
        sort (list[str] | Unset):
        include_inactive (bool | Unset):
        group (str | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EventListEntryCollection | list[ServiceError]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            lookup_id=lookup_id,
            category=category,
            event_id=event_id,
            start_date_from=start_date_from,
            start_date_to=start_date_to,
            date_added=date_added,
            last_modified=last_modified,
            fields=fields,
            sort=sort,
            include_inactive=include_inactive,
            group=group,
            limit=limit,
            offset=offset,
        )
    ).parsed

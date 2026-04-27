import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.api_collection_gift_read import ApiCollectionGiftRead


def _get_kwargs(
    *,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    post_status: list[str] | Unset = UNSET,
    gift_type: list[str] | Unset = UNSET,
    receipt_status: list[str] | Unset = UNSET,
    acknowledgement_status: list[str] | Unset = UNSET,
    campaign_id: list[str] | Unset = UNSET,
    fund_id: list[str] | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    start_gift_date: datetime.datetime | Unset = UNSET,
    end_gift_date: datetime.datetime | Unset = UNSET,
    start_gift_amount: float | Unset = UNSET,
    end_gift_amount: float | Unset = UNSET,
    list_id: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_added: str | Unset = UNSET
    if not isinstance(date_added, Unset):
        json_date_added = date_added.isoformat()
    params["date_added"] = json_date_added

    json_last_modified: str | Unset = UNSET
    if not isinstance(last_modified, Unset):
        json_last_modified = last_modified.isoformat()
    params["last_modified"] = json_last_modified

    params["sort_token"] = sort_token

    json_constituent_id: list[str] | Unset = UNSET
    if not isinstance(constituent_id, Unset):
        json_constituent_id = constituent_id

    params["constituent_id"] = json_constituent_id

    json_post_status: list[str] | Unset = UNSET
    if not isinstance(post_status, Unset):
        json_post_status = post_status

    params["post_status"] = json_post_status

    json_gift_type: list[str] | Unset = UNSET
    if not isinstance(gift_type, Unset):
        json_gift_type = gift_type

    params["gift_type"] = json_gift_type

    json_receipt_status: list[str] | Unset = UNSET
    if not isinstance(receipt_status, Unset):
        json_receipt_status = receipt_status

    params["receipt_status"] = json_receipt_status

    json_acknowledgement_status: list[str] | Unset = UNSET
    if not isinstance(acknowledgement_status, Unset):
        json_acknowledgement_status = acknowledgement_status

    params["acknowledgement_status"] = json_acknowledgement_status

    json_campaign_id: list[str] | Unset = UNSET
    if not isinstance(campaign_id, Unset):
        json_campaign_id = campaign_id

    params["campaign_id"] = json_campaign_id

    json_fund_id: list[str] | Unset = UNSET
    if not isinstance(fund_id, Unset):
        json_fund_id = fund_id

    params["fund_id"] = json_fund_id

    json_appeal_id: list[str] | Unset = UNSET
    if not isinstance(appeal_id, Unset):
        json_appeal_id = appeal_id

    params["appeal_id"] = json_appeal_id

    json_start_gift_date: str | Unset = UNSET
    if not isinstance(start_gift_date, Unset):
        json_start_gift_date = start_gift_date.isoformat()
    params["start_gift_date"] = json_start_gift_date

    json_end_gift_date: str | Unset = UNSET
    if not isinstance(end_gift_date, Unset):
        json_end_gift_date = end_gift_date.isoformat()
    params["end_gift_date"] = json_end_gift_date

    params["start_gift_amount"] = start_gift_amount

    params["end_gift_amount"] = end_gift_amount

    params["list_id"] = list_id

    json_sort: list[str] | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/gifts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ApiCollectionGiftRead | None:
    if response.status_code == 200:
        response_200 = ApiCollectionGiftRead.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
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
) -> Response[Any | ApiCollectionGiftRead]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    post_status: list[str] | Unset = UNSET,
    gift_type: list[str] | Unset = UNSET,
    receipt_status: list[str] | Unset = UNSET,
    acknowledgement_status: list[str] | Unset = UNSET,
    campaign_id: list[str] | Unset = UNSET,
    fund_id: list[str] | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    start_gift_date: datetime.datetime | Unset = UNSET,
    end_gift_date: datetime.datetime | Unset = UNSET,
    start_gift_amount: float | Unset = UNSET,
    end_gift_amount: float | Unset = UNSET,
    list_id: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionGiftRead]:
    """Gift list

     Returns a paginated list of gifts.
    <p />
    The default sorting behavior is to list gifts in ascending order based on the <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    gifts in ascending order based on when they were last modified, and the <code>date_added</code>
    parameter overrides the default sorting behavior to list gifts in ascending order based on when they
    were created. The <code>last_modified</code> and <code>date_added</code> parameters also add the
    <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that gifts are stably
    sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list gifts based on when they were last modified.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        post_status (list[str] | Unset):
        gift_type (list[str] | Unset):
        receipt_status (list[str] | Unset):
        acknowledgement_status (list[str] | Unset):
        campaign_id (list[str] | Unset):
        fund_id (list[str] | Unset):
        appeal_id (list[str] | Unset):
        start_gift_date (datetime.datetime | Unset):
        end_gift_date (datetime.datetime | Unset):
        start_gift_amount (float | Unset):
        end_gift_amount (float | Unset):
        list_id (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionGiftRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        constituent_id=constituent_id,
        post_status=post_status,
        gift_type=gift_type,
        receipt_status=receipt_status,
        acknowledgement_status=acknowledgement_status,
        campaign_id=campaign_id,
        fund_id=fund_id,
        appeal_id=appeal_id,
        start_gift_date=start_gift_date,
        end_gift_date=end_gift_date,
        start_gift_amount=start_gift_amount,
        end_gift_amount=end_gift_amount,
        list_id=list_id,
        sort=sort,
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
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    post_status: list[str] | Unset = UNSET,
    gift_type: list[str] | Unset = UNSET,
    receipt_status: list[str] | Unset = UNSET,
    acknowledgement_status: list[str] | Unset = UNSET,
    campaign_id: list[str] | Unset = UNSET,
    fund_id: list[str] | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    start_gift_date: datetime.datetime | Unset = UNSET,
    end_gift_date: datetime.datetime | Unset = UNSET,
    start_gift_amount: float | Unset = UNSET,
    end_gift_amount: float | Unset = UNSET,
    list_id: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionGiftRead | None:
    """Gift list

     Returns a paginated list of gifts.
    <p />
    The default sorting behavior is to list gifts in ascending order based on the <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    gifts in ascending order based on when they were last modified, and the <code>date_added</code>
    parameter overrides the default sorting behavior to list gifts in ascending order based on when they
    were created. The <code>last_modified</code> and <code>date_added</code> parameters also add the
    <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that gifts are stably
    sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list gifts based on when they were last modified.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        post_status (list[str] | Unset):
        gift_type (list[str] | Unset):
        receipt_status (list[str] | Unset):
        acknowledgement_status (list[str] | Unset):
        campaign_id (list[str] | Unset):
        fund_id (list[str] | Unset):
        appeal_id (list[str] | Unset):
        start_gift_date (datetime.datetime | Unset):
        end_gift_date (datetime.datetime | Unset):
        start_gift_amount (float | Unset):
        end_gift_amount (float | Unset):
        list_id (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionGiftRead
    """

    return sync_detailed(
        client=client,
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        constituent_id=constituent_id,
        post_status=post_status,
        gift_type=gift_type,
        receipt_status=receipt_status,
        acknowledgement_status=acknowledgement_status,
        campaign_id=campaign_id,
        fund_id=fund_id,
        appeal_id=appeal_id,
        start_gift_date=start_gift_date,
        end_gift_date=end_gift_date,
        start_gift_amount=start_gift_amount,
        end_gift_amount=end_gift_amount,
        list_id=list_id,
        sort=sort,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    post_status: list[str] | Unset = UNSET,
    gift_type: list[str] | Unset = UNSET,
    receipt_status: list[str] | Unset = UNSET,
    acknowledgement_status: list[str] | Unset = UNSET,
    campaign_id: list[str] | Unset = UNSET,
    fund_id: list[str] | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    start_gift_date: datetime.datetime | Unset = UNSET,
    end_gift_date: datetime.datetime | Unset = UNSET,
    start_gift_amount: float | Unset = UNSET,
    end_gift_amount: float | Unset = UNSET,
    list_id: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Response[Any | ApiCollectionGiftRead]:
    """Gift list

     Returns a paginated list of gifts.
    <p />
    The default sorting behavior is to list gifts in ascending order based on the <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    gifts in ascending order based on when they were last modified, and the <code>date_added</code>
    parameter overrides the default sorting behavior to list gifts in ascending order based on when they
    were created. The <code>last_modified</code> and <code>date_added</code> parameters also add the
    <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that gifts are stably
    sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list gifts based on when they were last modified.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        post_status (list[str] | Unset):
        gift_type (list[str] | Unset):
        receipt_status (list[str] | Unset):
        acknowledgement_status (list[str] | Unset):
        campaign_id (list[str] | Unset):
        fund_id (list[str] | Unset):
        appeal_id (list[str] | Unset):
        start_gift_date (datetime.datetime | Unset):
        end_gift_date (datetime.datetime | Unset):
        start_gift_amount (float | Unset):
        end_gift_amount (float | Unset):
        list_id (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ApiCollectionGiftRead]
    """

    kwargs = _get_kwargs(
        date_added=date_added,
        last_modified=last_modified,
        sort_token=sort_token,
        constituent_id=constituent_id,
        post_status=post_status,
        gift_type=gift_type,
        receipt_status=receipt_status,
        acknowledgement_status=acknowledgement_status,
        campaign_id=campaign_id,
        fund_id=fund_id,
        appeal_id=appeal_id,
        start_gift_date=start_gift_date,
        end_gift_date=end_gift_date,
        start_gift_amount=start_gift_amount,
        end_gift_amount=end_gift_amount,
        list_id=list_id,
        sort=sort,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    date_added: datetime.datetime | Unset = UNSET,
    last_modified: datetime.datetime | Unset = UNSET,
    sort_token: str | Unset = UNSET,
    constituent_id: list[str] | Unset = UNSET,
    post_status: list[str] | Unset = UNSET,
    gift_type: list[str] | Unset = UNSET,
    receipt_status: list[str] | Unset = UNSET,
    acknowledgement_status: list[str] | Unset = UNSET,
    campaign_id: list[str] | Unset = UNSET,
    fund_id: list[str] | Unset = UNSET,
    appeal_id: list[str] | Unset = UNSET,
    start_gift_date: datetime.datetime | Unset = UNSET,
    end_gift_date: datetime.datetime | Unset = UNSET,
    start_gift_amount: float | Unset = UNSET,
    end_gift_amount: float | Unset = UNSET,
    list_id: str | Unset = UNSET,
    sort: list[str] | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = UNSET,
) -> Any | ApiCollectionGiftRead | None:
    """Gift list

     Returns a paginated list of gifts.
    <p />
    The default sorting behavior is to list gifts in ascending order based on the <code>id</code>.
    <p />
    However, the <code>last_modified</code> parameter overrides the default sorting behavior to list
    gifts in ascending order based on when they were last modified, and the <code>date_added</code>
    parameter overrides the default sorting behavior to list gifts in ascending order based on when they
    were created. The <code>last_modified</code> and <code>date_added</code> parameters also add the
    <code>sort_token</code> parameter to the <code>next_link</code> URL to ensure that gifts are stably
    sorted and that order persists when changes occur while working through a paginated list.
    <p />
    If the <code>last_modified</code> and <code>date_added</code> parameters are both specified, the
    sorting behavior is to list gifts based on when they were last modified.
    <p /><b>Note:</b> This endpoint returns data with an average latency of about 30 minutes.

    Args:
        date_added (datetime.datetime | Unset):
        last_modified (datetime.datetime | Unset):
        sort_token (str | Unset):
        constituent_id (list[str] | Unset):
        post_status (list[str] | Unset):
        gift_type (list[str] | Unset):
        receipt_status (list[str] | Unset):
        acknowledgement_status (list[str] | Unset):
        campaign_id (list[str] | Unset):
        fund_id (list[str] | Unset):
        appeal_id (list[str] | Unset):
        start_gift_date (datetime.datetime | Unset):
        end_gift_date (datetime.datetime | Unset):
        start_gift_amount (float | Unset):
        end_gift_amount (float | Unset):
        list_id (str | Unset):
        sort (list[str] | Unset):
        limit (int | Unset):
        offset (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ApiCollectionGiftRead
    """

    return (
        await asyncio_detailed(
            client=client,
            date_added=date_added,
            last_modified=last_modified,
            sort_token=sort_token,
            constituent_id=constituent_id,
            post_status=post_status,
            gift_type=gift_type,
            receipt_status=receipt_status,
            acknowledgement_status=acknowledgement_status,
            campaign_id=campaign_id,
            fund_id=fund_id,
            appeal_id=appeal_id,
            start_gift_date=start_gift_date,
            end_gift_date=end_gift_date,
            start_gift_amount=start_gift_amount,
            end_gift_amount=end_gift_amount,
            list_id=list_id,
            sort=sort,
            limit=limit,
            offset=offset,
        )
    ).parsed

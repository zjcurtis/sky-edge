from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from sky_edge.next import errors
from sky_edge.next.client import AuthenticatedClient, Client
from sky_edge.next.types import UNSET, Response, Unset

from ...models.batch_gift_add_results import BatchGiftAddResults
from ...models.gifts_add import GiftsAdd


def _get_kwargs(
    batch_id: str,
    *,
    body: GiftsAdd | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/giftbatches/{batch_id}/gifts".format(
            batch_id=quote(str(batch_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | BatchGiftAddResults | None:
    if response.status_code == 200:
        response_200 = BatchGiftAddResults.from_dict(response.json())

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
) -> Response[Any | BatchGiftAddResults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftsAdd | Unset = UNSET,
) -> Response[Any | BatchGiftAddResults]:
    """Gift (Batch)

     Adds one or more gifts to a specified gift batch in the web view.

    Args:
        batch_id (str):
        body (GiftsAdd | Unset):  Example: {'gifts': [{'amount': {'value': 100}, 'constituent_id':
            '280', 'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value':
            100}, 'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id':
            '15', 'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous':
            False, 'lookup_id': '2225', 'payments': [{'payment_method': 'Cash'}], 'post_date':
            '2017-10-03T00:00:00.0000000+00:00', 'post_status': 'NotPosted', 'reference': 'newly added
            gift', 'soft_credits': [{'amount': {'value': 100}, 'constituent_id': '187'}], 'subtype':
            'Annuity', 'type': 'Donation'}, {'amount': {'value': 100}, 'constituent_id': '290',
            'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value': 100},
            'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id': '15',
            'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous': False,
            'lookup_id': '2225', 'origin': '{"name": "Gift origin name"}', 'payments':
            [{'payment_method': 'Cash'}], 'post_date': '2017-10-03T00:00:00.0000000+00:00',
            'post_status': 'NotPosted', 'reference': 'newly added gift', 'soft_credits': [{'amount':
            {'value': 100}, 'constituent_id': '187'}], 'subtype': 'Annuity', 'type': 'Donation',
            'tributes': [{'id': '12'}, {'id': '15', 'tribute_acknowledgees': [{'id': '33'}, {'id':
            '21'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BatchGiftAddResults]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftsAdd | Unset = UNSET,
) -> Any | BatchGiftAddResults | None:
    """Gift (Batch)

     Adds one or more gifts to a specified gift batch in the web view.

    Args:
        batch_id (str):
        body (GiftsAdd | Unset):  Example: {'gifts': [{'amount': {'value': 100}, 'constituent_id':
            '280', 'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value':
            100}, 'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id':
            '15', 'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous':
            False, 'lookup_id': '2225', 'payments': [{'payment_method': 'Cash'}], 'post_date':
            '2017-10-03T00:00:00.0000000+00:00', 'post_status': 'NotPosted', 'reference': 'newly added
            gift', 'soft_credits': [{'amount': {'value': 100}, 'constituent_id': '187'}], 'subtype':
            'Annuity', 'type': 'Donation'}, {'amount': {'value': 100}, 'constituent_id': '290',
            'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value': 100},
            'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id': '15',
            'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous': False,
            'lookup_id': '2225', 'origin': '{"name": "Gift origin name"}', 'payments':
            [{'payment_method': 'Cash'}], 'post_date': '2017-10-03T00:00:00.0000000+00:00',
            'post_status': 'NotPosted', 'reference': 'newly added gift', 'soft_credits': [{'amount':
            {'value': 100}, 'constituent_id': '187'}], 'subtype': 'Annuity', 'type': 'Donation',
            'tributes': [{'id': '12'}, {'id': '15', 'tribute_acknowledgees': [{'id': '33'}, {'id':
            '21'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BatchGiftAddResults
    """

    return sync_detailed(
        batch_id=batch_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftsAdd | Unset = UNSET,
) -> Response[Any | BatchGiftAddResults]:
    """Gift (Batch)

     Adds one or more gifts to a specified gift batch in the web view.

    Args:
        batch_id (str):
        body (GiftsAdd | Unset):  Example: {'gifts': [{'amount': {'value': 100}, 'constituent_id':
            '280', 'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value':
            100}, 'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id':
            '15', 'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous':
            False, 'lookup_id': '2225', 'payments': [{'payment_method': 'Cash'}], 'post_date':
            '2017-10-03T00:00:00.0000000+00:00', 'post_status': 'NotPosted', 'reference': 'newly added
            gift', 'soft_credits': [{'amount': {'value': 100}, 'constituent_id': '187'}], 'subtype':
            'Annuity', 'type': 'Donation'}, {'amount': {'value': 100}, 'constituent_id': '290',
            'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value': 100},
            'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id': '15',
            'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous': False,
            'lookup_id': '2225', 'origin': '{"name": "Gift origin name"}', 'payments':
            [{'payment_method': 'Cash'}], 'post_date': '2017-10-03T00:00:00.0000000+00:00',
            'post_status': 'NotPosted', 'reference': 'newly added gift', 'soft_credits': [{'amount':
            {'value': 100}, 'constituent_id': '187'}], 'subtype': 'Annuity', 'type': 'Donation',
            'tributes': [{'id': '12'}, {'id': '15', 'tribute_acknowledgees': [{'id': '33'}, {'id':
            '21'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | BatchGiftAddResults]
    """

    kwargs = _get_kwargs(
        batch_id=batch_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    batch_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GiftsAdd | Unset = UNSET,
) -> Any | BatchGiftAddResults | None:
    """Gift (Batch)

     Adds one or more gifts to a specified gift batch in the web view.

    Args:
        batch_id (str):
        body (GiftsAdd | Unset):  Example: {'gifts': [{'amount': {'value': 100}, 'constituent_id':
            '280', 'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value':
            100}, 'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id':
            '15', 'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous':
            False, 'lookup_id': '2225', 'payments': [{'payment_method': 'Cash'}], 'post_date':
            '2017-10-03T00:00:00.0000000+00:00', 'post_status': 'NotPosted', 'reference': 'newly added
            gift', 'soft_credits': [{'amount': {'value': 100}, 'constituent_id': '187'}], 'subtype':
            'Annuity', 'type': 'Donation'}, {'amount': {'value': 100}, 'constituent_id': '290',
            'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value': 100},
            'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id': '15',
            'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous': False,
            'lookup_id': '2225', 'origin': '{"name": "Gift origin name"}', 'payments':
            [{'payment_method': 'Cash'}], 'post_date': '2017-10-03T00:00:00.0000000+00:00',
            'post_status': 'NotPosted', 'reference': 'newly added gift', 'soft_credits': [{'amount':
            {'value': 100}, 'constituent_id': '187'}], 'subtype': 'Annuity', 'type': 'Donation',
            'tributes': [{'id': '12'}, {'id': '15', 'tribute_acknowledgees': [{'id': '33'}, {'id':
            '21'}]}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | BatchGiftAddResults
    """

    return (
        await asyncio_detailed(
            batch_id=batch_id,
            client=client,
            body=body,
        )
    ).parsed

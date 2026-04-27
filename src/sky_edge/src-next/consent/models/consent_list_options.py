from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.consent_list_options_category_filter_type import ConsentListOptionsCategoryFilterType
from ..models.consent_list_options_channels_type_0_item import ConsentListOptionsChannelsType0Item
from ..models.consent_list_options_response import ConsentListOptionsResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsentListOptions")


@_attrs_define
class ConsentListOptions:
    """Optional Get constituent consents filters.

    Attributes:
        channels (list[ConsentListOptionsChannelsType0Item] | None | Unset): Limit results to the given list of
            channels. All channels are included by default.
        constituent_ids (list[str] | None | Unset): Limit results to the given list of constituent identifiers.
        category_filter_type (ConsentListOptionsCategoryFilterType | Unset): Category filter
            type<p>Members:</p><ul><li><i>NoFilter</i> - Include all consents regardless of assigned
            category.</li><li><i>AnyCategory</i> - Include all consents assigned to any category.</li><li><i>NoCategory</i>
            - Include only consents without an assigned category.</li><li><i>SpecificCategory</i> - Include only consents
            assigned a specific category.</li></ul>
        category (None | str | Unset): The category name or identifier with which to filter by when CategoryFilterType
            is SpecificCategory.
        response (ConsentListOptionsResponse | Unset): Consent response<p>Members:</p><ul><li><i>OptIn</i> - Opt-
            in</li><li><i>OptOut</i> - Opt-out</li><li><i>NoResponse</i> - No response</li></ul>
        source (None | str | Unset): Source description or identifier
        from_date (datetime.datetime | None | Unset): From date filter
        to_date (datetime.datetime | None | Unset): To date filters
        continuation_token (None | str | Unset): Continuation token for paging
        limit (int | Unset): Represents the number of records to return. (The default is 500) Default: 500.
        offset (int | Unset): Represents the number of records to skip.(For use with pagination)
    """

    channels: list[ConsentListOptionsChannelsType0Item] | None | Unset = UNSET
    constituent_ids: list[str] | None | Unset = UNSET
    category_filter_type: ConsentListOptionsCategoryFilterType | Unset = UNSET
    category: None | str | Unset = UNSET
    response: ConsentListOptionsResponse | Unset = UNSET
    source: None | str | Unset = UNSET
    from_date: datetime.datetime | None | Unset = UNSET
    to_date: datetime.datetime | None | Unset = UNSET
    continuation_token: None | str | Unset = UNSET
    limit: int | Unset = 500
    offset: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channels: list[str] | None | Unset
        if isinstance(self.channels, Unset):
            channels = UNSET
        elif isinstance(self.channels, list):
            channels = []
            for channels_type_0_item_data in self.channels:
                channels_type_0_item = channels_type_0_item_data.value
                channels.append(channels_type_0_item)

        else:
            channels = self.channels

        constituent_ids: list[str] | None | Unset
        if isinstance(self.constituent_ids, Unset):
            constituent_ids = UNSET
        elif isinstance(self.constituent_ids, list):
            constituent_ids = self.constituent_ids

        else:
            constituent_ids = self.constituent_ids

        category_filter_type: str | Unset = UNSET
        if not isinstance(self.category_filter_type, Unset):
            category_filter_type = self.category_filter_type.value

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        response: str | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.value

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        from_date: None | str | Unset
        if isinstance(self.from_date, Unset):
            from_date = UNSET
        elif isinstance(self.from_date, datetime.datetime):
            from_date = self.from_date.isoformat()
        else:
            from_date = self.from_date

        to_date: None | str | Unset
        if isinstance(self.to_date, Unset):
            to_date = UNSET
        elif isinstance(self.to_date, datetime.datetime):
            to_date = self.to_date.isoformat()
        else:
            to_date = self.to_date

        continuation_token: None | str | Unset
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if constituent_ids is not UNSET:
            field_dict["constituent_ids"] = constituent_ids
        if category_filter_type is not UNSET:
            field_dict["category_filter_type"] = category_filter_type
        if category is not UNSET:
            field_dict["category"] = category
        if response is not UNSET:
            field_dict["response"] = response
        if source is not UNSET:
            field_dict["source"] = source
        if from_date is not UNSET:
            field_dict["from_date"] = from_date
        if to_date is not UNSET:
            field_dict["to_date"] = to_date
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_channels(data: object) -> list[ConsentListOptionsChannelsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channels_type_0 = []
                _channels_type_0 = data
                for channels_type_0_item_data in _channels_type_0:
                    channels_type_0_item = ConsentListOptionsChannelsType0Item(channels_type_0_item_data)

                    channels_type_0.append(channels_type_0_item)

                return channels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConsentListOptionsChannelsType0Item] | None | Unset, data)

        channels = _parse_channels(d.pop("channels", UNSET))

        def _parse_constituent_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                constituent_ids_type_0 = cast(list[str], data)

                return constituent_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        constituent_ids = _parse_constituent_ids(d.pop("constituent_ids", UNSET))

        _category_filter_type = d.pop("category_filter_type", UNSET)
        category_filter_type: ConsentListOptionsCategoryFilterType | Unset
        if isinstance(_category_filter_type, Unset):
            category_filter_type = UNSET
        else:
            category_filter_type = ConsentListOptionsCategoryFilterType(_category_filter_type)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        _response = d.pop("response", UNSET)
        response: ConsentListOptionsResponse | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = ConsentListOptionsResponse(_response)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_from_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_date_type_0 = isoparse(data)

                return from_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_date = _parse_from_date(d.pop("from_date", UNSET))

        def _parse_to_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_date_type_0 = isoparse(data)

                return to_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to_date = _parse_to_date(d.pop("to_date", UNSET))

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(d.pop("continuation_token", UNSET))

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        consent_list_options = cls(
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

        return consent_list_options

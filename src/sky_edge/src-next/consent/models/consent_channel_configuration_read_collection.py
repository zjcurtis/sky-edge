from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consent_channel_configuration_read import ConsentChannelConfigurationRead


T = TypeVar("T", bound="ConsentChannelConfigurationReadCollection")


@_attrs_define
class ConsentChannelConfigurationReadCollection:
    """The consent channel configurations.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection. Default: 0.
        limit (int): The limit representing the maximum number of items to retrieve or display. Default: 500.
        channel_configurations (list[ConsentChannelConfigurationRead] | None | Unset): The list of consent channel
            configurations.
        count (int | Unset): The total number of items in the collection.
        continuation_token (None | str | Unset): The continuation token used for pagination to retrieve the next set of
            results.
    """

    offset: int = 0
    limit: int = 500
    channel_configurations: list[ConsentChannelConfigurationRead] | None | Unset = UNSET
    count: int | Unset = UNSET
    continuation_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        channel_configurations: list[dict[str, Any]] | None | Unset
        if isinstance(self.channel_configurations, Unset):
            channel_configurations = UNSET
        elif isinstance(self.channel_configurations, list):
            channel_configurations = []
            for channel_configurations_type_0_item_data in self.channel_configurations:
                channel_configurations_type_0_item = channel_configurations_type_0_item_data.to_dict()
                channel_configurations.append(channel_configurations_type_0_item)

        else:
            channel_configurations = self.channel_configurations

        count = self.count

        continuation_token: None | str | Unset
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if channel_configurations is not UNSET:
            field_dict["channel_configurations"] = channel_configurations
        if count is not UNSET:
            field_dict["count"] = count
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_channel_configuration_read import ConsentChannelConfigurationRead

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_channel_configurations(data: object) -> list[ConsentChannelConfigurationRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                channel_configurations_type_0 = []
                _channel_configurations_type_0 = data
                for channel_configurations_type_0_item_data in _channel_configurations_type_0:
                    channel_configurations_type_0_item = ConsentChannelConfigurationRead.from_dict(
                        channel_configurations_type_0_item_data
                    )

                    channel_configurations_type_0.append(channel_configurations_type_0_item)

                return channel_configurations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConsentChannelConfigurationRead] | None | Unset, data)

        channel_configurations = _parse_channel_configurations(d.pop("channel_configurations", UNSET))

        count = d.pop("count", UNSET)

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(d.pop("continuation_token", UNSET))

        consent_channel_configuration_read_collection = cls(
            offset=offset,
            limit=limit,
            channel_configurations=channel_configurations,
            count=count,
            continuation_token=continuation_token,
        )

        return consent_channel_configuration_read_collection

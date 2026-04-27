from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.consent_channel_category_read import ConsentChannelCategoryRead

T = TypeVar("T", bound="ConsentChannelConfigurationRead")


@_attrs_define
class ConsentChannelConfigurationRead:
    """Represents the configured mappings between a consent channel and categories

    Attributes:
        channel (None | str | Unset): The channel of consent setting.
        inactive (bool | None | Unset): Flag indicating whether or not the consent channel is inactive.
        categories (list[ConsentChannelCategoryRead] | None | Unset): The list of channel category.
    """

    channel: None | str | Unset = UNSET
    inactive: bool | None | Unset = UNSET
    categories: list[ConsentChannelCategoryRead] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        inactive: bool | None | Unset
        if isinstance(self.inactive, Unset):
            inactive = UNSET
        else:
            inactive = self.inactive

        categories: list[dict[str, Any]] | None | Unset
        if isinstance(self.categories, Unset):
            categories = UNSET
        elif isinstance(self.categories, list):
            categories = []
            for categories_type_0_item_data in self.categories:
                categories_type_0_item = categories_type_0_item_data.to_dict()
                categories.append(categories_type_0_item)

        else:
            categories = self.categories

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_channel_category_read import ConsentChannelCategoryRead

        d = dict(src_dict)

        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))

        def _parse_inactive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inactive = _parse_inactive(d.pop("inactive", UNSET))

        def _parse_categories(
            data: object,
        ) -> list[ConsentChannelCategoryRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = []
                _categories_type_0 = data
                for categories_type_0_item_data in _categories_type_0:
                    categories_type_0_item = ConsentChannelCategoryRead.from_dict(
                        categories_type_0_item_data
                    )

                    categories_type_0.append(categories_type_0_item)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConsentChannelCategoryRead] | None | Unset, data)

        categories = _parse_categories(d.pop("categories", UNSET))

        consent_channel_configuration_read = cls(
            channel=channel,
            inactive=inactive,
            categories=categories,
        )

        return consent_channel_configuration_read

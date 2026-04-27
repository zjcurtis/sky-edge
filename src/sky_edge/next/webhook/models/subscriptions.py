from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription import Subscription


T = TypeVar("T", bound="Subscriptions")


@_attrs_define
class Subscriptions:
    """A collection of Webhook subscriptions

    Attributes:
        value (list[Subscription] | None | Unset): The subscriptions
        count (int | Unset): Count of subscriptions
    """

    value: list[Subscription] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        value: list[dict[str, Any]] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = []
            for value_type_0_item_data in self.value:
                value_type_0_item = value_type_0_item_data.to_dict()
                value.append(value_type_0_item)

        else:
            value = self.value

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription import Subscription

        d = dict(src_dict)

        def _parse_value(data: object) -> list[Subscription] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = []
                _value_type_0 = data
                for value_type_0_item_data in _value_type_0:
                    value_type_0_item = Subscription.from_dict(value_type_0_item_data)

                    value_type_0.append(value_type_0_item)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Subscription] | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        count = d.pop("count", UNSET)

        subscriptions = cls(
            value=value,
            count=count,
        )

        return subscriptions

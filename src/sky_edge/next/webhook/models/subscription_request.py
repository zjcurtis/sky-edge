from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SubscriptionRequest")


@_attrs_define
class SubscriptionRequest:
    """The request for the Webhook subscription.

    Attributes:
        webhook_url (str): The Webhook URL for the subscription.
        event_type (str): The event type for the subscription.
    """

    webhook_url: str
    event_type: str

    def to_dict(self) -> dict[str, Any]:
        webhook_url = self.webhook_url

        event_type = self.event_type

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "webhook_url": webhook_url,
                "event_type": event_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        webhook_url = d.pop("webhook_url")

        event_type = d.pop("event_type")

        subscription_request = cls(
            webhook_url=webhook_url,
            event_type=event_type,
        )

        return subscription_request

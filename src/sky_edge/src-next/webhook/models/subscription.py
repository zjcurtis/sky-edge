from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.subscription_provisioning_status import SubscriptionProvisioningStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """Webhook subscription

    Attributes:
        id (None | str | Unset): Subscription ID
        environment_id (None | str | Unset): Environment ID
        webhook_url (None | str | Unset): Subscription webhook url
        application_id (None | str | Unset): Application ID
        event_type (None | str | Unset): Event type
        provisioning_status (SubscriptionProvisioningStatus | Unset): The provisioning status of the subscription
    """

    id: None | str | Unset = UNSET
    environment_id: None | str | Unset = UNSET
    webhook_url: None | str | Unset = UNSET
    application_id: None | str | Unset = UNSET
    event_type: None | str | Unset = UNSET
    provisioning_status: SubscriptionProvisioningStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        environment_id: None | str | Unset
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        webhook_url: None | str | Unset
        if isinstance(self.webhook_url, Unset):
            webhook_url = UNSET
        else:
            webhook_url = self.webhook_url

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        else:
            application_id = self.application_id

        event_type: None | str | Unset
        if isinstance(self.event_type, Unset):
            event_type = UNSET
        else:
            event_type = self.event_type

        provisioning_status: str | Unset = UNSET
        if not isinstance(self.provisioning_status, Unset):
            provisioning_status = self.provisioning_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if environment_id is not UNSET:
            field_dict["environment_id"] = environment_id
        if webhook_url is not UNSET:
            field_dict["webhook_url"] = webhook_url
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if provisioning_status is not UNSET:
            field_dict["provisioning_status"] = provisioning_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_environment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        environment_id = _parse_environment_id(d.pop("environment_id", UNSET))

        def _parse_webhook_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        webhook_url = _parse_webhook_url(d.pop("webhook_url", UNSET))

        def _parse_application_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_id = _parse_application_id(d.pop("application_id", UNSET))

        def _parse_event_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_type = _parse_event_type(d.pop("event_type", UNSET))

        _provisioning_status = d.pop("provisioning_status", UNSET)
        provisioning_status: SubscriptionProvisioningStatus | Unset
        if isinstance(_provisioning_status, Unset):
            provisioning_status = UNSET
        else:
            provisioning_status = SubscriptionProvisioningStatus(_provisioning_status)

        subscription = cls(
            id=id,
            environment_id=environment_id,
            webhook_url=webhook_url,
            application_id=application_id,
            event_type=event_type,
            provisioning_status=provisioning_status,
        )

        return subscription

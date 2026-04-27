from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.subscription_created_provisioning_status import (
    SubscriptionCreatedProvisioningStatus,
)

T = TypeVar("T", bound="SubscriptionCreated")


@_attrs_define
class SubscriptionCreated:
    """Subscription created

    Attributes:
        id (None | str | Unset): Subscription ID
        provisioning_status (SubscriptionCreatedProvisioningStatus | Unset): The provisioning status of the subscription
    """

    id: None | str | Unset = UNSET
    provisioning_status: SubscriptionCreatedProvisioningStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        provisioning_status: str | Unset = UNSET
        if not isinstance(self.provisioning_status, Unset):
            provisioning_status = self.provisioning_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
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

        _provisioning_status = d.pop("provisioning_status", UNSET)
        provisioning_status: SubscriptionCreatedProvisioningStatus | Unset
        if isinstance(_provisioning_status, Unset):
            provisioning_status = UNSET
        else:
            provisioning_status = SubscriptionCreatedProvisioningStatus(
                _provisioning_status
            )

        subscription_created = cls(
            id=id,
            provisioning_status=provisioning_status,
        )

        return subscription_created

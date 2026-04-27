from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecurringGiftConversionOptions")


@_attrs_define
class RecurringGiftConversionOptions:
    """Options to configure conversion of a manual recurring gift to an automated recurring gift.

    Attributes:
        bbps_configuration_id (str | Unset): BBPS Configuration Id to put on the gift
        account_token (str | Unset): Account token to put on the gift payment
    """

    bbps_configuration_id: str | Unset = UNSET
    account_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bbps_configuration_id = self.bbps_configuration_id

        account_token = self.account_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bbps_configuration_id is not UNSET:
            field_dict["bbps_configuration_id"] = bbps_configuration_id
        if account_token is not UNSET:
            field_dict["account_token"] = account_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bbps_configuration_id = d.pop("bbps_configuration_id", UNSET)

        account_token = d.pop("account_token", UNSET)

        recurring_gift_conversion_options = cls(
            bbps_configuration_id=bbps_configuration_id,
            account_token=account_token,
        )

        recurring_gift_conversion_options.additional_properties = d
        return recurring_gift_conversion_options

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

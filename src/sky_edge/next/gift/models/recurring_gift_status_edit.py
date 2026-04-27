from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="RecurringGiftStatusEdit")


@_attrs_define
class RecurringGiftStatusEdit:
    """An object that contains information needed to update the status of a recurring gift.

    Attributes:
        gift_status (str | Unset): The new status of the recurring gift. Available values are <i>Active</i>,
            <i>Held</i>, <i>Terminated</i>, <i>Completed</i>, and <i>Cancelled.</i>
    """

    gift_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift_status = self.gift_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gift_status is not UNSET:
            field_dict["gift_status"] = gift_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gift_status = d.pop("gift_status", UNSET)

        recurring_gift_status_edit = cls(
            gift_status=gift_status,
        )

        recurring_gift_status_edit.additional_properties = d
        return recurring_gift_status_edit

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

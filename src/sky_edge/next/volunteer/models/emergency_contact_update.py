from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="EmergencyContactUpdate")


@_attrs_define
class EmergencyContactUpdate:
    """Represents emergency contact update information for a volunteer

    Attributes:
        name (None | str | Unset): Gets or sets the name of the emergency contact
        phone (None | str | Unset): Gets or sets the phone number of the emergency contact
        relationship (None | str | Unset): Gets or sets the relationship to the volunteer
    """

    name: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    relationship: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        relationship: None | str | Unset
        if isinstance(self.relationship, Unset):
            relationship = UNSET
        else:
            relationship = self.relationship

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if relationship is not UNSET:
            field_dict["relationship"] = relationship

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_relationship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship = _parse_relationship(d.pop("relationship", UNSET))

        emergency_contact_update = cls(
            name=name,
            phone=phone,
            relationship=relationship,
        )

        return emergency_contact_update

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.address_type_enum import AddressTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressTypeOrEnum")


@_attrs_define
class AddressTypeOrEnum:
    """Denotes which address to use for the address processing when one isn't found.
    If the Enum is SpecificAddressType, then the SpecificAddressTypeId is used.

        Attributes:
            address_type_enum (AddressTypeEnum | Unset): Denotes which address to use for the address processing when one
                isn't found<p>Members:</p><ul><li><i>SpecificAddressType</i></li><li><i>SpousePreferred</i></li><li><i>SpousePri
                maryBusiness</i></li><li><i>PrimaryBusiness</i></li><li><i>FirstInList</i></li><li><i>Preferred</i></li><li><i>N
                one</i></li></ul>
            specific_address_type_id (int | None | Unset): The address type from the address types code table to use when
                the AddressTypeEnum is set to SpecificAddressType
    """

    address_type_enum: AddressTypeEnum | Unset = UNSET
    specific_address_type_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address_type_enum: str | Unset = UNSET
        if not isinstance(self.address_type_enum, Unset):
            address_type_enum = self.address_type_enum.value

        specific_address_type_id: int | None | Unset
        if isinstance(self.specific_address_type_id, Unset):
            specific_address_type_id = UNSET
        else:
            specific_address_type_id = self.specific_address_type_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if address_type_enum is not UNSET:
            field_dict["address_type_enum"] = address_type_enum
        if specific_address_type_id is not UNSET:
            field_dict["specific_address_type_id"] = specific_address_type_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _address_type_enum = d.pop("address_type_enum", UNSET)
        address_type_enum: AddressTypeEnum | Unset
        if isinstance(_address_type_enum, Unset):
            address_type_enum = UNSET
        else:
            address_type_enum = AddressTypeEnum(_address_type_enum)

        def _parse_specific_address_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        specific_address_type_id = _parse_specific_address_type_id(d.pop("specific_address_type_id", UNSET))

        address_type_or_enum = cls(
            address_type_enum=address_type_enum,
            specific_address_type_id=specific_address_type_id,
        )

        return address_type_or_enum

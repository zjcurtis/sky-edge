from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_type_or_enum import AddressTypeOrEnum


T = TypeVar("T", bound="AddressProcessingFilter")


@_attrs_define
class AddressProcessingFilter:
    """A filter on an address processing criteria for a query

    Attributes:
        address_type_id_or_enum (AddressTypeOrEnum): Denotes which address to use for the address processing when one
            isn't found.
            If the Enum is SpecificAddressType, then the SpecificAddressTypeId is used.
        sequence (int | Unset): The position this holds among other filters for the respective tab
    """

    address_type_id_or_enum: AddressTypeOrEnum
    sequence: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        address_type_id_or_enum = self.address_type_id_or_enum.to_dict()

        sequence = self.sequence

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "address_type_id_or_enum": address_type_id_or_enum,
            }
        )
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_type_or_enum import AddressTypeOrEnum

        d = dict(src_dict)
        address_type_id_or_enum = AddressTypeOrEnum.from_dict(d.pop("address_type_id_or_enum"))

        sequence = d.pop("sequence", UNSET)

        address_processing_filter = cls(
            address_type_id_or_enum=address_type_id_or_enum,
            sequence=sequence,
        )

        return address_processing_filter

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_processing_filter import AddressProcessingFilter
    from ..models.address_type_or_enum import AddressTypeOrEnum


T = TypeVar("T", bound="OrganizationAddressProcessingConfiguration")


@_attrs_define
class OrganizationAddressProcessingConfiguration:
    """Address options used to determine if and which address should be printed for an organization.

    Attributes:
        default_specific_address_type_or_enum_for_organizations (AddressTypeOrEnum | Unset): Denotes which address to
            use for the address processing when one isn't found.
            If the Enum is SpecificAddressType, then the SpecificAddressTypeId is used.
        filter_collection (list[AddressProcessingFilter] | None | Unset): The collection of address filters for the
            criteria
    """

    default_specific_address_type_or_enum_for_organizations: AddressTypeOrEnum | Unset = UNSET
    filter_collection: list[AddressProcessingFilter] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        default_specific_address_type_or_enum_for_organizations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_specific_address_type_or_enum_for_organizations, Unset):
            default_specific_address_type_or_enum_for_organizations = (
                self.default_specific_address_type_or_enum_for_organizations.to_dict()
            )

        filter_collection: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_collection, Unset):
            filter_collection = UNSET
        elif isinstance(self.filter_collection, list):
            filter_collection = []
            for filter_collection_type_0_item_data in self.filter_collection:
                filter_collection_type_0_item = filter_collection_type_0_item_data.to_dict()
                filter_collection.append(filter_collection_type_0_item)

        else:
            filter_collection = self.filter_collection

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if default_specific_address_type_or_enum_for_organizations is not UNSET:
            field_dict["default_specific_address_type_or_enum_for_organizations"] = (
                default_specific_address_type_or_enum_for_organizations
            )
        if filter_collection is not UNSET:
            field_dict["filter_collection"] = filter_collection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_processing_filter import AddressProcessingFilter
        from ..models.address_type_or_enum import AddressTypeOrEnum

        d = dict(src_dict)
        _default_specific_address_type_or_enum_for_organizations = d.pop(
            "default_specific_address_type_or_enum_for_organizations", UNSET
        )
        default_specific_address_type_or_enum_for_organizations: AddressTypeOrEnum | Unset
        if isinstance(_default_specific_address_type_or_enum_for_organizations, Unset):
            default_specific_address_type_or_enum_for_organizations = UNSET
        else:
            default_specific_address_type_or_enum_for_organizations = AddressTypeOrEnum.from_dict(
                _default_specific_address_type_or_enum_for_organizations
            )

        def _parse_filter_collection(data: object) -> list[AddressProcessingFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_collection_type_0 = []
                _filter_collection_type_0 = data
                for filter_collection_type_0_item_data in _filter_collection_type_0:
                    filter_collection_type_0_item = AddressProcessingFilter.from_dict(
                        filter_collection_type_0_item_data
                    )

                    filter_collection_type_0.append(filter_collection_type_0_item)

                return filter_collection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AddressProcessingFilter] | None | Unset, data)

        filter_collection = _parse_filter_collection(d.pop("filter_collection", UNSET))

        organization_address_processing_configuration = cls(
            default_specific_address_type_or_enum_for_organizations=default_specific_address_type_or_enum_for_organizations,
            filter_collection=filter_collection,
        )

        return organization_address_processing_configuration

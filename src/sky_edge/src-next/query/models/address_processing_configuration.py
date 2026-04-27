from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_address_processing_configuration import IndividualAddressProcessingConfiguration
    from ..models.organization_address_processing_configuration import OrganizationAddressProcessingConfiguration


T = TypeVar("T", bound="AddressProcessingConfiguration")


@_attrs_define
class AddressProcessingConfiguration:
    """Address processing information for the query

    Attributes:
        individual_address_processing_configuration (IndividualAddressProcessingConfiguration | Unset): Address options
            used to determine if and which address should be printed for an individual.
        organization_address_processing_configuration (OrganizationAddressProcessingConfiguration | Unset): Address
            options used to determine if and which address should be printed for an organization.
    """

    individual_address_processing_configuration: IndividualAddressProcessingConfiguration | Unset = UNSET
    organization_address_processing_configuration: OrganizationAddressProcessingConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        individual_address_processing_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.individual_address_processing_configuration, Unset):
            individual_address_processing_configuration = self.individual_address_processing_configuration.to_dict()

        organization_address_processing_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization_address_processing_configuration, Unset):
            organization_address_processing_configuration = self.organization_address_processing_configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if individual_address_processing_configuration is not UNSET:
            field_dict["individual_address_processing_configuration"] = individual_address_processing_configuration
        if organization_address_processing_configuration is not UNSET:
            field_dict["organization_address_processing_configuration"] = organization_address_processing_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.individual_address_processing_configuration import IndividualAddressProcessingConfiguration
        from ..models.organization_address_processing_configuration import OrganizationAddressProcessingConfiguration

        d = dict(src_dict)
        _individual_address_processing_configuration = d.pop("individual_address_processing_configuration", UNSET)
        individual_address_processing_configuration: IndividualAddressProcessingConfiguration | Unset
        if isinstance(_individual_address_processing_configuration, Unset):
            individual_address_processing_configuration = UNSET
        else:
            individual_address_processing_configuration = IndividualAddressProcessingConfiguration.from_dict(
                _individual_address_processing_configuration
            )

        _organization_address_processing_configuration = d.pop("organization_address_processing_configuration", UNSET)
        organization_address_processing_configuration: OrganizationAddressProcessingConfiguration | Unset
        if isinstance(_organization_address_processing_configuration, Unset):
            organization_address_processing_configuration = UNSET
        else:
            organization_address_processing_configuration = OrganizationAddressProcessingConfiguration.from_dict(
                _organization_address_processing_configuration
            )

        address_processing_configuration = cls(
            individual_address_processing_configuration=individual_address_processing_configuration,
            organization_address_processing_configuration=organization_address_processing_configuration,
        )

        return address_processing_configuration

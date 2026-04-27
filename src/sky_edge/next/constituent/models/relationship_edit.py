from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="RelationshipEdit")


@_attrs_define
class RelationshipEdit:
    """Relationships describe connections between constituents and other individuals and organizations such as family,
    friends, and employers. Tracking constituent relationships can enhance fundraising efforts and interactions.

        Attributes:
            comment (str | Unset): The comment on the relationship.
            end (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            is_organization_contact (bool | Unset): Indicates whether the related individual represents the organization as
                a contact. Only applies to relationships between organizations and individuals.
            is_primary_business (bool | Unset): Indicates whether the related organization is the individual's primary
                business. Only applies to relationships between organizations and individuals.
            is_spouse (bool | Unset): Indicates whether the related constituent is the constituent's spouse. Only applies to
                relationships between individuals.
            is_spouse_head_of_household (bool | Unset): Indicates whether the spouse constituent is the head household. Only
                applies to spousal relationships between individuals.
            is_constituent_head_of_household (bool | Unset): Indicates whether the constituent is the head of household.
                Only applies to spousal relationships between individuals.
            organization_contact_type (str | Unset): Provides context for interactions with the related individual who
                represents the organization as a contact. Available values are the entries in the <a href="https://developer.sky
                .blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListOrganizationContactTypes"><b>Contact
                Types</b></a> table. Only applies to relationships between organizations and individuals.
            position (str | Unset): The individual's position in the organization. Only applies to relationships between
                organizations and individuals. Character limit: 50.
            reciprocal_type (str | Unset): Describes the constituent's relationship to the related constituent. For example,
                in a relationship between a male constituent and a female sibling, the reciprocal relationship type would be
                brother. Available values are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b7
                6470069a0509c8f1c5b3/operations/ListRelationshipTypes"><b>Relationships</b></a> table.
            start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            type_ (str | Unset): The type of relation that the relationship represents. Available values are the entries in
                the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListRelations
                hipTypes"><b>Relationships</b></a> table.
    """

    comment: str | Unset = UNSET
    end: FuzzyDate | Unset = UNSET
    is_organization_contact: bool | Unset = UNSET
    is_primary_business: bool | Unset = UNSET
    is_spouse: bool | Unset = UNSET
    is_spouse_head_of_household: bool | Unset = UNSET
    is_constituent_head_of_household: bool | Unset = UNSET
    organization_contact_type: str | Unset = UNSET
    position: str | Unset = UNSET
    reciprocal_type: str | Unset = UNSET
    start: FuzzyDate | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comment = self.comment

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        is_organization_contact = self.is_organization_contact

        is_primary_business = self.is_primary_business

        is_spouse = self.is_spouse

        is_spouse_head_of_household = self.is_spouse_head_of_household

        is_constituent_head_of_household = self.is_constituent_head_of_household

        organization_contact_type = self.organization_contact_type

        position = self.position

        reciprocal_type = self.reciprocal_type

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if end is not UNSET:
            field_dict["end"] = end
        if is_organization_contact is not UNSET:
            field_dict["is_organization_contact"] = is_organization_contact
        if is_primary_business is not UNSET:
            field_dict["is_primary_business"] = is_primary_business
        if is_spouse is not UNSET:
            field_dict["is_spouse"] = is_spouse
        if is_spouse_head_of_household is not UNSET:
            field_dict["is_spouse_head_of_household"] = is_spouse_head_of_household
        if is_constituent_head_of_household is not UNSET:
            field_dict["is_constituent_head_of_household"] = (
                is_constituent_head_of_household
            )
        if organization_contact_type is not UNSET:
            field_dict["organization_contact_type"] = organization_contact_type
        if position is not UNSET:
            field_dict["position"] = position
        if reciprocal_type is not UNSET:
            field_dict["reciprocal_type"] = reciprocal_type
        if start is not UNSET:
            field_dict["start"] = start
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        comment = d.pop("comment", UNSET)

        _end = d.pop("end", UNSET)
        end: FuzzyDate | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = FuzzyDate.from_dict(_end)

        is_organization_contact = d.pop("is_organization_contact", UNSET)

        is_primary_business = d.pop("is_primary_business", UNSET)

        is_spouse = d.pop("is_spouse", UNSET)

        is_spouse_head_of_household = d.pop("is_spouse_head_of_household", UNSET)

        is_constituent_head_of_household = d.pop(
            "is_constituent_head_of_household", UNSET
        )

        organization_contact_type = d.pop("organization_contact_type", UNSET)

        position = d.pop("position", UNSET)

        reciprocal_type = d.pop("reciprocal_type", UNSET)

        _start = d.pop("start", UNSET)
        start: FuzzyDate | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = FuzzyDate.from_dict(_start)

        type_ = d.pop("type", UNSET)

        relationship_edit = cls(
            comment=comment,
            end=end,
            is_organization_contact=is_organization_contact,
            is_primary_business=is_primary_business,
            is_spouse=is_spouse,
            is_spouse_head_of_household=is_spouse_head_of_household,
            is_constituent_head_of_household=is_constituent_head_of_household,
            organization_contact_type=organization_contact_type,
            position=position,
            reciprocal_type=reciprocal_type,
            start=start,
            type_=type_,
        )

        relationship_edit.additional_properties = d
        return relationship_edit

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

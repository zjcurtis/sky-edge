from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate
    from ..models.non_constituent_add import NonConstituentAdd


T = TypeVar("T", bound="RelationshipAdd")


@_attrs_define
class RelationshipAdd:
    """Relationships describe connections between constituents and other individuals and organizations such as family,
    friends, and employers. Tracking constituent relationships can enhance fundraising efforts and interactions.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the relationship.
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
            relation_id (str | Unset): The immutable system record ID of the related individual or organization.
            relation (NonConstituentAdd | Unset): Non-constituents are the individuals and organizations related to
                constituents.
            start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            type_ (str | Unset): The type of relation that the relationship represents. Available values are the entries in
                the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListRelations
                hipTypes"><b>Relationships</b></a> table.
            do_not_reciprocate (bool | Unset): When set to true, indicates that a reciprocal relationship should not be
                created.
    """

    constituent_id: str
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
    relation_id: str | Unset = UNSET
    relation: NonConstituentAdd | Unset = UNSET
    start: FuzzyDate | Unset = UNSET
    type_: str | Unset = UNSET
    do_not_reciprocate: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

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

        relation_id = self.relation_id

        relation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        type_ = self.type_

        do_not_reciprocate = self.do_not_reciprocate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
            }
        )
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
            field_dict["is_constituent_head_of_household"] = is_constituent_head_of_household
        if organization_contact_type is not UNSET:
            field_dict["organization_contact_type"] = organization_contact_type
        if position is not UNSET:
            field_dict["position"] = position
        if reciprocal_type is not UNSET:
            field_dict["reciprocal_type"] = reciprocal_type
        if relation_id is not UNSET:
            field_dict["relation_id"] = relation_id
        if relation is not UNSET:
            field_dict["relation"] = relation
        if start is not UNSET:
            field_dict["start"] = start
        if type_ is not UNSET:
            field_dict["type"] = type_
        if do_not_reciprocate is not UNSET:
            field_dict["do_not_reciprocate"] = do_not_reciprocate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate
        from ..models.non_constituent_add import NonConstituentAdd

        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

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

        is_constituent_head_of_household = d.pop("is_constituent_head_of_household", UNSET)

        organization_contact_type = d.pop("organization_contact_type", UNSET)

        position = d.pop("position", UNSET)

        reciprocal_type = d.pop("reciprocal_type", UNSET)

        relation_id = d.pop("relation_id", UNSET)

        _relation = d.pop("relation", UNSET)
        relation: NonConstituentAdd | Unset
        if isinstance(_relation, Unset):
            relation = UNSET
        else:
            relation = NonConstituentAdd.from_dict(_relation)

        _start = d.pop("start", UNSET)
        start: FuzzyDate | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = FuzzyDate.from_dict(_start)

        type_ = d.pop("type", UNSET)

        do_not_reciprocate = d.pop("do_not_reciprocate", UNSET)

        relationship_add = cls(
            constituent_id=constituent_id,
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
            relation_id=relation_id,
            relation=relation,
            start=start,
            type_=type_,
            do_not_reciprocate=do_not_reciprocate,
        )

        relationship_add.additional_properties = d
        return relationship_add

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

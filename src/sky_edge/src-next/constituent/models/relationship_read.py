from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="RelationshipRead")


@_attrs_define
class RelationshipRead:
    """Relationships describe connections between constituents and other individuals and organizations such as family,
    friends, and employers. Tracking constituent relationships can enhance fundraising efforts and interactions.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the relationship.
            id (str | Unset): The immutable system record ID of the relationship.
            comment (str | Unset): The comment on the relationship.
            date_added (datetime.datetime | Unset): The date when the relationship was created. Includes an offset from UTC
                in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the relationship was last modified. Includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
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
            name (str | Unset): The name of the related constituent. If the constituent's <code>type</code> is
                <i>Individual</i>, this computed field indicates the full name of the constituent based on the target
                organization’s display name settings.
            organization_contact_type (str | Unset): Provides context for interactions with the related individual who
                represents the organization as a contact. Available values are the entries in the <a href="https://developer.sky
                .blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListOrganizationContactTypes"><b>Contact
                Types</b></a> table. Only applies to relationships between organizations and individuals.
            position (str | Unset): The individual's position in the organization. Only applies to relationships between
                organizations and individuals.
            reciprocal_relationship_id (str | Unset): The identifier for the reciprocal relationship record. This value is
                read-only and is automatically generated when the relationship is created. Changes made to this record will also
                be reflected on the reciprocal, with the exception of the comments property.
            reciprocal_type (str | Unset): Describes the constituent's relationship to the related constituent. For example,
                in a relationship between a male constituent and a female sibling, the reciprocal relationship type would be
                brother. Available values are the entries in the <a href="https://developer.sky.blackbaud.com/docs/services/56b7
                6470069a0509c8f1c5b3/operations/ListRelationshipTypes"><b>Relationships</b></a> table.
            relation_id (str | Unset): The immutable system record ID of the related individual or organization.
            start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            type_ (str | Unset): The type of relation that the relationship represents. Available values are the entries in
                the <a href="https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListRelations
                hipTypes"><b>Relationships</b></a> table.
            first_name (str | Unset): The first name of the constituent. For individuals only.
            last_name (str | Unset): The last name of the constituent. For individuals only.
    """

    constituent_id: str
    id: str | Unset = UNSET
    comment: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    end: FuzzyDate | Unset = UNSET
    is_organization_contact: bool | Unset = UNSET
    is_primary_business: bool | Unset = UNSET
    is_spouse: bool | Unset = UNSET
    is_spouse_head_of_household: bool | Unset = UNSET
    is_constituent_head_of_household: bool | Unset = UNSET
    name: str | Unset = UNSET
    organization_contact_type: str | Unset = UNSET
    position: str | Unset = UNSET
    reciprocal_relationship_id: str | Unset = UNSET
    reciprocal_type: str | Unset = UNSET
    relation_id: str | Unset = UNSET
    start: FuzzyDate | Unset = UNSET
    type_: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        id = self.id

        comment = self.comment

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        is_organization_contact = self.is_organization_contact

        is_primary_business = self.is_primary_business

        is_spouse = self.is_spouse

        is_spouse_head_of_household = self.is_spouse_head_of_household

        is_constituent_head_of_household = self.is_constituent_head_of_household

        name = self.name

        organization_contact_type = self.organization_contact_type

        position = self.position

        reciprocal_relationship_id = self.reciprocal_relationship_id

        reciprocal_type = self.reciprocal_type

        relation_id = self.relation_id

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        type_ = self.type_

        first_name = self.first_name

        last_name = self.last_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
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
        if name is not UNSET:
            field_dict["name"] = name
        if organization_contact_type is not UNSET:
            field_dict["organization_contact_type"] = organization_contact_type
        if position is not UNSET:
            field_dict["position"] = position
        if reciprocal_relationship_id is not UNSET:
            field_dict["reciprocal_relationship_id"] = reciprocal_relationship_id
        if reciprocal_type is not UNSET:
            field_dict["reciprocal_type"] = reciprocal_type
        if relation_id is not UNSET:
            field_dict["relation_id"] = relation_id
        if start is not UNSET:
            field_dict["start"] = start
        if type_ is not UNSET:
            field_dict["type"] = type_
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        id = d.pop("id", UNSET)

        comment = d.pop("comment", UNSET)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

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

        name = d.pop("name", UNSET)

        organization_contact_type = d.pop("organization_contact_type", UNSET)

        position = d.pop("position", UNSET)

        reciprocal_relationship_id = d.pop("reciprocal_relationship_id", UNSET)

        reciprocal_type = d.pop("reciprocal_type", UNSET)

        relation_id = d.pop("relation_id", UNSET)

        _start = d.pop("start", UNSET)
        start: FuzzyDate | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = FuzzyDate.from_dict(_start)

        type_ = d.pop("type", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        relationship_read = cls(
            constituent_id=constituent_id,
            id=id,
            comment=comment,
            date_added=date_added,
            date_modified=date_modified,
            end=end,
            is_organization_contact=is_organization_contact,
            is_primary_business=is_primary_business,
            is_spouse=is_spouse,
            is_spouse_head_of_household=is_spouse_head_of_household,
            is_constituent_head_of_household=is_constituent_head_of_household,
            name=name,
            organization_contact_type=organization_contact_type,
            position=position,
            reciprocal_relationship_id=reciprocal_relationship_id,
            reciprocal_type=reciprocal_type,
            relation_id=relation_id,
            start=start,
            type_=type_,
            first_name=first_name,
            last_name=last_name,
        )

        relationship_read.additional_properties = d
        return relationship_read

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

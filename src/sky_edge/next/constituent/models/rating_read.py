from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.rating_read_type import RatingReadType

if TYPE_CHECKING:
    from ..models.rating_read_value import RatingReadValue


T = TypeVar("T", bound="RatingRead")


@_attrs_define
class RatingRead:
    """Ratings indicate the estimated wealth of constituents and their capacity to give. Ratings information such as
    overall wealth ratings, suggested ask amounts, and total identified assets can help to determine where to focus
    efforts, whether to pursue prospects or major gifts, and how much to ask from donors.

        Attributes:
            id (str | Unset): The immutable system record ID of the rating.
            category (str | Unset): The category of the rating. Available values are the entries in the <a href="https://dev
                eloper.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListRatingCategories"><b>Rating
                Categories</b></a> table.
            comment (str | Unset): A comment about the rating.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the rating.
            date (datetime.datetime | Unset): The date of the rating. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            inactive (bool | Unset): This computed field indicates that the rating is active if the <code>category</code> is
                active.
            source (str | Unset): The source of the rating.
            type_ (RatingReadType | Unset): This computed field indicates the type of data that the rating represents based
                on the <code>category</code> property. Available values <a href="#RatingTypes">are listed below</a>.
            value (RatingReadValue | Unset): The value of the rating. The <code>type</code> property determines the format.
    """

    id: str | Unset = UNSET
    category: str | Unset = UNSET
    comment: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    inactive: bool | Unset = UNSET
    source: str | Unset = UNSET
    type_: RatingReadType | Unset = UNSET
    value: RatingReadValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        comment = self.comment

        constituent_id = self.constituent_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        inactive = self.inactive

        source = self.source

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if comment is not UNSET:
            field_dict["comment"] = comment
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date is not UNSET:
            field_dict["date"] = date
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if source is not UNSET:
            field_dict["source"] = source
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rating_read_value import RatingReadValue

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        category = d.pop("category", UNSET)

        comment = d.pop("comment", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        inactive = d.pop("inactive", UNSET)

        source = d.pop("source", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: RatingReadType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RatingReadType(_type_)

        _value = d.pop("value", UNSET)
        value: RatingReadValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RatingReadValue.from_dict(_value)

        rating_read = cls(
            id=id,
            category=category,
            comment=comment,
            constituent_id=constituent_id,
            date=date,
            inactive=inactive,
            source=source,
            type_=type_,
            value=value,
        )

        rating_read.additional_properties = d
        return rating_read

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rating_add_value import RatingAddValue


T = TypeVar("T", bound="RatingAdd")


@_attrs_define
class RatingAdd:
    """Ratings indicate the estimated wealth of constituents and their capacity to give. Ratings information such as
    overall wealth ratings, suggested ask amounts, and total identified assets can help to determine where to focus
    efforts, whether to pursue prospects or major gifts, and how much to ask from donors.

        Attributes:
            category (str): The category of the rating. Available values are the entries in the <a href="https://developer.s
                ky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListRatingCategories"><b>Rating
                Categories</b></a> table.
            constituent_id (str): The immutable system record ID of the constituent associated with the rating.
            date (datetime.datetime): The date of the rating. Uses <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
                format: </a><i>1969-11-21T10:29:43</i>.
            comment (str | Unset): A comment about the rating. Character limit: 255.
            source (str | Unset): Required when the rating category has a source. The source of the new rating.
            value (RatingAddValue | Unset): The value of the rating. The <code>type</code> property determines the format
                and the character limit.
    """

    category: str
    constituent_id: str
    date: datetime.datetime
    comment: str | Unset = UNSET
    source: str | Unset = UNSET
    value: RatingAddValue | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        constituent_id = self.constituent_id

        date = self.date.isoformat()

        comment = self.comment

        source = self.source

        value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "constituent_id": constituent_id,
                "date": date,
            }
        )
        if comment is not UNSET:
            field_dict["comment"] = comment
        if source is not UNSET:
            field_dict["source"] = source
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rating_add_value import RatingAddValue

        d = dict(src_dict)
        category = d.pop("category")

        constituent_id = d.pop("constituent_id")

        date = isoparse(d.pop("date"))

        comment = d.pop("comment", UNSET)

        source = d.pop("source", UNSET)

        _value = d.pop("value", UNSET)
        value: RatingAddValue | Unset
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = RatingAddValue.from_dict(_value)

        rating_add = cls(
            category=category,
            constituent_id=constituent_id,
            date=date,
            comment=comment,
            source=source,
            value=value,
        )

        rating_add.additional_properties = d
        return rating_add

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

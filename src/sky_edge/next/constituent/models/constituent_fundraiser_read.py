from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="ConstituentFundraiserRead")


@_attrs_define
class ConstituentFundraiserRead:
    """Fundraiser constituents interact with other constituents and prospects on behalf of your organization to cultivate
    relationships and request donations.

        Attributes:
            constituent_id (str | Unset): The immutable system record ID of the fundraiser.
            end (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            type_ (str | Unset): The type of fundraiser. Available values are the entries in the <b>Solicitor Type</b>
                table.
    """

    constituent_id: str | Unset = UNSET
    end: FuzzyDate | Unset = UNSET
    start: FuzzyDate | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        constituent_id = d.pop("constituent_id", UNSET)

        _end = d.pop("end", UNSET)
        end: FuzzyDate | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = FuzzyDate.from_dict(_end)

        _start = d.pop("start", UNSET)
        start: FuzzyDate | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = FuzzyDate.from_dict(_start)

        type_ = d.pop("type", UNSET)

        constituent_fundraiser_read = cls(
            constituent_id=constituent_id,
            end=end,
            start=start,
            type_=type_,
        )

        constituent_fundraiser_read.additional_properties = d
        return constituent_fundraiser_read

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

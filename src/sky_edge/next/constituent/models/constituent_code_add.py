from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="ConstituentCodeAdd")


@_attrs_define
class ConstituentCodeAdd:
    """Constituent codes define the high-level affiliations between constituents and your organization — such as Board
    member, Vendor, and Volunteer — to provide context for why constituents are in the database.

        Attributes:
            constituent_id (str): The immutable system record ID of the constituent associated with the constituent code.
            description (str): The description of the constituent code. Available values are the entries in the <a href="htt
                ps://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListConstituentCodeTypes"><b>
                Constituent Codes</b></a> table.
            end (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            start (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as February 9
                (with no year indicated).
            sequence (int | Unset): The sequence of the constituent code.
    """

    constituent_id: str
    description: str
    end: FuzzyDate | Unset = UNSET
    start: FuzzyDate | Unset = UNSET
    sequence: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        description = self.description

        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        sequence = self.sequence

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constituent_id": constituent_id,
                "description": description,
            }
        )
        if end is not UNSET:
            field_dict["end"] = end
        if start is not UNSET:
            field_dict["start"] = start
        if sequence is not UNSET:
            field_dict["sequence"] = sequence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        description = d.pop("description")

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

        sequence = d.pop("sequence", UNSET)

        constituent_code_add = cls(
            constituent_id=constituent_id,
            description=description,
            end=end,
            start=start,
            sequence=sequence,
        )

        constituent_code_add.additional_properties = d
        return constituent_code_add

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

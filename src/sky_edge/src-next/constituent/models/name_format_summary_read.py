from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_format_read import NameFormatRead
    from ..models.primary_name_format_read import PrimaryNameFormatRead


T = TypeVar("T", bound="NameFormatSummaryRead")


@_attrs_define
class NameFormatSummaryRead:
    """All name formats associated with the constituent. This includes both primary addressee and salutation, as well as a
    list of additional standard name formats.

        Attributes:
            additional_name_formats (list[NameFormatRead] | Unset): The additional name formats of the constituent.
            primary_addressee (PrimaryNameFormatRead | Unset): Primary name formats are elevated name formats used for the
                constituent's most commonly used addressee and salutation name formats.
            primary_salutation (PrimaryNameFormatRead | Unset): Primary name formats are elevated name formats used for the
                constituent's most commonly used addressee and salutation name formats.
    """

    additional_name_formats: list[NameFormatRead] | Unset = UNSET
    primary_addressee: PrimaryNameFormatRead | Unset = UNSET
    primary_salutation: PrimaryNameFormatRead | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_name_formats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.additional_name_formats, Unset):
            additional_name_formats = []
            for additional_name_formats_item_data in self.additional_name_formats:
                additional_name_formats_item = additional_name_formats_item_data.to_dict()
                additional_name_formats.append(additional_name_formats_item)

        primary_addressee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_addressee, Unset):
            primary_addressee = self.primary_addressee.to_dict()

        primary_salutation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_salutation, Unset):
            primary_salutation = self.primary_salutation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_name_formats is not UNSET:
            field_dict["additional_name_formats"] = additional_name_formats
        if primary_addressee is not UNSET:
            field_dict["primary_addressee"] = primary_addressee
        if primary_salutation is not UNSET:
            field_dict["primary_salutation"] = primary_salutation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.name_format_read import NameFormatRead
        from ..models.primary_name_format_read import PrimaryNameFormatRead

        d = dict(src_dict)
        _additional_name_formats = d.pop("additional_name_formats", UNSET)
        additional_name_formats: list[NameFormatRead] | Unset = UNSET
        if _additional_name_formats is not UNSET:
            additional_name_formats = []
            for additional_name_formats_item_data in _additional_name_formats:
                additional_name_formats_item = NameFormatRead.from_dict(additional_name_formats_item_data)

                additional_name_formats.append(additional_name_formats_item)

        _primary_addressee = d.pop("primary_addressee", UNSET)
        primary_addressee: PrimaryNameFormatRead | Unset
        if isinstance(_primary_addressee, Unset):
            primary_addressee = UNSET
        else:
            primary_addressee = PrimaryNameFormatRead.from_dict(_primary_addressee)

        _primary_salutation = d.pop("primary_salutation", UNSET)
        primary_salutation: PrimaryNameFormatRead | Unset
        if isinstance(_primary_salutation, Unset):
            primary_salutation = UNSET
        else:
            primary_salutation = PrimaryNameFormatRead.from_dict(_primary_salutation)

        name_format_summary_read = cls(
            additional_name_formats=additional_name_formats,
            primary_addressee=primary_addressee,
            primary_salutation=primary_salutation,
        )

        name_format_summary_read.additional_properties = d
        return name_format_summary_read

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

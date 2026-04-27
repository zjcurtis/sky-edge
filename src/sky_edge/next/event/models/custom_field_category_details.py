from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.custom_field_category_details_type import CustomFieldCategoryDetailsType

T = TypeVar("T", bound="CustomFieldCategoryDetails")


@_attrs_define
class CustomFieldCategoryDetails:
    """Represents the custom field category details.

    Attributes:
        name (None | str | Unset): The category name.
        type_ (CustomFieldCategoryDetailsType | Unset): The type of value of category.<p>Available
            values:</p><ul><li><i>Text</i> - Defines the custom field as a string value.</li><li><i>Number</i> - Defines the
            custom field as a integer value.</li><li><i>Date</i> - Defines the custom field as a date
            value.</li><li><i>Currency</i> - Defines the custom field as a decimal value.</li><li><i>Boolean</i> - Defines
            the custom field as a boolean value.</li><li><i>CodeTableEntry</i> - Defines the custom field as a code table
            entry identifier.</li><li><i>ConstituentId</i> - Defines the custom field as a constituent
            identifier.</li><li><i>FuzzyDate</i> - Defines the custom field as a fuzzy date value.</li></ul>
        code_table_id (None | str | Unset): The code table identifier for the category.
        one_per_record (bool | None | Unset): The flag indicating that only one value for the category is allowed per
            record.
    """

    name: None | str | Unset = UNSET
    type_: CustomFieldCategoryDetailsType | Unset = UNSET
    code_table_id: None | str | Unset = UNSET
    one_per_record: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        code_table_id: None | str | Unset
        if isinstance(self.code_table_id, Unset):
            code_table_id = UNSET
        else:
            code_table_id = self.code_table_id

        one_per_record: bool | None | Unset
        if isinstance(self.one_per_record, Unset):
            one_per_record = UNSET
        else:
            one_per_record = self.one_per_record

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if code_table_id is not UNSET:
            field_dict["code_table_id"] = code_table_id
        if one_per_record is not UNSET:
            field_dict["one_per_record"] = one_per_record

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: CustomFieldCategoryDetailsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CustomFieldCategoryDetailsType(_type_)

        def _parse_code_table_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code_table_id = _parse_code_table_id(d.pop("code_table_id", UNSET))

        def _parse_one_per_record(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        one_per_record = _parse_one_per_record(d.pop("one_per_record", UNSET))

        custom_field_category_details = cls(
            name=name,
            type_=type_,
            code_table_id=code_table_id,
            one_per_record=one_per_record,
        )

        return custom_field_category_details

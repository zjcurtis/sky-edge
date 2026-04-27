from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="AdvancedProcessingOptions")


@_attrs_define
class AdvancedProcessingOptions:
    """Advanced query processing options

    Attributes:
        use_alternate_sql_code_table_fields (bool | Unset): Use alternate SQL method for code table fields
        use_alternate_sql_multiple_attributes (bool | Unset): Use alternate SQL method for multiple attributes
    """

    use_alternate_sql_code_table_fields: bool | Unset = UNSET
    use_alternate_sql_multiple_attributes: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        use_alternate_sql_code_table_fields = self.use_alternate_sql_code_table_fields

        use_alternate_sql_multiple_attributes = (
            self.use_alternate_sql_multiple_attributes
        )

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if use_alternate_sql_code_table_fields is not UNSET:
            field_dict["use_alternate_sql_code_table_fields"] = (
                use_alternate_sql_code_table_fields
            )
        if use_alternate_sql_multiple_attributes is not UNSET:
            field_dict["use_alternate_sql_multiple_attributes"] = (
                use_alternate_sql_multiple_attributes
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_alternate_sql_code_table_fields = d.pop(
            "use_alternate_sql_code_table_fields", UNSET
        )

        use_alternate_sql_multiple_attributes = d.pop(
            "use_alternate_sql_multiple_attributes", UNSET
        )

        advanced_processing_options = cls(
            use_alternate_sql_code_table_fields=use_alternate_sql_code_table_fields,
            use_alternate_sql_multiple_attributes=use_alternate_sql_multiple_attributes,
        )

        return advanced_processing_options

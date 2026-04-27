from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.allowed_filter_operators import AllowedFilterOperators
from ..models.attribute_value_type import AttributeValueType
from ..models.query_value_type import QueryValueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryField")


@_attrs_define
class QueryField:
    """A field available for use in a query

    Attributes:
        id (int | Unset): ID of the field
        available_field_name (None | str | Unset): The name of the field to display in the available fields list
        selected_field_name (None | str | Unset): The name of the field to display when the field is selected for
            filter, output, or sort
        unique_id (None | str | Unset): The attribute type ID, or the specific type ID
        attribute_type_of_data (AttributeValueType | Unset): The type of value for attributes<p>Members:</p><ul><li><i>T
            ext</i></li><li><i>Number</i></li><li><i>Date</i></li><li><i>Currency</i></li><li><i>Boolean</i></li><li><i>Tabl
            eEntry</i></li><li><i>Constituent</i></li><li><i>FuzzyDate</i></li></ul>
        value_type (QueryValueType | Unset): The type of value for a field.  Indicates which UI control should be
            offered to the user for entering filter values.<p>Members:</p><ul><li><i>Text</i> - Text value (string, number,
            etc.) that doesn't have a list of values or other special functionality (date, search,
            etc.)</li><li><i>Boolean</i> - Combo box with Yes and No values</li><li><i>Date</i> - Absolute/relative date
            options</li><li><i>FuzzyDate</i> - Absolute/relative fuzzy date options</li><li><i>TableEntry</i> - Combo box
            displaying values from a code table lookup</li><li><i>Lookup</i> - Combo box displaying values from a table
            lookup</li><li><i>Search</i> - Search field</li><li><i>StaticEntry</i> - Combo box displaying a static list of
            entries</li><li><i>Summary</i> - Summary fields (sum, average, etc.)</li><li><i>FESummaryDate</i> - FE specific
            value type for date used in certain summary fields</li></ul>
        one_to_many (bool | Unset): Indicates if the field has a one-to-many relationship with the query's base type.
        output_sort_can_add_edit (bool | Unset): True if add/edit is supported on the output and sort tabs
        criteria_can_add_edit (bool | Unset): True if add/edit is supported on the criteria tab
        execute_by_id_supported (bool | Unset): True if a query that references this field can be executed by ID
        allowed_filter_operators (list[AllowedFilterOperators] | None | Unset): The set of allowed filter operators for
            this field.
        additional_properties (Any | Unset): Additional properties of the query field
        summary_value_type (QueryValueType | Unset): The type of value for a field.  Indicates which UI control should
            be offered to the user for entering filter values.<p>Members:</p><ul><li><i>Text</i> - Text value (string,
            number, etc.) that doesn't have a list of values or other special functionality (date, search,
            etc.)</li><li><i>Boolean</i> - Combo box with Yes and No values</li><li><i>Date</i> - Absolute/relative date
            options</li><li><i>FuzzyDate</i> - Absolute/relative fuzzy date options</li><li><i>TableEntry</i> - Combo box
            displaying values from a code table lookup</li><li><i>Lookup</i> - Combo box displaying values from a table
            lookup</li><li><i>Search</i> - Search field</li><li><i>StaticEntry</i> - Combo box displaying a static list of
            entries</li><li><i>Summary</i> - Summary fields (sum, average, etc.)</li><li><i>FESummaryDate</i> - FE specific
            value type for date used in certain summary fields</li></ul>
        summary_has_available_fields (bool | None | Unset): Whether the field is a Summary field that has child filters
            available.
        summary_has_default_filters (bool | None | Unset): Whether the field is an FE Summary field that has default
            filters applied.
        address_processing (bool | Unset): Whether the field is an RE Address Processing field.
        web_view_only (bool | Unset): Whether the field is only available in web view.
    """

    id: int | Unset = UNSET
    available_field_name: None | str | Unset = UNSET
    selected_field_name: None | str | Unset = UNSET
    unique_id: None | str | Unset = UNSET
    attribute_type_of_data: AttributeValueType | Unset = UNSET
    value_type: QueryValueType | Unset = UNSET
    one_to_many: bool | Unset = UNSET
    output_sort_can_add_edit: bool | Unset = UNSET
    criteria_can_add_edit: bool | Unset = UNSET
    execute_by_id_supported: bool | Unset = UNSET
    allowed_filter_operators: list[AllowedFilterOperators] | None | Unset = UNSET
    additional_properties: Any | Unset = UNSET
    summary_value_type: QueryValueType | Unset = UNSET
    summary_has_available_fields: bool | None | Unset = UNSET
    summary_has_default_filters: bool | None | Unset = UNSET
    address_processing: bool | Unset = UNSET
    web_view_only: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        available_field_name: None | str | Unset
        if isinstance(self.available_field_name, Unset):
            available_field_name = UNSET
        else:
            available_field_name = self.available_field_name

        selected_field_name: None | str | Unset
        if isinstance(self.selected_field_name, Unset):
            selected_field_name = UNSET
        else:
            selected_field_name = self.selected_field_name

        unique_id: None | str | Unset
        if isinstance(self.unique_id, Unset):
            unique_id = UNSET
        else:
            unique_id = self.unique_id

        attribute_type_of_data: str | Unset = UNSET
        if not isinstance(self.attribute_type_of_data, Unset):
            attribute_type_of_data = self.attribute_type_of_data.value

        value_type: str | Unset = UNSET
        if not isinstance(self.value_type, Unset):
            value_type = self.value_type.value

        one_to_many = self.one_to_many

        output_sort_can_add_edit = self.output_sort_can_add_edit

        criteria_can_add_edit = self.criteria_can_add_edit

        execute_by_id_supported = self.execute_by_id_supported

        allowed_filter_operators: list[str] | None | Unset
        if isinstance(self.allowed_filter_operators, Unset):
            allowed_filter_operators = UNSET
        elif isinstance(self.allowed_filter_operators, list):
            allowed_filter_operators = []
            for allowed_filter_operators_type_0_item_data in self.allowed_filter_operators:
                allowed_filter_operators_type_0_item = allowed_filter_operators_type_0_item_data.value
                allowed_filter_operators.append(allowed_filter_operators_type_0_item)

        else:
            allowed_filter_operators = self.allowed_filter_operators

        additional_properties = self.additional_properties

        summary_value_type: str | Unset = UNSET
        if not isinstance(self.summary_value_type, Unset):
            summary_value_type = self.summary_value_type.value

        summary_has_available_fields: bool | None | Unset
        if isinstance(self.summary_has_available_fields, Unset):
            summary_has_available_fields = UNSET
        else:
            summary_has_available_fields = self.summary_has_available_fields

        summary_has_default_filters: bool | None | Unset
        if isinstance(self.summary_has_default_filters, Unset):
            summary_has_default_filters = UNSET
        else:
            summary_has_default_filters = self.summary_has_default_filters

        address_processing = self.address_processing

        web_view_only = self.web_view_only

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if available_field_name is not UNSET:
            field_dict["available_field_name"] = available_field_name
        if selected_field_name is not UNSET:
            field_dict["selected_field_name"] = selected_field_name
        if unique_id is not UNSET:
            field_dict["unique_id"] = unique_id
        if attribute_type_of_data is not UNSET:
            field_dict["attribute_type_of_data"] = attribute_type_of_data
        if value_type is not UNSET:
            field_dict["value_type"] = value_type
        if one_to_many is not UNSET:
            field_dict["one_to_many"] = one_to_many
        if output_sort_can_add_edit is not UNSET:
            field_dict["output_sort_can_add_edit"] = output_sort_can_add_edit
        if criteria_can_add_edit is not UNSET:
            field_dict["criteria_can_add_edit"] = criteria_can_add_edit
        if execute_by_id_supported is not UNSET:
            field_dict["execute_by_id_supported"] = execute_by_id_supported
        if allowed_filter_operators is not UNSET:
            field_dict["allowed_filter_operators"] = allowed_filter_operators
        if additional_properties is not UNSET:
            field_dict["additional_properties"] = additional_properties
        if summary_value_type is not UNSET:
            field_dict["summary_value_type"] = summary_value_type
        if summary_has_available_fields is not UNSET:
            field_dict["summary_has_available_fields"] = summary_has_available_fields
        if summary_has_default_filters is not UNSET:
            field_dict["summary_has_default_filters"] = summary_has_default_filters
        if address_processing is not UNSET:
            field_dict["address_processing"] = address_processing
        if web_view_only is not UNSET:
            field_dict["web_view_only"] = web_view_only

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_available_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        available_field_name = _parse_available_field_name(d.pop("available_field_name", UNSET))

        def _parse_selected_field_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        selected_field_name = _parse_selected_field_name(d.pop("selected_field_name", UNSET))

        def _parse_unique_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_id = _parse_unique_id(d.pop("unique_id", UNSET))

        _attribute_type_of_data = d.pop("attribute_type_of_data", UNSET)
        attribute_type_of_data: AttributeValueType | Unset
        if isinstance(_attribute_type_of_data, Unset):
            attribute_type_of_data = UNSET
        else:
            attribute_type_of_data = AttributeValueType(_attribute_type_of_data)

        _value_type = d.pop("value_type", UNSET)
        value_type: QueryValueType | Unset
        if isinstance(_value_type, Unset):
            value_type = UNSET
        else:
            value_type = QueryValueType(_value_type)

        one_to_many = d.pop("one_to_many", UNSET)

        output_sort_can_add_edit = d.pop("output_sort_can_add_edit", UNSET)

        criteria_can_add_edit = d.pop("criteria_can_add_edit", UNSET)

        execute_by_id_supported = d.pop("execute_by_id_supported", UNSET)

        def _parse_allowed_filter_operators(data: object) -> list[AllowedFilterOperators] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                allowed_filter_operators_type_0 = []
                _allowed_filter_operators_type_0 = data
                for allowed_filter_operators_type_0_item_data in _allowed_filter_operators_type_0:
                    allowed_filter_operators_type_0_item = AllowedFilterOperators(
                        allowed_filter_operators_type_0_item_data
                    )

                    allowed_filter_operators_type_0.append(allowed_filter_operators_type_0_item)

                return allowed_filter_operators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AllowedFilterOperators] | None | Unset, data)

        allowed_filter_operators = _parse_allowed_filter_operators(d.pop("allowed_filter_operators", UNSET))

        additional_properties = d.pop("additional_properties", UNSET)

        _summary_value_type = d.pop("summary_value_type", UNSET)
        summary_value_type: QueryValueType | Unset
        if isinstance(_summary_value_type, Unset):
            summary_value_type = UNSET
        else:
            summary_value_type = QueryValueType(_summary_value_type)

        def _parse_summary_has_available_fields(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        summary_has_available_fields = _parse_summary_has_available_fields(d.pop("summary_has_available_fields", UNSET))

        def _parse_summary_has_default_filters(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        summary_has_default_filters = _parse_summary_has_default_filters(d.pop("summary_has_default_filters", UNSET))

        address_processing = d.pop("address_processing", UNSET)

        web_view_only = d.pop("web_view_only", UNSET)

        query_field = cls(
            id=id,
            available_field_name=available_field_name,
            selected_field_name=selected_field_name,
            unique_id=unique_id,
            attribute_type_of_data=attribute_type_of_data,
            value_type=value_type,
            one_to_many=one_to_many,
            output_sort_can_add_edit=output_sort_can_add_edit,
            criteria_can_add_edit=criteria_can_add_edit,
            execute_by_id_supported=execute_by_id_supported,
            allowed_filter_operators=allowed_filter_operators,
            additional_properties=additional_properties,
            summary_value_type=summary_value_type,
            summary_has_available_fields=summary_has_available_fields,
            summary_has_default_filters=summary_has_default_filters,
            address_processing=address_processing,
            web_view_only=web_view_only,
        )

        return query_field

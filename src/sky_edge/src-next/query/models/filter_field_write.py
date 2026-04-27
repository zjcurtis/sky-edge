from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.compare_type import CompareType
from ..models.filter_operator import FilterOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_field_write_filter_values_type_0_item import FilterFieldWriteFilterValuesType0Item


T = TypeVar("T", bound="FilterFieldWrite")


@_attrs_define
class FilterFieldWrite:
    """A query field used for filtering records (WHERE clause)

    Attributes:
        query_field_id (int | Unset): ID of the query field
        unique_id (None | str | Unset): The attribute type ID, or the specific type ID
        compare_type (CompareType | Unset): Types of logical joins for filter fields<p>Members:</p><ul><li><i>None</i> -
            The first filter field</li><li><i>And</i> - Use "and" logic</li><li><i>Or</i> - Use "or" logic</li></ul>
        filter_values (list[FilterFieldWriteFilterValuesType0Item] | None | Unset): Values for the filter.

            The filter operator determines the required number of values:
            - Blank, NotBlank, Ask, Any: No values
            - OneOf, NotOneOf, OneOfEach: One or more values
            - Between, NotBetween: Two values in the desired order
            - All others: One value

            The value_type of the query field determines the type of the value(s):
            - Text: string, int32, or double, depending on the field
            - Boolean: boolean
            - Date: date-time or one of the relative date values for Date fields listed below
            - FuzzyDate: FuzzyDate (an object with optional properties "day", "month", and "year") or one of the relative
            date values for FuzzyDate fields listed below.
                The query field's additional_properties entry for yearRequired indicates whether or not the year is required
            when filtering by a specific FuzzyDate.
            - TableEntry, Lookup, Search, and StaticEntry: An object with properties "id" and "description" on GET; int32 on
            POST/PATCH (the ID of the record on which to filter)
            - Summary: Not yet supported

            Relative date values for Date fields:
            - Today
            - Yesterday
            - Tomorrow
            - ThisWeek
            - LastWeek
            - NextWeek
            - ThisMonth
            - LastMonth
            - NextMonth
            - MonthToDate
            - ThisQuarter
            - LastQuarter
            - NextQuarter
            - QuarterToDate
            - ThisYear
            - LastYear
            - NextYear
            - YearToDate

            Supplementary relative date values for Date fields (FE only):
            - EarliestFiscalYear
            - FiscalYearToDate
            - ThisFiscalPeriod
            - LastFiscalPeriod
            - NextFiscalPeriod
            - ThisFiscalYear
            - LastFiscalYear
            - NextFiscalYear

            Relative date values for FuzzyDate fields (RE only):
            - ThisMonth
            - LastMonth
            - NextMonth
            - ThisYear
            - LastYear
            - NextYear
            - January
            - February
            - March
            - April
            - May
            - June
            - July
            - August
            - September
            - October
            - November
            - December

            The month values will match any fuzzy dates with that month (any year).

            The valid values for Lookup, Search, and StaticEntries fields can be found using the Get lookup values endpoint.
            Note that that the filter_values returned when reading a query may contain a different type of value than the
            type of value required when writing (described above).  For example, Lookup fields return an object containing
            the ID and description on read, but should only contain the ID on write.
        operator (FilterOperator | Unset): Available filter operators<p>Members:</p><ul><li><i>Equals</i></li><li><i>Doe
            sNotEqual</i></li><li><i>GreaterThan</i></li><li><i>GreaterThanOrEqualTo</i></li><li><i>LessThan</i></li><li><i>
            LessThanOrEqualTo</i></li><li><i>OneOf</i></li><li><i>NotOneOf</i></li><li><i>Between</i></li><li><i>NotBetween<
            /i></li><li><i>BeginsWith</i></li><li><i>DoesNotBeginWith</i></li><li><i>Contains</i></li><li><i>DoesNotContain<
            /i></li><li><i>Like</i></li><li><i>NotLike</i></li><li><i>Blank</i></li><li><i>NotBlank</i></li><li><i>Ask</i></
            li><li><i>SoundsLike</i></li><li><i>Any</i></li><li><i>OneOfEach</i></li></ul>
        left_parenthesis (bool | Unset): Whether this field begins a group of filters enclosed in parentheses
        right_parenthesis (bool | Unset): Whether this field ends a group of filters enclosed in parentheses
        summary_instance (int | None | Unset): For filter fields referencing summary fields, the summary_instance of the
            summary field.
    """

    query_field_id: int | Unset = UNSET
    unique_id: None | str | Unset = UNSET
    compare_type: CompareType | Unset = UNSET
    filter_values: list[FilterFieldWriteFilterValuesType0Item] | None | Unset = UNSET
    operator: FilterOperator | Unset = UNSET
    left_parenthesis: bool | Unset = UNSET
    right_parenthesis: bool | Unset = UNSET
    summary_instance: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query_field_id = self.query_field_id

        unique_id: None | str | Unset
        if isinstance(self.unique_id, Unset):
            unique_id = UNSET
        else:
            unique_id = self.unique_id

        compare_type: str | Unset = UNSET
        if not isinstance(self.compare_type, Unset):
            compare_type = self.compare_type.value

        filter_values: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_values, Unset):
            filter_values = UNSET
        elif isinstance(self.filter_values, list):
            filter_values = []
            for filter_values_type_0_item_data in self.filter_values:
                filter_values_type_0_item = filter_values_type_0_item_data.to_dict()
                filter_values.append(filter_values_type_0_item)

        else:
            filter_values = self.filter_values

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        left_parenthesis = self.left_parenthesis

        right_parenthesis = self.right_parenthesis

        summary_instance: int | None | Unset
        if isinstance(self.summary_instance, Unset):
            summary_instance = UNSET
        else:
            summary_instance = self.summary_instance

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if query_field_id is not UNSET:
            field_dict["query_field_id"] = query_field_id
        if unique_id is not UNSET:
            field_dict["unique_id"] = unique_id
        if compare_type is not UNSET:
            field_dict["compare_type"] = compare_type
        if filter_values is not UNSET:
            field_dict["filter_values"] = filter_values
        if operator is not UNSET:
            field_dict["operator"] = operator
        if left_parenthesis is not UNSET:
            field_dict["left_parenthesis"] = left_parenthesis
        if right_parenthesis is not UNSET:
            field_dict["right_parenthesis"] = right_parenthesis
        if summary_instance is not UNSET:
            field_dict["summary_instance"] = summary_instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_field_write_filter_values_type_0_item import FilterFieldWriteFilterValuesType0Item

        d = dict(src_dict)
        query_field_id = d.pop("query_field_id", UNSET)

        def _parse_unique_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unique_id = _parse_unique_id(d.pop("unique_id", UNSET))

        _compare_type = d.pop("compare_type", UNSET)
        compare_type: CompareType | Unset
        if isinstance(_compare_type, Unset):
            compare_type = UNSET
        else:
            compare_type = CompareType(_compare_type)

        def _parse_filter_values(data: object) -> list[FilterFieldWriteFilterValuesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_values_type_0 = []
                _filter_values_type_0 = data
                for filter_values_type_0_item_data in _filter_values_type_0:
                    filter_values_type_0_item = FilterFieldWriteFilterValuesType0Item.from_dict(
                        filter_values_type_0_item_data
                    )

                    filter_values_type_0.append(filter_values_type_0_item)

                return filter_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterFieldWriteFilterValuesType0Item] | None | Unset, data)

        filter_values = _parse_filter_values(d.pop("filter_values", UNSET))

        _operator = d.pop("operator", UNSET)
        operator: FilterOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FilterOperator(_operator)

        left_parenthesis = d.pop("left_parenthesis", UNSET)

        right_parenthesis = d.pop("right_parenthesis", UNSET)

        def _parse_summary_instance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        summary_instance = _parse_summary_instance(d.pop("summary_instance", UNSET))

        filter_field_write = cls(
            query_field_id=query_field_id,
            unique_id=unique_id,
            compare_type=compare_type,
            filter_values=filter_values,
            operator=operator,
            left_parenthesis=left_parenthesis,
            right_parenthesis=right_parenthesis,
            summary_instance=summary_instance,
        )

        return filter_field_write

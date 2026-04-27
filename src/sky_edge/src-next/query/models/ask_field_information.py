from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.filter_operator import FilterOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="AskFieldInformation")


@_attrs_define
class AskFieldInformation:
    """Information regarding ask fields to provide values at execution

    Attributes:
        filter_values (list[Any] | None | Unset): Values for the filter.

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
    """

    filter_values: list[Any] | None | Unset = UNSET
    operator: FilterOperator | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        filter_values: list[Any] | None | Unset
        if isinstance(self.filter_values, Unset):
            filter_values = UNSET
        elif isinstance(self.filter_values, list):
            filter_values = self.filter_values

        else:
            filter_values = self.filter_values

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if filter_values is not UNSET:
            field_dict["filter_values"] = filter_values
        if operator is not UNSET:
            field_dict["operator"] = operator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_filter_values(data: object) -> list[Any] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_values_type_0 = cast(list[Any], data)

                return filter_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | Unset, data)

        filter_values = _parse_filter_values(d.pop("filter_values", UNSET))

        _operator = d.pop("operator", UNSET)
        operator: FilterOperator | Unset
        if isinstance(_operator, Unset):
            operator = UNSET
        else:
            operator = FilterOperator(_operator)

        ask_field_information = cls(
            filter_values=filter_values,
            operator=operator,
        )

        return ask_field_information

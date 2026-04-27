from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.query_format import QueryFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_processing_configuration import AddressProcessingConfiguration
    from ..models.advanced_processing_options import AdvancedProcessingOptions
    from ..models.constituent_filters import ConstituentFilters
    from ..models.filter_field_write import FilterFieldWrite
    from ..models.gift_processing_options import GiftProcessingOptions
    from ..models.merged_query_details import MergedQueryDetails
    from ..models.output_limit import OutputLimit
    from ..models.select_field_write import SelectFieldWrite
    from ..models.sort_field_write import SortFieldWrite
    from ..models.summary_field_write import SummaryFieldWrite


T = TypeVar("T", bound="QueryEdit")


@_attrs_define
class QueryEdit:
    """A model to edit an existing query

    Attributes:
        format_ (QueryFormat | Unset): Available formats for queries<p>Members:</p><ul><li><i>Dynamic</i> - The query
            results are obtained by executing the query SQL</li><li><i>Static</i> - The IDs of the records found by the
            query are saved to a table</li></ul>
        select_from_query_id (int | None | Unset): The ID of a query used as a base select for the query
        type_id (int | None | Unset): The type identifier of the query corresponding to types like as Constituent or
            Invoice
        others_can_execute (bool | None | Unset): Whether users other than the user that created the query can execute
            the query
        others_can_modify (bool | None | Unset): Whether users other than the user that created the query can modify the
            query
        category_id (int | None | Unset): The category identifier in which this query appears
        suppress_duplicates (bool | None | Unset): Whether to suppress duplicate (base) records in the query results
        name (None | str | Unset): The unique name of the query
        description (None | str | Unset): Description of the query
        select_fields (list[SelectFieldWrite] | None | Unset): The select fields of the query (SELECT clause).
            If this property is specified on a PATCH request, you must provide all the desired items in the collection with
            all the desired properties.
            The collection you provide will fully overwrite the existing collection.
            This is different from standard PATCH collection handling, where only the key values of items in
            the collection are required to retain existing items.
        filter_fields (list[FilterFieldWrite] | None | Unset): The filter fields of the query (WHERE clause).
            If this property is specified on a PATCH request, you must provide all the desired items in the collection with
            all the desired properties.
            The collection you provide will fully overwrite the existing collection.
            This is different from standard PATCH collection handling, where only the key values of items in
            the collection are required to retain existing items.
        sort_fields (list[SortFieldWrite] | None | Unset): The sort fields of the query (ORDER BY clause).
            If this property is specified on a PATCH request, you must provide all the desired items in the collection with
            all the desired properties.
            The collection you provide will fully overwrite the existing collection.
            This is different from standard PATCH collection handling, where only the key values of items in
            the collection are required to retain existing items.
        summary_fields (list[SummaryFieldWrite] | None | Unset): The summary fields of the query, which are typically
            aggregations or totals related to the query record type.
            The objects present in this collection must have unique combinations of query_field_id and summary_instance.
            When making any changes to the filter fields or summary fields of a query with summary fields or filter fields,
            all the following rules apply:
            - All of summary fields and filter fields must be provided provided in the request.
            - If one or more select fields reference a summary field, the entire select fields collection must be provided
            in the request as well. Note that this means providing all of filter_fields, select_fields, and summary_fields.
            - Sort fields are handled the same as select fields. Note that for queries with summary fields in both
            select_fields and sort_fields, all of filter_fields, summary_fields, select_fields, and sort_fields must be
            provided on the request to make any changes to any of the collections.
        merged_query_details (MergedQueryDetails | Unset): Details for queries that merge two other queries to create a
            base select
        gift_processing_options (GiftProcessingOptions | Unset): Query options for gift processing specific to RE
        advanced_processing_options (AdvancedProcessingOptions | Unset): Advanced query processing options
        address_processing_configuration (AddressProcessingConfiguration | Unset): Address processing information for
            the query
        output_limit (OutputLimit | Unset): A limit on the number of rows saved for a static query
        constituent_filters (ConstituentFilters | Unset): Common convenience filters specific to RE queries
        date_last_run (datetime.datetime | None | Unset): The date the query was last executed
        elapsed_ms (int | None | Unset): The elapsed milliseconds for the last execution
        num_records (int | None | Unset): The number of records resulting from the last execution
    """

    format_: QueryFormat | Unset = UNSET
    select_from_query_id: int | None | Unset = UNSET
    type_id: int | None | Unset = UNSET
    others_can_execute: bool | None | Unset = UNSET
    others_can_modify: bool | None | Unset = UNSET
    category_id: int | None | Unset = UNSET
    suppress_duplicates: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    select_fields: list[SelectFieldWrite] | None | Unset = UNSET
    filter_fields: list[FilterFieldWrite] | None | Unset = UNSET
    sort_fields: list[SortFieldWrite] | None | Unset = UNSET
    summary_fields: list[SummaryFieldWrite] | None | Unset = UNSET
    merged_query_details: MergedQueryDetails | Unset = UNSET
    gift_processing_options: GiftProcessingOptions | Unset = UNSET
    advanced_processing_options: AdvancedProcessingOptions | Unset = UNSET
    address_processing_configuration: AddressProcessingConfiguration | Unset = UNSET
    output_limit: OutputLimit | Unset = UNSET
    constituent_filters: ConstituentFilters | Unset = UNSET
    date_last_run: datetime.datetime | None | Unset = UNSET
    elapsed_ms: int | None | Unset = UNSET
    num_records: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        select_from_query_id: int | None | Unset
        if isinstance(self.select_from_query_id, Unset):
            select_from_query_id = UNSET
        else:
            select_from_query_id = self.select_from_query_id

        type_id: int | None | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

        others_can_execute: bool | None | Unset
        if isinstance(self.others_can_execute, Unset):
            others_can_execute = UNSET
        else:
            others_can_execute = self.others_can_execute

        others_can_modify: bool | None | Unset
        if isinstance(self.others_can_modify, Unset):
            others_can_modify = UNSET
        else:
            others_can_modify = self.others_can_modify

        category_id: int | None | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        suppress_duplicates: bool | None | Unset
        if isinstance(self.suppress_duplicates, Unset):
            suppress_duplicates = UNSET
        else:
            suppress_duplicates = self.suppress_duplicates

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        select_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.select_fields, Unset):
            select_fields = UNSET
        elif isinstance(self.select_fields, list):
            select_fields = []
            for select_fields_type_0_item_data in self.select_fields:
                select_fields_type_0_item = select_fields_type_0_item_data.to_dict()
                select_fields.append(select_fields_type_0_item)

        else:
            select_fields = self.select_fields

        filter_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_fields, Unset):
            filter_fields = UNSET
        elif isinstance(self.filter_fields, list):
            filter_fields = []
            for filter_fields_type_0_item_data in self.filter_fields:
                filter_fields_type_0_item = filter_fields_type_0_item_data.to_dict()
                filter_fields.append(filter_fields_type_0_item)

        else:
            filter_fields = self.filter_fields

        sort_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.sort_fields, Unset):
            sort_fields = UNSET
        elif isinstance(self.sort_fields, list):
            sort_fields = []
            for sort_fields_type_0_item_data in self.sort_fields:
                sort_fields_type_0_item = sort_fields_type_0_item_data.to_dict()
                sort_fields.append(sort_fields_type_0_item)

        else:
            sort_fields = self.sort_fields

        summary_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.summary_fields, Unset):
            summary_fields = UNSET
        elif isinstance(self.summary_fields, list):
            summary_fields = []
            for summary_fields_type_0_item_data in self.summary_fields:
                summary_fields_type_0_item = summary_fields_type_0_item_data.to_dict()
                summary_fields.append(summary_fields_type_0_item)

        else:
            summary_fields = self.summary_fields

        merged_query_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merged_query_details, Unset):
            merged_query_details = self.merged_query_details.to_dict()

        gift_processing_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_processing_options, Unset):
            gift_processing_options = self.gift_processing_options.to_dict()

        advanced_processing_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_processing_options, Unset):
            advanced_processing_options = self.advanced_processing_options.to_dict()

        address_processing_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address_processing_configuration, Unset):
            address_processing_configuration = self.address_processing_configuration.to_dict()

        output_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_limit, Unset):
            output_limit = self.output_limit.to_dict()

        constituent_filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.constituent_filters, Unset):
            constituent_filters = self.constituent_filters.to_dict()

        date_last_run: None | str | Unset
        if isinstance(self.date_last_run, Unset):
            date_last_run = UNSET
        elif isinstance(self.date_last_run, datetime.datetime):
            date_last_run = self.date_last_run.isoformat()
        else:
            date_last_run = self.date_last_run

        elapsed_ms: int | None | Unset
        if isinstance(self.elapsed_ms, Unset):
            elapsed_ms = UNSET
        else:
            elapsed_ms = self.elapsed_ms

        num_records: int | None | Unset
        if isinstance(self.num_records, Unset):
            num_records = UNSET
        else:
            num_records = self.num_records

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if select_from_query_id is not UNSET:
            field_dict["select_from_query_id"] = select_from_query_id
        if type_id is not UNSET:
            field_dict["type_id"] = type_id
        if others_can_execute is not UNSET:
            field_dict["others_can_execute"] = others_can_execute
        if others_can_modify is not UNSET:
            field_dict["others_can_modify"] = others_can_modify
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if suppress_duplicates is not UNSET:
            field_dict["suppress_duplicates"] = suppress_duplicates
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if select_fields is not UNSET:
            field_dict["select_fields"] = select_fields
        if filter_fields is not UNSET:
            field_dict["filter_fields"] = filter_fields
        if sort_fields is not UNSET:
            field_dict["sort_fields"] = sort_fields
        if summary_fields is not UNSET:
            field_dict["summary_fields"] = summary_fields
        if merged_query_details is not UNSET:
            field_dict["merged_query_details"] = merged_query_details
        if gift_processing_options is not UNSET:
            field_dict["gift_processing_options"] = gift_processing_options
        if advanced_processing_options is not UNSET:
            field_dict["advanced_processing_options"] = advanced_processing_options
        if address_processing_configuration is not UNSET:
            field_dict["address_processing_configuration"] = address_processing_configuration
        if output_limit is not UNSET:
            field_dict["output_limit"] = output_limit
        if constituent_filters is not UNSET:
            field_dict["constituent_filters"] = constituent_filters
        if date_last_run is not UNSET:
            field_dict["date_last_run"] = date_last_run
        if elapsed_ms is not UNSET:
            field_dict["elapsed_ms"] = elapsed_ms
        if num_records is not UNSET:
            field_dict["num_records"] = num_records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_processing_configuration import AddressProcessingConfiguration
        from ..models.advanced_processing_options import AdvancedProcessingOptions
        from ..models.constituent_filters import ConstituentFilters
        from ..models.filter_field_write import FilterFieldWrite
        from ..models.gift_processing_options import GiftProcessingOptions
        from ..models.merged_query_details import MergedQueryDetails
        from ..models.output_limit import OutputLimit
        from ..models.select_field_write import SelectFieldWrite
        from ..models.sort_field_write import SortFieldWrite
        from ..models.summary_field_write import SummaryFieldWrite

        d = dict(src_dict)
        _format_ = d.pop("format", UNSET)
        format_: QueryFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = QueryFormat(_format_)

        def _parse_select_from_query_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        select_from_query_id = _parse_select_from_query_id(d.pop("select_from_query_id", UNSET))

        def _parse_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        type_id = _parse_type_id(d.pop("type_id", UNSET))

        def _parse_others_can_execute(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        others_can_execute = _parse_others_can_execute(d.pop("others_can_execute", UNSET))

        def _parse_others_can_modify(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        others_can_modify = _parse_others_can_modify(d.pop("others_can_modify", UNSET))

        def _parse_category_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

        def _parse_suppress_duplicates(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        suppress_duplicates = _parse_suppress_duplicates(d.pop("suppress_duplicates", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_select_fields(data: object) -> list[SelectFieldWrite] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                select_fields_type_0 = []
                _select_fields_type_0 = data
                for select_fields_type_0_item_data in _select_fields_type_0:
                    select_fields_type_0_item = SelectFieldWrite.from_dict(select_fields_type_0_item_data)

                    select_fields_type_0.append(select_fields_type_0_item)

                return select_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SelectFieldWrite] | None | Unset, data)

        select_fields = _parse_select_fields(d.pop("select_fields", UNSET))

        def _parse_filter_fields(data: object) -> list[FilterFieldWrite] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_fields_type_0 = []
                _filter_fields_type_0 = data
                for filter_fields_type_0_item_data in _filter_fields_type_0:
                    filter_fields_type_0_item = FilterFieldWrite.from_dict(filter_fields_type_0_item_data)

                    filter_fields_type_0.append(filter_fields_type_0_item)

                return filter_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterFieldWrite] | None | Unset, data)

        filter_fields = _parse_filter_fields(d.pop("filter_fields", UNSET))

        def _parse_sort_fields(data: object) -> list[SortFieldWrite] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_fields_type_0 = []
                _sort_fields_type_0 = data
                for sort_fields_type_0_item_data in _sort_fields_type_0:
                    sort_fields_type_0_item = SortFieldWrite.from_dict(sort_fields_type_0_item_data)

                    sort_fields_type_0.append(sort_fields_type_0_item)

                return sort_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SortFieldWrite] | None | Unset, data)

        sort_fields = _parse_sort_fields(d.pop("sort_fields", UNSET))

        def _parse_summary_fields(data: object) -> list[SummaryFieldWrite] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                summary_fields_type_0 = []
                _summary_fields_type_0 = data
                for summary_fields_type_0_item_data in _summary_fields_type_0:
                    summary_fields_type_0_item = SummaryFieldWrite.from_dict(summary_fields_type_0_item_data)

                    summary_fields_type_0.append(summary_fields_type_0_item)

                return summary_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SummaryFieldWrite] | None | Unset, data)

        summary_fields = _parse_summary_fields(d.pop("summary_fields", UNSET))

        _merged_query_details = d.pop("merged_query_details", UNSET)
        merged_query_details: MergedQueryDetails | Unset
        if isinstance(_merged_query_details, Unset):
            merged_query_details = UNSET
        else:
            merged_query_details = MergedQueryDetails.from_dict(_merged_query_details)

        _gift_processing_options = d.pop("gift_processing_options", UNSET)
        gift_processing_options: GiftProcessingOptions | Unset
        if isinstance(_gift_processing_options, Unset):
            gift_processing_options = UNSET
        else:
            gift_processing_options = GiftProcessingOptions.from_dict(_gift_processing_options)

        _advanced_processing_options = d.pop("advanced_processing_options", UNSET)
        advanced_processing_options: AdvancedProcessingOptions | Unset
        if isinstance(_advanced_processing_options, Unset):
            advanced_processing_options = UNSET
        else:
            advanced_processing_options = AdvancedProcessingOptions.from_dict(_advanced_processing_options)

        _address_processing_configuration = d.pop("address_processing_configuration", UNSET)
        address_processing_configuration: AddressProcessingConfiguration | Unset
        if isinstance(_address_processing_configuration, Unset):
            address_processing_configuration = UNSET
        else:
            address_processing_configuration = AddressProcessingConfiguration.from_dict(
                _address_processing_configuration
            )

        _output_limit = d.pop("output_limit", UNSET)
        output_limit: OutputLimit | Unset
        if isinstance(_output_limit, Unset):
            output_limit = UNSET
        else:
            output_limit = OutputLimit.from_dict(_output_limit)

        _constituent_filters = d.pop("constituent_filters", UNSET)
        constituent_filters: ConstituentFilters | Unset
        if isinstance(_constituent_filters, Unset):
            constituent_filters = UNSET
        else:
            constituent_filters = ConstituentFilters.from_dict(_constituent_filters)

        def _parse_date_last_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_last_run_type_0 = isoparse(data)

                return date_last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_last_run = _parse_date_last_run(d.pop("date_last_run", UNSET))

        def _parse_elapsed_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        elapsed_ms = _parse_elapsed_ms(d.pop("elapsed_ms", UNSET))

        def _parse_num_records(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_records = _parse_num_records(d.pop("num_records", UNSET))

        query_edit = cls(
            format_=format_,
            select_from_query_id=select_from_query_id,
            type_id=type_id,
            others_can_execute=others_can_execute,
            others_can_modify=others_can_modify,
            category_id=category_id,
            suppress_duplicates=suppress_duplicates,
            name=name,
            description=description,
            select_fields=select_fields,
            filter_fields=filter_fields,
            sort_fields=sort_fields,
            summary_fields=summary_fields,
            merged_query_details=merged_query_details,
            gift_processing_options=gift_processing_options,
            advanced_processing_options=advanced_processing_options,
            address_processing_configuration=address_processing_configuration,
            output_limit=output_limit,
            constituent_filters=constituent_filters,
            date_last_run=date_last_run,
            elapsed_ms=elapsed_ms,
            num_records=num_records,
        )

        return query_edit

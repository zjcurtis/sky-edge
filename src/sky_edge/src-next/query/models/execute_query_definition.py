from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sql_generation_mode import SqlGenerationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_processing_configuration import AddressProcessingConfiguration
    from ..models.advanced_processing_options import AdvancedProcessingOptions
    from ..models.constituent_filters import ConstituentFilters
    from ..models.filter_field_write import FilterFieldWrite
    from ..models.gift_processing_options import GiftProcessingOptions
    from ..models.select_field_write import SelectFieldWrite
    from ..models.sort_field_write import SortFieldWrite
    from ..models.summary_field_write import SummaryFieldWrite


T = TypeVar("T", bound="ExecuteQueryDefinition")


@_attrs_define
class ExecuteQueryDefinition:
    """Query fields for a query execution request

    Attributes:
        type_id (int): The query type ID
        select_fields (list[SelectFieldWrite] | None | Unset): The select fields of the query (SELECT clause)
        filter_fields (list[FilterFieldWrite] | None | Unset): The filter fields of the query (WHERE clause)
        sort_fields (list[SortFieldWrite] | None | Unset): The sort fields of the query (ORDER BY clause)
        summary_fields (list[SummaryFieldWrite] | None | Unset): The summary fields of the query, which are typically
            aggregations or totals related to the query record type.
        sql_generation_mode (SqlGenerationMode | Unset): SQL generation mode having an effect on the select columns
            used<p>Members:</p><ul><li><i>Query</i> - Use the query's select fields plus QRECID</li><li><i>Export</i> - Use
            the query's select fields without adding QRECID</li><li><i>Report</i> - Only select QRECID</li></ul>
        gift_processing_options (GiftProcessingOptions | Unset): Query options for gift processing specific to RE
        advanced_processing_options (AdvancedProcessingOptions | Unset): Advanced query processing options
        address_processing_configuration (AddressProcessingConfiguration | Unset): Address processing information for
            the query
        select_from_query_id (int | None | Unset): The ID of a query used as a base select for this query
        suppress_duplicates (bool | Unset): Whether to suppress duplicate (base) records in the query results
        constituent_filters (ConstituentFilters | Unset): Common convenience filters specific to RE queries
    """

    type_id: int
    select_fields: list[SelectFieldWrite] | None | Unset = UNSET
    filter_fields: list[FilterFieldWrite] | None | Unset = UNSET
    sort_fields: list[SortFieldWrite] | None | Unset = UNSET
    summary_fields: list[SummaryFieldWrite] | None | Unset = UNSET
    sql_generation_mode: SqlGenerationMode | Unset = UNSET
    gift_processing_options: GiftProcessingOptions | Unset = UNSET
    advanced_processing_options: AdvancedProcessingOptions | Unset = UNSET
    address_processing_configuration: AddressProcessingConfiguration | Unset = UNSET
    select_from_query_id: int | None | Unset = UNSET
    suppress_duplicates: bool | Unset = UNSET
    constituent_filters: ConstituentFilters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_id = self.type_id

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

        sql_generation_mode: str | Unset = UNSET
        if not isinstance(self.sql_generation_mode, Unset):
            sql_generation_mode = self.sql_generation_mode.value

        gift_processing_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_processing_options, Unset):
            gift_processing_options = self.gift_processing_options.to_dict()

        advanced_processing_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_processing_options, Unset):
            advanced_processing_options = self.advanced_processing_options.to_dict()

        address_processing_configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address_processing_configuration, Unset):
            address_processing_configuration = self.address_processing_configuration.to_dict()

        select_from_query_id: int | None | Unset
        if isinstance(self.select_from_query_id, Unset):
            select_from_query_id = UNSET
        else:
            select_from_query_id = self.select_from_query_id

        suppress_duplicates = self.suppress_duplicates

        constituent_filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.constituent_filters, Unset):
            constituent_filters = self.constituent_filters.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type_id": type_id,
            }
        )
        if select_fields is not UNSET:
            field_dict["select_fields"] = select_fields
        if filter_fields is not UNSET:
            field_dict["filter_fields"] = filter_fields
        if sort_fields is not UNSET:
            field_dict["sort_fields"] = sort_fields
        if summary_fields is not UNSET:
            field_dict["summary_fields"] = summary_fields
        if sql_generation_mode is not UNSET:
            field_dict["sql_generation_mode"] = sql_generation_mode
        if gift_processing_options is not UNSET:
            field_dict["gift_processing_options"] = gift_processing_options
        if advanced_processing_options is not UNSET:
            field_dict["advanced_processing_options"] = advanced_processing_options
        if address_processing_configuration is not UNSET:
            field_dict["address_processing_configuration"] = address_processing_configuration
        if select_from_query_id is not UNSET:
            field_dict["select_from_query_id"] = select_from_query_id
        if suppress_duplicates is not UNSET:
            field_dict["suppress_duplicates"] = suppress_duplicates
        if constituent_filters is not UNSET:
            field_dict["constituent_filters"] = constituent_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_processing_configuration import AddressProcessingConfiguration
        from ..models.advanced_processing_options import AdvancedProcessingOptions
        from ..models.constituent_filters import ConstituentFilters
        from ..models.filter_field_write import FilterFieldWrite
        from ..models.gift_processing_options import GiftProcessingOptions
        from ..models.select_field_write import SelectFieldWrite
        from ..models.sort_field_write import SortFieldWrite
        from ..models.summary_field_write import SummaryFieldWrite

        d = dict(src_dict)
        type_id = d.pop("type_id")

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

        _sql_generation_mode = d.pop("sql_generation_mode", UNSET)
        sql_generation_mode: SqlGenerationMode | Unset
        if isinstance(_sql_generation_mode, Unset):
            sql_generation_mode = UNSET
        else:
            sql_generation_mode = SqlGenerationMode(_sql_generation_mode)

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

        def _parse_select_from_query_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        select_from_query_id = _parse_select_from_query_id(d.pop("select_from_query_id", UNSET))

        suppress_duplicates = d.pop("suppress_duplicates", UNSET)

        _constituent_filters = d.pop("constituent_filters", UNSET)
        constituent_filters: ConstituentFilters | Unset
        if isinstance(_constituent_filters, Unset):
            constituent_filters = UNSET
        else:
            constituent_filters = ConstituentFilters.from_dict(_constituent_filters)

        execute_query_definition = cls(
            type_id=type_id,
            select_fields=select_fields,
            filter_fields=filter_fields,
            sort_fields=sort_fields,
            summary_fields=summary_fields,
            sql_generation_mode=sql_generation_mode,
            gift_processing_options=gift_processing_options,
            advanced_processing_options=advanced_processing_options,
            address_processing_configuration=address_processing_configuration,
            select_from_query_id=select_from_query_id,
            suppress_duplicates=suppress_duplicates,
            constituent_filters=constituent_filters,
        )

        return execute_query_definition

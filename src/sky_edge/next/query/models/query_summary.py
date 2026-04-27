from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.execution_modes import ExecutionModes
from ..models.query_format import QueryFormat

if TYPE_CHECKING:
    from ..models.constituent_filters import ConstituentFilters
    from ..models.output_limit import OutputLimit


T = TypeVar("T", bound="QuerySummary")


@_attrs_define
class QuerySummary:
    """Summary model of a query definition

    Attributes:
        id (int | Unset): The immutable ID
        type_ (None | str | Unset): The type of the query
        added_by (None | str | Unset): The name of the user that added the query
        date_added (datetime.datetime | Unset): When the query was added
        last_changed_by (None | str | Unset): The name of the user that last changed the query
        date_changed (datetime.datetime | Unset): When the query was last changed
        select_from_query_name (None | str | Unset): The name of a query used as a base select for the query
        category (None | str | Unset): The category in which this query appears
        query_list (bool | Unset): True if the query is a Query List query. Applies To Raiser's Edge only.
        can_modify (bool | Unset): True if the user that requested the query can modify it
        can_execute (bool | Unset): True if the user that requested the query can execute it
        view_supported (bool | Unset): True if viewing the query is supported
        edit_supported (bool | Unset): True if editing the query is supported (based on its current query fields).
        supported_execution_modes (ExecutionModes | Unset): Modes of execution supported by a
            query<p>Members:</p><ul><li><i>None</i> - Execution is not supported</li><li><i>ById</i> - Execute by ID is
            supported</li><li><i>AdHoc</i> - Ad-hoc execution is supported</li><li><i>Both</i> - Execute by ID and ad-hoc
            execution are supported</li></ul>
        favorite (bool | Unset): True if this is a favorite query for user.
        created_by_query (bool | Unset): True if the query was created within the query module. False otherwise.
        has_ask_fields (bool | Unset): True if the query includes any filter fields with the ask operator
        name (None | str | Unset): The unique name of the query
        description (None | str | Unset): Description of the query
        format_ (QueryFormat | Unset): Available formats for queries<p>Members:</p><ul><li><i>Dynamic</i> - The query
            results are obtained by executing the query SQL</li><li><i>Static</i> - The IDs of the records found by the
            query are saved to a table</li></ul>
        others_can_execute (bool | Unset): Whether users other than the user that created the query can execute the
            query
        others_can_modify (bool | Unset): Whether users other than the user that created the query can modify the query
        category_id (int | Unset): The category identifier in which this query appears. Default to 1 for the General
            query category.
        output_limit (OutputLimit | Unset): A limit on the number of rows saved for a static query
        date_last_run (datetime.datetime | None | Unset): The date the query was last executed
        elapsed_ms (int | None | Unset): The elapsed milliseconds for the last execution
        num_records (int | None | Unset): The number of records resulting from the last execution
        type_id (int | Unset): The ID of the query type
        select_from_query_id (int | None | Unset): The ID of a query used as a base select for this query
        suppress_duplicates (bool | Unset): Whether to suppress duplicate (base) records in the query results
        constituent_filters (ConstituentFilters | Unset): Common convenience filters specific to RE queries
    """

    id: int | Unset = UNSET
    type_: None | str | Unset = UNSET
    added_by: None | str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    last_changed_by: None | str | Unset = UNSET
    date_changed: datetime.datetime | Unset = UNSET
    select_from_query_name: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    query_list: bool | Unset = UNSET
    can_modify: bool | Unset = UNSET
    can_execute: bool | Unset = UNSET
    view_supported: bool | Unset = UNSET
    edit_supported: bool | Unset = UNSET
    supported_execution_modes: ExecutionModes | Unset = UNSET
    favorite: bool | Unset = UNSET
    created_by_query: bool | Unset = UNSET
    has_ask_fields: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    format_: QueryFormat | Unset = UNSET
    others_can_execute: bool | Unset = UNSET
    others_can_modify: bool | Unset = UNSET
    category_id: int | Unset = UNSET
    output_limit: OutputLimit | Unset = UNSET
    date_last_run: datetime.datetime | None | Unset = UNSET
    elapsed_ms: int | None | Unset = UNSET
    num_records: int | None | Unset = UNSET
    type_id: int | Unset = UNSET
    select_from_query_id: int | None | Unset = UNSET
    suppress_duplicates: bool | Unset = UNSET
    constituent_filters: ConstituentFilters | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        added_by: None | str | Unset
        if isinstance(self.added_by, Unset):
            added_by = UNSET
        else:
            added_by = self.added_by

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        last_changed_by: None | str | Unset
        if isinstance(self.last_changed_by, Unset):
            last_changed_by = UNSET
        else:
            last_changed_by = self.last_changed_by

        date_changed: str | Unset = UNSET
        if not isinstance(self.date_changed, Unset):
            date_changed = self.date_changed.isoformat()

        select_from_query_name: None | str | Unset
        if isinstance(self.select_from_query_name, Unset):
            select_from_query_name = UNSET
        else:
            select_from_query_name = self.select_from_query_name

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        query_list = self.query_list

        can_modify = self.can_modify

        can_execute = self.can_execute

        view_supported = self.view_supported

        edit_supported = self.edit_supported

        supported_execution_modes: str | Unset = UNSET
        if not isinstance(self.supported_execution_modes, Unset):
            supported_execution_modes = self.supported_execution_modes.value

        favorite = self.favorite

        created_by_query = self.created_by_query

        has_ask_fields = self.has_ask_fields

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

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        others_can_execute = self.others_can_execute

        others_can_modify = self.others_can_modify

        category_id = self.category_id

        output_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_limit, Unset):
            output_limit = self.output_limit.to_dict()

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

        type_id = self.type_id

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

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if added_by is not UNSET:
            field_dict["added_by"] = added_by
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if last_changed_by is not UNSET:
            field_dict["last_changed_by"] = last_changed_by
        if date_changed is not UNSET:
            field_dict["date_changed"] = date_changed
        if select_from_query_name is not UNSET:
            field_dict["select_from_query_name"] = select_from_query_name
        if category is not UNSET:
            field_dict["category"] = category
        if query_list is not UNSET:
            field_dict["query_list"] = query_list
        if can_modify is not UNSET:
            field_dict["can_modify"] = can_modify
        if can_execute is not UNSET:
            field_dict["can_execute"] = can_execute
        if view_supported is not UNSET:
            field_dict["view_supported"] = view_supported
        if edit_supported is not UNSET:
            field_dict["edit_supported"] = edit_supported
        if supported_execution_modes is not UNSET:
            field_dict["supported_execution_modes"] = supported_execution_modes
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if created_by_query is not UNSET:
            field_dict["created_by_query"] = created_by_query
        if has_ask_fields is not UNSET:
            field_dict["has_ask_fields"] = has_ask_fields
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if format_ is not UNSET:
            field_dict["format"] = format_
        if others_can_execute is not UNSET:
            field_dict["others_can_execute"] = others_can_execute
        if others_can_modify is not UNSET:
            field_dict["others_can_modify"] = others_can_modify
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if output_limit is not UNSET:
            field_dict["output_limit"] = output_limit
        if date_last_run is not UNSET:
            field_dict["date_last_run"] = date_last_run
        if elapsed_ms is not UNSET:
            field_dict["elapsed_ms"] = elapsed_ms
        if num_records is not UNSET:
            field_dict["num_records"] = num_records
        if type_id is not UNSET:
            field_dict["type_id"] = type_id
        if select_from_query_id is not UNSET:
            field_dict["select_from_query_id"] = select_from_query_id
        if suppress_duplicates is not UNSET:
            field_dict["suppress_duplicates"] = suppress_duplicates
        if constituent_filters is not UNSET:
            field_dict["constituent_filters"] = constituent_filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constituent_filters import ConstituentFilters
        from ..models.output_limit import OutputLimit

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_added_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        added_by = _parse_added_by(d.pop("added_by", UNSET))

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        def _parse_last_changed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_changed_by = _parse_last_changed_by(d.pop("last_changed_by", UNSET))

        _date_changed = d.pop("date_changed", UNSET)
        date_changed: datetime.datetime | Unset
        if isinstance(_date_changed, Unset):
            date_changed = UNSET
        else:
            date_changed = isoparse(_date_changed)

        def _parse_select_from_query_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        select_from_query_name = _parse_select_from_query_name(
            d.pop("select_from_query_name", UNSET)
        )

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        query_list = d.pop("query_list", UNSET)

        can_modify = d.pop("can_modify", UNSET)

        can_execute = d.pop("can_execute", UNSET)

        view_supported = d.pop("view_supported", UNSET)

        edit_supported = d.pop("edit_supported", UNSET)

        _supported_execution_modes = d.pop("supported_execution_modes", UNSET)
        supported_execution_modes: ExecutionModes | Unset
        if isinstance(_supported_execution_modes, Unset):
            supported_execution_modes = UNSET
        else:
            supported_execution_modes = ExecutionModes(_supported_execution_modes)

        favorite = d.pop("favorite", UNSET)

        created_by_query = d.pop("created_by_query", UNSET)

        has_ask_fields = d.pop("has_ask_fields", UNSET)

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

        _format_ = d.pop("format", UNSET)
        format_: QueryFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = QueryFormat(_format_)

        others_can_execute = d.pop("others_can_execute", UNSET)

        others_can_modify = d.pop("others_can_modify", UNSET)

        category_id = d.pop("category_id", UNSET)

        _output_limit = d.pop("output_limit", UNSET)
        output_limit: OutputLimit | Unset
        if isinstance(_output_limit, Unset):
            output_limit = UNSET
        else:
            output_limit = OutputLimit.from_dict(_output_limit)

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

        type_id = d.pop("type_id", UNSET)

        def _parse_select_from_query_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        select_from_query_id = _parse_select_from_query_id(
            d.pop("select_from_query_id", UNSET)
        )

        suppress_duplicates = d.pop("suppress_duplicates", UNSET)

        _constituent_filters = d.pop("constituent_filters", UNSET)
        constituent_filters: ConstituentFilters | Unset
        if isinstance(_constituent_filters, Unset):
            constituent_filters = UNSET
        else:
            constituent_filters = ConstituentFilters.from_dict(_constituent_filters)

        query_summary = cls(
            id=id,
            type_=type_,
            added_by=added_by,
            date_added=date_added,
            last_changed_by=last_changed_by,
            date_changed=date_changed,
            select_from_query_name=select_from_query_name,
            category=category,
            query_list=query_list,
            can_modify=can_modify,
            can_execute=can_execute,
            view_supported=view_supported,
            edit_supported=edit_supported,
            supported_execution_modes=supported_execution_modes,
            favorite=favorite,
            created_by_query=created_by_query,
            has_ask_fields=has_ask_fields,
            name=name,
            description=description,
            format_=format_,
            others_can_execute=others_can_execute,
            others_can_modify=others_can_modify,
            category_id=category_id,
            output_limit=output_limit,
            date_last_run=date_last_run,
            elapsed_ms=elapsed_ms,
            num_records=num_records,
            type_id=type_id,
            select_from_query_id=select_from_query_id,
            suppress_duplicates=suppress_duplicates,
            constituent_filters=constituent_filters,
        )

        return query_summary

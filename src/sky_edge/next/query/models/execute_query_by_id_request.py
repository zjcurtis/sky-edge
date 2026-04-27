from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.formatting_mode import FormattingMode
from ..models.output_format import OutputFormat
from ..models.sql_generation_mode import SqlGenerationMode
from ..models.ux_mode import UXMode

if TYPE_CHECKING:
    from ..models.ask_field_information import AskFieldInformation


T = TypeVar("T", bound="ExecuteQueryByIdRequest")


@_attrs_define
class ExecuteQueryByIdRequest:
    """Request model for executing a query by ID.

    Attributes:
        id (int): Query identifier
        ux_mode (UXMode | Unset): User experience mode<p>Members:</p><ul><li><i>Synchronous</i> - Use this mode when an
            end-user is waiting on the job results.  The consumer will poll the job status until completion.
                        If the job gets throttled, you will receive a 429 response and the job will not be queued.  NOTE:
            You
                        must poll the job status using GET Query execution job at least every 10 seconds until the job
            completes
                        or the job will be cancelled due to inactivity.</li><li><i>Asynchronous</i> - Use this mode when no
            end-user is waiting on the job results.  The consumer will poll the job status until completion.
                        If the job gets throttled, the job will still be queued, up to a cap on the number of queued jobs.
            (There are no polling
                        requirements in this mode.)</li></ul>
        output_format (OutputFormat | Unset): Output format<p>Members:</p><ul><li><i>Csv</i> - Comma-separated
            values</li><li><i>Json</i> - JSON array</li><li><i>Jsonl</i> - JSON lines</li><li><i>Xlsx</i> - Excel</li></ul>
        formatting_mode (FormattingMode | Unset): Available modes for applying additional formatting to values retrieved
            by the query SQL<p>Members:</p><ul><li><i>None</i> - Do not apply any formatting to the values retrieved from
            the SQL</li><li><i>UI</i> - Use formatting rules appropriate for displaying the results in the
            UI</li><li><i>Export</i> - Use formatting rules appropriate for an export</li></ul>
        sql_generation_mode (SqlGenerationMode | Unset): SQL generation mode having an effect on the select columns
            used<p>Members:</p><ul><li><i>Query</i> - Use the query's select fields plus QRECID</li><li><i>Export</i> - Use
            the query's select fields without adding QRECID</li><li><i>Report</i> - Only select QRECID</li></ul>
        use_static_query_id_set (bool | Unset): When false, the query is run dynamically regardless of its format
            (dynamic or static).
            When true, the results only include the records in the static query's saved ID set.
            True is only valid for static queries that have a saved ID set.  For a static query to have a saved ID set, one
            of the following must be true:
            - The query was created or its format was changed to static in database view.
            - The query was created or its format was changed to static via the web view UI.
            - The query was created via the query API, POST /queries/refreshstaticquery was called for it, and that job
            completed successfully.
        results_file_name (None | str | Unset): Name of the file to be downloaded, without the file extension.
        ask_fields (list[AskFieldInformation] | None | Unset): A collection to provide ask field values. The order of
            this list should correspond to
            the order of filter fields with the operator set to Ask.
        display_code_table_long_description (bool | None | Unset): Display code table entries by long description
            (instead of short description).
            Optional override of the same-named stored setting in UserOptions.
        time_zone_offset_in_minutes (int | None | Unset): Optional time zone offset in minutes to account for the user's
            offset from UTC, used for relative date filter values.
    """

    id: int
    ux_mode: UXMode | Unset = UNSET
    output_format: OutputFormat | Unset = UNSET
    formatting_mode: FormattingMode | Unset = UNSET
    sql_generation_mode: SqlGenerationMode | Unset = UNSET
    use_static_query_id_set: bool | Unset = UNSET
    results_file_name: None | str | Unset = UNSET
    ask_fields: list[AskFieldInformation] | None | Unset = UNSET
    display_code_table_long_description: bool | None | Unset = UNSET
    time_zone_offset_in_minutes: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ux_mode: str | Unset = UNSET
        if not isinstance(self.ux_mode, Unset):
            ux_mode = self.ux_mode.value

        output_format: str | Unset = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value

        formatting_mode: str | Unset = UNSET
        if not isinstance(self.formatting_mode, Unset):
            formatting_mode = self.formatting_mode.value

        sql_generation_mode: str | Unset = UNSET
        if not isinstance(self.sql_generation_mode, Unset):
            sql_generation_mode = self.sql_generation_mode.value

        use_static_query_id_set = self.use_static_query_id_set

        results_file_name: None | str | Unset
        if isinstance(self.results_file_name, Unset):
            results_file_name = UNSET
        else:
            results_file_name = self.results_file_name

        ask_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.ask_fields, Unset):
            ask_fields = UNSET
        elif isinstance(self.ask_fields, list):
            ask_fields = []
            for ask_fields_type_0_item_data in self.ask_fields:
                ask_fields_type_0_item = ask_fields_type_0_item_data.to_dict()
                ask_fields.append(ask_fields_type_0_item)

        else:
            ask_fields = self.ask_fields

        display_code_table_long_description: bool | None | Unset
        if isinstance(self.display_code_table_long_description, Unset):
            display_code_table_long_description = UNSET
        else:
            display_code_table_long_description = (
                self.display_code_table_long_description
            )

        time_zone_offset_in_minutes: int | None | Unset
        if isinstance(self.time_zone_offset_in_minutes, Unset):
            time_zone_offset_in_minutes = UNSET
        else:
            time_zone_offset_in_minutes = self.time_zone_offset_in_minutes

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if ux_mode is not UNSET:
            field_dict["ux_mode"] = ux_mode
        if output_format is not UNSET:
            field_dict["output_format"] = output_format
        if formatting_mode is not UNSET:
            field_dict["formatting_mode"] = formatting_mode
        if sql_generation_mode is not UNSET:
            field_dict["sql_generation_mode"] = sql_generation_mode
        if use_static_query_id_set is not UNSET:
            field_dict["use_static_query_id_set"] = use_static_query_id_set
        if results_file_name is not UNSET:
            field_dict["results_file_name"] = results_file_name
        if ask_fields is not UNSET:
            field_dict["ask_fields"] = ask_fields
        if display_code_table_long_description is not UNSET:
            field_dict["display_code_table_long_description"] = (
                display_code_table_long_description
            )
        if time_zone_offset_in_minutes is not UNSET:
            field_dict["time_zone_offset_in_minutes"] = time_zone_offset_in_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ask_field_information import AskFieldInformation

        d = dict(src_dict)
        id = d.pop("id")

        _ux_mode = d.pop("ux_mode", UNSET)
        ux_mode: UXMode | Unset
        if isinstance(_ux_mode, Unset):
            ux_mode = UNSET
        else:
            ux_mode = UXMode(_ux_mode)

        _output_format = d.pop("output_format", UNSET)
        output_format: OutputFormat | Unset
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = OutputFormat(_output_format)

        _formatting_mode = d.pop("formatting_mode", UNSET)
        formatting_mode: FormattingMode | Unset
        if isinstance(_formatting_mode, Unset):
            formatting_mode = UNSET
        else:
            formatting_mode = FormattingMode(_formatting_mode)

        _sql_generation_mode = d.pop("sql_generation_mode", UNSET)
        sql_generation_mode: SqlGenerationMode | Unset
        if isinstance(_sql_generation_mode, Unset):
            sql_generation_mode = UNSET
        else:
            sql_generation_mode = SqlGenerationMode(_sql_generation_mode)

        use_static_query_id_set = d.pop("use_static_query_id_set", UNSET)

        def _parse_results_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        results_file_name = _parse_results_file_name(d.pop("results_file_name", UNSET))

        def _parse_ask_fields(data: object) -> list[AskFieldInformation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ask_fields_type_0 = []
                _ask_fields_type_0 = data
                for ask_fields_type_0_item_data in _ask_fields_type_0:
                    ask_fields_type_0_item = AskFieldInformation.from_dict(
                        ask_fields_type_0_item_data
                    )

                    ask_fields_type_0.append(ask_fields_type_0_item)

                return ask_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AskFieldInformation] | None | Unset, data)

        ask_fields = _parse_ask_fields(d.pop("ask_fields", UNSET))

        def _parse_display_code_table_long_description(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        display_code_table_long_description = (
            _parse_display_code_table_long_description(
                d.pop("display_code_table_long_description", UNSET)
            )
        )

        def _parse_time_zone_offset_in_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_zone_offset_in_minutes = _parse_time_zone_offset_in_minutes(
            d.pop("time_zone_offset_in_minutes", UNSET)
        )

        execute_query_by_id_request = cls(
            id=id,
            ux_mode=ux_mode,
            output_format=output_format,
            formatting_mode=formatting_mode,
            sql_generation_mode=sql_generation_mode,
            use_static_query_id_set=use_static_query_id_set,
            results_file_name=results_file_name,
            ask_fields=ask_fields,
            display_code_table_long_description=display_code_table_long_description,
            time_zone_offset_in_minutes=time_zone_offset_in_minutes,
        )

        return execute_query_by_id_request

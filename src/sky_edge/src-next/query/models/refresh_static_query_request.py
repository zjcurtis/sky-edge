from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.ux_mode import UXMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ask_field_information import AskFieldInformation


T = TypeVar("T", bound="RefreshStaticQueryRequest")


@_attrs_define
class RefreshStaticQueryRequest:
    """Request model for refreshing a static query

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
    ask_fields: list[AskFieldInformation] | None | Unset = UNSET
    display_code_table_long_description: bool | None | Unset = UNSET
    time_zone_offset_in_minutes: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ux_mode: str | Unset = UNSET
        if not isinstance(self.ux_mode, Unset):
            ux_mode = self.ux_mode.value

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
            display_code_table_long_description = self.display_code_table_long_description

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
        if ask_fields is not UNSET:
            field_dict["ask_fields"] = ask_fields
        if display_code_table_long_description is not UNSET:
            field_dict["display_code_table_long_description"] = display_code_table_long_description
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
                    ask_fields_type_0_item = AskFieldInformation.from_dict(ask_fields_type_0_item_data)

                    ask_fields_type_0.append(ask_fields_type_0_item)

                return ask_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AskFieldInformation] | None | Unset, data)

        ask_fields = _parse_ask_fields(d.pop("ask_fields", UNSET))

        def _parse_display_code_table_long_description(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        display_code_table_long_description = _parse_display_code_table_long_description(
            d.pop("display_code_table_long_description", UNSET)
        )

        def _parse_time_zone_offset_in_minutes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_zone_offset_in_minutes = _parse_time_zone_offset_in_minutes(d.pop("time_zone_offset_in_minutes", UNSET))

        refresh_static_query_request = cls(
            id=id,
            ux_mode=ux_mode,
            ask_fields=ask_fields,
            display_code_table_long_description=display_code_table_long_description,
            time_zone_offset_in_minutes=time_zone_offset_in_minutes,
        )

        return refresh_static_query_request

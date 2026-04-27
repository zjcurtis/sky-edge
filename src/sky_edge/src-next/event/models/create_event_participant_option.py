from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_event_participant_option_input_type import CreateEventParticipantOptionInputType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_participant_option_list_option import CreateParticipantOptionListOption


T = TypeVar("T", bound="CreateEventParticipantOption")


@_attrs_define
class CreateEventParticipantOption:
    """Event participant options are fields that collects details about participants, such as t-shirt sizes, meal
    preferences, or seating requests.
    Set options and their values for an event and then add responses for each participant.

        Attributes:
            name (str): The name of the event participant option.
            input_type (CreateEventParticipantOptionInputType): The types of values participants can use to provide
                responses.<p>Available values:</p><ul><li><i>Boolean</i> - Represents a true/false option.</li><li><i>String</i>
                - Represents a free-form text option.</li><li><i>List</i> - Represents an option with a list of possible
                values.</li></ul>
            multi_select (bool | Unset): Determines if participants can select more than one value for the List input type.
            list_options (list[CreateParticipantOptionListOption] | None | Unset): The available options for the List input
                type.
    """

    name: str
    input_type: CreateEventParticipantOptionInputType
    multi_select: bool | Unset = UNSET
    list_options: list[CreateParticipantOptionListOption] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        input_type = self.input_type.value

        multi_select = self.multi_select

        list_options: list[dict[str, Any]] | None | Unset
        if isinstance(self.list_options, Unset):
            list_options = UNSET
        elif isinstance(self.list_options, list):
            list_options = []
            for list_options_type_0_item_data in self.list_options:
                list_options_type_0_item = list_options_type_0_item_data.to_dict()
                list_options.append(list_options_type_0_item)

        else:
            list_options = self.list_options

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "input_type": input_type,
            }
        )
        if multi_select is not UNSET:
            field_dict["multi_select"] = multi_select
        if list_options is not UNSET:
            field_dict["list_options"] = list_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_participant_option_list_option import CreateParticipantOptionListOption

        d = dict(src_dict)
        name = d.pop("name")

        input_type = CreateEventParticipantOptionInputType(d.pop("input_type"))

        multi_select = d.pop("multi_select", UNSET)

        def _parse_list_options(data: object) -> list[CreateParticipantOptionListOption] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                list_options_type_0 = []
                _list_options_type_0 = data
                for list_options_type_0_item_data in _list_options_type_0:
                    list_options_type_0_item = CreateParticipantOptionListOption.from_dict(
                        list_options_type_0_item_data
                    )

                    list_options_type_0.append(list_options_type_0_item)

                return list_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateParticipantOptionListOption] | None | Unset, data)

        list_options = _parse_list_options(d.pop("list_options", UNSET))

        create_event_participant_option = cls(
            name=name,
            input_type=input_type,
            multi_select=multi_select,
            list_options=list_options,
        )

        return create_event_participant_option

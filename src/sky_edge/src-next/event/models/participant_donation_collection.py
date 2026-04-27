from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant_donation import ParticipantDonation


T = TypeVar("T", bound="ParticipantDonationCollection")


@_attrs_define
class ParticipantDonationCollection:
    """Defines a collection of participant donations.

    Attributes:
        count (int | Unset): The total number of items in the collection before limit/offset.
        value (list[ParticipantDonation] | None | Unset): The set of items included in the response. This may be a
            subset of the items in the collection.
    """

    count: int | Unset = UNSET
    value: list[ParticipantDonation] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        value: list[dict[str, Any]] | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        elif isinstance(self.value, list):
            value = []
            for value_type_0_item_data in self.value:
                value_type_0_item = value_type_0_item_data.to_dict()
                value.append(value_type_0_item)

        else:
            value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.participant_donation import ParticipantDonation

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_value(data: object) -> list[ParticipantDonation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_type_0 = []
                _value_type_0 = data
                for value_type_0_item_data in _value_type_0:
                    value_type_0_item = ParticipantDonation.from_dict(value_type_0_item_data)

                    value_type_0.append(value_type_0_item)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ParticipantDonation] | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        participant_donation_collection = cls(
            count=count,
            value=value,
        )

        return participant_donation_collection

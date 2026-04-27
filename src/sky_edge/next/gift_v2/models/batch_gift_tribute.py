from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.batch_gift_tribute_gift_tribute_acknowledge_status import (
    BatchGiftTributeGiftTributeAcknowledgeStatus,
)

if TYPE_CHECKING:
    from ..models.batch_gift_tribute_acknowledgee import BatchGiftTributeAcknowledgee


T = TypeVar("T", bound="BatchGiftTribute")


@_attrs_define
class BatchGiftTribute:
    """Represents a batch gift tribute record

    Attributes:
        batch_gift_id (None | str | Unset): ID of the batch gift to which this gift tribute belongs
        batch_id (None | str | Unset): ID of the batch to which this tribute belongs
        tribute_id (None | str | Unset): ID of the constituent tribute record
        sequence (int | None | Unset): The sequence
        acknowledgees (list[BatchGiftTributeAcknowledgee] | None | Unset): Acknowledgees belonging to this gift tribute
        acknowledge_status (BatchGiftTributeGiftTributeAcknowledgeStatus | Unset): The acknowledgement type.
        can_view_honor_or_memorial_constituent (bool | None | Unset): Whether the user has permissions to view the
            constituent being honored or memorialized.
        gift_tribute_id (None | str | Unset): The gift tribute ID.
        honor_or_memorial_constituent_id (None | str | Unset): The constituent identifier for the person being honored
            or memorialized.
        honor_or_memorial_constituent_name (None | str | Unset): The constituent identifier for the person being honored
            or memorialized.
        tribute_code (None | str | Unset): The code table value of the tribute description.
        tribute_description (None | str | Unset): The tribute description from the code value.
        tribute_type_code (None | str | Unset): The code table value of the tribute type description.
        tribute_type_description (None | str | Unset): The tribute's type description from the code value.
    """

    batch_gift_id: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    tribute_id: None | str | Unset = UNSET
    sequence: int | None | Unset = UNSET
    acknowledgees: list[BatchGiftTributeAcknowledgee] | None | Unset = UNSET
    acknowledge_status: BatchGiftTributeGiftTributeAcknowledgeStatus | Unset = UNSET
    can_view_honor_or_memorial_constituent: bool | None | Unset = UNSET
    gift_tribute_id: None | str | Unset = UNSET
    honor_or_memorial_constituent_id: None | str | Unset = UNSET
    honor_or_memorial_constituent_name: None | str | Unset = UNSET
    tribute_code: None | str | Unset = UNSET
    tribute_description: None | str | Unset = UNSET
    tribute_type_code: None | str | Unset = UNSET
    tribute_type_description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        batch_gift_id: None | str | Unset
        if isinstance(self.batch_gift_id, Unset):
            batch_gift_id = UNSET
        else:
            batch_gift_id = self.batch_gift_id

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        tribute_id: None | str | Unset
        if isinstance(self.tribute_id, Unset):
            tribute_id = UNSET
        else:
            tribute_id = self.tribute_id

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

        acknowledgees: list[dict[str, Any]] | None | Unset
        if isinstance(self.acknowledgees, Unset):
            acknowledgees = UNSET
        elif isinstance(self.acknowledgees, list):
            acknowledgees = []
            for acknowledgees_type_0_item_data in self.acknowledgees:
                acknowledgees_type_0_item = acknowledgees_type_0_item_data.to_dict()
                acknowledgees.append(acknowledgees_type_0_item)

        else:
            acknowledgees = self.acknowledgees

        acknowledge_status: str | Unset = UNSET
        if not isinstance(self.acknowledge_status, Unset):
            acknowledge_status = self.acknowledge_status.value

        can_view_honor_or_memorial_constituent: bool | None | Unset
        if isinstance(self.can_view_honor_or_memorial_constituent, Unset):
            can_view_honor_or_memorial_constituent = UNSET
        else:
            can_view_honor_or_memorial_constituent = (
                self.can_view_honor_or_memorial_constituent
            )

        gift_tribute_id: None | str | Unset
        if isinstance(self.gift_tribute_id, Unset):
            gift_tribute_id = UNSET
        else:
            gift_tribute_id = self.gift_tribute_id

        honor_or_memorial_constituent_id: None | str | Unset
        if isinstance(self.honor_or_memorial_constituent_id, Unset):
            honor_or_memorial_constituent_id = UNSET
        else:
            honor_or_memorial_constituent_id = self.honor_or_memorial_constituent_id

        honor_or_memorial_constituent_name: None | str | Unset
        if isinstance(self.honor_or_memorial_constituent_name, Unset):
            honor_or_memorial_constituent_name = UNSET
        else:
            honor_or_memorial_constituent_name = self.honor_or_memorial_constituent_name

        tribute_code: None | str | Unset
        if isinstance(self.tribute_code, Unset):
            tribute_code = UNSET
        else:
            tribute_code = self.tribute_code

        tribute_description: None | str | Unset
        if isinstance(self.tribute_description, Unset):
            tribute_description = UNSET
        else:
            tribute_description = self.tribute_description

        tribute_type_code: None | str | Unset
        if isinstance(self.tribute_type_code, Unset):
            tribute_type_code = UNSET
        else:
            tribute_type_code = self.tribute_type_code

        tribute_type_description: None | str | Unset
        if isinstance(self.tribute_type_description, Unset):
            tribute_type_description = UNSET
        else:
            tribute_type_description = self.tribute_type_description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if batch_gift_id is not UNSET:
            field_dict["batch_gift_id"] = batch_gift_id
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if tribute_id is not UNSET:
            field_dict["tribute_id"] = tribute_id
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
        if acknowledgees is not UNSET:
            field_dict["acknowledgees"] = acknowledgees
        if acknowledge_status is not UNSET:
            field_dict["acknowledge_status"] = acknowledge_status
        if can_view_honor_or_memorial_constituent is not UNSET:
            field_dict["can_view_honor_or_memorial_constituent"] = (
                can_view_honor_or_memorial_constituent
            )
        if gift_tribute_id is not UNSET:
            field_dict["gift_tribute_id"] = gift_tribute_id
        if honor_or_memorial_constituent_id is not UNSET:
            field_dict["honor_or_memorial_constituent_id"] = (
                honor_or_memorial_constituent_id
            )
        if honor_or_memorial_constituent_name is not UNSET:
            field_dict["honor_or_memorial_constituent_name"] = (
                honor_or_memorial_constituent_name
            )
        if tribute_code is not UNSET:
            field_dict["tribute_code"] = tribute_code
        if tribute_description is not UNSET:
            field_dict["tribute_description"] = tribute_description
        if tribute_type_code is not UNSET:
            field_dict["tribute_type_code"] = tribute_type_code
        if tribute_type_description is not UNSET:
            field_dict["tribute_type_description"] = tribute_type_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.batch_gift_tribute_acknowledgee import (
            BatchGiftTributeAcknowledgee,
        )

        d = dict(src_dict)

        def _parse_batch_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_gift_id = _parse_batch_gift_id(d.pop("batch_gift_id", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        def _parse_tribute_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_id = _parse_tribute_id(d.pop("tribute_id", UNSET))

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

        def _parse_acknowledgees(
            data: object,
        ) -> list[BatchGiftTributeAcknowledgee] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                acknowledgees_type_0 = []
                _acknowledgees_type_0 = data
                for acknowledgees_type_0_item_data in _acknowledgees_type_0:
                    acknowledgees_type_0_item = BatchGiftTributeAcknowledgee.from_dict(
                        acknowledgees_type_0_item_data
                    )

                    acknowledgees_type_0.append(acknowledgees_type_0_item)

                return acknowledgees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftTributeAcknowledgee] | None | Unset, data)

        acknowledgees = _parse_acknowledgees(d.pop("acknowledgees", UNSET))

        _acknowledge_status = d.pop("acknowledge_status", UNSET)
        acknowledge_status: BatchGiftTributeGiftTributeAcknowledgeStatus | Unset
        if isinstance(_acknowledge_status, Unset):
            acknowledge_status = UNSET
        else:
            acknowledge_status = BatchGiftTributeGiftTributeAcknowledgeStatus(
                _acknowledge_status
            )

        def _parse_can_view_honor_or_memorial_constituent(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_view_honor_or_memorial_constituent = (
            _parse_can_view_honor_or_memorial_constituent(
                d.pop("can_view_honor_or_memorial_constituent", UNSET)
            )
        )

        def _parse_gift_tribute_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_tribute_id = _parse_gift_tribute_id(d.pop("gift_tribute_id", UNSET))

        def _parse_honor_or_memorial_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        honor_or_memorial_constituent_id = _parse_honor_or_memorial_constituent_id(
            d.pop("honor_or_memorial_constituent_id", UNSET)
        )

        def _parse_honor_or_memorial_constituent_name(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        honor_or_memorial_constituent_name = _parse_honor_or_memorial_constituent_name(
            d.pop("honor_or_memorial_constituent_name", UNSET)
        )

        def _parse_tribute_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_code = _parse_tribute_code(d.pop("tribute_code", UNSET))

        def _parse_tribute_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_description = _parse_tribute_description(
            d.pop("tribute_description", UNSET)
        )

        def _parse_tribute_type_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_type_code = _parse_tribute_type_code(d.pop("tribute_type_code", UNSET))

        def _parse_tribute_type_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_type_description = _parse_tribute_type_description(
            d.pop("tribute_type_description", UNSET)
        )

        batch_gift_tribute = cls(
            batch_gift_id=batch_gift_id,
            batch_id=batch_id,
            tribute_id=tribute_id,
            sequence=sequence,
            acknowledgees=acknowledgees,
            acknowledge_status=acknowledge_status,
            can_view_honor_or_memorial_constituent=can_view_honor_or_memorial_constituent,
            gift_tribute_id=gift_tribute_id,
            honor_or_memorial_constituent_id=honor_or_memorial_constituent_id,
            honor_or_memorial_constituent_name=honor_or_memorial_constituent_name,
            tribute_code=tribute_code,
            tribute_description=tribute_description,
            tribute_type_code=tribute_type_code,
            tribute_type_description=tribute_type_description,
        )

        return batch_gift_tribute

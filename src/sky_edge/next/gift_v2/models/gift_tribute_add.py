from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.gift_tribute_add_acknowledgement_status import (
    GiftTributeAddAcknowledgementStatus,
)

if TYPE_CHECKING:
    from ..models.gift_tribute_acknowledgee_add import GiftTributeAcknowledgeeAdd


T = TypeVar("T", bound="GiftTributeAdd")


@_attrs_define
class GiftTributeAdd:
    """Represents a tribute record.

    Attributes:
        id (None | str | Unset): ID of the gift tribute Example: 12345.
        gift_legacy_id (None | str | Unset): The record ID of the gift to which this tribute belongs. Example: 12345.
        gift_lookup_id (None | str | Unset): The lookup ID of the gift to which this tribute belongs. Example:
            Lookup-12345.
        parent_gift_date (datetime.datetime | None | Unset): The date of the gift to validate.
        tribute_id (None | str | Unset): Tribute record ID. Example: 12345.
        tribute_type_id (None | str | Unset): Tribute type ID. Example: 12345.
        tribute_acknowledgees (list[GiftTributeAcknowledgeeAdd] | None | Unset): Validatable acknowledgees.
        acknowledge_status (GiftTributeAddAcknowledgementStatus | Unset): The acknowledgement status.
    """

    id: None | str | Unset = UNSET
    gift_legacy_id: None | str | Unset = UNSET
    gift_lookup_id: None | str | Unset = UNSET
    parent_gift_date: datetime.datetime | None | Unset = UNSET
    tribute_id: None | str | Unset = UNSET
    tribute_type_id: None | str | Unset = UNSET
    tribute_acknowledgees: list[GiftTributeAcknowledgeeAdd] | None | Unset = UNSET
    acknowledge_status: GiftTributeAddAcknowledgementStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        gift_legacy_id: None | str | Unset
        if isinstance(self.gift_legacy_id, Unset):
            gift_legacy_id = UNSET
        else:
            gift_legacy_id = self.gift_legacy_id

        gift_lookup_id: None | str | Unset
        if isinstance(self.gift_lookup_id, Unset):
            gift_lookup_id = UNSET
        else:
            gift_lookup_id = self.gift_lookup_id

        parent_gift_date: None | str | Unset
        if isinstance(self.parent_gift_date, Unset):
            parent_gift_date = UNSET
        elif isinstance(self.parent_gift_date, datetime.datetime):
            parent_gift_date = self.parent_gift_date.isoformat()
        else:
            parent_gift_date = self.parent_gift_date

        tribute_id: None | str | Unset
        if isinstance(self.tribute_id, Unset):
            tribute_id = UNSET
        else:
            tribute_id = self.tribute_id

        tribute_type_id: None | str | Unset
        if isinstance(self.tribute_type_id, Unset):
            tribute_type_id = UNSET
        else:
            tribute_type_id = self.tribute_type_id

        tribute_acknowledgees: list[dict[str, Any]] | None | Unset
        if isinstance(self.tribute_acknowledgees, Unset):
            tribute_acknowledgees = UNSET
        elif isinstance(self.tribute_acknowledgees, list):
            tribute_acknowledgees = []
            for tribute_acknowledgees_type_0_item_data in self.tribute_acknowledgees:
                tribute_acknowledgees_type_0_item = (
                    tribute_acknowledgees_type_0_item_data.to_dict()
                )
                tribute_acknowledgees.append(tribute_acknowledgees_type_0_item)

        else:
            tribute_acknowledgees = self.tribute_acknowledgees

        acknowledge_status: str | Unset = UNSET
        if not isinstance(self.acknowledge_status, Unset):
            acknowledge_status = self.acknowledge_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gift_legacy_id is not UNSET:
            field_dict["gift_legacy_id"] = gift_legacy_id
        if gift_lookup_id is not UNSET:
            field_dict["gift_lookup_id"] = gift_lookup_id
        if parent_gift_date is not UNSET:
            field_dict["parent_gift_date"] = parent_gift_date
        if tribute_id is not UNSET:
            field_dict["tribute_id"] = tribute_id
        if tribute_type_id is not UNSET:
            field_dict["tribute_type_id"] = tribute_type_id
        if tribute_acknowledgees is not UNSET:
            field_dict["tribute_acknowledgees"] = tribute_acknowledgees
        if acknowledge_status is not UNSET:
            field_dict["acknowledge_status"] = acknowledge_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_tribute_acknowledgee_add import GiftTributeAcknowledgeeAdd

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_gift_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_legacy_id = _parse_gift_legacy_id(d.pop("gift_legacy_id", UNSET))

        def _parse_gift_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_lookup_id = _parse_gift_lookup_id(d.pop("gift_lookup_id", UNSET))

        def _parse_parent_gift_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_gift_date_type_0 = isoparse(data)

                return parent_gift_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        parent_gift_date = _parse_parent_gift_date(d.pop("parent_gift_date", UNSET))

        def _parse_tribute_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_id = _parse_tribute_id(d.pop("tribute_id", UNSET))

        def _parse_tribute_type_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tribute_type_id = _parse_tribute_type_id(d.pop("tribute_type_id", UNSET))

        def _parse_tribute_acknowledgees(
            data: object,
        ) -> list[GiftTributeAcknowledgeeAdd] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tribute_acknowledgees_type_0 = []
                _tribute_acknowledgees_type_0 = data
                for (
                    tribute_acknowledgees_type_0_item_data
                ) in _tribute_acknowledgees_type_0:
                    tribute_acknowledgees_type_0_item = (
                        GiftTributeAcknowledgeeAdd.from_dict(
                            tribute_acknowledgees_type_0_item_data
                        )
                    )

                    tribute_acknowledgees_type_0.append(
                        tribute_acknowledgees_type_0_item
                    )

                return tribute_acknowledgees_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftTributeAcknowledgeeAdd] | None | Unset, data)

        tribute_acknowledgees = _parse_tribute_acknowledgees(
            d.pop("tribute_acknowledgees", UNSET)
        )

        _acknowledge_status = d.pop("acknowledge_status", UNSET)
        acknowledge_status: GiftTributeAddAcknowledgementStatus | Unset
        if isinstance(_acknowledge_status, Unset):
            acknowledge_status = UNSET
        else:
            acknowledge_status = GiftTributeAddAcknowledgementStatus(
                _acknowledge_status
            )

        gift_tribute_add = cls(
            id=id,
            gift_legacy_id=gift_legacy_id,
            gift_lookup_id=gift_lookup_id,
            parent_gift_date=parent_gift_date,
            tribute_id=tribute_id,
            tribute_type_id=tribute_type_id,
            tribute_acknowledgees=tribute_acknowledgees,
            acknowledge_status=acknowledge_status,
        )

        return gift_tribute_add

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchGiftTributeAcknowledgee")


@_attrs_define
class BatchGiftTributeAcknowledgee:
    """An acknowledgee for a batch gift tribute

    Attributes:
        id (None | str | Unset): System ID of the acknowledgee record
        batch_gift_id (None | str | Unset): System ID of the batch gift to which this acknowledgee belongs
        batch_id (None | str | Unset): System ID of the batch to which this acknowledgee belongs
        batch_gift_tribute_id (None | str | Unset): System ID of the batch gift tribute to which this acknowledgee
            belongs
        relationship_id (None | str | Unset): System ID of the relationship this acknowledgee has with the constituent
        relationship_code_value (None | str | Unset): Name of the relationship this acknowledgee has with the
            constituent
        acknowledge_date (datetime.datetime | None | Unset): The acknowledgement date.
        can_view (bool | None | Unset): Whether the user has permissions to view the acknowledgee.
        contact_id (None | str | Unset): The acknowledgee's contact ID (equivalent to acknowledgee's constituent ID).
        acknowledgee_name (None | str | Unset): The name of the acknowledgee
        acknowledged (bool | None | Unset): Whether the acknowledgee has acknowledged.
        self_acknowledgee (bool | None | Unset): If the acknowledgee is a subject of the tribute.
        letter_code (None | str | Unset): The letter's code table value.
        letter_name (None | str | Unset): The name of the letter.
        relationship (None | str | Unset): The relationship.
        relationship_code (None | str | Unset): The relationship's code table value.
    """

    id: None | str | Unset = UNSET
    batch_gift_id: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    batch_gift_tribute_id: None | str | Unset = UNSET
    relationship_id: None | str | Unset = UNSET
    relationship_code_value: None | str | Unset = UNSET
    acknowledge_date: datetime.datetime | None | Unset = UNSET
    can_view: bool | None | Unset = UNSET
    contact_id: None | str | Unset = UNSET
    acknowledgee_name: None | str | Unset = UNSET
    acknowledged: bool | None | Unset = UNSET
    self_acknowledgee: bool | None | Unset = UNSET
    letter_code: None | str | Unset = UNSET
    letter_name: None | str | Unset = UNSET
    relationship: None | str | Unset = UNSET
    relationship_code: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

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

        batch_gift_tribute_id: None | str | Unset
        if isinstance(self.batch_gift_tribute_id, Unset):
            batch_gift_tribute_id = UNSET
        else:
            batch_gift_tribute_id = self.batch_gift_tribute_id

        relationship_id: None | str | Unset
        if isinstance(self.relationship_id, Unset):
            relationship_id = UNSET
        else:
            relationship_id = self.relationship_id

        relationship_code_value: None | str | Unset
        if isinstance(self.relationship_code_value, Unset):
            relationship_code_value = UNSET
        else:
            relationship_code_value = self.relationship_code_value

        acknowledge_date: None | str | Unset
        if isinstance(self.acknowledge_date, Unset):
            acknowledge_date = UNSET
        elif isinstance(self.acknowledge_date, datetime.datetime):
            acknowledge_date = self.acknowledge_date.isoformat()
        else:
            acknowledge_date = self.acknowledge_date

        can_view: bool | None | Unset
        if isinstance(self.can_view, Unset):
            can_view = UNSET
        else:
            can_view = self.can_view

        contact_id: None | str | Unset
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = self.contact_id

        acknowledgee_name: None | str | Unset
        if isinstance(self.acknowledgee_name, Unset):
            acknowledgee_name = UNSET
        else:
            acknowledgee_name = self.acknowledgee_name

        acknowledged: bool | None | Unset
        if isinstance(self.acknowledged, Unset):
            acknowledged = UNSET
        else:
            acknowledged = self.acknowledged

        self_acknowledgee: bool | None | Unset
        if isinstance(self.self_acknowledgee, Unset):
            self_acknowledgee = UNSET
        else:
            self_acknowledgee = self.self_acknowledgee

        letter_code: None | str | Unset
        if isinstance(self.letter_code, Unset):
            letter_code = UNSET
        else:
            letter_code = self.letter_code

        letter_name: None | str | Unset
        if isinstance(self.letter_name, Unset):
            letter_name = UNSET
        else:
            letter_name = self.letter_name

        relationship: None | str | Unset
        if isinstance(self.relationship, Unset):
            relationship = UNSET
        else:
            relationship = self.relationship

        relationship_code: None | str | Unset
        if isinstance(self.relationship_code, Unset):
            relationship_code = UNSET
        else:
            relationship_code = self.relationship_code

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if batch_gift_id is not UNSET:
            field_dict["batch_gift_id"] = batch_gift_id
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if batch_gift_tribute_id is not UNSET:
            field_dict["batch_gift_tribute_id"] = batch_gift_tribute_id
        if relationship_id is not UNSET:
            field_dict["relationship_id"] = relationship_id
        if relationship_code_value is not UNSET:
            field_dict["relationship_code_value"] = relationship_code_value
        if acknowledge_date is not UNSET:
            field_dict["acknowledge_date"] = acknowledge_date
        if can_view is not UNSET:
            field_dict["can_view"] = can_view
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if acknowledgee_name is not UNSET:
            field_dict["acknowledgee_name"] = acknowledgee_name
        if acknowledged is not UNSET:
            field_dict["acknowledged"] = acknowledged
        if self_acknowledgee is not UNSET:
            field_dict["self_acknowledgee"] = self_acknowledgee
        if letter_code is not UNSET:
            field_dict["letter_code"] = letter_code
        if letter_name is not UNSET:
            field_dict["letter_name"] = letter_name
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if relationship_code is not UNSET:
            field_dict["relationship_code"] = relationship_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

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

        def _parse_batch_gift_tribute_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_gift_tribute_id = _parse_batch_gift_tribute_id(d.pop("batch_gift_tribute_id", UNSET))

        def _parse_relationship_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship_id = _parse_relationship_id(d.pop("relationship_id", UNSET))

        def _parse_relationship_code_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship_code_value = _parse_relationship_code_value(d.pop("relationship_code_value", UNSET))

        def _parse_acknowledge_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledge_date_type_0 = isoparse(data)

                return acknowledge_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acknowledge_date = _parse_acknowledge_date(d.pop("acknowledge_date", UNSET))

        def _parse_can_view(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        can_view = _parse_can_view(d.pop("can_view", UNSET))

        def _parse_contact_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_id = _parse_contact_id(d.pop("contact_id", UNSET))

        def _parse_acknowledgee_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        acknowledgee_name = _parse_acknowledgee_name(d.pop("acknowledgee_name", UNSET))

        def _parse_acknowledged(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        acknowledged = _parse_acknowledged(d.pop("acknowledged", UNSET))

        def _parse_self_acknowledgee(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        self_acknowledgee = _parse_self_acknowledgee(d.pop("self_acknowledgee", UNSET))

        def _parse_letter_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        letter_code = _parse_letter_code(d.pop("letter_code", UNSET))

        def _parse_letter_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        letter_name = _parse_letter_name(d.pop("letter_name", UNSET))

        def _parse_relationship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship = _parse_relationship(d.pop("relationship", UNSET))

        def _parse_relationship_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship_code = _parse_relationship_code(d.pop("relationship_code", UNSET))

        batch_gift_tribute_acknowledgee = cls(
            id=id,
            batch_gift_id=batch_gift_id,
            batch_id=batch_id,
            batch_gift_tribute_id=batch_gift_tribute_id,
            relationship_id=relationship_id,
            relationship_code_value=relationship_code_value,
            acknowledge_date=acknowledge_date,
            can_view=can_view,
            contact_id=contact_id,
            acknowledgee_name=acknowledgee_name,
            acknowledged=acknowledged,
            self_acknowledgee=self_acknowledgee,
            letter_code=letter_code,
            letter_name=letter_name,
            relationship=relationship,
            relationship_code=relationship_code,
        )

        return batch_gift_tribute_acknowledgee

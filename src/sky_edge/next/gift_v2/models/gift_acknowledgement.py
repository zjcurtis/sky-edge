from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.gift_acknowledgement_acknowledgement_status import (
    GiftAcknowledgementAcknowledgementStatus,
)

if TYPE_CHECKING:
    from ..models.acknowledgement_letter import AcknowledgementLetter


T = TypeVar("T", bound="GiftAcknowledgement")


@_attrs_define
class GiftAcknowledgement:
    """Acknowledgement information for a gift.

    Attributes:
        gift_legacy_id (None | str | Unset): The legacy ID of the acknowledgement's associated gift. Example: 12345.
        status (GiftAcknowledgementAcknowledgementStatus | Unset): The gift acknowledgement's status. Example:
            NotAcknowledged.
        acknowledgement_date (datetime.datetime | None | Unset): The acknowledgement's date. Deprecated. Please use the
            date property instead.
        date (datetime.date | None | Unset): The acknowledgement's date.
        letter (AcknowledgementLetter | Unset): Model representing an acknowledgement letter.
        gift_lookup_id (None | str | Unset): Lookupd ID of the acknowledgement's associated gift. Example:
            LookupId-12345.
    """

    gift_legacy_id: None | str | Unset = UNSET
    status: GiftAcknowledgementAcknowledgementStatus | Unset = UNSET
    acknowledgement_date: datetime.datetime | None | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    letter: AcknowledgementLetter | Unset = UNSET
    gift_lookup_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        gift_legacy_id: None | str | Unset
        if isinstance(self.gift_legacy_id, Unset):
            gift_legacy_id = UNSET
        else:
            gift_legacy_id = self.gift_legacy_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        acknowledgement_date: None | str | Unset
        if isinstance(self.acknowledgement_date, Unset):
            acknowledgement_date = UNSET
        elif isinstance(self.acknowledgement_date, datetime.datetime):
            acknowledgement_date = self.acknowledgement_date.isoformat()
        else:
            acknowledgement_date = self.acknowledgement_date

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        letter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.letter, Unset):
            letter = self.letter.to_dict()

        gift_lookup_id: None | str | Unset
        if isinstance(self.gift_lookup_id, Unset):
            gift_lookup_id = UNSET
        else:
            gift_lookup_id = self.gift_lookup_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if gift_legacy_id is not UNSET:
            field_dict["gift_legacy_id"] = gift_legacy_id
        if status is not UNSET:
            field_dict["status"] = status
        if acknowledgement_date is not UNSET:
            field_dict["acknowledgement_date"] = acknowledgement_date
        if date is not UNSET:
            field_dict["date"] = date
        if letter is not UNSET:
            field_dict["letter"] = letter
        if gift_lookup_id is not UNSET:
            field_dict["gift_lookup_id"] = gift_lookup_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acknowledgement_letter import AcknowledgementLetter

        d = dict(src_dict)

        def _parse_gift_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_legacy_id = _parse_gift_legacy_id(d.pop("gift_legacy_id", UNSET))

        _status = d.pop("status", UNSET)
        status: GiftAcknowledgementAcknowledgementStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GiftAcknowledgementAcknowledgementStatus(_status)

        def _parse_acknowledgement_date(
            data: object,
        ) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledgement_date_type_0 = isoparse(data)

                return acknowledgement_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acknowledgement_date = _parse_acknowledgement_date(
            d.pop("acknowledgement_date", UNSET)
        )

        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data).date()

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        _letter = d.pop("letter", UNSET)
        letter: AcknowledgementLetter | Unset
        if isinstance(_letter, Unset):
            letter = UNSET
        else:
            letter = AcknowledgementLetter.from_dict(_letter)

        def _parse_gift_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gift_lookup_id = _parse_gift_lookup_id(d.pop("gift_lookup_id", UNSET))

        gift_acknowledgement = cls(
            gift_legacy_id=gift_legacy_id,
            status=status,
            acknowledgement_date=acknowledgement_date,
            date=date,
            letter=letter,
            gift_lookup_id=gift_lookup_id,
        )

        return gift_acknowledgement

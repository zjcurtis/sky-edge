from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate
    from ..models.gift_marketing_detail_edit import GiftMarketingDetailEdit


T = TypeVar("T", bound="GiftEdit")


@_attrs_define
class GiftEdit:
    """An object that represents the gift to edit.
    Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot of information associated
    with them to ensure that they are properly allocated and acknowledged.

        Attributes:
            lookup_id (str | Unset): The user-defined identifier for the gift. Character limit: 50.
            date (datetime.datetime | Unset): The gift date. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            is_anonymous (bool | Unset): Indicates whether the gift is anonymous.
                If no value is provided, the default anonymity of the donor will be used.
            reference (str | Unset): Notes to track special details about a gift such as the motivation behind it or a
                detailed description of a gift-in-kind. Character limit: 255.
            gift_status (str | Unset): The status of the gift. Available values are <i>Active</i>, <i>Held</i>,
                <i>Terminated</i>, <i>Completed</i>, and <i>Cancelled.</i>
                The status can only be changed for gifts of type pledge and recurring gift.
                The status cannot be changed from Terminated, Completed, or Cancelled to Active or Held.
            recurring_gift_status_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial
                dates such as February 9 (with no year indicated).
            gift_code (str | Unset): The gift code of the gift.
            subtype (str | Unset): The subtype of the gift. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/58bdd5edd7dcde06046081d6/operations/ListGiftSubtypes"><b>Gift
                Subtypes</b></a> table.
            constituency (str | Unset): The constituency of the gift.
            marketing_details (GiftMarketingDetailEdit | Unset): Represents marketing information for a gift.
    """

    lookup_id: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    reference: str | Unset = UNSET
    gift_status: str | Unset = UNSET
    recurring_gift_status_date: FuzzyDate | Unset = UNSET
    gift_code: str | Unset = UNSET
    subtype: str | Unset = UNSET
    constituency: str | Unset = UNSET
    marketing_details: GiftMarketingDetailEdit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lookup_id = self.lookup_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        is_anonymous = self.is_anonymous

        reference = self.reference

        gift_status = self.gift_status

        recurring_gift_status_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurring_gift_status_date, Unset):
            recurring_gift_status_date = self.recurring_gift_status_date.to_dict()

        gift_code = self.gift_code

        subtype = self.subtype

        constituency = self.constituency

        marketing_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.marketing_details, Unset):
            marketing_details = self.marketing_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if date is not UNSET:
            field_dict["date"] = date
        if is_anonymous is not UNSET:
            field_dict["is_anonymous"] = is_anonymous
        if reference is not UNSET:
            field_dict["reference"] = reference
        if gift_status is not UNSET:
            field_dict["gift_status"] = gift_status
        if recurring_gift_status_date is not UNSET:
            field_dict["recurring_gift_status_date"] = recurring_gift_status_date
        if gift_code is not UNSET:
            field_dict["gift_code"] = gift_code
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if constituency is not UNSET:
            field_dict["constituency"] = constituency
        if marketing_details is not UNSET:
            field_dict["marketing_details"] = marketing_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate
        from ..models.gift_marketing_detail_edit import GiftMarketingDetailEdit

        d = dict(src_dict)
        lookup_id = d.pop("lookup_id", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        is_anonymous = d.pop("is_anonymous", UNSET)

        reference = d.pop("reference", UNSET)

        gift_status = d.pop("gift_status", UNSET)

        _recurring_gift_status_date = d.pop("recurring_gift_status_date", UNSET)
        recurring_gift_status_date: FuzzyDate | Unset
        if isinstance(_recurring_gift_status_date, Unset):
            recurring_gift_status_date = UNSET
        else:
            recurring_gift_status_date = FuzzyDate.from_dict(_recurring_gift_status_date)

        gift_code = d.pop("gift_code", UNSET)

        subtype = d.pop("subtype", UNSET)

        constituency = d.pop("constituency", UNSET)

        _marketing_details = d.pop("marketing_details", UNSET)
        marketing_details: GiftMarketingDetailEdit | Unset
        if isinstance(_marketing_details, Unset):
            marketing_details = UNSET
        else:
            marketing_details = GiftMarketingDetailEdit.from_dict(_marketing_details)

        gift_edit = cls(
            lookup_id=lookup_id,
            date=date,
            is_anonymous=is_anonymous,
            reference=reference,
            gift_status=gift_status,
            recurring_gift_status_date=recurring_gift_status_date,
            gift_code=gift_code,
            subtype=subtype,
            constituency=constituency,
            marketing_details=marketing_details,
        )

        gift_edit.additional_properties = d
        return gift_edit

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

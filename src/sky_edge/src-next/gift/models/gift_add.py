from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledgement_add import AcknowledgementAdd
    from ..models.currency import Currency
    from ..models.custom_field_add import CustomFieldAdd
    from ..models.gift_fundraiser_add import GiftFundraiserAdd
    from ..models.gift_split_add import GiftSplitAdd
    from ..models.payment_add import PaymentAdd
    from ..models.receipt_add import ReceiptAdd
    from ..models.recurring_gift_schedule_add import RecurringGiftScheduleAdd
    from ..models.soft_credit_add import SoftCreditAdd


T = TypeVar("T", bound="GiftAdd")


@_attrs_define
class GiftAdd:
    """Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot of information associated
    with them to ensure that they are properly allocated and acknowledged.

        Attributes:
            amount (Currency): For consistency, currency is configured at the organization level. This ensures that all
                monetary amounts are consistent, regardless of where they are entered or viewed.
            constituent_id (str): The immutable system record ID of the constituent associated with the gift.
            gift_splits (list[GiftSplitAdd]): The set of gift splits associated with the gift.
            type_ (str): The gift type. Available values are <i>Donation</i>, <i>Other</i>, <i>GiftInKind</i>,
                <i>RecurringGift</i>, and <i>RecurringGiftPayment</i>.
            payments (list[PaymentAdd]): The payment on the gift. Array length must be less than or equal to 1.
            is_manual (bool | Unset): Indicates whether the gift is a manual gift.
                If set to true, credit card and direct debit payments with transaction details will not charge. Recurring gifts
                that are manual will not have automated recurring gift payments generated.
                If no value is provided, the value will default to false.
            acknowledgements (list[AcknowledgementAdd] | Unset): The acknowledgement associated with the gift. Array length
                must be less than or equal to 1.
                If none are provided, an empty acknowledgement with a status of <i>NEEDSACKNOWLEDGEMENT</i> will be created
                alongside the gift.
            batch_number (str | Unset): Gets or sets the batch number. Character limit: 50 (including the batch prefix).
            batch_prefix (str | Unset): Gets or sets the batch prefix. This must include at least one letter. It is required
                when BatchNumber has a value and defaults to "API" if no value is provided.
            constituency (str | Unset): The constituency value of the gift. If no value is provided, the default
                constituency of the donor will be used.
            date (datetime.datetime | Unset): The gift date. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            default_fundraiser_credits (bool | Unset): Indicates whether to use default fundraiser credits.
                If no value is provided, defaults will not be used.
            default_soft_credits (bool | Unset): Indicates whether to use default soft credits.
                If no value is provided, defaults will not be used.
            fundraisers (list[GiftFundraiserAdd] | Unset): The set of fundraisers who receive credit for the gift.
            gift_code (str | Unset): The gift code. Available values are the entries in the Gift Code table.
            gift_status (str | Unset): The status of the gift. Available values are <i>Active</i>, <i>Held</i>,
                <i>Terminated</i>, <i>Completed</i>, and <i>Cancelled.</i>
            is_anonymous (bool | Unset): Indicates whether the gift is anonymous.
                If no value is provided, the default anonymity of the donor will be used.
            linked_gifts (list[str] | Unset): The recurring gift associated with the payment being added.
                When adding a recurring gift payment, a <code>linked_gifts</code> field must be included as an array of strings
                with the ID of the recurring gift to which the payment is linked. Array length must be less than or equal to 1.
            lookup_id (str | Unset): The user-defined identifier for the gift. Character limit: 50. Lookup IDs for gifts
                created from an approved batch are automatically generated based on configuration settings in the database view.
            origin (str | Unset): The origin of the gift.
                When provided, it must parse to a valid JSON object with one string field called "name". Additional fields may
                be added as desired.
            post_date (datetime.datetime | Unset): The date that the gift was posted to general ledger. Includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            post_status (str | Unset): The general ledger post status of the gift. Available values are <i>Posted</i>,
                <i>NotPosted</i>, and <i>DoNotPost.</i>
                When <code>post_status</code> is set to <i>DoNotPost</i>, <code>post_date</code> should be null.
                When it is set to <i>NotPosted</i>, <code>post_date</code> is required but remains editable.
                When it is set to <i>Posted</i>, <code>post_date</code> is required and is no longer editable.
                If no value is provided, a default value of <i>NotPosted</i> will be used.
            receipts (list[ReceiptAdd] | Unset): The receipt associated with the gift. Array length must be less than or
                equal to 1.
                If none are provided, an empty receipt with a status of <i>NEEDSRECEIPT</i> will be added alongside the gift.
            recurring_gift_schedule (RecurringGiftScheduleAdd | Unset): Defines a recurring gift schedule to add
            reference (str | Unset): Notes to track special details about a gift such as the motivation behind it or a
                detailed description of a gift-in-kind. Character limit: 255.
            soft_credits (list[SoftCreditAdd] | Unset): The set of soft credits associated with the gift.
            subtype (str | Unset): The subtype of the gift. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/58bdd5edd7dcde06046081d6/operations/ListGiftSubtypes"><b>Gift
                Subtypes</b></a> table.
            custom_fields (list[CustomFieldAdd] | Unset): The set of custom fields associated with the gift.
    """

    amount: Currency
    constituent_id: str
    gift_splits: list[GiftSplitAdd]
    type_: str
    payments: list[PaymentAdd]
    is_manual: bool | Unset = UNSET
    acknowledgements: list[AcknowledgementAdd] | Unset = UNSET
    batch_number: str | Unset = UNSET
    batch_prefix: str | Unset = UNSET
    constituency: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    default_fundraiser_credits: bool | Unset = UNSET
    default_soft_credits: bool | Unset = UNSET
    fundraisers: list[GiftFundraiserAdd] | Unset = UNSET
    gift_code: str | Unset = UNSET
    gift_status: str | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    linked_gifts: list[str] | Unset = UNSET
    lookup_id: str | Unset = UNSET
    origin: str | Unset = UNSET
    post_date: datetime.datetime | Unset = UNSET
    post_status: str | Unset = UNSET
    receipts: list[ReceiptAdd] | Unset = UNSET
    recurring_gift_schedule: RecurringGiftScheduleAdd | Unset = UNSET
    reference: str | Unset = UNSET
    soft_credits: list[SoftCreditAdd] | Unset = UNSET
    subtype: str | Unset = UNSET
    custom_fields: list[CustomFieldAdd] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount.to_dict()

        constituent_id = self.constituent_id

        gift_splits = []
        for gift_splits_item_data in self.gift_splits:
            gift_splits_item = gift_splits_item_data.to_dict()
            gift_splits.append(gift_splits_item)

        type_ = self.type_

        payments = []
        for payments_item_data in self.payments:
            payments_item = payments_item_data.to_dict()
            payments.append(payments_item)

        is_manual = self.is_manual

        acknowledgements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acknowledgements, Unset):
            acknowledgements = []
            for acknowledgements_item_data in self.acknowledgements:
                acknowledgements_item = acknowledgements_item_data.to_dict()
                acknowledgements.append(acknowledgements_item)

        batch_number = self.batch_number

        batch_prefix = self.batch_prefix

        constituency = self.constituency

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        default_fundraiser_credits = self.default_fundraiser_credits

        default_soft_credits = self.default_soft_credits

        fundraisers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fundraisers, Unset):
            fundraisers = []
            for fundraisers_item_data in self.fundraisers:
                fundraisers_item = fundraisers_item_data.to_dict()
                fundraisers.append(fundraisers_item)

        gift_code = self.gift_code

        gift_status = self.gift_status

        is_anonymous = self.is_anonymous

        linked_gifts: list[str] | Unset = UNSET
        if not isinstance(self.linked_gifts, Unset):
            linked_gifts = self.linked_gifts

        lookup_id = self.lookup_id

        origin = self.origin

        post_date: str | Unset = UNSET
        if not isinstance(self.post_date, Unset):
            post_date = self.post_date.isoformat()

        post_status = self.post_status

        receipts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.receipts, Unset):
            receipts = []
            for receipts_item_data in self.receipts:
                receipts_item = receipts_item_data.to_dict()
                receipts.append(receipts_item)

        recurring_gift_schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurring_gift_schedule, Unset):
            recurring_gift_schedule = self.recurring_gift_schedule.to_dict()

        reference = self.reference

        soft_credits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.soft_credits, Unset):
            soft_credits = []
            for soft_credits_item_data in self.soft_credits:
                soft_credits_item = soft_credits_item_data.to_dict()
                soft_credits.append(soft_credits_item)

        subtype = self.subtype

        custom_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = []
            for custom_fields_item_data in self.custom_fields:
                custom_fields_item = custom_fields_item_data.to_dict()
                custom_fields.append(custom_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "constituent_id": constituent_id,
                "gift_splits": gift_splits,
                "type": type_,
                "payments": payments,
            }
        )
        if is_manual is not UNSET:
            field_dict["is_manual"] = is_manual
        if acknowledgements is not UNSET:
            field_dict["acknowledgements"] = acknowledgements
        if batch_number is not UNSET:
            field_dict["batch_number"] = batch_number
        if batch_prefix is not UNSET:
            field_dict["batch_prefix"] = batch_prefix
        if constituency is not UNSET:
            field_dict["constituency"] = constituency
        if date is not UNSET:
            field_dict["date"] = date
        if default_fundraiser_credits is not UNSET:
            field_dict["default_fundraiser_credits"] = default_fundraiser_credits
        if default_soft_credits is not UNSET:
            field_dict["default_soft_credits"] = default_soft_credits
        if fundraisers is not UNSET:
            field_dict["fundraisers"] = fundraisers
        if gift_code is not UNSET:
            field_dict["gift_code"] = gift_code
        if gift_status is not UNSET:
            field_dict["gift_status"] = gift_status
        if is_anonymous is not UNSET:
            field_dict["is_anonymous"] = is_anonymous
        if linked_gifts is not UNSET:
            field_dict["linked_gifts"] = linked_gifts
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if origin is not UNSET:
            field_dict["origin"] = origin
        if post_date is not UNSET:
            field_dict["post_date"] = post_date
        if post_status is not UNSET:
            field_dict["post_status"] = post_status
        if receipts is not UNSET:
            field_dict["receipts"] = receipts
        if recurring_gift_schedule is not UNSET:
            field_dict["recurring_gift_schedule"] = recurring_gift_schedule
        if reference is not UNSET:
            field_dict["reference"] = reference
        if soft_credits is not UNSET:
            field_dict["soft_credits"] = soft_credits
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acknowledgement_add import AcknowledgementAdd
        from ..models.currency import Currency
        from ..models.custom_field_add import CustomFieldAdd
        from ..models.gift_fundraiser_add import GiftFundraiserAdd
        from ..models.gift_split_add import GiftSplitAdd
        from ..models.payment_add import PaymentAdd
        from ..models.receipt_add import ReceiptAdd
        from ..models.recurring_gift_schedule_add import RecurringGiftScheduleAdd
        from ..models.soft_credit_add import SoftCreditAdd

        d = dict(src_dict)
        amount = Currency.from_dict(d.pop("amount"))

        constituent_id = d.pop("constituent_id")

        gift_splits = []
        _gift_splits = d.pop("gift_splits")
        for gift_splits_item_data in _gift_splits:
            gift_splits_item = GiftSplitAdd.from_dict(gift_splits_item_data)

            gift_splits.append(gift_splits_item)

        type_ = d.pop("type")

        payments = []
        _payments = d.pop("payments")
        for payments_item_data in _payments:
            payments_item = PaymentAdd.from_dict(payments_item_data)

            payments.append(payments_item)

        is_manual = d.pop("is_manual", UNSET)

        _acknowledgements = d.pop("acknowledgements", UNSET)
        acknowledgements: list[AcknowledgementAdd] | Unset = UNSET
        if _acknowledgements is not UNSET:
            acknowledgements = []
            for acknowledgements_item_data in _acknowledgements:
                acknowledgements_item = AcknowledgementAdd.from_dict(acknowledgements_item_data)

                acknowledgements.append(acknowledgements_item)

        batch_number = d.pop("batch_number", UNSET)

        batch_prefix = d.pop("batch_prefix", UNSET)

        constituency = d.pop("constituency", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        default_fundraiser_credits = d.pop("default_fundraiser_credits", UNSET)

        default_soft_credits = d.pop("default_soft_credits", UNSET)

        _fundraisers = d.pop("fundraisers", UNSET)
        fundraisers: list[GiftFundraiserAdd] | Unset = UNSET
        if _fundraisers is not UNSET:
            fundraisers = []
            for fundraisers_item_data in _fundraisers:
                fundraisers_item = GiftFundraiserAdd.from_dict(fundraisers_item_data)

                fundraisers.append(fundraisers_item)

        gift_code = d.pop("gift_code", UNSET)

        gift_status = d.pop("gift_status", UNSET)

        is_anonymous = d.pop("is_anonymous", UNSET)

        linked_gifts = cast(list[str], d.pop("linked_gifts", UNSET))

        lookup_id = d.pop("lookup_id", UNSET)

        origin = d.pop("origin", UNSET)

        _post_date = d.pop("post_date", UNSET)
        post_date: datetime.datetime | Unset
        if isinstance(_post_date, Unset):
            post_date = UNSET
        else:
            post_date = isoparse(_post_date)

        post_status = d.pop("post_status", UNSET)

        _receipts = d.pop("receipts", UNSET)
        receipts: list[ReceiptAdd] | Unset = UNSET
        if _receipts is not UNSET:
            receipts = []
            for receipts_item_data in _receipts:
                receipts_item = ReceiptAdd.from_dict(receipts_item_data)

                receipts.append(receipts_item)

        _recurring_gift_schedule = d.pop("recurring_gift_schedule", UNSET)
        recurring_gift_schedule: RecurringGiftScheduleAdd | Unset
        if isinstance(_recurring_gift_schedule, Unset):
            recurring_gift_schedule = UNSET
        else:
            recurring_gift_schedule = RecurringGiftScheduleAdd.from_dict(_recurring_gift_schedule)

        reference = d.pop("reference", UNSET)

        _soft_credits = d.pop("soft_credits", UNSET)
        soft_credits: list[SoftCreditAdd] | Unset = UNSET
        if _soft_credits is not UNSET:
            soft_credits = []
            for soft_credits_item_data in _soft_credits:
                soft_credits_item = SoftCreditAdd.from_dict(soft_credits_item_data)

                soft_credits.append(soft_credits_item)

        subtype = d.pop("subtype", UNSET)

        _custom_fields = d.pop("custom_fields", UNSET)
        custom_fields: list[CustomFieldAdd] | Unset = UNSET
        if _custom_fields is not UNSET:
            custom_fields = []
            for custom_fields_item_data in _custom_fields:
                custom_fields_item = CustomFieldAdd.from_dict(custom_fields_item_data)

                custom_fields.append(custom_fields_item)

        gift_add = cls(
            amount=amount,
            constituent_id=constituent_id,
            gift_splits=gift_splits,
            type_=type_,
            payments=payments,
            is_manual=is_manual,
            acknowledgements=acknowledgements,
            batch_number=batch_number,
            batch_prefix=batch_prefix,
            constituency=constituency,
            date=date,
            default_fundraiser_credits=default_fundraiser_credits,
            default_soft_credits=default_soft_credits,
            fundraisers=fundraisers,
            gift_code=gift_code,
            gift_status=gift_status,
            is_anonymous=is_anonymous,
            linked_gifts=linked_gifts,
            lookup_id=lookup_id,
            origin=origin,
            post_date=post_date,
            post_status=post_status,
            receipts=receipts,
            recurring_gift_schedule=recurring_gift_schedule,
            reference=reference,
            soft_credits=soft_credits,
            subtype=subtype,
            custom_fields=custom_fields,
        )

        gift_add.additional_properties = d
        return gift_add

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

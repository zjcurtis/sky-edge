from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledgement_read import AcknowledgementRead
    from ..models.currency import Currency
    from ..models.fuzzy_date import FuzzyDate
    from ..models.gift_batch_gift_error import GiftBatchGiftError
    from ..models.gift_fundraiser_read import GiftFundraiserRead
    from ..models.gift_split_read import GiftSplitRead
    from ..models.payment_read import PaymentRead
    from ..models.receipt_read import ReceiptRead
    from ..models.recurring_gift_schedule_read import RecurringGiftScheduleRead
    from ..models.soft_credit_read import SoftCreditRead
    from ..models.tribute_read import TributeRead


T = TypeVar("T", bound="BatchGiftRead")


@_attrs_define
class BatchGiftRead:
    """Gifts are the primary goal of fundraising efforts. They come in many forms and have a lot of information associated
    with them to ensure that they are properly allocated and acknowledged.

        Attributes:
            batch_id (str | Unset): The ID of the batch to which the gift was added.
            approved_gift_id (str | Unset): The ID of the gift to which the batch gift was approved.
            tributes (list[TributeRead] | Unset): The collection of tributes added to the batch gift.
            errors (list[GiftBatchGiftError] | Unset): The errors associated with the batch gift.
            id (str | Unset): The immutable system record ID of the gift.
            acknowledgements (list[AcknowledgementRead] | Unset): The set of acknowledgements associated with the gift.
            amount (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            balance (Currency | Unset): For consistency, currency is configured at the organization level. This ensures that
                all monetary amounts are consistent, regardless of where they are entered or viewed.
            batch_number (str | Unset): The batch number associated with this gift.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the gift.
            date (datetime.datetime | Unset): The gift date. Uses <a href="https://tools.ietf.org/html/rfc3339">ISO-8601
                format: </a><i>1969-11-21T10:29:43</i>.
            date_added (datetime.datetime | Unset): The date when the gift was created. Includes an offset from UTC in <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the gift was last modified. Includes an offset from UTC
                in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            fundraisers (list[GiftFundraiserRead] | Unset): The set of fundraisers who receive credit for the gift.
            gift_aid_amount (Currency | Unset): For consistency, currency is configured at the organization level. This
                ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            gift_aid_qualification_status (str | Unset): This computed field determines the Gift Aid qualification status
                based on tax declaration information and the database format. Available values are: <i>Qualified</i>,
                <i>NotQualified</i>, and <i>PartlyQualified</i>. For the UK only.
            gift_code (str | Unset): The gift code value associated with the gift.
            gift_splits (list[GiftSplitRead] | Unset): The set of gift splits associated with the gift.
            gift_status (str | Unset): The status of the gift. Available values are <i>Active</i>, <i>Held</i>,
                <i>Terminated</i>, <i>Completed</i>, and <i>Cancelled.</i>
            is_anonymous (bool | Unset): Indicates whether the gift is anonymous.
            linked_gifts (list[str] | Unset): The identifiers of other gifts that are linked to this gift.
            constituency (str | Unset): The constituency of the gift.
            lookup_id (str | Unset): The user-defined identifier for the gift.
            origin (str | Unset): The origin of the gift.
            payments (list[PaymentRead] | Unset): The payments on the gift.
            post_date (datetime.datetime | Unset): The date that the gift was posted to general ledger. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            post_status (str | Unset): The general ledger post status of the gift. Available values are <i>Posted</i>,
                <i>NotPosted</i>, and <i>DoNotPost.</i> When <code>post_status</code> is set to <i>DoNotPost</i>,
                <code>post_date</code> should be null. When it is set to <i>NotPosted</i>, <code>post_date</code> is required
                but remains editable. When it is set to <i>Posted</i>, <code>post_date</code> is required and is no longer
                editable.
            receipts (list[ReceiptRead] | Unset): The set of receipts associated with the gift.
            recurring_gift_schedule (RecurringGiftScheduleRead | Unset): Defines a recurring gift schedule to view.
            recurring_gift_status_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial
                dates such as February 9 (with no year indicated).
            reference (str | Unset): Notes to track special details about a gift such as the motivation behind it or a
                detailed description of a gift-in-kind.
            soft_credits (list[SoftCreditRead] | Unset): The set of soft credits associated with the gift.
            subtype (str | Unset): The subtype of the gift. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/58bdd5edd7dcde06046081d6/operations/ListGiftSubtypes"><b>Gift
                Subtypes</b></a> table.
            type_ (str | Unset): The gift type. Available values are <i>Donation</i>, <i>GiftInKind</i>, <i>Pledge</i>,
                <i>PledgePayment</i>, <i>RecurringGift</i>, <i>RecurringGiftPayment</i>,
                <i>Stock</i>, <i>SoldStock</i>, <i>Other</i>, <i>PlannedGift</i>, <i>MatchingGiftPledge</i>,
                <i>MatchingGiftPayment</i>
    """

    batch_id: str | Unset = UNSET
    approved_gift_id: str | Unset = UNSET
    tributes: list[TributeRead] | Unset = UNSET
    errors: list[GiftBatchGiftError] | Unset = UNSET
    id: str | Unset = UNSET
    acknowledgements: list[AcknowledgementRead] | Unset = UNSET
    amount: Currency | Unset = UNSET
    balance: Currency | Unset = UNSET
    batch_number: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    fundraisers: list[GiftFundraiserRead] | Unset = UNSET
    gift_aid_amount: Currency | Unset = UNSET
    gift_aid_qualification_status: str | Unset = UNSET
    gift_code: str | Unset = UNSET
    gift_splits: list[GiftSplitRead] | Unset = UNSET
    gift_status: str | Unset = UNSET
    is_anonymous: bool | Unset = UNSET
    linked_gifts: list[str] | Unset = UNSET
    constituency: str | Unset = UNSET
    lookup_id: str | Unset = UNSET
    origin: str | Unset = UNSET
    payments: list[PaymentRead] | Unset = UNSET
    post_date: datetime.datetime | Unset = UNSET
    post_status: str | Unset = UNSET
    receipts: list[ReceiptRead] | Unset = UNSET
    recurring_gift_schedule: RecurringGiftScheduleRead | Unset = UNSET
    recurring_gift_status_date: FuzzyDate | Unset = UNSET
    reference: str | Unset = UNSET
    soft_credits: list[SoftCreditRead] | Unset = UNSET
    subtype: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        batch_id = self.batch_id

        approved_gift_id = self.approved_gift_id

        tributes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tributes, Unset):
            tributes = []
            for tributes_item_data in self.tributes:
                tributes_item = tributes_item_data.to_dict()
                tributes.append(tributes_item)

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        id = self.id

        acknowledgements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acknowledgements, Unset):
            acknowledgements = []
            for acknowledgements_item_data in self.acknowledgements:
                acknowledgements_item = acknowledgements_item_data.to_dict()
                acknowledgements.append(acknowledgements_item)

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        balance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.balance, Unset):
            balance = self.balance.to_dict()

        batch_number = self.batch_number

        constituent_id = self.constituent_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        fundraisers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fundraisers, Unset):
            fundraisers = []
            for fundraisers_item_data in self.fundraisers:
                fundraisers_item = fundraisers_item_data.to_dict()
                fundraisers.append(fundraisers_item)

        gift_aid_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_aid_amount, Unset):
            gift_aid_amount = self.gift_aid_amount.to_dict()

        gift_aid_qualification_status = self.gift_aid_qualification_status

        gift_code = self.gift_code

        gift_splits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gift_splits, Unset):
            gift_splits = []
            for gift_splits_item_data in self.gift_splits:
                gift_splits_item = gift_splits_item_data.to_dict()
                gift_splits.append(gift_splits_item)

        gift_status = self.gift_status

        is_anonymous = self.is_anonymous

        linked_gifts: list[str] | Unset = UNSET
        if not isinstance(self.linked_gifts, Unset):
            linked_gifts = self.linked_gifts

        constituency = self.constituency

        lookup_id = self.lookup_id

        origin = self.origin

        payments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)

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

        recurring_gift_status_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.recurring_gift_status_date, Unset):
            recurring_gift_status_date = self.recurring_gift_status_date.to_dict()

        reference = self.reference

        soft_credits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.soft_credits, Unset):
            soft_credits = []
            for soft_credits_item_data in self.soft_credits:
                soft_credits_item = soft_credits_item_data.to_dict()
                soft_credits.append(soft_credits_item)

        subtype = self.subtype

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if approved_gift_id is not UNSET:
            field_dict["approved_gift_id"] = approved_gift_id
        if tributes is not UNSET:
            field_dict["tributes"] = tributes
        if errors is not UNSET:
            field_dict["errors"] = errors
        if id is not UNSET:
            field_dict["id"] = id
        if acknowledgements is not UNSET:
            field_dict["acknowledgements"] = acknowledgements
        if amount is not UNSET:
            field_dict["amount"] = amount
        if balance is not UNSET:
            field_dict["balance"] = balance
        if batch_number is not UNSET:
            field_dict["batch_number"] = batch_number
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date is not UNSET:
            field_dict["date"] = date
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if fundraisers is not UNSET:
            field_dict["fundraisers"] = fundraisers
        if gift_aid_amount is not UNSET:
            field_dict["gift_aid_amount"] = gift_aid_amount
        if gift_aid_qualification_status is not UNSET:
            field_dict["gift_aid_qualification_status"] = gift_aid_qualification_status
        if gift_code is not UNSET:
            field_dict["gift_code"] = gift_code
        if gift_splits is not UNSET:
            field_dict["gift_splits"] = gift_splits
        if gift_status is not UNSET:
            field_dict["gift_status"] = gift_status
        if is_anonymous is not UNSET:
            field_dict["is_anonymous"] = is_anonymous
        if linked_gifts is not UNSET:
            field_dict["linked_gifts"] = linked_gifts
        if constituency is not UNSET:
            field_dict["constituency"] = constituency
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if origin is not UNSET:
            field_dict["origin"] = origin
        if payments is not UNSET:
            field_dict["payments"] = payments
        if post_date is not UNSET:
            field_dict["post_date"] = post_date
        if post_status is not UNSET:
            field_dict["post_status"] = post_status
        if receipts is not UNSET:
            field_dict["receipts"] = receipts
        if recurring_gift_schedule is not UNSET:
            field_dict["recurring_gift_schedule"] = recurring_gift_schedule
        if recurring_gift_status_date is not UNSET:
            field_dict["recurring_gift_status_date"] = recurring_gift_status_date
        if reference is not UNSET:
            field_dict["reference"] = reference
        if soft_credits is not UNSET:
            field_dict["soft_credits"] = soft_credits
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acknowledgement_read import AcknowledgementRead
        from ..models.currency import Currency
        from ..models.fuzzy_date import FuzzyDate
        from ..models.gift_batch_gift_error import GiftBatchGiftError
        from ..models.gift_fundraiser_read import GiftFundraiserRead
        from ..models.gift_split_read import GiftSplitRead
        from ..models.payment_read import PaymentRead
        from ..models.receipt_read import ReceiptRead
        from ..models.recurring_gift_schedule_read import RecurringGiftScheduleRead
        from ..models.soft_credit_read import SoftCreditRead
        from ..models.tribute_read import TributeRead

        d = dict(src_dict)
        batch_id = d.pop("batch_id", UNSET)

        approved_gift_id = d.pop("approved_gift_id", UNSET)

        _tributes = d.pop("tributes", UNSET)
        tributes: list[TributeRead] | Unset = UNSET
        if _tributes is not UNSET:
            tributes = []
            for tributes_item_data in _tributes:
                tributes_item = TributeRead.from_dict(tributes_item_data)

                tributes.append(tributes_item)

        _errors = d.pop("errors", UNSET)
        errors: list[GiftBatchGiftError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = GiftBatchGiftError.from_dict(errors_item_data)

                errors.append(errors_item)

        id = d.pop("id", UNSET)

        _acknowledgements = d.pop("acknowledgements", UNSET)
        acknowledgements: list[AcknowledgementRead] | Unset = UNSET
        if _acknowledgements is not UNSET:
            acknowledgements = []
            for acknowledgements_item_data in _acknowledgements:
                acknowledgements_item = AcknowledgementRead.from_dict(acknowledgements_item_data)

                acknowledgements.append(acknowledgements_item)

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        _balance = d.pop("balance", UNSET)
        balance: Currency | Unset
        if isinstance(_balance, Unset):
            balance = UNSET
        else:
            balance = Currency.from_dict(_balance)

        batch_number = d.pop("batch_number", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        _fundraisers = d.pop("fundraisers", UNSET)
        fundraisers: list[GiftFundraiserRead] | Unset = UNSET
        if _fundraisers is not UNSET:
            fundraisers = []
            for fundraisers_item_data in _fundraisers:
                fundraisers_item = GiftFundraiserRead.from_dict(fundraisers_item_data)

                fundraisers.append(fundraisers_item)

        _gift_aid_amount = d.pop("gift_aid_amount", UNSET)
        gift_aid_amount: Currency | Unset
        if isinstance(_gift_aid_amount, Unset):
            gift_aid_amount = UNSET
        else:
            gift_aid_amount = Currency.from_dict(_gift_aid_amount)

        gift_aid_qualification_status = d.pop("gift_aid_qualification_status", UNSET)

        gift_code = d.pop("gift_code", UNSET)

        _gift_splits = d.pop("gift_splits", UNSET)
        gift_splits: list[GiftSplitRead] | Unset = UNSET
        if _gift_splits is not UNSET:
            gift_splits = []
            for gift_splits_item_data in _gift_splits:
                gift_splits_item = GiftSplitRead.from_dict(gift_splits_item_data)

                gift_splits.append(gift_splits_item)

        gift_status = d.pop("gift_status", UNSET)

        is_anonymous = d.pop("is_anonymous", UNSET)

        linked_gifts = cast(list[str], d.pop("linked_gifts", UNSET))

        constituency = d.pop("constituency", UNSET)

        lookup_id = d.pop("lookup_id", UNSET)

        origin = d.pop("origin", UNSET)

        _payments = d.pop("payments", UNSET)
        payments: list[PaymentRead] | Unset = UNSET
        if _payments is not UNSET:
            payments = []
            for payments_item_data in _payments:
                payments_item = PaymentRead.from_dict(payments_item_data)

                payments.append(payments_item)

        _post_date = d.pop("post_date", UNSET)
        post_date: datetime.datetime | Unset
        if isinstance(_post_date, Unset):
            post_date = UNSET
        else:
            post_date = isoparse(_post_date)

        post_status = d.pop("post_status", UNSET)

        _receipts = d.pop("receipts", UNSET)
        receipts: list[ReceiptRead] | Unset = UNSET
        if _receipts is not UNSET:
            receipts = []
            for receipts_item_data in _receipts:
                receipts_item = ReceiptRead.from_dict(receipts_item_data)

                receipts.append(receipts_item)

        _recurring_gift_schedule = d.pop("recurring_gift_schedule", UNSET)
        recurring_gift_schedule: RecurringGiftScheduleRead | Unset
        if isinstance(_recurring_gift_schedule, Unset):
            recurring_gift_schedule = UNSET
        else:
            recurring_gift_schedule = RecurringGiftScheduleRead.from_dict(_recurring_gift_schedule)

        _recurring_gift_status_date = d.pop("recurring_gift_status_date", UNSET)
        recurring_gift_status_date: FuzzyDate | Unset
        if isinstance(_recurring_gift_status_date, Unset):
            recurring_gift_status_date = UNSET
        else:
            recurring_gift_status_date = FuzzyDate.from_dict(_recurring_gift_status_date)

        reference = d.pop("reference", UNSET)

        _soft_credits = d.pop("soft_credits", UNSET)
        soft_credits: list[SoftCreditRead] | Unset = UNSET
        if _soft_credits is not UNSET:
            soft_credits = []
            for soft_credits_item_data in _soft_credits:
                soft_credits_item = SoftCreditRead.from_dict(soft_credits_item_data)

                soft_credits.append(soft_credits_item)

        subtype = d.pop("subtype", UNSET)

        type_ = d.pop("type", UNSET)

        batch_gift_read = cls(
            batch_id=batch_id,
            approved_gift_id=approved_gift_id,
            tributes=tributes,
            errors=errors,
            id=id,
            acknowledgements=acknowledgements,
            amount=amount,
            balance=balance,
            batch_number=batch_number,
            constituent_id=constituent_id,
            date=date,
            date_added=date_added,
            date_modified=date_modified,
            fundraisers=fundraisers,
            gift_aid_amount=gift_aid_amount,
            gift_aid_qualification_status=gift_aid_qualification_status,
            gift_code=gift_code,
            gift_splits=gift_splits,
            gift_status=gift_status,
            is_anonymous=is_anonymous,
            linked_gifts=linked_gifts,
            constituency=constituency,
            lookup_id=lookup_id,
            origin=origin,
            payments=payments,
            post_date=post_date,
            post_status=post_status,
            receipts=receipts,
            recurring_gift_schedule=recurring_gift_schedule,
            recurring_gift_status_date=recurring_gift_status_date,
            reference=reference,
            soft_credits=soft_credits,
            subtype=subtype,
            type_=type_,
        )

        batch_gift_read.additional_properties = d
        return batch_gift_read

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

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.batch_gift_add_with_tribute_lookup_gift_post_status import (
    BatchGiftAddWithTributeLookupGiftPostStatus,
)
from ..models.batch_gift_add_with_tribute_lookup_gift_status import (
    BatchGiftAddWithTributeLookupGiftStatus,
)
from ..models.batch_gift_add_with_tribute_lookup_gift_type import (
    BatchGiftAddWithTributeLookupGiftType,
)

if TYPE_CHECKING:
    from ..models.apply_payment import ApplyPayment
    from ..models.code_table_entry import CodeTableEntry
    from ..models.currency import Currency
    from ..models.fundraiser_credit import FundraiserCredit
    from ..models.fuzzy_date import FuzzyDate
    from ..models.gift_acknowledgement import GiftAcknowledgement
    from ..models.gift_constituent import GiftConstituent
    from ..models.gift_custom_field_add import GiftCustomFieldAdd
    from ..models.gift_payment_record import GiftPaymentRecord
    from ..models.gift_receipt import GiftReceipt
    from ..models.gift_split import GiftSplit
    from ..models.gift_subtype import GiftSubtype
    from ..models.issuer_details import IssuerDetails
    from ..models.pledge_installment_add import PledgeInstallmentAdd
    from ..models.schedule import Schedule
    from ..models.soft_credit import SoftCredit
    from ..models.tribute_lookup import TributeLookup


T = TypeVar("T", bound="BatchGiftAddWithTributeLookup")


@_attrs_define
class BatchGiftAddWithTributeLookup:
    """Represents a batch gift to be added, with lookup for tribute

    Attributes:
        amount (Currency): An amount denominated in a specific currency.
        gift_type (BatchGiftAddWithTributeLookupGiftType): The gift type.
        constituent (GiftConstituent): The constituent who makes a gift.
        batch_id (None | str | Unset): ID of the batch to which this gift should be added.
        tributes (list[TributeLookup] | None | Unset): A collection of tribute lookups.
        gift_splits (list[GiftSplit] | None | Unset): The gift's splits.
        apply_payments (list[ApplyPayment] | None | Unset): Applies partial payments to multiple pledges.
        charge_first_payment (bool | None | Unset): True if a recurring gift payment should be charged immediately. Only
            applicable for recurring gifts.
        parent_gift_id (None | str | Unset): The linked parent gift ID for a recurring gift payment.
        custom_fields (list[GiftCustomFieldAdd] | None | Unset): Gets or sets the custom fields.
        processes_manually (bool | None | Unset): Gets or sets the is manual flag for recurring gifts.
        pledge_installments (list[PledgeInstallmentAdd] | None | Unset): Pledge installments
        gift_date (datetime.datetime | None | Unset): The date the gift was given.
        lookup_id (None | str | Unset): The gift's lookup ID. Example: Lookup-12345.
        comments (None | str | Unset): Comments associated with the gift. Character limit: 255. Example: This is a
            comment.
        gift_post_status (BatchGiftAddWithTributeLookupGiftPostStatus | Unset): The post status of the gift. Example:
            NotPosted.
        gift_post_date (datetime.datetime | None | Unset): The post date of the gift. Must be set if post status is
            NotPosted or Posted. Must be null if post status is DoNotPost.
        issuer_details (IssuerDetails | Unset): Represents issuer detils for a stock gift
        origin (None | str | Unset): The gift's origin.
        payments (list[GiftPaymentRecord] | None | Unset): The gift's payments. Required for Recurring Gift type.
        schedule (Schedule | Unset): A gift schedule.
        adjustment_notes (None | str | Unset): The gift's adjustment notes. Used by the Adjustment Gift type. Example:
            Refunded gift.
        receipts (list[GiftReceipt] | None | Unset): The gift's receipts.
        fundraiser_credits (list[FundraiserCredit] | None | Unset): The gift's fundraiser credits.
        soft_credits (list[SoftCredit] | None | Unset): The gift's soft credits.
        send_reminder (bool | None | Unset): Gets or sets the send reminder flag for pledge gifts. If no value is
            provided, it will default to true for pledges, false otherwise.
        acknowledgements (list[GiftAcknowledgement] | None | Unset): The gift's acknowledgements.
        gift_subtype (GiftSubtype | Unset): Model representing a gift subtype.
        anonymous (bool | None | Unset): Notes whether the gift should remain anonymous or not, i.e. do not publicly
            show the donor's name.
        gift_code (CodeTableEntry | Unset): A predefined entry in a code table.
        gift_status (BatchGiftAddWithTributeLookupGiftStatus | Unset): The status of a gift. Example: Active.
        gift_status_date (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        gift_constituency (CodeTableEntry | Unset): A predefined entry in a code table.
    """

    amount: Currency
    gift_type: BatchGiftAddWithTributeLookupGiftType
    constituent: GiftConstituent
    batch_id: None | str | Unset = UNSET
    tributes: list[TributeLookup] | None | Unset = UNSET
    gift_splits: list[GiftSplit] | None | Unset = UNSET
    apply_payments: list[ApplyPayment] | None | Unset = UNSET
    charge_first_payment: bool | None | Unset = UNSET
    parent_gift_id: None | str | Unset = UNSET
    custom_fields: list[GiftCustomFieldAdd] | None | Unset = UNSET
    processes_manually: bool | None | Unset = UNSET
    pledge_installments: list[PledgeInstallmentAdd] | None | Unset = UNSET
    gift_date: datetime.datetime | None | Unset = UNSET
    lookup_id: None | str | Unset = UNSET
    comments: None | str | Unset = UNSET
    gift_post_status: BatchGiftAddWithTributeLookupGiftPostStatus | Unset = UNSET
    gift_post_date: datetime.datetime | None | Unset = UNSET
    issuer_details: IssuerDetails | Unset = UNSET
    origin: None | str | Unset = UNSET
    payments: list[GiftPaymentRecord] | None | Unset = UNSET
    schedule: Schedule | Unset = UNSET
    adjustment_notes: None | str | Unset = UNSET
    receipts: list[GiftReceipt] | None | Unset = UNSET
    fundraiser_credits: list[FundraiserCredit] | None | Unset = UNSET
    soft_credits: list[SoftCredit] | None | Unset = UNSET
    send_reminder: bool | None | Unset = UNSET
    acknowledgements: list[GiftAcknowledgement] | None | Unset = UNSET
    gift_subtype: GiftSubtype | Unset = UNSET
    anonymous: bool | None | Unset = UNSET
    gift_code: CodeTableEntry | Unset = UNSET
    gift_status: BatchGiftAddWithTributeLookupGiftStatus | Unset = UNSET
    gift_status_date: FuzzyDate | Unset = UNSET
    gift_constituency: CodeTableEntry | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount.to_dict()

        gift_type = self.gift_type.value

        constituent = self.constituent.to_dict()

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        tributes: list[dict[str, Any]] | None | Unset
        if isinstance(self.tributes, Unset):
            tributes = UNSET
        elif isinstance(self.tributes, list):
            tributes = []
            for tributes_type_0_item_data in self.tributes:
                tributes_type_0_item = tributes_type_0_item_data.to_dict()
                tributes.append(tributes_type_0_item)

        else:
            tributes = self.tributes

        gift_splits: list[dict[str, Any]] | None | Unset
        if isinstance(self.gift_splits, Unset):
            gift_splits = UNSET
        elif isinstance(self.gift_splits, list):
            gift_splits = []
            for gift_splits_type_0_item_data in self.gift_splits:
                gift_splits_type_0_item = gift_splits_type_0_item_data.to_dict()
                gift_splits.append(gift_splits_type_0_item)

        else:
            gift_splits = self.gift_splits

        apply_payments: list[dict[str, Any]] | None | Unset
        if isinstance(self.apply_payments, Unset):
            apply_payments = UNSET
        elif isinstance(self.apply_payments, list):
            apply_payments = []
            for apply_payments_type_0_item_data in self.apply_payments:
                apply_payments_type_0_item = apply_payments_type_0_item_data.to_dict()
                apply_payments.append(apply_payments_type_0_item)

        else:
            apply_payments = self.apply_payments

        charge_first_payment: bool | None | Unset
        if isinstance(self.charge_first_payment, Unset):
            charge_first_payment = UNSET
        else:
            charge_first_payment = self.charge_first_payment

        parent_gift_id: None | str | Unset
        if isinstance(self.parent_gift_id, Unset):
            parent_gift_id = UNSET
        else:
            parent_gift_id = self.parent_gift_id

        custom_fields: list[dict[str, Any]] | None | Unset
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, list):
            custom_fields = []
            for custom_fields_type_0_item_data in self.custom_fields:
                custom_fields_type_0_item = custom_fields_type_0_item_data.to_dict()
                custom_fields.append(custom_fields_type_0_item)

        else:
            custom_fields = self.custom_fields

        processes_manually: bool | None | Unset
        if isinstance(self.processes_manually, Unset):
            processes_manually = UNSET
        else:
            processes_manually = self.processes_manually

        pledge_installments: list[dict[str, Any]] | None | Unset
        if isinstance(self.pledge_installments, Unset):
            pledge_installments = UNSET
        elif isinstance(self.pledge_installments, list):
            pledge_installments = []
            for pledge_installments_type_0_item_data in self.pledge_installments:
                pledge_installments_type_0_item = (
                    pledge_installments_type_0_item_data.to_dict()
                )
                pledge_installments.append(pledge_installments_type_0_item)

        else:
            pledge_installments = self.pledge_installments

        gift_date: None | str | Unset
        if isinstance(self.gift_date, Unset):
            gift_date = UNSET
        elif isinstance(self.gift_date, datetime.datetime):
            gift_date = self.gift_date.isoformat()
        else:
            gift_date = self.gift_date

        lookup_id: None | str | Unset
        if isinstance(self.lookup_id, Unset):
            lookup_id = UNSET
        else:
            lookup_id = self.lookup_id

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        gift_post_status: str | Unset = UNSET
        if not isinstance(self.gift_post_status, Unset):
            gift_post_status = self.gift_post_status.value

        gift_post_date: None | str | Unset
        if isinstance(self.gift_post_date, Unset):
            gift_post_date = UNSET
        elif isinstance(self.gift_post_date, datetime.datetime):
            gift_post_date = self.gift_post_date.isoformat()
        else:
            gift_post_date = self.gift_post_date

        issuer_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issuer_details, Unset):
            issuer_details = self.issuer_details.to_dict()

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        payments: list[dict[str, Any]] | None | Unset
        if isinstance(self.payments, Unset):
            payments = UNSET
        elif isinstance(self.payments, list):
            payments = []
            for payments_type_0_item_data in self.payments:
                payments_type_0_item = payments_type_0_item_data.to_dict()
                payments.append(payments_type_0_item)

        else:
            payments = self.payments

        schedule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        adjustment_notes: None | str | Unset
        if isinstance(self.adjustment_notes, Unset):
            adjustment_notes = UNSET
        else:
            adjustment_notes = self.adjustment_notes

        receipts: list[dict[str, Any]] | None | Unset
        if isinstance(self.receipts, Unset):
            receipts = UNSET
        elif isinstance(self.receipts, list):
            receipts = []
            for receipts_type_0_item_data in self.receipts:
                receipts_type_0_item = receipts_type_0_item_data.to_dict()
                receipts.append(receipts_type_0_item)

        else:
            receipts = self.receipts

        fundraiser_credits: list[dict[str, Any]] | None | Unset
        if isinstance(self.fundraiser_credits, Unset):
            fundraiser_credits = UNSET
        elif isinstance(self.fundraiser_credits, list):
            fundraiser_credits = []
            for fundraiser_credits_type_0_item_data in self.fundraiser_credits:
                fundraiser_credits_type_0_item = (
                    fundraiser_credits_type_0_item_data.to_dict()
                )
                fundraiser_credits.append(fundraiser_credits_type_0_item)

        else:
            fundraiser_credits = self.fundraiser_credits

        soft_credits: list[dict[str, Any]] | None | Unset
        if isinstance(self.soft_credits, Unset):
            soft_credits = UNSET
        elif isinstance(self.soft_credits, list):
            soft_credits = []
            for soft_credits_type_0_item_data in self.soft_credits:
                soft_credits_type_0_item = soft_credits_type_0_item_data.to_dict()
                soft_credits.append(soft_credits_type_0_item)

        else:
            soft_credits = self.soft_credits

        send_reminder: bool | None | Unset
        if isinstance(self.send_reminder, Unset):
            send_reminder = UNSET
        else:
            send_reminder = self.send_reminder

        acknowledgements: list[dict[str, Any]] | None | Unset
        if isinstance(self.acknowledgements, Unset):
            acknowledgements = UNSET
        elif isinstance(self.acknowledgements, list):
            acknowledgements = []
            for acknowledgements_type_0_item_data in self.acknowledgements:
                acknowledgements_type_0_item = (
                    acknowledgements_type_0_item_data.to_dict()
                )
                acknowledgements.append(acknowledgements_type_0_item)

        else:
            acknowledgements = self.acknowledgements

        gift_subtype: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_subtype, Unset):
            gift_subtype = self.gift_subtype.to_dict()

        anonymous: bool | None | Unset
        if isinstance(self.anonymous, Unset):
            anonymous = UNSET
        else:
            anonymous = self.anonymous

        gift_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_code, Unset):
            gift_code = self.gift_code.to_dict()

        gift_status: str | Unset = UNSET
        if not isinstance(self.gift_status, Unset):
            gift_status = self.gift_status.value

        gift_status_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_status_date, Unset):
            gift_status_date = self.gift_status_date.to_dict()

        gift_constituency: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gift_constituency, Unset):
            gift_constituency = self.gift_constituency.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "gift_type": gift_type,
                "constituent": constituent,
            }
        )
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if tributes is not UNSET:
            field_dict["tributes"] = tributes
        if gift_splits is not UNSET:
            field_dict["gift_splits"] = gift_splits
        if apply_payments is not UNSET:
            field_dict["apply_payments"] = apply_payments
        if charge_first_payment is not UNSET:
            field_dict["charge_first_payment"] = charge_first_payment
        if parent_gift_id is not UNSET:
            field_dict["parent_gift_id"] = parent_gift_id
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if processes_manually is not UNSET:
            field_dict["processes_manually"] = processes_manually
        if pledge_installments is not UNSET:
            field_dict["pledge_installments"] = pledge_installments
        if gift_date is not UNSET:
            field_dict["gift_date"] = gift_date
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if comments is not UNSET:
            field_dict["comments"] = comments
        if gift_post_status is not UNSET:
            field_dict["gift_post_status"] = gift_post_status
        if gift_post_date is not UNSET:
            field_dict["gift_post_date"] = gift_post_date
        if issuer_details is not UNSET:
            field_dict["issuer_details"] = issuer_details
        if origin is not UNSET:
            field_dict["origin"] = origin
        if payments is not UNSET:
            field_dict["payments"] = payments
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if adjustment_notes is not UNSET:
            field_dict["adjustment_notes"] = adjustment_notes
        if receipts is not UNSET:
            field_dict["receipts"] = receipts
        if fundraiser_credits is not UNSET:
            field_dict["fundraiser_credits"] = fundraiser_credits
        if soft_credits is not UNSET:
            field_dict["soft_credits"] = soft_credits
        if send_reminder is not UNSET:
            field_dict["send_reminder"] = send_reminder
        if acknowledgements is not UNSET:
            field_dict["acknowledgements"] = acknowledgements
        if gift_subtype is not UNSET:
            field_dict["gift_subtype"] = gift_subtype
        if anonymous is not UNSET:
            field_dict["anonymous"] = anonymous
        if gift_code is not UNSET:
            field_dict["gift_code"] = gift_code
        if gift_status is not UNSET:
            field_dict["gift_status"] = gift_status
        if gift_status_date is not UNSET:
            field_dict["gift_status_date"] = gift_status_date
        if gift_constituency is not UNSET:
            field_dict["gift_constituency"] = gift_constituency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apply_payment import ApplyPayment
        from ..models.code_table_entry import CodeTableEntry
        from ..models.currency import Currency
        from ..models.fundraiser_credit import FundraiserCredit
        from ..models.fuzzy_date import FuzzyDate
        from ..models.gift_acknowledgement import GiftAcknowledgement
        from ..models.gift_constituent import GiftConstituent
        from ..models.gift_custom_field_add import GiftCustomFieldAdd
        from ..models.gift_payment_record import GiftPaymentRecord
        from ..models.gift_receipt import GiftReceipt
        from ..models.gift_split import GiftSplit
        from ..models.gift_subtype import GiftSubtype
        from ..models.issuer_details import IssuerDetails
        from ..models.pledge_installment_add import PledgeInstallmentAdd
        from ..models.schedule import Schedule
        from ..models.soft_credit import SoftCredit
        from ..models.tribute_lookup import TributeLookup

        d = dict(src_dict)
        amount = Currency.from_dict(d.pop("amount"))

        gift_type = BatchGiftAddWithTributeLookupGiftType(d.pop("gift_type"))

        constituent = GiftConstituent.from_dict(d.pop("constituent"))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        def _parse_tributes(data: object) -> list[TributeLookup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tributes_type_0 = []
                _tributes_type_0 = data
                for tributes_type_0_item_data in _tributes_type_0:
                    tributes_type_0_item = TributeLookup.from_dict(
                        tributes_type_0_item_data
                    )

                    tributes_type_0.append(tributes_type_0_item)

                return tributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TributeLookup] | None | Unset, data)

        tributes = _parse_tributes(d.pop("tributes", UNSET))

        def _parse_gift_splits(data: object) -> list[GiftSplit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                gift_splits_type_0 = []
                _gift_splits_type_0 = data
                for gift_splits_type_0_item_data in _gift_splits_type_0:
                    gift_splits_type_0_item = GiftSplit.from_dict(
                        gift_splits_type_0_item_data
                    )

                    gift_splits_type_0.append(gift_splits_type_0_item)

                return gift_splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftSplit] | None | Unset, data)

        gift_splits = _parse_gift_splits(d.pop("gift_splits", UNSET))

        def _parse_apply_payments(data: object) -> list[ApplyPayment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                apply_payments_type_0 = []
                _apply_payments_type_0 = data
                for apply_payments_type_0_item_data in _apply_payments_type_0:
                    apply_payments_type_0_item = ApplyPayment.from_dict(
                        apply_payments_type_0_item_data
                    )

                    apply_payments_type_0.append(apply_payments_type_0_item)

                return apply_payments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ApplyPayment] | None | Unset, data)

        apply_payments = _parse_apply_payments(d.pop("apply_payments", UNSET))

        def _parse_charge_first_payment(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        charge_first_payment = _parse_charge_first_payment(
            d.pop("charge_first_payment", UNSET)
        )

        def _parse_parent_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_gift_id = _parse_parent_gift_id(d.pop("parent_gift_id", UNSET))

        def _parse_custom_fields(
            data: object,
        ) -> list[GiftCustomFieldAdd] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                custom_fields_type_0 = []
                _custom_fields_type_0 = data
                for custom_fields_type_0_item_data in _custom_fields_type_0:
                    custom_fields_type_0_item = GiftCustomFieldAdd.from_dict(
                        custom_fields_type_0_item_data
                    )

                    custom_fields_type_0.append(custom_fields_type_0_item)

                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftCustomFieldAdd] | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("custom_fields", UNSET))

        def _parse_processes_manually(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        processes_manually = _parse_processes_manually(
            d.pop("processes_manually", UNSET)
        )

        def _parse_pledge_installments(
            data: object,
        ) -> list[PledgeInstallmentAdd] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pledge_installments_type_0 = []
                _pledge_installments_type_0 = data
                for pledge_installments_type_0_item_data in _pledge_installments_type_0:
                    pledge_installments_type_0_item = PledgeInstallmentAdd.from_dict(
                        pledge_installments_type_0_item_data
                    )

                    pledge_installments_type_0.append(pledge_installments_type_0_item)

                return pledge_installments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PledgeInstallmentAdd] | None | Unset, data)

        pledge_installments = _parse_pledge_installments(
            d.pop("pledge_installments", UNSET)
        )

        def _parse_gift_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gift_date_type_0 = isoparse(data)

                return gift_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        gift_date = _parse_gift_date(d.pop("gift_date", UNSET))

        def _parse_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lookup_id = _parse_lookup_id(d.pop("lookup_id", UNSET))

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        _gift_post_status = d.pop("gift_post_status", UNSET)
        gift_post_status: BatchGiftAddWithTributeLookupGiftPostStatus | Unset
        if isinstance(_gift_post_status, Unset):
            gift_post_status = UNSET
        else:
            gift_post_status = BatchGiftAddWithTributeLookupGiftPostStatus(
                _gift_post_status
            )

        def _parse_gift_post_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gift_post_date_type_0 = isoparse(data)

                return gift_post_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        gift_post_date = _parse_gift_post_date(d.pop("gift_post_date", UNSET))

        _issuer_details = d.pop("issuer_details", UNSET)
        issuer_details: IssuerDetails | Unset
        if isinstance(_issuer_details, Unset):
            issuer_details = UNSET
        else:
            issuer_details = IssuerDetails.from_dict(_issuer_details)

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_payments(data: object) -> list[GiftPaymentRecord] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payments_type_0 = []
                _payments_type_0 = data
                for payments_type_0_item_data in _payments_type_0:
                    payments_type_0_item = GiftPaymentRecord.from_dict(
                        payments_type_0_item_data
                    )

                    payments_type_0.append(payments_type_0_item)

                return payments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftPaymentRecord] | None | Unset, data)

        payments = _parse_payments(d.pop("payments", UNSET))

        _schedule = d.pop("schedule", UNSET)
        schedule: Schedule | Unset
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = Schedule.from_dict(_schedule)

        def _parse_adjustment_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        adjustment_notes = _parse_adjustment_notes(d.pop("adjustment_notes", UNSET))

        def _parse_receipts(data: object) -> list[GiftReceipt] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                receipts_type_0 = []
                _receipts_type_0 = data
                for receipts_type_0_item_data in _receipts_type_0:
                    receipts_type_0_item = GiftReceipt.from_dict(
                        receipts_type_0_item_data
                    )

                    receipts_type_0.append(receipts_type_0_item)

                return receipts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftReceipt] | None | Unset, data)

        receipts = _parse_receipts(d.pop("receipts", UNSET))

        def _parse_fundraiser_credits(
            data: object,
        ) -> list[FundraiserCredit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fundraiser_credits_type_0 = []
                _fundraiser_credits_type_0 = data
                for fundraiser_credits_type_0_item_data in _fundraiser_credits_type_0:
                    fundraiser_credits_type_0_item = FundraiserCredit.from_dict(
                        fundraiser_credits_type_0_item_data
                    )

                    fundraiser_credits_type_0.append(fundraiser_credits_type_0_item)

                return fundraiser_credits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FundraiserCredit] | None | Unset, data)

        fundraiser_credits = _parse_fundraiser_credits(
            d.pop("fundraiser_credits", UNSET)
        )

        def _parse_soft_credits(data: object) -> list[SoftCredit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                soft_credits_type_0 = []
                _soft_credits_type_0 = data
                for soft_credits_type_0_item_data in _soft_credits_type_0:
                    soft_credits_type_0_item = SoftCredit.from_dict(
                        soft_credits_type_0_item_data
                    )

                    soft_credits_type_0.append(soft_credits_type_0_item)

                return soft_credits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SoftCredit] | None | Unset, data)

        soft_credits = _parse_soft_credits(d.pop("soft_credits", UNSET))

        def _parse_send_reminder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        send_reminder = _parse_send_reminder(d.pop("send_reminder", UNSET))

        def _parse_acknowledgements(
            data: object,
        ) -> list[GiftAcknowledgement] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                acknowledgements_type_0 = []
                _acknowledgements_type_0 = data
                for acknowledgements_type_0_item_data in _acknowledgements_type_0:
                    acknowledgements_type_0_item = GiftAcknowledgement.from_dict(
                        acknowledgements_type_0_item_data
                    )

                    acknowledgements_type_0.append(acknowledgements_type_0_item)

                return acknowledgements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftAcknowledgement] | None | Unset, data)

        acknowledgements = _parse_acknowledgements(d.pop("acknowledgements", UNSET))

        _gift_subtype = d.pop("gift_subtype", UNSET)
        gift_subtype: GiftSubtype | Unset
        if isinstance(_gift_subtype, Unset):
            gift_subtype = UNSET
        else:
            gift_subtype = GiftSubtype.from_dict(_gift_subtype)

        def _parse_anonymous(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        anonymous = _parse_anonymous(d.pop("anonymous", UNSET))

        _gift_code = d.pop("gift_code", UNSET)
        gift_code: CodeTableEntry | Unset
        if isinstance(_gift_code, Unset):
            gift_code = UNSET
        else:
            gift_code = CodeTableEntry.from_dict(_gift_code)

        _gift_status = d.pop("gift_status", UNSET)
        gift_status: BatchGiftAddWithTributeLookupGiftStatus | Unset
        if isinstance(_gift_status, Unset):
            gift_status = UNSET
        else:
            gift_status = BatchGiftAddWithTributeLookupGiftStatus(_gift_status)

        _gift_status_date = d.pop("gift_status_date", UNSET)
        gift_status_date: FuzzyDate | Unset
        if isinstance(_gift_status_date, Unset):
            gift_status_date = UNSET
        else:
            gift_status_date = FuzzyDate.from_dict(_gift_status_date)

        _gift_constituency = d.pop("gift_constituency", UNSET)
        gift_constituency: CodeTableEntry | Unset
        if isinstance(_gift_constituency, Unset):
            gift_constituency = UNSET
        else:
            gift_constituency = CodeTableEntry.from_dict(_gift_constituency)

        batch_gift_add_with_tribute_lookup = cls(
            amount=amount,
            gift_type=gift_type,
            constituent=constituent,
            batch_id=batch_id,
            tributes=tributes,
            gift_splits=gift_splits,
            apply_payments=apply_payments,
            charge_first_payment=charge_first_payment,
            parent_gift_id=parent_gift_id,
            custom_fields=custom_fields,
            processes_manually=processes_manually,
            pledge_installments=pledge_installments,
            gift_date=gift_date,
            lookup_id=lookup_id,
            comments=comments,
            gift_post_status=gift_post_status,
            gift_post_date=gift_post_date,
            issuer_details=issuer_details,
            origin=origin,
            payments=payments,
            schedule=schedule,
            adjustment_notes=adjustment_notes,
            receipts=receipts,
            fundraiser_credits=fundraiser_credits,
            soft_credits=soft_credits,
            send_reminder=send_reminder,
            acknowledgements=acknowledgements,
            gift_subtype=gift_subtype,
            anonymous=anonymous,
            gift_code=gift_code,
            gift_status=gift_status,
            gift_status_date=gift_status_date,
            gift_constituency=gift_constituency,
        )

        return batch_gift_add_with_tribute_lookup

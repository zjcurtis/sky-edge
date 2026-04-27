from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.batch_gift_edit_gift_post_status import BatchGiftEditGiftPostStatus
from ..models.batch_gift_edit_gift_status import BatchGiftEditGiftStatus
from ..models.batch_gift_edit_gift_type import BatchGiftEditGiftType

if TYPE_CHECKING:
    from ..models.batch_gift_custom_field_edit import BatchGiftCustomFieldEdit
    from ..models.batch_gift_fundraiser_credit import BatchGiftFundraiserCredit
    from ..models.batch_gift_installment import BatchGiftInstallment
    from ..models.batch_gift_installment_payment import BatchGiftInstallmentPayment
    from ..models.batch_gift_soft_credit import BatchGiftSoftCredit
    from ..models.batch_gift_split import BatchGiftSplit
    from ..models.code_table_entry import CodeTableEntry
    from ..models.currency import Currency
    from ..models.fuzzy_date import FuzzyDate
    from ..models.gift_acknowledgement import GiftAcknowledgement
    from ..models.gift_constituent import GiftConstituent
    from ..models.gift_payment_record import GiftPaymentRecord
    from ..models.gift_receipt import GiftReceipt
    from ..models.gift_subtype import GiftSubtype
    from ..models.gift_tribute_add import GiftTributeAdd
    from ..models.issuer_details import IssuerDetails
    from ..models.schedule import Schedule


T = TypeVar("T", bound="BatchGiftEdit")


@_attrs_define
class BatchGiftEdit:
    """A batch gift to be edited, only including fields that can be changed

    Attributes:
        batch_gift_id (None | str | Unset): The batch gift record ID.
        batch_number (None | str | Unset): Batch number for the batch this gift is assigned to
        date_added (datetime.datetime | None | Unset): Date this batch gift was added to the system
        charge_first_payment (bool | None | Unset): True if a recurring gift payment should be processed immediately.
            Only applicable for recurring gifts.
        processes_manually (bool | None | Unset): Gets or sets the is manual flag for recurring gifts.
        custom_fields (list[BatchGiftCustomFieldEdit] | None | Unset): Custom fields associated with the batch gift
        installments (list[BatchGiftInstallment] | None | Unset): Installments created for this gift
        installment_payments (list[BatchGiftInstallmentPayment] | None | Unset): Installment payments paid by this gift
        tributes (list[GiftTributeAdd] | None | Unset): A collection of validatable tributes
        batch_id (None | str | Unset): System ID of the batch to which this batch gift belongs
        gift_splits (list[BatchGiftSplit] | None | Unset): The gift splits belonging to this batch gift
        fundraiser_credits (list[BatchGiftFundraiserCredit] | None | Unset): The fundraiser credits belonging to this
            batch gift
        soft_credits (list[BatchGiftSoftCredit] | None | Unset): The soft credits belonging to this batch gift
        gift_date (datetime.date | None | Unset): The date the gift was given.
        gift_post_date (datetime.date | None | Unset): The post date of the gift. Must be set if post status is
            NotPosted or Posted. Must be null if post status is DoNotPost.
        lookup_id (None | str | Unset): The gift's lookup ID. Example: Lookup-12345.
        amount (Currency | Unset): An amount denominated in a specific currency.
        comments (None | str | Unset): Comments associated with the gift. Character limit: 255. Example: This is a
            comment.
        constituent (GiftConstituent | Unset): The constituent who makes a gift.
        gift_post_status (BatchGiftEditGiftPostStatus | Unset): The post status of the gift. Example: NotPosted.
        gift_type (BatchGiftEditGiftType | Unset): The gift type. Example: Donation.
        issuer_details (IssuerDetails | Unset): Represents issuer detils for a stock gift
        origin (None | str | Unset): The gift's origin.
        payments (list[GiftPaymentRecord] | None | Unset): The gift's payments. Required for Recurring Gift type.
        schedule (Schedule | Unset): A gift schedule.
        adjustment_notes (None | str | Unset): The gift's adjustment notes. Used by the Adjustment Gift type. Example:
            Refunded gift.
        receipts (list[GiftReceipt] | None | Unset): The gift's receipts.
        send_reminder (bool | None | Unset): Gets or sets the send reminder flag for pledge gifts. If no value is
            provided, it will default to true for pledges, false otherwise.
        acknowledgements (list[GiftAcknowledgement] | None | Unset): The gift's acknowledgements.
        gift_subtype (GiftSubtype | Unset): Model representing a gift subtype.
        anonymous (bool | None | Unset): Notes whether the gift should remain anonymous or not, i.e. do not publicly
            show the donor's name.
        gift_code (CodeTableEntry | Unset): A predefined entry in a code table.
        gift_status (BatchGiftEditGiftStatus | Unset): The status of a gift. Example: Active.
        gift_status_date (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        gift_constituency (CodeTableEntry | Unset): A predefined entry in a code table.
    """

    batch_gift_id: None | str | Unset = UNSET
    batch_number: None | str | Unset = UNSET
    date_added: datetime.datetime | None | Unset = UNSET
    charge_first_payment: bool | None | Unset = UNSET
    processes_manually: bool | None | Unset = UNSET
    custom_fields: list[BatchGiftCustomFieldEdit] | None | Unset = UNSET
    installments: list[BatchGiftInstallment] | None | Unset = UNSET
    installment_payments: list[BatchGiftInstallmentPayment] | None | Unset = UNSET
    tributes: list[GiftTributeAdd] | None | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    gift_splits: list[BatchGiftSplit] | None | Unset = UNSET
    fundraiser_credits: list[BatchGiftFundraiserCredit] | None | Unset = UNSET
    soft_credits: list[BatchGiftSoftCredit] | None | Unset = UNSET
    gift_date: datetime.date | None | Unset = UNSET
    gift_post_date: datetime.date | None | Unset = UNSET
    lookup_id: None | str | Unset = UNSET
    amount: Currency | Unset = UNSET
    comments: None | str | Unset = UNSET
    constituent: GiftConstituent | Unset = UNSET
    gift_post_status: BatchGiftEditGiftPostStatus | Unset = UNSET
    gift_type: BatchGiftEditGiftType | Unset = UNSET
    issuer_details: IssuerDetails | Unset = UNSET
    origin: None | str | Unset = UNSET
    payments: list[GiftPaymentRecord] | None | Unset = UNSET
    schedule: Schedule | Unset = UNSET
    adjustment_notes: None | str | Unset = UNSET
    receipts: list[GiftReceipt] | None | Unset = UNSET
    send_reminder: bool | None | Unset = UNSET
    acknowledgements: list[GiftAcknowledgement] | None | Unset = UNSET
    gift_subtype: GiftSubtype | Unset = UNSET
    anonymous: bool | None | Unset = UNSET
    gift_code: CodeTableEntry | Unset = UNSET
    gift_status: BatchGiftEditGiftStatus | Unset = UNSET
    gift_status_date: FuzzyDate | Unset = UNSET
    gift_constituency: CodeTableEntry | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        batch_gift_id: None | str | Unset
        if isinstance(self.batch_gift_id, Unset):
            batch_gift_id = UNSET
        else:
            batch_gift_id = self.batch_gift_id

        batch_number: None | str | Unset
        if isinstance(self.batch_number, Unset):
            batch_number = UNSET
        else:
            batch_number = self.batch_number

        date_added: None | str | Unset
        if isinstance(self.date_added, Unset):
            date_added = UNSET
        elif isinstance(self.date_added, datetime.datetime):
            date_added = self.date_added.isoformat()
        else:
            date_added = self.date_added

        charge_first_payment: bool | None | Unset
        if isinstance(self.charge_first_payment, Unset):
            charge_first_payment = UNSET
        else:
            charge_first_payment = self.charge_first_payment

        processes_manually: bool | None | Unset
        if isinstance(self.processes_manually, Unset):
            processes_manually = UNSET
        else:
            processes_manually = self.processes_manually

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

        installments: list[dict[str, Any]] | None | Unset
        if isinstance(self.installments, Unset):
            installments = UNSET
        elif isinstance(self.installments, list):
            installments = []
            for installments_type_0_item_data in self.installments:
                installments_type_0_item = installments_type_0_item_data.to_dict()
                installments.append(installments_type_0_item)

        else:
            installments = self.installments

        installment_payments: list[dict[str, Any]] | None | Unset
        if isinstance(self.installment_payments, Unset):
            installment_payments = UNSET
        elif isinstance(self.installment_payments, list):
            installment_payments = []
            for installment_payments_type_0_item_data in self.installment_payments:
                installment_payments_type_0_item = (
                    installment_payments_type_0_item_data.to_dict()
                )
                installment_payments.append(installment_payments_type_0_item)

        else:
            installment_payments = self.installment_payments

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

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

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

        gift_date: None | str | Unset
        if isinstance(self.gift_date, Unset):
            gift_date = UNSET
        elif isinstance(self.gift_date, datetime.date):
            gift_date = self.gift_date.isoformat()
        else:
            gift_date = self.gift_date

        gift_post_date: None | str | Unset
        if isinstance(self.gift_post_date, Unset):
            gift_post_date = UNSET
        elif isinstance(self.gift_post_date, datetime.date):
            gift_post_date = self.gift_post_date.isoformat()
        else:
            gift_post_date = self.gift_post_date

        lookup_id: None | str | Unset
        if isinstance(self.lookup_id, Unset):
            lookup_id = UNSET
        else:
            lookup_id = self.lookup_id

        amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amount, Unset):
            amount = self.amount.to_dict()

        comments: None | str | Unset
        if isinstance(self.comments, Unset):
            comments = UNSET
        else:
            comments = self.comments

        constituent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.constituent, Unset):
            constituent = self.constituent.to_dict()

        gift_post_status: str | Unset = UNSET
        if not isinstance(self.gift_post_status, Unset):
            gift_post_status = self.gift_post_status.value

        gift_type: str | Unset = UNSET
        if not isinstance(self.gift_type, Unset):
            gift_type = self.gift_type.value

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

        field_dict.update({})
        if batch_gift_id is not UNSET:
            field_dict["batch_gift_id"] = batch_gift_id
        if batch_number is not UNSET:
            field_dict["batch_number"] = batch_number
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if charge_first_payment is not UNSET:
            field_dict["charge_first_payment"] = charge_first_payment
        if processes_manually is not UNSET:
            field_dict["processes_manually"] = processes_manually
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if installments is not UNSET:
            field_dict["installments"] = installments
        if installment_payments is not UNSET:
            field_dict["installment_payments"] = installment_payments
        if tributes is not UNSET:
            field_dict["tributes"] = tributes
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if gift_splits is not UNSET:
            field_dict["gift_splits"] = gift_splits
        if fundraiser_credits is not UNSET:
            field_dict["fundraiser_credits"] = fundraiser_credits
        if soft_credits is not UNSET:
            field_dict["soft_credits"] = soft_credits
        if gift_date is not UNSET:
            field_dict["gift_date"] = gift_date
        if gift_post_date is not UNSET:
            field_dict["gift_post_date"] = gift_post_date
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if comments is not UNSET:
            field_dict["comments"] = comments
        if constituent is not UNSET:
            field_dict["constituent"] = constituent
        if gift_post_status is not UNSET:
            field_dict["gift_post_status"] = gift_post_status
        if gift_type is not UNSET:
            field_dict["gift_type"] = gift_type
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
        from ..models.batch_gift_custom_field_edit import BatchGiftCustomFieldEdit
        from ..models.batch_gift_fundraiser_credit import BatchGiftFundraiserCredit
        from ..models.batch_gift_installment import BatchGiftInstallment
        from ..models.batch_gift_installment_payment import BatchGiftInstallmentPayment
        from ..models.batch_gift_soft_credit import BatchGiftSoftCredit
        from ..models.batch_gift_split import BatchGiftSplit
        from ..models.code_table_entry import CodeTableEntry
        from ..models.currency import Currency
        from ..models.fuzzy_date import FuzzyDate
        from ..models.gift_acknowledgement import GiftAcknowledgement
        from ..models.gift_constituent import GiftConstituent
        from ..models.gift_payment_record import GiftPaymentRecord
        from ..models.gift_receipt import GiftReceipt
        from ..models.gift_subtype import GiftSubtype
        from ..models.gift_tribute_add import GiftTributeAdd
        from ..models.issuer_details import IssuerDetails
        from ..models.schedule import Schedule

        d = dict(src_dict)

        def _parse_batch_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_gift_id = _parse_batch_gift_id(d.pop("batch_gift_id", UNSET))

        def _parse_batch_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_number = _parse_batch_number(d.pop("batch_number", UNSET))

        def _parse_date_added(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_added_type_0 = isoparse(data)

                return date_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_added = _parse_date_added(d.pop("date_added", UNSET))

        def _parse_charge_first_payment(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        charge_first_payment = _parse_charge_first_payment(
            d.pop("charge_first_payment", UNSET)
        )

        def _parse_processes_manually(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        processes_manually = _parse_processes_manually(
            d.pop("processes_manually", UNSET)
        )

        def _parse_custom_fields(
            data: object,
        ) -> list[BatchGiftCustomFieldEdit] | None | Unset:
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
                    custom_fields_type_0_item = BatchGiftCustomFieldEdit.from_dict(
                        custom_fields_type_0_item_data
                    )

                    custom_fields_type_0.append(custom_fields_type_0_item)

                return custom_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftCustomFieldEdit] | None | Unset, data)

        custom_fields = _parse_custom_fields(d.pop("custom_fields", UNSET))

        def _parse_installments(
            data: object,
        ) -> list[BatchGiftInstallment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                installments_type_0 = []
                _installments_type_0 = data
                for installments_type_0_item_data in _installments_type_0:
                    installments_type_0_item = BatchGiftInstallment.from_dict(
                        installments_type_0_item_data
                    )

                    installments_type_0.append(installments_type_0_item)

                return installments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftInstallment] | None | Unset, data)

        installments = _parse_installments(d.pop("installments", UNSET))

        def _parse_installment_payments(
            data: object,
        ) -> list[BatchGiftInstallmentPayment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                installment_payments_type_0 = []
                _installment_payments_type_0 = data
                for (
                    installment_payments_type_0_item_data
                ) in _installment_payments_type_0:
                    installment_payments_type_0_item = (
                        BatchGiftInstallmentPayment.from_dict(
                            installment_payments_type_0_item_data
                        )
                    )

                    installment_payments_type_0.append(installment_payments_type_0_item)

                return installment_payments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftInstallmentPayment] | None | Unset, data)

        installment_payments = _parse_installment_payments(
            d.pop("installment_payments", UNSET)
        )

        def _parse_tributes(data: object) -> list[GiftTributeAdd] | None | Unset:
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
                    tributes_type_0_item = GiftTributeAdd.from_dict(
                        tributes_type_0_item_data
                    )

                    tributes_type_0.append(tributes_type_0_item)

                return tributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftTributeAdd] | None | Unset, data)

        tributes = _parse_tributes(d.pop("tributes", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        def _parse_gift_splits(data: object) -> list[BatchGiftSplit] | None | Unset:
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
                    gift_splits_type_0_item = BatchGiftSplit.from_dict(
                        gift_splits_type_0_item_data
                    )

                    gift_splits_type_0.append(gift_splits_type_0_item)

                return gift_splits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftSplit] | None | Unset, data)

        gift_splits = _parse_gift_splits(d.pop("gift_splits", UNSET))

        def _parse_fundraiser_credits(
            data: object,
        ) -> list[BatchGiftFundraiserCredit] | None | Unset:
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
                    fundraiser_credits_type_0_item = (
                        BatchGiftFundraiserCredit.from_dict(
                            fundraiser_credits_type_0_item_data
                        )
                    )

                    fundraiser_credits_type_0.append(fundraiser_credits_type_0_item)

                return fundraiser_credits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftFundraiserCredit] | None | Unset, data)

        fundraiser_credits = _parse_fundraiser_credits(
            d.pop("fundraiser_credits", UNSET)
        )

        def _parse_soft_credits(
            data: object,
        ) -> list[BatchGiftSoftCredit] | None | Unset:
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
                    soft_credits_type_0_item = BatchGiftSoftCredit.from_dict(
                        soft_credits_type_0_item_data
                    )

                    soft_credits_type_0.append(soft_credits_type_0_item)

                return soft_credits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BatchGiftSoftCredit] | None | Unset, data)

        soft_credits = _parse_soft_credits(d.pop("soft_credits", UNSET))

        def _parse_gift_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gift_date_type_0 = isoparse(data).date()

                return gift_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        gift_date = _parse_gift_date(d.pop("gift_date", UNSET))

        def _parse_gift_post_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                gift_post_date_type_0 = isoparse(data).date()

                return gift_post_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        gift_post_date = _parse_gift_post_date(d.pop("gift_post_date", UNSET))

        def _parse_lookup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lookup_id = _parse_lookup_id(d.pop("lookup_id", UNSET))

        _amount = d.pop("amount", UNSET)
        amount: Currency | Unset
        if isinstance(_amount, Unset):
            amount = UNSET
        else:
            amount = Currency.from_dict(_amount)

        def _parse_comments(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comments = _parse_comments(d.pop("comments", UNSET))

        _constituent = d.pop("constituent", UNSET)
        constituent: GiftConstituent | Unset
        if isinstance(_constituent, Unset):
            constituent = UNSET
        else:
            constituent = GiftConstituent.from_dict(_constituent)

        _gift_post_status = d.pop("gift_post_status", UNSET)
        gift_post_status: BatchGiftEditGiftPostStatus | Unset
        if isinstance(_gift_post_status, Unset):
            gift_post_status = UNSET
        else:
            gift_post_status = BatchGiftEditGiftPostStatus(_gift_post_status)

        _gift_type = d.pop("gift_type", UNSET)
        gift_type: BatchGiftEditGiftType | Unset
        if isinstance(_gift_type, Unset):
            gift_type = UNSET
        else:
            gift_type = BatchGiftEditGiftType(_gift_type)

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
        gift_status: BatchGiftEditGiftStatus | Unset
        if isinstance(_gift_status, Unset):
            gift_status = UNSET
        else:
            gift_status = BatchGiftEditGiftStatus(_gift_status)

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

        batch_gift_edit = cls(
            batch_gift_id=batch_gift_id,
            batch_number=batch_number,
            date_added=date_added,
            charge_first_payment=charge_first_payment,
            processes_manually=processes_manually,
            custom_fields=custom_fields,
            installments=installments,
            installment_payments=installment_payments,
            tributes=tributes,
            batch_id=batch_id,
            gift_splits=gift_splits,
            fundraiser_credits=fundraiser_credits,
            soft_credits=soft_credits,
            gift_date=gift_date,
            gift_post_date=gift_post_date,
            lookup_id=lookup_id,
            amount=amount,
            comments=comments,
            constituent=constituent,
            gift_post_status=gift_post_status,
            gift_type=gift_type,
            issuer_details=issuer_details,
            origin=origin,
            payments=payments,
            schedule=schedule,
            adjustment_notes=adjustment_notes,
            receipts=receipts,
            send_reminder=send_reminder,
            acknowledgements=acknowledgements,
            gift_subtype=gift_subtype,
            anonymous=anonymous,
            gift_code=gift_code,
            gift_status=gift_status,
            gift_status_date=gift_status_date,
            gift_constituency=gift_constituency,
        )

        return batch_gift_edit

from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.pledge_installments_read_payment_method import (
    PledgeInstallmentsReadPaymentMethod,
)
from ..models.pledge_installments_read_schedule_frequency import (
    PledgeInstallmentsReadScheduleFrequency,
)

if TYPE_CHECKING:
    from ..models.pledge_installment_read import PledgeInstallmentRead


T = TypeVar("T", bound="PledgeInstallmentsRead")


@_attrs_define
class PledgeInstallmentsRead:
    """The installments of a pledge gift.

    Attributes:
        pledge_id (None | str | Unset): The ID of the pledge the installments are for.
        start_date (datetime.datetime | None | Unset): The date that the gift schedule starts.
        frequency (PledgeInstallmentsReadScheduleFrequency | Unset): The frequency of the gift schedule.
        installments (list[PledgeInstallmentRead] | None | Unset): The installments for the pledge gift.
        concurrency_token (None | str | Unset): Concurrency token
        payment_method (PledgeInstallmentsReadPaymentMethod | Unset): The payment method of the gift.
        bbps_configuration_currency (None | str | Unset): The currency of the BBPS configuration associated with the
            gift.
    """

    pledge_id: None | str | Unset = UNSET
    start_date: datetime.datetime | None | Unset = UNSET
    frequency: PledgeInstallmentsReadScheduleFrequency | Unset = UNSET
    installments: list[PledgeInstallmentRead] | None | Unset = UNSET
    concurrency_token: None | str | Unset = UNSET
    payment_method: PledgeInstallmentsReadPaymentMethod | Unset = UNSET
    bbps_configuration_currency: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        pledge_id: None | str | Unset
        if isinstance(self.pledge_id, Unset):
            pledge_id = UNSET
        else:
            pledge_id = self.pledge_id

        start_date: None | str | Unset
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        frequency: str | Unset = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

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

        concurrency_token: None | str | Unset
        if isinstance(self.concurrency_token, Unset):
            concurrency_token = UNSET
        else:
            concurrency_token = self.concurrency_token

        payment_method: str | Unset = UNSET
        if not isinstance(self.payment_method, Unset):
            payment_method = self.payment_method.value

        bbps_configuration_currency: None | str | Unset
        if isinstance(self.bbps_configuration_currency, Unset):
            bbps_configuration_currency = UNSET
        else:
            bbps_configuration_currency = self.bbps_configuration_currency

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pledge_id is not UNSET:
            field_dict["pledge_id"] = pledge_id
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if installments is not UNSET:
            field_dict["installments"] = installments
        if concurrency_token is not UNSET:
            field_dict["concurrency_token"] = concurrency_token
        if payment_method is not UNSET:
            field_dict["payment_method"] = payment_method
        if bbps_configuration_currency is not UNSET:
            field_dict["bbps_configuration_currency"] = bbps_configuration_currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pledge_installment_read import PledgeInstallmentRead

        d = dict(src_dict)

        def _parse_pledge_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pledge_id = _parse_pledge_id(d.pop("pledge_id", UNSET))

        def _parse_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_date = _parse_start_date(d.pop("start_date", UNSET))

        _frequency = d.pop("frequency", UNSET)
        frequency: PledgeInstallmentsReadScheduleFrequency | Unset
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = PledgeInstallmentsReadScheduleFrequency(_frequency)

        def _parse_installments(
            data: object,
        ) -> list[PledgeInstallmentRead] | None | Unset:
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
                    installments_type_0_item = PledgeInstallmentRead.from_dict(
                        installments_type_0_item_data
                    )

                    installments_type_0.append(installments_type_0_item)

                return installments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PledgeInstallmentRead] | None | Unset, data)

        installments = _parse_installments(d.pop("installments", UNSET))

        def _parse_concurrency_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        concurrency_token = _parse_concurrency_token(d.pop("concurrency_token", UNSET))

        _payment_method = d.pop("payment_method", UNSET)
        payment_method: PledgeInstallmentsReadPaymentMethod | Unset
        if isinstance(_payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = PledgeInstallmentsReadPaymentMethod(_payment_method)

        def _parse_bbps_configuration_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bbps_configuration_currency = _parse_bbps_configuration_currency(
            d.pop("bbps_configuration_currency", UNSET)
        )

        pledge_installments_read = cls(
            pledge_id=pledge_id,
            start_date=start_date,
            frequency=frequency,
            installments=installments,
            concurrency_token=concurrency_token,
            payment_method=payment_method,
            bbps_configuration_currency=bbps_configuration_currency,
        )

        return pledge_installments_read

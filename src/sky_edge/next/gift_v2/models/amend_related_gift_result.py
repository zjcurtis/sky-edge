from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

from ..models.amend_related_gift_result_recurring_gift_amendment_status import (
    AmendRelatedGiftResultRecurringGiftAmendmentStatus,
)

T = TypeVar("T", bound="AmendRelatedGiftResult")


@_attrs_define
class AmendRelatedGiftResult:
    """The result of an amend gift operation that affected a related recurring gift.

    Attributes:
        recurring_gift_legacy_id (None | str | Unset): The legacy ID of the recurring gift that was amended.
        amendment_legacy_id (None | str | Unset): The legacy ID of the new amendment which was added.
        correlation_id (None | str | Unset): The correlation ID of the amendment.
        status (AmendRelatedGiftResultRecurringGiftAmendmentStatus | Unset): Defines the types of amendment status.
        error_message (None | str | Unset): If the amendment failed, the error message indicates why the failure
            occurred.
    """

    recurring_gift_legacy_id: None | str | Unset = UNSET
    amendment_legacy_id: None | str | Unset = UNSET
    correlation_id: None | str | Unset = UNSET
    status: AmendRelatedGiftResultRecurringGiftAmendmentStatus | Unset = UNSET
    error_message: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        recurring_gift_legacy_id: None | str | Unset
        if isinstance(self.recurring_gift_legacy_id, Unset):
            recurring_gift_legacy_id = UNSET
        else:
            recurring_gift_legacy_id = self.recurring_gift_legacy_id

        amendment_legacy_id: None | str | Unset
        if isinstance(self.amendment_legacy_id, Unset):
            amendment_legacy_id = UNSET
        else:
            amendment_legacy_id = self.amendment_legacy_id

        correlation_id: None | str | Unset
        if isinstance(self.correlation_id, Unset):
            correlation_id = UNSET
        else:
            correlation_id = self.correlation_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if recurring_gift_legacy_id is not UNSET:
            field_dict["recurring_gift_legacy_id"] = recurring_gift_legacy_id
        if amendment_legacy_id is not UNSET:
            field_dict["amendment_legacy_id"] = amendment_legacy_id
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_recurring_gift_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recurring_gift_legacy_id = _parse_recurring_gift_legacy_id(
            d.pop("recurring_gift_legacy_id", UNSET)
        )

        def _parse_amendment_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amendment_legacy_id = _parse_amendment_legacy_id(
            d.pop("amendment_legacy_id", UNSET)
        )

        def _parse_correlation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        correlation_id = _parse_correlation_id(d.pop("correlation_id", UNSET))

        _status = d.pop("status", UNSET)
        status: AmendRelatedGiftResultRecurringGiftAmendmentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AmendRelatedGiftResultRecurringGiftAmendmentStatus(_status)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        amend_related_gift_result = cls(
            recurring_gift_legacy_id=recurring_gift_legacy_id,
            amendment_legacy_id=amendment_legacy_id,
            correlation_id=correlation_id,
            status=status,
            error_message=error_message,
        )

        return amend_related_gift_result

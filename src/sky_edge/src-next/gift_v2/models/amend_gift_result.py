from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.amend_gift_result_recurring_gift_amendment_status import AmendGiftResultRecurringGiftAmendmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.amend_related_gift_result import AmendRelatedGiftResult


T = TypeVar("T", bound="AmendGiftResult")


@_attrs_define
class AmendGiftResult:
    """The result of an amend gift operation.

    Attributes:
        legacy_id (None | str | Unset): The legacy ID of the amendment that was added.
        status (AmendGiftResultRecurringGiftAmendmentStatus | Unset): Defines the types of amendment status.
        correlation_id (None | str | Unset): The correlation ID of the amendment.
        related_gifts (list[AmendRelatedGiftResult] | None | Unset): If other recurring gifts were also amended, these
            are their amend results
    """

    legacy_id: None | str | Unset = UNSET
    status: AmendGiftResultRecurringGiftAmendmentStatus | Unset = UNSET
    correlation_id: None | str | Unset = UNSET
    related_gifts: list[AmendRelatedGiftResult] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        legacy_id: None | str | Unset
        if isinstance(self.legacy_id, Unset):
            legacy_id = UNSET
        else:
            legacy_id = self.legacy_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        correlation_id: None | str | Unset
        if isinstance(self.correlation_id, Unset):
            correlation_id = UNSET
        else:
            correlation_id = self.correlation_id

        related_gifts: list[dict[str, Any]] | None | Unset
        if isinstance(self.related_gifts, Unset):
            related_gifts = UNSET
        elif isinstance(self.related_gifts, list):
            related_gifts = []
            for related_gifts_type_0_item_data in self.related_gifts:
                related_gifts_type_0_item = related_gifts_type_0_item_data.to_dict()
                related_gifts.append(related_gifts_type_0_item)

        else:
            related_gifts = self.related_gifts

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if legacy_id is not UNSET:
            field_dict["legacy_id"] = legacy_id
        if status is not UNSET:
            field_dict["status"] = status
        if correlation_id is not UNSET:
            field_dict["correlation_id"] = correlation_id
        if related_gifts is not UNSET:
            field_dict["related_gifts"] = related_gifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.amend_related_gift_result import AmendRelatedGiftResult

        d = dict(src_dict)

        def _parse_legacy_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legacy_id = _parse_legacy_id(d.pop("legacy_id", UNSET))

        _status = d.pop("status", UNSET)
        status: AmendGiftResultRecurringGiftAmendmentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AmendGiftResultRecurringGiftAmendmentStatus(_status)

        def _parse_correlation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        correlation_id = _parse_correlation_id(d.pop("correlation_id", UNSET))

        def _parse_related_gifts(data: object) -> list[AmendRelatedGiftResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                related_gifts_type_0 = []
                _related_gifts_type_0 = data
                for related_gifts_type_0_item_data in _related_gifts_type_0:
                    related_gifts_type_0_item = AmendRelatedGiftResult.from_dict(related_gifts_type_0_item_data)

                    related_gifts_type_0.append(related_gifts_type_0_item)

                return related_gifts_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AmendRelatedGiftResult] | None | Unset, data)

        related_gifts = _parse_related_gifts(d.pop("related_gifts", UNSET))

        amend_gift_result = cls(
            legacy_id=legacy_id,
            status=status,
            correlation_id=correlation_id,
            related_gifts=related_gifts,
        )

        return amend_gift_result
